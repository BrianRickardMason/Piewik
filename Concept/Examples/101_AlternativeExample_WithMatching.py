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

from Concept.Action           import Alternative
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
    def __init__(self, aParameter):
        self.mRunsOn    = ComponentA
        self.mParameter = aParameter

    def __call__(self, aComponent):
        if isinstance(aComponent, self.mRunsOn):
            aComponent.mTestPort.send(self.mParameter)
        else:
            # TODO: Raise a meaningful exception.
            raise

class Function_ComponentB(Function):
    def __init__(self):
        self.mRunsOn = ComponentB

    def __call__(self, aComponent):
        if isinstance(aComponent, self.mRunsOn):
            aComponent.executeBlockingAction(
                Alternative([
                    Blocking(PortReceiveExpectation(aComponent.mTestPortA1, "Foo")),
                    Blocking(PortReceiveExpectation(aComponent.mTestPortA2, "Bar"))
                ])
            )
            aComponent.executeBlockingAction(
                Alternative([
                    Blocking(PortReceiveExpectation(aComponent.mTestPortA1, "Foo")),
                    Blocking(PortReceiveExpectation(aComponent.mTestPortA2, "Bar"))
                ])
            )
        else:
            # TODO: Raise a meaningful exception.
            raise

class ComponentA(Component):
    def __init__(self, aMtc, aSystem, aName):
        Component.__init__(self, aMtc, aSystem, aName)
        self.mTestPort = Port(self.mEventQueue)

class ComponentB(Component):
    def __init__(self, aMtc, aSystem, aName):
        Component.__init__(self, aMtc, aSystem, aName)
        self.mTestPortA1 = Port(self.mEventQueue)
        self.mTestPortA2 = Port(self.mEventQueue)

class SimpleTestcase1(Testcase):
    def __init__(self):
        Testcase.__init__(self)

    def execute(self):
        componentA1 = ComponentA(self.mMtc, None, "ComponentA1")
        componentA2 = ComponentA(self.mMtc, None, "ComponentA2")
        componentB  = ComponentB(self.mMtc, None, "ComponentB")

        componentA1.addFunction(Function_ComponentA("Foo"))
        componentA2.addFunction(Function_ComponentA("Bar"))
        componentB .addFunction(Function_ComponentB())

        connect(componentA1.mTestPort, componentB.mTestPortA1)
        connect(componentA2.mTestPort, componentB.mTestPortA2)

        componentA1.start()
        componentA2.start()
        componentB.start()

        componentA1.join()
        componentA2.join()
        componentB.join()

class SimpleTestcase2(Testcase):
    def __init__(self):
        Testcase.__init__(self)

    def execute(self):
        componentA1 = ComponentA(self.mMtc, None, "ComponentA1")
        componentA2 = ComponentA(self.mMtc, None, "ComponentA2")
        componentB  = ComponentB(self.mMtc, None, "ComponentB")

        componentA1.addFunction(Function_ComponentA("Foo"))
        componentA2.addFunction(Function_ComponentA("Bar"))
        componentB .addFunction(Function_ComponentB())

        connect(componentA1.mTestPort, componentB.mTestPortA1)
        connect(componentA2.mTestPort, componentB.mTestPortA2)

        componentA2.start()
        componentA1.start()
        componentB.start()

        componentA1.join()
        componentA2.join()
        componentB.join()

c1 = Control(Mtc("MTC", SimpleTestcase1()))
c1()

c2 = Control(Mtc("MTC", SimpleTestcase2()))
c2()
