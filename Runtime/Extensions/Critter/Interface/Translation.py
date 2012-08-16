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
                        {'type': Charstring,
                         'nick': Charstring})

class PiewikHeartbeatAnnouncement(Record):
    def __init__(self):
        Record.__init__(self,
                        {'messageName': Charstring,
                         'sender':      PiewikCritterData,
                         'timestamp':   Float})

class PiewikPresentYourselfRequest(Record):
    def __init__(self):
        Record.__init__(self,
                        {'messageName': Charstring,
                         'sender':      PiewikCritterData,
                         'receiver':    PiewikCritterData})

class PiewikPresentYourselfResponse(Record):
    def __init__(self):
        Record.__init__(self,
                        {'messageName': Charstring,
                         'sender':      PiewikCritterData,
                         'receiver':    PiewikCritterData})

class PiewikPokeAnnouncement(Record):
    def __init__(self):
        Record.__init__(self,
                        {'messageName': Charstring,
                         'sender':      PiewikCritterData})

class PiewikExecuteGraphAnnouncement(Record):
    def __init__(self):
        Record.__init__(self,
                        {'messageName': Charstring,
                         'sender':      PiewikCritterData,
                         'graphName':   Charstring})

class PiewikGraphData(Record):
    def __init__(self):
        Record.__init__(self,
                        {'graphName': Charstring})

class PiewikWorkData(Record):
    def __init__(self):
        Record.__init__(self,
                        {'graphName': Charstring,
                         'workName':  Charstring})

class PiewikWorkPredecessorData(Record):
    def __init__(self):
        Record.__init__(self,
                        {'workName':           Charstring,
                        'predecessorWorkName': Charstring})

class PiewikLoadGraphAndWorkRequest(Record):
    def __init__(self):
        Record.__init__(self,
                        {'messageName': Charstring,
                         'sender':      PiewikCritterData})

class PiewikLoadGraphAndWorkResponse(Record):
    def __init__(self):
        Record.__init__(self,
                        {'messageName':      Charstring,
                         'sender':           PiewikCritterData,
                         'receiver':         PiewikCritterData,
                         'graphs':           RecordOf,
                         'works':            RecordOf,
                         'workPredecessors': RecordOf})

class PiewikWorkDetailsData(Record):
    def __init__(self):
        Record.__init__(self,
                        {'workName': Charstring,
                         'dummy':    Integer})

class PiewikLoadWorkDetailsRequest(Record):
    def __init__(self):
        Record.__init__(self,
                        {'messageName': Charstring,
                         'sender':      PiewikCritterData})

class PiewikLoadWorkDetailsResponse(Record):
    def __init__(self):
        Record.__init__(self,
                        {'messageName': Charstring,
                         'sender':      PiewikCritterData,
                         'receiver':    PiewikCritterData,
                         'details':     RecordOf})

class PiewikDetermineGraphCycleRequest(Record):
    def __init__(self):
        Record.__init__(self,
                        {'messageName': Charstring,
                         'sender':      PiewikCritterData,
                         'graphName':   Charstring})

class PiewikDetermineGraphCycleResponse(Record):
    def __init__(self):
        Record.__init__(self,
                        {'messageName': Charstring,
                         'sender':      PiewikCritterData,
                         'receiver':    PiewikCritterData,
                         'graphName':   Charstring,
                         'cycle':       Integer})

class PiewikCommandWorkExecutionAnnouncement(Record):
    def __init__(self):
        Record.__init__(self,
                        {'messageName': Charstring,
                         'sender':      PiewikCritterData,
                         'graphName':   Charstring,
                         'cycle':       Integer,
                         'workName':    Charstring})

class PiewikExecuteWorkAnnouncement(Record):
    def __init__(self):
        Record.__init__(self,
                        {'messageName': Charstring,
                         'sender':      PiewikCritterData,
                         'receiver':    PiewikCritterData,
                         'graphName':   Charstring,
                         'cycle':       Integer,
                         'workName':    Charstring})

class PiewikDetermineWorkCycleRequest(Record):
    def __init__(self):
        Record.__init__(self,
                        {'messageName': Charstring,
                         'sender':      PiewikCritterData,
                         'graphName':   Charstring,
                         'cycle':       Integer,
                         'workName':    Charstring})

class PiewikDetermineWorkCycleResponse(Record):
    def __init__(self):
        Record.__init__(self,
                        {'messageName': Charstring,
                         'sender':      PiewikCritterData,
                         'receiver':    PiewikCritterData,
                         'graphName':   Charstring,
                         'cycle':       Integer,
                         'workName':    Charstring,
                         'workCycle':   Integer})

class PiewikReportFinishedWorkAnnouncement(Record):
    def __init__(self):
        Record.__init__(self,
                        {'messageName': Charstring,
                         'sender':      PiewikCritterData,
                         'graphName':   Charstring,
                         'graphCycle':  Integer,
                         'workName':    Charstring,
                         'workCycle':   Integer,
                         'result':      Boolean})

