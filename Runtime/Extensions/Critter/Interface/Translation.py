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

from Runtime.TypeSystem import *

#
# NOTE: Header, Payload and Envelope are not translated.
#

class PiewikCritterData(Record):
    def __init__(self):
        Record.__init__(self,
                        SimpleType(),
                        {'type': Charstring(SimpleType()),
                         'nick': Charstring(SimpleType())})

class PiewikHeartbeatAnnouncement(Record):
    def __init__(self):
        Record.__init__(self,
                        SimpleType(),
                        {'messageName': Charstring(SimpleType()),
                         'sender':      PiewikCritterData(),
                         'timestamp':   Float(SimpleType())})

class PiewikPresentYourselfRequest(Record):
    def __init__(self):
        Record.__init__(self,
                        SimpleType(),
                        {'messageName': Charstring(SimpleType()),
                         'sender':      PiewikCritterData(),
                         'receiver':    PiewikCritterData()})

class PiewikPresentYourselfResponse(Record):
    def __init__(self):
        Record.__init__(self,
                        SimpleType(),
                        {'messageName': Charstring(SimpleType()),
                         'sender':      PiewikCritterData(),
                         'receiver':    PiewikCritterData()})

class PiewikPokeAnnouncement(Record):
    def __init__(self):
        Record.__init__(self,
                        SimpleType(),
                        {'messageName': Charstring(SimpleType()),
                         'sender':      PiewikCritterData()})

class PiewikExecuteGraphAnnouncement(Record):
    def __init__(self):
        Record.__init__(self,
                        SimpleType(),
                        {'messageName': Charstring(SimpleType()),
                         'sender':      PiewikCritterData(),
                         'graphName':   Charstring(SimpleType())})

class PiewikGraphData(Record):
    def __init__(self):
        Record.__init__(self,
                        SimpleType(),
                        {'graphName': Charstring(SimpleType())})

class PiewikWorkData(Record):
    def __init__(self):
        Record.__init__(self,
                        SimpleType(),
                        {'graphName': Charstring(SimpleType()),
                         'workName':  Charstring(SimpleType())})

class PiewikWorkPredecessorData(Record):
    def __init__(self):
        Record.__init__(self,
                        SimpleType(),
                        {'workName':           Charstring(SimpleType()),
                        'predecessorWorkName': Charstring(SimpleType())})

class PiewikRecordOfGraphData(RecordOf):
    def __init__(self):
        RecordOf.__init__(self, SimpleType(), PiewikGraphData())

class PiewikRecordOfWorkData(RecordOf):
    def __init__(self):
        RecordOf.__init__(self, SimpleType(), PiewikWorkData())

class PiewikRecordOfWorkPredecessorData(RecordOf):
    def __init__(self):
        RecordOf.__init__(self, SimpleType(), PiewikWorkPredecessorData())

class PiewikLoadGraphAndWorkRequest(Record):
    def __init__(self):
        Record.__init__(self,
                        SimpleType(),
                        {'messageName': Charstring(SimpleType()),
                         'sender':      PiewikCritterData()})

class PiewikLoadGraphAndWorkResponse(Record):
    def __init__(self):
        Record.__init__(self,
                        SimpleType(),
                        {'messageName':      Charstring(SimpleType()),
                         'sender':           PiewikCritterData(),
                         'receiver':         PiewikCritterData(),
                         'graphs':           PiewikRecordOfGraphData(),
                         'works':            PiewikRecordOfWorkData(),
                         'workPredecessors': PiewikRecordOfWorkPredecessorData()})

class PiewikWorkDetailsData(Record):
    def __init__(self):
        Record.__init__(self,
                        SimpleType(),
                        {'workName': Charstring(SimpleType()),
                         'dummy':    Integer(SimpleType())})

class PiewikRecordOfWorkDetailsData(RecordOf):
    def __init__(self):
        RecordOf.__init__(self, SimpleType(), PiewikWorkDetailsData())

class PiewikLoadWorkDetailsRequest(Record):
    def __init__(self):
        Record.__init__(self,
                        SimpleType(),
                        {'messageName': Charstring(SimpleType()),
                         'sender':      PiewikCritterData()})

class PiewikLoadWorkDetailsResponse(Record):
    def __init__(self):
        Record.__init__(self,
                        SimpleType(),
                        {'messageName': Charstring(SimpleType()),
                         'sender':      PiewikCritterData(),
                         'receiver':    PiewikCritterData(),
                         'details':     PiewikRecordOfWorkDetailsData()})

class PiewikDetermineGraphCycleRequest(Record):
    def __init__(self):
        Record.__init__(self,
                        SimpleType(),
                        {'messageName': Charstring(SimpleType()),
                         'sender':      PiewikCritterData(),
                         'graphName':   Charstring(SimpleType())})

class PiewikDetermineGraphCycleResponse(Record):
    def __init__(self):
        Record.__init__(self,
                        SimpleType(),
                        {'messageName': Charstring(SimpleType()),
                         'sender':      PiewikCritterData(),
                         'receiver':    PiewikCritterData(),
                         'graphName':   Charstring(SimpleType()),
                         'cycle':       Integer(SimpleType())})

class PiewikCommandWorkExecutionAnnouncement(Record):
    def __init__(self):
        Record.__init__(self,
                        SimpleType(),
                        {'messageName': Charstring(SimpleType()),
                         'sender':      PiewikCritterData(),
                         'graphName':   Charstring(SimpleType()),
                         'cycle':       Integer(SimpleType()),
                         'workName':    Charstring(SimpleType())})

class PiewikExecuteWorkAnnouncement(Record):
    def __init__(self):
        Record.__init__(self,
                        SimpleType(),
                        {'messageName': Charstring(SimpleType()),
                         'sender':      PiewikCritterData(),
                         'receiver':    PiewikCritterData(),
                         'graphName':   Charstring(SimpleType()),
                         'cycle':       Integer(SimpleType()),
                         'workName':    Charstring(SimpleType())})

class PiewikDetermineWorkCycleRequest(Record):
    def __init__(self):
        Record.__init__(self,
                        SimpleType(),
                        {'messageName': Charstring(SimpleType()),
                         'sender':      PiewikCritterData(),
                         'graphName':   Charstring(SimpleType()),
                         'cycle':       Integer(SimpleType()),
                         'workName':    Charstring(SimpleType())})

class PiewikDetermineWorkCycleResponse(Record):
    def __init__(self):
        Record.__init__(self,
                        SimpleType(),
                        {'messageName': Charstring(SimpleType()),
                         'sender':      PiewikCritterData(),
                         'receiver':    PiewikCritterData(),
                         'graphName':   Charstring(SimpleType()),
                         'cycle':       Integer(SimpleType()),
                         'workName':    Charstring(SimpleType()),
                         'workCycle':   Integer(SimpleType())})

class PiewikReportFinishedWorkAnnouncement(Record):
    def __init__(self):
        Record.__init__(self,
                        SimpleType(),
                        {'messageName': Charstring(SimpleType()),
                         'sender':      PiewikCritterData(),
                         'graphName':   Charstring(SimpleType()),
                         'graphCycle':  Integer(SimpleType()),
                         'workName':    Charstring(SimpleType()),
                         'workCycle':   Integer(SimpleType()),
                         'result':      Boolean(SimpleType())})

class PiewikCantExecuteWorkNowAnnouncement(Record):
    def __init__(self):
        Record.__init__(self,
                        SimpleType(),
                        {'messageName': Charstring(SimpleType()),
                         'sender':      PiewikCritterData(),
                         'receiver':    PiewikCritterData(),
                         'graphName':   Charstring(SimpleType()),
                         'cycle':       Integer(SimpleType()),
                         'workName':    Charstring(SimpleType())})
