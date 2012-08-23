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

from Runtime.NewTypeSystem import Type

class Port(object):
    def __init__(self, aAddress, aMapParam, aUnmapParam, aIn, aOut, aInOut):
        self.__controlTypes(aIn, aOut, aInOut) # Self test.
        self.mAddress    = aAddress
        self.mMapParam   = aMapParam
        self.mUnmapParam = aUnmapParam
        self.mIn         = aIn
        self.mOut        = aOut
        self.mInOut      = aInOut

    def canSend(self, aMessage):
        if len(self.mOut)   > 0 or \
           len(self.mInOut) > 0    :
            for messageType in self.mOut:
                if isinstance(aMessage, messageType):
                    return True
            for messageType in self.mInOut:
                if isinstance(aMessage, messageType):
                    return True
            return False
        else:
            return True

    def canReceive(self, aMessage):
        if len(self.mIn)    > 0 or \
           len(self.mInOut) > 0    :
            for messageType in self.mIn:
                if isinstance(aMessage, messageType):
                    return True
            for messageType in self.mInOut:
                if isinstance(aMessage, messageType):
                    return True
            return False
        else:
            return True

    def __controlTypes(self, aIn, aOut, aInOut):
        # TODO: Add a meaningful exception.
        if type(aIn) is not list:
            raise Exception
        if type(aOut) is not list:
            raise Exception
        if type(aInOut) is not list:
            raise Exception
        for messageType in aIn:
            if not issubclass(messageType, Type):
                raise Exception
        for messageType in aOut:
            if not issubclass(messageType, Type):
                raise Exception
        for messageType in aInOut:
            if not issubclass(messageType, Type):
                raise Exception

class MessagePort(Port):
    def __init__(self, aAddress, aMapParam, aUnmapParam, aIn, aOut, aInOut):
        Port.__init__(self, aAddress, aMapParam, aUnmapParam, aIn, aOut, aInOut)

class ProcedurePort(Port):
    def __init__(self, aAddress, aMapParam, aUnmapParam, aIn, aOut, aInOut):
        raise NotImplementedError
