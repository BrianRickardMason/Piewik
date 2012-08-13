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

from Runtime.Action           import Alternative
from Runtime.Action           import Blocking
from Runtime.Action           import Interleave
from Runtime.Component        import Component
from Runtime.Control          import Control
from Runtime.Event            import PortReceivedEvent
from Runtime.EventExpectation import ComponentDoneExpectation
from Runtime.EventExpectation import PortReceiveExpectation
from Runtime.Port             import MessagePort
from Runtime.Testcase         import Testcase
from Runtime.TypeSystem       import Charstring

class MyPort(MessagePort):
    def __init__(self, aEventQueue):
        MessagePort.__init__(self,
                             aAddress=None,
                             aMapParam=None,
                             aUnmapParam=None,
                             aIn=[],
                             aOut=[],
                             aInOut=[Charstring])
        self.mEventQueue = aEventQueue
        self.mConnected  = None

    def inject(self, aMessage):
        if self.canReceive(aMessage):
            self.mEventQueue.put(PortReceivedEvent(self, aMessage, None))
        else:
            raise Exception

    def connect(self, aPort):
        self.mConnected = aPort

    def send(self, aMessage):
        if self.canSend(aMessage):
            self.mConnected.inject(aMessage)
        else:
            raise Exception

def connect(aPort1, aPort2):
    aPort1.connect(aPort2)
    aPort2.connect(aPort1)

class Function(object):
    def __init__(self):
        self.mRunsOn = None

class Function_SendMessage(Function):
    def __init__(self, aParameter):
        self.mRunsOn    = ComponentA
        self.mParameter = aParameter

    def __call__(self, aComponent):
        if isinstance(aComponent, self.mRunsOn):
            aComponent.mTestPort.send(self.mParameter)
        else:
            # TODO: Raise a meaningful exception.
            raise

class Function_ReceiveMessages(Function):
    def __init__(self):
        self.mRunsOn = ComponentB

    def __call__(self, aComponent):
        if isinstance(aComponent, self.mRunsOn):
            aComponent.executeBlockingAction(
                Alternative([
                    Blocking(PortReceiveExpectation(aComponent.mTestPortA1, Charstring().assign("Foo"))),
                    Blocking(PortReceiveExpectation(aComponent.mTestPortA2, Charstring().assign("Bar")))
                ])
            )
            aComponent.executeBlockingAction(
                Alternative([
                    Blocking(PortReceiveExpectation(aComponent.mTestPortA1, Charstring().assign("Foo"))),
                    Blocking(PortReceiveExpectation(aComponent.mTestPortA2, Charstring().assign("Bar")))
                ])
            )
        else:
            # TODO: Raise a meaningful exception.
            raise

class Mtc(Component):
    def __init__(self, aName, aTestcase):
        Component.__init__(self, aName)
        self.mTestcase = aTestcase

    def run(self):
        self.mTestcase.executePTC()

class ComponentA(Component):
    def __init__(self, aName):
        Component.__init__(self, aName)
        self.mTestPort = MyPort(self.mEventQueue)

class ComponentB(Component):
    def __init__(self, aName):
        Component.__init__(self, aName)
        self.mTestPortA1 = MyPort(self.mEventQueue)
        self.mTestPortA2 = MyPort(self.mEventQueue)

class SimpleTestcase(Testcase):
    def __init__(self):
        Testcase.__init__(self)
        self.mRunsOn = Mtc
        self.mMtc    = Mtc("MTC", self)

    def executeMTC(self):
        self.mMtc.start()
        self.mMtc.join()

    def executePTC(self):
        componentA1 = ComponentA("ComponentA1")
        componentA2 = ComponentA("ComponentA2")
        componentB  = ComponentB("ComponentB")

        # Setting the contexts.
        componentA1.setContext(self.mMtc, self)
        componentA2.setContext(self.mMtc, self)
        componentB .setContext(self.mMtc, self)

        componentA1.addFunction(Function_SendMessage(Charstring().assign("Foo")))
        componentA2.addFunction(Function_SendMessage(Charstring().assign("Bar")))
        componentB .addFunction(Function_ReceiveMessages())

        connect(componentA1.mTestPort, componentB.mTestPortA1)
        connect(componentA2.mTestPort, componentB.mTestPortA2)

        componentA1.start()
        componentA2.start()
        componentB .start()

        self.mMtc.executeBlockingAction(
            Interleave([
                Blocking(ComponentDoneExpectation(componentA1)),
                Blocking(ComponentDoneExpectation(componentA2)),
                Blocking(ComponentDoneExpectation(componentB ))
            ])
        )

        componentA1.join()
        componentA2.join()
        componentB .join()

testcase = SimpleTestcase()
control = Control()
control.execute(testcase)
