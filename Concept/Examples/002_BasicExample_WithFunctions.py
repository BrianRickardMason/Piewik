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

import os
os.sys.path.append("..")

from Concept.Action           import Blocking
from Concept.Component        import Component
from Concept.Component        import Mtc
from Concept.Control          import Control
from Concept.EventExpectation import PortReceiveExpectation
from Concept.Port             import Port
from Concept.Port             import connect
from Concept.Testcase         import Testcase

class Function(object):
    pass

class Function_ComponentA(Function):
    def __init__(self, aRunsOn):
        self.mRunsOn = aRunsOn

    def __call__(self, aComponent):
        if isinstance(aComponent, self.mRunsOn):
            aComponent.mTestPort.send("Foo")
        else:
            # TODO: Raise a meaningful exception.
            raise

class Function_ComponentB(Function):
    def __init__(self, aRunsOn):
        self.mRunsOn = aRunsOn

    def __call__(self, aComponent):
        if isinstance(aComponent, self.mRunsOn):
            aComponent.executeBlockingAction(Blocking(PortReceiveExpectation(aComponent.mTestPort)))
        else:
            # TODO: Raise a meaningful exception.
            raise

class ComponentA(Component):
    def __init__(self, aMtc, aSystem, aName):
        Component.__init__(self, aMtc, aSystem, aName)
        self.mTestPort = Port(self.mEventQueue)

    def addFunction(self, aFunction):
        self.mFunction = aFunction

    def behaviour(self):
        self.mFunction(self)

class ComponentB(Component):
    def __init__(self, aMtc, aSystem, aName):
        Component.__init__(self, aMtc, aSystem, aName)
        self.mTestPort = Port(self.mEventQueue)

    def addFunction(self, aFunction):
        self.mFunction = aFunction

    def behaviour(self):
        self.mFunction(self)

class SimpleTestcase(Testcase):
    def __init__(self):
        Testcase.__init__(self)

    def execute(self):
        componentA = ComponentA(self.mMtc, None, "ComponentA")
        componentA = ComponentA(self.mMtc, None, "ComponentA")
        componentB = ComponentB(self.mMtc, None, "ComponentB")

        componentA.addFunction(Function_ComponentA(ComponentA))
        componentB.addFunction(Function_ComponentB(ComponentB))

        connect(componentA.mTestPort, componentB.mTestPort)

        componentA.start()
        componentB.start()

        componentA.join()
        componentB.join()

c = Control(Mtc("MTC", SimpleTestcase()))
c()