# -*- coding: utf-8 -*-
#
# Copyright (C) 2012 Piewik Project.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
# 3. Neither the name of the project nor the names of its contributors
#    may be used to endorse or promote products derived from this software
#    without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE PROJECT AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE PROJECT OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
# OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
# OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
# SUCH DAMAGE.

from google.protobuf.internal.containers import RepeatedCompositeFieldContainer

from Concept.Decoder                                                   import Decoder
from Concept.Extensions.CritterProtobuf.CritterInterface.MessageCommon import *
from Concept.Extensions.CritterProtobuf.CritterInterface.Messages_pb2  import *
from Concept.Extensions.CritterProtobuf.CritterInterface.Translation   import *
from Concept.TypeSystem                                                import *

class ProtobufDecoder(Decoder):
    def decode(self, aBytesRead):
        envelope = Envelope()
        envelope.ParseFromString(aBytesRead)

        if   envelope.header.id == COMMAND_WORK_EXECUTION_ANNOUNCEMENT: message = CommandWorkExecutionAnnouncement()
        elif envelope.header.id == DETERMINE_GRAPH_CYCLE_REQUEST:       message = DetermineGraphCycleRequest()
        elif envelope.header.id == DETERMINE_GRAPH_CYCLE_RESPONSE:      message = DetermineGraphCycleResponse()
        elif envelope.header.id == DETERMINE_WORK_CYCLE_REQUEST:        message = DetermineWorkCycleRequest()
        elif envelope.header.id == DETERMINE_WORK_CYCLE_RESPONSE:       message = DetermineWorkCycleResponse()
        elif envelope.header.id == EXECUTE_GRAPH_ANNOUNCEMENT:          message = ExecuteGraphAnnouncement()
        elif envelope.header.id == EXECUTE_WORK_ANNOUNCEMENT:           message = ExecuteWorkAnnouncement()
        elif envelope.header.id == HEARTBEAT_ANNOUNCEMENT:              message = HeartbeatAnnouncement()
        elif envelope.header.id == LOAD_GRAPH_AND_WORK_REQUEST:         message = LoadGraphAndWorkRequest()
        elif envelope.header.id == LOAD_GRAPH_AND_WORK_RESPONSE:        message = LoadGraphAndWorkResponse()
        elif envelope.header.id == POKE_ANNOUNCEMENT:                   message = PokeAnnouncement()
        elif envelope.header.id == PRESENT_YOURSELF_REQUEST:            message = PresentYourselfRequest()
        elif envelope.header.id == PRESENT_YOURSELF_RESPONSE:           message = PresentYourselfResponse()
        elif envelope.header.id == REPORT_FINISHED_WORK_ANNOUNCEMENT:   message = ReportFinishedWorkAnnouncement()
        # TODO: Raise a meaningful exception.
        else:                                                           raise

        message.ParseFromString(envelope.payload.payload)

        # Translation of the python representation of protobuf to the Piewik representation.
        return self.encodeInternally(message)

    def encodeInternally(self, aData):
        aHook = getCorrespondingPiewikType(aData)()
        dictionary = self.encodeDictionary(aData)
        aHook.assign(dictionary)
        return aHook

    def encodeDictionary(self, aData):
        dictionary = {}

        for field in aData.ListFields():
            # TODO: Integer, float...
            if type(field[1]) in (str, unicode):
                # TODO: Potentially dangerous casting of unicode to str.
                dictionary[field[0].name] = Charstring().assign(str(field[1]))
            if type(field[1]) is CritterData:
                # TODO: Mapping needed here! (Piewik -> protobuf).
                dictionary[field[0].name] = PiewikCritterData().assign(self.encodeDictionary(field[1]))
            if type(field[1]) is RepeatedCompositeFieldContainer:
                # TODO: What if there's nothing?
                piewikType = getCorrespondingPiewikType(field[1][0])
                recordOf = RecordOf(piewikType)
                list = []
                for element in field[1]:
                    list.append(piewikType().assign(self.encodeDictionary(element)))
                    self.encodeDictionary(element)
                recordOf.assign(list)
                dictionary[field[0].name] = recordOf

        return dictionary

def getCorrespondingPiewikType(aProtobufType):
    # TODO: All types.
    # Messages.
    if   type(aProtobufType) is LoadGraphAndWorkResponse: return PiewikLoadGraphAndWorkResponse

    # Structures.
    elif type(aProtobufType) is GraphData:                return PiewikGraphData
    elif type(aProtobufType) is WorkData:                 return PiewikWorkData
    elif type(aProtobufType) is WorkPredecessorData:      return PiewikWorkPredecessorData

    # TODO: A meaningful exception.
    # Not found.
    else:                                                 raise
