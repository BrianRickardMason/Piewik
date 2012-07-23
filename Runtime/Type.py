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
# Types - exceptions.
#
class InvalidTTCN3Type(Exception):
    pass

class UnmetRestriction(Exception):
    pass

#
# Types.
#
class TTCN3Type(object):
    def __init__(self):
        self.mValue        = None
        self.mRestrictions = []

    def value(self):
        return self.mValue

#
# Built-in types.
#
class TTCN3BuiltInType(TTCN3Type):
    def __init__(self, aValue, aRestrictions):
        TTCN3Type.__init__(self)

        self.mValue        = aValue
        self.mRestrictions = aRestrictions

        for restriction in self.mRestrictions:
            if restriction.check(self) == False:
                raise UnmetRestriction()

class Boolean(TTCN3BuiltInType):
    def __init__(self, aValue, aRestrictions=[]):
        if type(aValue) is not bool:
            raise InvalidTTCN3Type

        TTCN3BuiltInType.__init__(self, aValue, aRestrictions)

    def match(self, aOtherType):
        # TODO: On the fly conversion: e.g. integer.
        if isinstance(aOtherType, Boolean):
            return self.mValue == aOtherType.mValue
        else:
            return False

class Integer(TTCN3BuiltInType):
    def __init__(self, aValue, aRestrictions=[]):
        if type(aValue) is not int:
            raise InvalidTTCN3Type

        TTCN3BuiltInType.__init__(self, aValue, aRestrictions)

    def match(self, aOtherType):
        if isinstance(aOtherType, Integer):
            return self.mValue == aOtherType.mValue
        else:
            return False

class Float(TTCN3BuiltInType):
    def __init__(self, aValue, aRestrictions=[]):
        if type(aValue) is not float:
            raise InvalidTTCN3Type

        TTCN3BuiltInType.__init__(self, aValue, aRestrictions)

    def match(self, aOtherType):
        if isinstance(aOtherType, Float):
            return self.mValue == aOtherType.mValue
        else:
            return False

class Charstring(TTCN3BuiltInType):
    def __init__(self, aValue, aRestrictions=[]):
        if type(aValue) is not str:
            raise InvalidTTCN3Type

        TTCN3BuiltInType.__init__(self, aValue, aRestrictions)

    def match(self, aOtherType):
        if isinstance(aOtherType, Charstring):
            return self.mValue == aOtherType.mValue
        else:
            return False

class UniversalCharstring(TTCN3BuiltInType):
    pass

class Verdicttype(TTCN3BuiltInType):
    pass

class Bitstring(TTCN3BuiltInType):
    pass

class Octetstring(TTCN3BuiltInType):
    pass

class Hexstring(TTCN3BuiltInType):
    pass

class Objid(TTCN3BuiltInType):
    pass

class Default(TTCN3BuiltInType):
    pass

#
# User-defined types.
#
class TTCN3UserDefinedType(TTCN3Type):
    def __init__(self, aValue, aRestrictions):
        TTCN3Type.__init__(self)

        self.mValue        = aValue
        self.mRestrictions = aRestrictions

        for restriction in self.mRestrictions:
            if restriction.check(self) == False:
                raise UnmetRestriction()

class Enumeration(TTCN3UserDefinedType):
    pass

class Record(TTCN3UserDefinedType):
    def __init__(self, aValue={}, aRestrictions=[]):
        if type(aValue) is not dict:
            raise InvalidTTCN3Type

        for value in aValue.values():
            if not isinstance(value, TTCN3Type):
                raise InvalidTTCN3Type

        TTCN3UserDefinedType.__init__(self, aValue, aRestrictions)

    def match(self, aOtherType):
        if isinstance(aOtherType, Record):
            if len(self.mValue) != len(aOtherType.mValue):
                return False

            for key in self.mValue.keys():
                if not key in aOtherType.mValue:
                    return False
                else:
                    if self.mValue[key].match(aOtherType.mValue[key]) == False:
                        return False
            return True
        else:
            return False

class Set(TTCN3UserDefinedType):
    pass

class Union(TTCN3UserDefinedType):
    pass

class RecordOf(TTCN3UserDefinedType):
    pass

class Array(TTCN3UserDefinedType):
    pass

class MultiDimensionalArray(TTCN3UserDefinedType):
    pass

class SetOf(TTCN3UserDefinedType):
    pass

#
# Restrictions - exceptions.
#
class UnapplicableRestriction(Exception):
    pass

#
# Restrictions.
#
class TTCN3Restriction(object):
    pass

class TypeAlias(TTCN3Restriction):
    pass

class ValueList(TTCN3Restriction):
    # TODO: Value list might not be empty.
    def __init__(self, aAllowedValues):
        self.mAllowedValues = aAllowedValues

    def check(self, aType):
        if self.__checkApplicability(aType) == False:
            raise UnapplicableRestriction

        for allowedValue in self.mAllowedValues:
            if allowedValue.match(aType):
                return True

        return False

    def __checkApplicability(self, aType):
        if isinstance(aType, Boolean   ) or \
           isinstance(aType, Integer   ) or \
           isinstance(aType, Float     ) or \
           isinstance(aType, Charstring)    :
            return True
        else:
            return False

class ValueRange(TTCN3Restriction):
    pass

class CharacterSet(TTCN3Restriction):
    pass

class Length(TTCN3Restriction):
    pass
