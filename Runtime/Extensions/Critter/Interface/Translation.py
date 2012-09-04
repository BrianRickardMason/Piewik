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

from Runtime.NewTypeSystem import *

#
# NOTE: Header, Payload and Envelope are not translated.
#

class Piewik_CritterData(Record):
    def __init__(self):
        Record.__init__(self,
                        {'type': Charstring(),
                         'nick': Charstring()})

class Piewik_HeartbeatAnnouncement(Record):
    def __init__(self):
        Record.__init__(self,
                        {'messageName': Charstring(),
                         'sender':      Piewik_CritterData(),
                         'timestamp':   Float()})

class Piewik_PresentYourselfRequest(Record):
    def __init__(self):
        Record.__init__(self,
                        {'messageName': Charstring(),
                         'sender':      Piewik_CritterData(),
                         'receiver':    Piewik_CritterData()})

class Piewik_PresentYourselfResponse(Record):
    def __init__(self):
        Record.__init__(self,
                        {'messageName': Charstring(),
                         'sender':      Piewik_CritterData(),
                         'receiver':    Piewik_CritterData()})

class Piewik_PokeAnnouncement(Record):
    def __init__(self):
        Record.__init__(self,
                        {'messageName': Charstring(),
                         'sender':      Piewik_CritterData()})

class Piewik_GraphData(Record):
    def __init__(self):
        Record.__init__(self,
                        {'graphName': Charstring()})

class Piewik_WorkData(Record):
    def __init__(self):
        Record.__init__(self,
                        {'graphName': Charstring(),
                         'workName':  Charstring()})

class Piewik_WorkPredecessorData(Record):
    def __init__(self):
        Record.__init__(self,
                        {'workName':           Charstring(),
                        'predecessorWorkName': Charstring()})

class Piewik_RecordOfGraphData(RecordOf):
    def __init__(self):
        RecordOf.__init__(self, Piewik_GraphData())

class Piewik_RecordOfWorkData(RecordOf):
    def __init__(self):
        RecordOf.__init__(self, Piewik_WorkData())

class Piewik_RecordOfWorkPredecessorData(RecordOf):
    def __init__(self):
        RecordOf.__init__(self, Piewik_WorkPredecessorData())

class Piewik_LoadGraphAndWorkRequest(Record):
    def __init__(self):
        Record.__init__(self,
                        {'messageName': Charstring(),
                         'sender':      Piewik_CritterData()})

class Piewik_LoadGraphAndWorkResponse(Record):
    def __init__(self):
        Record.__init__(self,
                        {'messageName':      Charstring(),
                         'sender':           Piewik_CritterData(),
                         'receiver':         Piewik_CritterData(),
                         'graphs':           Piewik_RecordOfGraphData(),
                         'works':            Piewik_RecordOfWorkData(),
                         'workPredecessors': Piewik_RecordOfWorkPredecessorData()})

class Piewik_CantExecuteWorkNowAnnouncement(Record):
    def __init__(self):
        Record.__init__(self,
                        {'messageName': Charstring(),
                         'sender':      Piewik_CritterData(),
                         'receiver':    Piewik_CritterData(),
                         'graphName':   Charstring(),
                         'cycle':       Integer(),
                         'workName':    Charstring()})

class Piewik_WorkDetailsData(Record):
    def __init__(self):
        Record.__init__(self,
                        {'workName':    Charstring(),
                         'softTimeout': Integer(),
                         'hardTimeout': Integer(),
                         'dummy':       Integer()})

class Piewik_RecordOfWorkDetailsData(RecordOf):
    def __init__(self):
        RecordOf.__init__(self, Piewik_WorkDetailsData())

class Piewik_LoadWorkDetailsRequest(Record):
    def __init__(self):
        Record.__init__(self,
                        {'messageName': Charstring(),
                         'sender':      Piewik_CritterData()})

class Piewik_LoadWorkDetailsResponse(Record):
    def __init__(self):
        Record.__init__(self,
                        {'messageName': Charstring(),
                         'sender':      Piewik_CritterData(),
                         'receiver':    Piewik_CritterData(),
                         'details':     Piewik_RecordOfWorkDetailsData()})

class Piewik_Command_Election_Req(Record):
    def __init__(self):
        Record.__init__(self,
                        {'messageName': Charstring(),
                         'critthash':   Charstring(),
                         'crittnick':   Charstring()})

class Piewik_Command_Election_Res(Record):
    def __init__(self):
        Record.__init__(self,
                        {'messageName': Charstring(),
                         'critthash':   Charstring(),
                         'crittnick':   Charstring()})

class Piewik_Command_ExecuteGraph_Req(Record):
    def __init__(self):
        Record.__init__(self,
                        {'messageName':             Charstring(),
                         'graphExecutionCritthash': Charstring(),
                         'graphName':               Charstring()})

class Piewik_Command_ExecuteGraph_Res(Record):
    def __init__(self):
        Record.__init__(self,
                        {'messageName':             Charstring(),
                         'graphExecutionCritthash': Charstring()})

class Piewik_Command_DetermineGraphCycle_Req(Record):
    def __init__(self):
        Record.__init__(self,
                        {'messageName':             Charstring(),
                         'graphExecutionCritthash': Charstring(),
                         'graphName':               Charstring()})

class Piewik_Command_DetermineGraphCycle_Res(Record):
    def __init__(self):
        Record.__init__(self,
                        {'messageName':             Charstring(),
                         'graphExecutionCritthash': Charstring(),
                         'graphName':               Charstring(),
                         'graphCycle':              Integer()})

class Piewik_Command_OrderWorkExecution_Req(Record):
    def __init__(self):
        Record.__init__(self,
                        {'messageName':             Charstring(),
                         'graphExecutionCritthash': Charstring(),
                         'graphName':               Charstring(),
                         'graphCycle':              Integer(),
                         'workExecutionCritthash':  Charstring(),
                         'workName':                Charstring()})

class Piewik_Command_OrderWorkExecution_Res(Record):
    def __init__(self):
        Record.__init__(self,
                        {'messageName':             Charstring(),
                         'graphExecutionCritthash': Charstring(),
                         'graphName':               Charstring(),
                         'graphCycle':              Integer(),
                         'workExecutionCritthash':  Charstring(),
                         'workName':                Charstring()})

class Piewik_Command_ExecuteWork_Req(Record):
    def __init__(self):
        Record.__init__(self,
                        {'messageName':             Charstring(),
                         'receiverCrittnick':       Charstring(),
                         'graphExecutionCritthash': Charstring(),
                         'graphName':               Charstring(),
                         'graphCycle':              Integer(),
                         'workExecutionCritthash':  Charstring(),
                         'workName':                Charstring()})

class Piewik_Command_ExecuteWork_Res(Record):
    def __init__(self):
        Record.__init__(self,
                        {'messageName':             Charstring(),
                         'graphExecutionCritthash': Charstring(),
                         'graphName':               Charstring(),
                         'graphCycle':              Integer(),
                         'workExecutionCritthash':  Charstring(),
                         'workName':                Charstring()})

class Piewik_Command_DetermineWorkCycle_Req(Record):
    def __init__(self):
        Record.__init__(self,
                        {'messageName':             Charstring(),
                         'graphExecutionCritthash': Charstring(),
                         'graphName':               Charstring(),
                         'graphCycle':              Integer(),
                         'workExecutionCritthash':  Charstring(),
                         'workName':                Charstring()})

class Piewik_Command_DetermineWorkCycle_Res(Record):
    def __init__(self):
        Record.__init__(self,
                        {'messageName':             Charstring(),
                         'graphExecutionCritthash': Charstring(),
                         'graphName':               Charstring(),
                         'graphCycle':              Integer(),
                         'workExecutionCritthash':  Charstring(),
                         'workName':                Charstring(),
                         'workCycle':               Integer()})
