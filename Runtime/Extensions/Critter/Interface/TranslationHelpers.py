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

from Runtime.Extensions.Critter.Interface.MessageCommon import *
from Runtime.Extensions.Critter.Interface.Messages_pb2  import *
from Runtime.Extensions.Critter.Interface.Translation   import *

#
# NOTE: Header, Payload and Envelope are not translated.
#

def getHeaderIdAndMessageTypeByMessageName(aMessageName):
    if   aMessageName == 'CantExecuteWorkNowAnnouncement':   return (CANT_EXECUTE_WORK_NOW_ANNOUNCEMENT,  CantExecuteWorkNowAnnouncement)
    elif aMessageName == 'CommandWorkExecutionAnnouncement': return (COMMAND_WORK_EXECUTION_ANNOUNCEMENT, CommandWorkExecutionAnnouncement)
    elif aMessageName == 'DetermineGraphCycleRequest':       return (DETERMINE_GRAPH_CYCLE_REQUEST,       DetermineGraphCycleRequest)
    elif aMessageName == 'DetermineGraphCycleResponse':      return (DETERMINE_GRAPH_CYCLE_RESPONSE,      DetermineGraphCycleResponse)
    elif aMessageName == 'DetermineWorkCycleRequest':        return (DETERMINE_WORK_CYCLE_REQUEST,        DetermineWorkCycleRequest)
    elif aMessageName == 'DetermineWorkCycleResponse':       return (DETERMINE_WORK_CYCLE_RESPONSE,       DetermineWorkCycleResponse)
    elif aMessageName == 'ExecuteGraphAnnouncement':         return (EXECUTE_GRAPH_ANNOUNCEMENT,          ExecuteGraphAnnouncement)
    elif aMessageName == 'ExecuteWorkAnnouncement':          return (EXECUTE_WORK_ANNOUNCEMENT,           ExecuteWorkAnnouncement)
    elif aMessageName == 'HeartbeatAnnouncement':            return (HEARTBEAT_ANNOUNCEMENT,              HeartbeatAnnouncement)
    elif aMessageName == 'LoadGraphAndWorkRequest':          return (LOAD_GRAPH_AND_WORK_REQUEST,         LoadGraphAndWorkRequest)
    elif aMessageName == 'LoadGraphAndWorkResponse':         return (LOAD_GRAPH_AND_WORK_RESPONSE,        LoadGraphAndWorkResponse)
    elif aMessageName == 'LoadWorkDetailsRequest':           return (LOAD_WORK_DETAILS_REQUEST,           LoadWorkDetailsRequest)
    elif aMessageName == 'LoadWorkDetailsResponse':          return (LOAD_WORK_DETAILS_RESPONSE,          LoadWorkDetailsResponse)
    elif aMessageName == 'PokeAnnouncement':                 return (POKE_ANNOUNCEMENT,                   PokeAnnouncement)
    elif aMessageName == 'PresentYourselfRequest':           return (PRESENT_YOURSELF_REQUEST,            PresentYourselfRequest)
    elif aMessageName == 'PresentYourselfResponse':          return (PRESENT_YOURSELF_RESPONSE,           PresentYourselfResponse)
    elif aMessageName == 'ReportFinishedWorkAnnouncement':   return (REPORT_FINISHED_WORK_ANNOUNCEMENT,   ReportFinishedWorkAnnouncement)
    # TODO: Raise a meaningful exception.
    # Not found.
    else:                                                    raise

def getMessageByHeaderId(aId):
    if   aId == CANT_EXECUTE_WORK_NOW_ANNOUNCEMENT:  return CantExecuteWorkNowAnnouncement()
    elif aId == COMMAND_WORK_EXECUTION_ANNOUNCEMENT: return CommandWorkExecutionAnnouncement()
    elif aId == DETERMINE_GRAPH_CYCLE_REQUEST:       return DetermineGraphCycleRequest()
    elif aId == DETERMINE_GRAPH_CYCLE_RESPONSE:      return DetermineGraphCycleResponse()
    elif aId == DETERMINE_WORK_CYCLE_REQUEST:        return DetermineWorkCycleRequest()
    elif aId == DETERMINE_WORK_CYCLE_RESPONSE:       return DetermineWorkCycleResponse()
    elif aId == EXECUTE_GRAPH_ANNOUNCEMENT:          return ExecuteGraphAnnouncement()
    elif aId == EXECUTE_WORK_ANNOUNCEMENT:           return ExecuteWorkAnnouncement()
    elif aId == HEARTBEAT_ANNOUNCEMENT:              return HeartbeatAnnouncement()
    elif aId == LOAD_GRAPH_AND_WORK_REQUEST:         return LoadGraphAndWorkRequest()
    elif aId == LOAD_GRAPH_AND_WORK_RESPONSE:        return LoadGraphAndWorkResponse()
    elif aId == LOAD_WORK_DETAILS_REQUEST:           return LoadWorkDetailsRequest()
    elif aId == LOAD_WORK_DETAILS_RESPONSE:          return LoadWorkDetailsResponse()
    elif aId == POKE_ANNOUNCEMENT:                   return PokeAnnouncement()
    elif aId == PRESENT_YOURSELF_REQUEST:            return PresentYourselfRequest()
    elif aId == PRESENT_YOURSELF_RESPONSE:           return PresentYourselfResponse()
    elif aId == REPORT_FINISHED_WORK_ANNOUNCEMENT:   return ReportFinishedWorkAnnouncement()
    # TODO: Raise a meaningful exception.
    # Not found.
    else:                                            raise

def getCorrespondingPiewikType(aProtobufType):
    # Structures.
    if   type(aProtobufType) is CritterData:                      return PiewikCritterData
    elif type(aProtobufType) is GraphData:                        return PiewikGraphData
    elif type(aProtobufType) is WorkData:                         return PiewikWorkData
    elif type(aProtobufType) is WorkDetailsData:                  return PiewikWorkDetailsData
    elif type(aProtobufType) is WorkPredecessorData:              return PiewikWorkPredecessorData
    # Messages.
    elif type(aProtobufType) is CantExecuteWorkNowAnnouncement:   return PiewikCantExecuteWorkNowAnnouncement
    elif type(aProtobufType) is HeartbeatAnnouncement:            return PiewikHeartbeatAnnouncement
    elif type(aProtobufType) is PresentYourselfRequest:           return PiewikPresentYourselfRequest
    elif type(aProtobufType) is PresentYourselfResponse:          return PiewikPresentYourselfResponse
    elif type(aProtobufType) is PokeAnnouncement:                 return PiewikPokeAnnouncement
    elif type(aProtobufType) is ExecuteGraphAnnouncement:         return PiewikExecuteGraphAnnouncement
    elif type(aProtobufType) is LoadGraphAndWorkRequest:          return PiewikLoadGraphAndWorkRequest
    elif type(aProtobufType) is LoadGraphAndWorkResponse:         return PiewikLoadGraphAndWorkResponse
    elif type(aProtobufType) is LoadWorkDetailsRequest:           return PiewikLoadWorkDetailsRequest
    elif type(aProtobufType) is LoadWorkDetailsResponse:          return PiewikLoadWorkDetailsResponse
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
