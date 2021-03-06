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

class Action(object):
    def __init__(self):
        self.mDone = False

    def execute(self):
        self.mDone = True

    def isDone(self):
        return self.mDone

class Blocking(Action):
    def __init__ (self, aEvExpectation):
        Action.__init__(self)
        self.mExpectation = aEvExpectation

    def applies(self, aEvent):
        if self.mExpectation.match(aEvent):
            return self
        else:
            return False

class Alternative(Action):
    def __init__(self, aListOfActions):
        self.mActionList = aListOfActions

    def applies(self, aEvent):
        for action in self.mActionList:
            command = action.applies(aEvent)
            if command:
                return command
        return False

    def isDone(self):
        for action in self.mActionList:
            if action.isDone():
                return True
        return False

class Interleave(Action):
    def __init__(self, aListOfActions):
        self.mActionList = aListOfActions

    def applies(self, aEvent):
        for action in self.mActionList:
            if not action.isDone():
                command = action.applies(aEvent)
                if command:
                    return command
        return False

    def isDone(self):
        for action in self.mActionList:
            if not action.isDone():
                return False
        return True
