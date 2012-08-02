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

import Queue
import threading

class ComponentReference(object):
    def __init__(self, aMtc, aSystem, aSelf):
        self.mMtc    = aMtc
        self.mSystem = aSystem
        self.mSelf   = aSelf

class Component(threading.Thread):
    def __init__(self, aMtc, aSystem, aName):
        threading.Thread.__init__(self, name=aName)

        self.mComponentReference = ComponentReference(aMtc, aSystem, self)
        self.mName               = aName
        self.mEventQueue         = Queue.Queue()

    def getVerdict(self):
        raise NotImplementedError

    def run(self):
        try:
            self.behaviour()
        except:
            # Set verdict ERROR.
            raise

    def executeBlockingAction(self, aAction):
        command = None
        repeat  = True
        while repeat:
            if not command:
                event = self.mEventQueue.get()
                command = aAction.applies(event)
            if command:
                repeat = False

    def log(self, aString):
        print(self.mName + ": " + aString);

class Mtc(Component):
    def __init__(self, aName, aTestcase):
        Component.__init__(self, self, None, aName)
        self.mTestcase = aTestcase

    def getVerdict(self):
        return True

    def run(self):
        self.mTestcase.setMtc(self)
        self.mTestcase.execute()
