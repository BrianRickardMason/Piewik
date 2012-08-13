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

from Messages_pb2 import *
from Translation  import *

#
# NOTE: Header, Payload and Envelope are not translated.
#

def getCorrespondingPiewikType(aProtobufType):
    # Structures.
    if   type(aProtobufType) is CritterData:                      return PiewikCritterData
    elif type(aProtobufType) is GraphData:                        return PiewikGraphData
    elif type(aProtobufType) is WorkData:                         return PiewikWorkData
    elif type(aProtobufType) is WorkPredecessorData:              return PiewikWorkPredecessorData
    # Messages.
    elif type(aProtobufType) is HeartbeatAnnouncement:            return PiewikHeartbeatAnnouncement
    elif type(aProtobufType) is PresentYourselfRequest:           return PiewikPresentYourselfRequest
    elif type(aProtobufType) is PresentYourselfResponse:          return PiewikPresentYourselfResponse
    elif type(aProtobufType) is PokeAnnouncement:                 return PiewikPokeAnnouncement
    elif type(aProtobufType) is ExecuteGraphAnnouncement:         return PiewikExecuteGraphAnnouncement
    elif type(aProtobufType) is LoadGraphAndWorkRequest:          return PiewikLoadGraphAndWorkRequest
    elif type(aProtobufType) is LoadGraphAndWorkResponse:         return PiewikLoadGraphAndWorkResponse
    elif type(aProtobufType) is DetermineGraphCycleRequest:       return PiewikDetermineGraphCycleRequest
    elif type(aProtobufType) is DetermineGraphCycleResponse:      return PiewikDetermineGraphCycleResponse
    elif type(aProtobufType) is CommandWorkExecutionAnnouncement: return PiewikCommandWorkExecutionAnnouncement
    elif type(aProtobufType) is ExecuteWorkAnnouncement:          return PiewikExecuteWorkAnnouncement
    elif type(aProtobufType) is DetermineWorkCycleRequest:        return PiewikDetermineWorkCycleRequest
    elif type(aProtobufType) is DetermineWorkCycleResponse:       return PiewikDetermineWorkCycleResponse
    elif type(aProtobufType) is ReportFinishedWorkAnnouncement:   return PiewikReportFinishedWorkAnnouncement
    # TODO: A meaningful exception.
    # Not found.
    else:                                                         raise
