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
class TTCN3SimpleType(TTCN3Type):
    def __init__(self, aValue, aRestrictions):
        TTCN3Type.__init__(self)

        self.mValue        = aValue
        self.mRestrictions = aRestrictions

        for restriction in self.mRestrictions:
            if restriction.check(self) == False:
                raise UnmetRestriction

class Boolean(TTCN3SimpleType):
    def __init__(self, aValue, aRestrictions=[]):
        if type(aValue) is not bool:
            raise InvalidTTCN3Type

        TTCN3SimpleType.__init__(self, aValue, aRestrictions)

    def __eq__(self, aOther):
        # TODO: On the fly conversion: e.g. integer.
        if isinstance(aOther, Boolean):
            return self.mValue == aOther.mValue
        else:
            return False

class Integer(TTCN3SimpleType):
    def __init__(self, aValue, aRestrictions=[]):
        if type(aValue) is not int:
            raise InvalidTTCN3Type

        TTCN3SimpleType.__init__(self, aValue, aRestrictions)

    def __eq__(self, aOther):
        if isinstance(aOther, Integer):
            return self.mValue == aOther.mValue
        else:
            return False

class Float(TTCN3SimpleType):
    def __init__(self, aValue, aRestrictions=[]):
        if type(aValue) is not float:
            raise InvalidTTCN3Type

        TTCN3SimpleType.__init__(self, aValue, aRestrictions)

    def __eq__(self, aOther):
        if isinstance(aOther, Float):
            return self.mValue == aOther.mValue
        else:
            return False

class Charstring(TTCN3SimpleType):
    def __init__(self, aValue, aRestrictions=[]):
        if type(aValue) is not str:
            raise InvalidTTCN3Type

        TTCN3SimpleType.__init__(self, aValue, aRestrictions)

    def __eq__(self, aOther):
        if isinstance(aOther, Charstring):
            return self.mValue == aOther.mValue
        else:
            return False

class UniversalCharstring(TTCN3SimpleType):
    pass

class Verdicttype(TTCN3SimpleType):
    pass

class Bitstring(TTCN3SimpleType):
    pass

class Octetstring(TTCN3SimpleType):
    pass

class Hexstring(TTCN3SimpleType):
    pass

class Objid(TTCN3SimpleType):
    pass

class Default(TTCN3SimpleType):
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
                raise UnmetRestriction

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

    def __eq__(self, aOther):
        if isinstance(aOther, Record):
            if len(self.mValue) != len(aOther.mValue):
                return False

            for key in self.mValue.keys():
                if not key in aOther.mValue:
                    return False
                else:
                    # TODO: Check !=.
                    if (self.mValue[key] == aOther.mValue[key]) == False:
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
# Special symbols.
#
class TTCN3SpecialSymbolType(TTCN3Type):
    def __init__(self, aValue, aRestrictions):
        TTCN3Type.__init__(self)

        self.mValue        = aValue
        self.mRestrictions = aRestrictions

        for restriction in self.mRestrictions:
            if restriction.check(self) == False:
                raise UnmetRestriction

#
# Special symbols used instead of values.
#
class TTCN3SpecialSymbolUsedInsteadOfAValueType(TTCN3SpecialSymbolType):
    pass

class Any(TTCN3SpecialSymbolUsedInsteadOfAValueType):
    def __init__(self, aValue=None, aRestrictions=None):
        TTCN3SpecialSymbolType.__init__(self, aValue, aRestrictions)

    def __eq__(self, aOther):
        if isinstance(aOther, TTCN3Type):
            return True
        else:
            return False

class AnyOrNone(TTCN3SpecialSymbolUsedInsteadOfAValueType):
    pass

class Omit(TTCN3SpecialSymbolUsedInsteadOfAValueType):
    pass

class List(TTCN3SpecialSymbolUsedInsteadOfAValueType):
    pass

class Complement(TTCN3SpecialSymbolUsedInsteadOfAValueType):
    pass

class Range(TTCN3SpecialSymbolUsedInsteadOfAValueType):
    pass

class Superset(TTCN3SpecialSymbolUsedInsteadOfAValueType):
    pass

class Subset(TTCN3SpecialSymbolUsedInsteadOfAValueType):
    pass

class Pattern(TTCN3SpecialSymbolUsedInsteadOfAValueType):
    pass

#
# Special symbols used inside values.
#
class TTCN3SpecialSymbolUsedInsideAValueType(TTCN3SpecialSymbolType):
    pass

class AnySingleElement(TTCN3SpecialSymbolUsedInsideAValueType):
    pass

class AnyNumberOfElements(TTCN3SpecialSymbolUsedInsideAValueType):
    pass

class Permutation(TTCN3SpecialSymbolUsedInsideAValueType):
    pass

#
# Special symbols which describe attributes of values.
#
class TTCN3SpecialSymbolWhichDescribeAttributeOfAValueType(TTCN3SpecialSymbolType):
    pass

# TODO: Introduce namespaces.
class SpecialSymbolLength(TTCN3SpecialSymbolWhichDescribeAttributeOfAValueType):
    pass

class Present(TTCN3SpecialSymbolWhichDescribeAttributeOfAValueType):
    pass

#
# Restrictions - exceptions.
#
class UnapplicableRestriction(Exception):
    pass

# TODO: Different type restrictions and template restrictions.

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
        # TODO: Assertion if any of allowed values is not an instance of TTCN3Type.
        if self.__checkApplicability(aType) == False:
            raise UnapplicableRestriction

        for allowedValue in self.mAllowedValues:
            if allowedValue == aType:
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
