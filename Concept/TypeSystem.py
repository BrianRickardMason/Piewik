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

#
# Piewik type system. An attempt to reach a type system as close to the TTCN-3's one as possible.
#
# A selected approach is to try to implement as many TTCN-3's features (template matching mechanism, subtyping,
# template restrictions, etc.) inside the type system.
#

#
# Exceptions used in Piewik type system.
#
class TypeSystemException(Exception):
    pass

class InvalidTTCN3TypeInCtor(TypeSystemException):
    pass

class InvalidTTCN3TypeInComparison(TypeSystemException):
    pass

#
# Types.
#
class TTCN3Type(object):
    def __init__(self, aValue):
        self.mValue = aValue

    def __ne__(self, aOther):
        return not self.__eq__(aOther)

    def value(self):
        return self.mValue

class TTCN3SimpleType(TTCN3Type):
    def __init__(self, aValue):
        TTCN3Type.__init__(self, aValue)

#
# Simple types.
#
class Boolean(TTCN3SimpleType):
    def __init__(self, aValue=False):
        if type(aValue) is not bool:
            raise InvalidTTCN3TypeInCtor

        TTCN3SimpleType.__init__(self, aValue)

    def __eq__(self, aOther):
        if isinstance(aOther, Boolean):
            return self.mValue == aOther.mValue
        else:
            raise InvalidTTCN3TypeInComparison

class Integer(TTCN3SimpleType):
    def __init__(self, aValue=0):
        if type(aValue) is not int:
            raise InvalidTTCN3TypeInCtor

        TTCN3SimpleType.__init__(self, aValue)

    def __eq__(self, aOther):
        if isinstance(aOther, Integer):
            return self.mValue == aOther.mValue
        else:
            raise InvalidTTCN3TypeInComparison

class Float(TTCN3SimpleType):
    def __init__(self, aValue=0.0):
        if type(aValue) is not float:
            raise InvalidTTCN3TypeInCtor

        TTCN3SimpleType.__init__(self, aValue)

    def __eq__(self, aOther):
        if isinstance(aOther, Float):
            return self.mValue == aOther.mValue
        else:
            raise InvalidTTCN3TypeInComparison

class Charstring(TTCN3SimpleType):
    pass
