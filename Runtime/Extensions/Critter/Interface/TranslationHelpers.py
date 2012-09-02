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
    if False: pass
    elif aMessageName == 'CantExecuteWorkNowAnnouncement':  return (CANT_EXECUTE_WORK_NOW_ANNOUNCEMENT, CantExecuteWorkNowAnnouncement)
    elif aMessageName == 'Command_DetermineGraphCycle_Req': return (COMMAND_DETERMINE_GRAPH_CYCLE_REQ, Command_DetermineGraphCycle_Req)
    elif aMessageName == 'Command_DetermineGraphCycle_Res': return (COMMAND_DETERMINE_GRAPH_CYCLE_RES, Command_DetermineGraphCycle_Res)
    elif aMessageName == 'Command_DetermineWorkCycle_Req':  return (COMMAND_DETERMINE_WORK_CYCLE_REQ, Command_DetermineWorkCycle_Req)
    elif aMessageName == 'Command_DetermineWorkCycle_Res':  return (COMMAND_DETERMINE_WORK_CYCLE_RES, Command_DetermineWorkCycle_Res)
    elif aMessageName == 'Command_Election_Req':            return (COMMAND_ELECTION_REQ, Command_Election_Req)
    elif aMessageName == 'Command_Election_Res':            return (COMMAND_ELECTION_RES, Command_Election_Res)
    elif aMessageName == 'Command_ExecuteGraph_Req':        return (COMMAND_EXECUTE_GRAPH_REQ, Command_ExecuteGraph_Req)
    elif aMessageName == 'Command_ExecuteGraph_Res':        return (COMMAND_EXECUTE_GRAPH_RES, Command_ExecuteGraph_Res)
    elif aMessageName == 'Command_ExecuteWork_Req':         return (COMMAND_EXECUTE_WORK_REQ, Command_ExecuteWork_Req)
    elif aMessageName == 'Command_ExecuteWork_Res':         return (COMMAND_EXECUTE_WORK_RES, Command_ExecuteWork_Res)
    elif aMessageName == 'Command_OrderWorkExecution_Req':  return (COMMAND_ORDER_WORK_EXECUTION_REQ, Command_OrderWorkExecution_Req)
    elif aMessageName == 'Command_OrderWorkExecution_Res':  return (COMMAND_ORDER_WORK_EXECUTION_RES, Command_OrderWorkExecution_Res)
    elif aMessageName == 'HeartbeatAnnouncement':           return (HEARTBEAT_ANNOUNCEMENT, HeartbeatAnnouncement)
    elif aMessageName == 'LoadGraphAndWorkRequest':         return (LOAD_GRAPH_AND_WORK_REQUEST, LoadGraphAndWorkRequest)
    elif aMessageName == 'LoadGraphAndWorkResponse':        return (LOAD_GRAPH_AND_WORK_RESPONSE, LoadGraphAndWorkResponse)
    elif aMessageName == 'LoadWorkDetailsRequest':          return (LOAD_WORK_DETAILS_REQUEST, LoadWorkDetailsRequest)
    elif aMessageName == 'LoadWorkDetailsResponse':         return (LOAD_WORK_DETAILS_RESPONSE, LoadWorkDetailsResponse)
    elif aMessageName == 'PokeAnnouncement':                return (POKE_ANNOUNCEMENT, PokeAnnouncement)
    elif aMessageName == 'PresentYourselfRequest':          return (PRESENT_YOURSELF_REQUEST, PresentYourselfRequest)
    elif aMessageName == 'PresentYourselfResponse':         return (PRESENT_YOURSELF_RESPONSE, PresentYourselfResponse)
    # TODO: Raise a meaningful exception.
    # Not found.
    else:                                                   raise

def getMessageByHeaderId(aId):
    if False: pass
    elif aId == CANT_EXECUTE_WORK_NOW_ANNOUNCEMENT: return CantExecuteWorkNowAnnouncement()
    elif aId == COMMAND_DETERMINE_GRAPH_CYCLE_REQ:  return Command_DetermineGraphCycle_Req()
    elif aId == COMMAND_DETERMINE_GRAPH_CYCLE_RES:  return Command_DetermineGraphCycle_Res()
    elif aId == COMMAND_DETERMINE_WORK_CYCLE_REQ:   return Command_DetermineWorkCycle_Req()
    elif aId == COMMAND_DETERMINE_WORK_CYCLE_RES:   return Command_DetermineWorkCycle_Res()
    elif aId == COMMAND_ELECTION_REQ:               return Command_Election_Req()
    elif aId == COMMAND_ELECTION_RES:               return Command_Election_Res()
    elif aId == COMMAND_EXECUTE_GRAPH_REQ:          return Command_ExecuteGraph_Req()
    elif aId == COMMAND_EXECUTE_GRAPH_RES:          return Command_ExecuteGraph_Res()
    elif aId == COMMAND_EXECUTE_WORK_REQ:           return Command_ExecuteWork_Req()
    elif aId == COMMAND_EXECUTE_WORK_RES:           return Command_ExecuteWork_Res()
    elif aId == COMMAND_ORDER_WORK_EXECUTION_REQ:   return Command_OrderWorkExecution_Req()
    elif aId == COMMAND_ORDER_WORK_EXECUTION_RES:   return Command_OrderWorkExecution_Res()
    elif aId == HEARTBEAT_ANNOUNCEMENT:             return HeartbeatAnnouncement()
    elif aId == LOAD_GRAPH_AND_WORK_REQUEST:        return LoadGraphAndWorkRequest()
    elif aId == LOAD_GRAPH_AND_WORK_RESPONSE:       return LoadGraphAndWorkResponse()
    elif aId == LOAD_WORK_DETAILS_REQUEST:          return LoadWorkDetailsRequest()
    elif aId == LOAD_WORK_DETAILS_RESPONSE:         return LoadWorkDetailsResponse()
    elif aId == POKE_ANNOUNCEMENT:                  return PokeAnnouncement()
    elif aId == PRESENT_YOURSELF_REQUEST:           return PresentYourselfRequest()
    elif aId == PRESENT_YOURSELF_RESPONSE:          return PresentYourselfResponse()
    # TODO: Raise a meaningful exception.
    # Not found.
    else:                                           raise

def getCorrespondingPiewikType(aProtobufType):
    if False: pass
    # Structures.
    elif type(aProtobufType) is CritterData:                     return Piewik_CritterData
    elif type(aProtobufType) is GraphData:                       return Piewik_GraphData
    elif type(aProtobufType) is WorkData:                        return Piewik_WorkData
    elif type(aProtobufType) is WorkDetailsData:                 return Piewik_WorkDetailsData
    elif type(aProtobufType) is WorkPredecessorData:             return Piewik_WorkPredecessorData
    # Messages.
    elif type(aProtobufType) is CantExecuteWorkNowAnnouncement:  return Piewik_CantExecuteWorkNowAnnouncement
    elif type(aProtobufType) is Command_DetermineGraphCycle_Req: return Piewik_Command_DetermineGraphCycle_Req
    elif type(aProtobufType) is Command_DetermineGraphCycle_Res: return Piewik_Command_DetermineGraphCycle_Res
    elif type(aProtobufType) is Command_DetermineWorkCycle_Req:  return Piewik_Command_DetermineWorkCycle_Req
    elif type(aProtobufType) is Command_DetermineWorkCycle_Res:  return Piewik_Command_DetermineWorkCycle_Res
    elif type(aProtobufType) is Command_Election_Req:            return Piewik_Command_Election_Req
    elif type(aProtobufType) is Command_Election_Res:            return Piewik_Command_Election_Res
    elif type(aProtobufType) is Command_ExecuteGraph_Req:        return Piewik_Command_ExecuteGraph_Req
    elif type(aProtobufType) is Command_ExecuteGraph_Res:        return Piewik_Command_ExecuteGraph_Res
    elif type(aProtobufType) is Command_ExecuteWork_Req:         return Piewik_Command_ExecuteWork_Req
    elif type(aProtobufType) is Command_ExecuteWork_Res:         return Piewik_Command_ExecuteWork_Res
    elif type(aProtobufType) is Command_OrderWorkExecution_Req:  return Piewik_Command_OrderWorkExecution_Req
    elif type(aProtobufType) is Command_OrderWorkExecution_Res:  return Piewik_Command_OrderWorkExecution_Res
    elif type(aProtobufType) is HeartbeatAnnouncement:           return Piewik_HeartbeatAnnouncement
    elif type(aProtobufType) is LoadGraphAndWorkRequest:         return Piewik_LoadGraphAndWorkRequest
    elif type(aProtobufType) is LoadGraphAndWorkResponse:        return Piewik_LoadGraphAndWorkResponse
    elif type(aProtobufType) is LoadWorkDetailsRequest:          return Piewik_LoadWorkDetailsRequest
    elif type(aProtobufType) is LoadWorkDetailsResponse:         return Piewik_LoadWorkDetailsResponse
    elif type(aProtobufType) is PokeAnnouncement:                return Piewik_PokeAnnouncement
    elif type(aProtobufType) is PresentYourselfRequest:          return Piewik_PresentYourselfRequest
    elif type(aProtobufType) is PresentYourselfResponse:         return Piewik_PresentYourselfResponse
    # TODO: A meaningful exception.
    # Not found.
    else:                                                         raise
