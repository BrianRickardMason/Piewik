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

class Component(threading.Thread):
    def __init__(self, aName):
        threading.Thread.__init__(self, name=aName)

        self.mName       = aName
        self.mEventQueue = Queue.Queue()
        self.mRunning    = False
        self.mDone       = False

    def getVerdict(self):
        raise NotImplementedError

    def addFunction(self, aFunction):
        self.mFunction = aFunction

    def behaviour(self):
        self.mFunction(self)

    def run(self):
        self.mRunning = True
        try:
            self.behaviour()
        except:
            self.mRunning = False
            self.mDone    = True
            # Set verdict ERROR.
            raise
        self.mRunning = False
        self.mDone    = True

    def executeBlockingAction(self, aAction):
        event = self.mEventQueue.get()
        result = aAction.applies(event)

    def log(self, aString):
        print(self.mName + ": " + aString);

    def running(self):
        return self.mRunning

    def done(self):
        return self.mDone
