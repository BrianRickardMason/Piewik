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
# TODO: Type conversion (e.g. in comparison).
#

#
# Exceptions used in Piewik type system.
#
class TypeSystemException(Exception):
    pass

class InvalidTTCN3Type(TypeSystemException):
    pass

class InvalidTTCN3TypeInComparison(InvalidTTCN3Type):
    pass

class UnmetRestriction(TypeSystemException):
    pass

#
# Types.
#
class TTCN3Type(object):
    def __init__(self, aValue, aRestrictions):
        self.mValue        = aValue
        self.mRestrictions = aRestrictions

        for restriction in self.mRestrictions:
            if restriction.check(self) == False:
                raise UnmetRestriction

    def __ne__(self, aOther):
        return not self.__eq__(aOther)

    def value(self):
        return self.mValue

class TTCN3MessageType(TTCN3Type):
    """Represents all types that might be used in a message or in a template."""
    def __init__(self, aValue, aRestrictions):
        TTCN3Type.__init__(self, aValue, aRestrictions)

class TTCN3TemplateType(TTCN3Type):
    """Represents all types that might be used in a template."""
    def __init__(self, aValue, aRestrictions):
        TTCN3Type.__init__(self, aValue, aRestrictions)

class TTCN3SimpleType(TTCN3MessageType):
    def __init__(self, aValue, aRestrictions):
        TTCN3Type.__init__(self, aValue, aRestrictions)

class TTCN3StructuredType(TTCN3MessageType):
    def __init__(self, aValue, aRestrictions):
        TTCN3Type.__init__(self, aValue, aRestrictions)

#
# Simple types.
#
class Boolean(TTCN3SimpleType):
    def __init__(self, aValue, aRestrictions=[]):
        if type(aValue) is not bool:
            raise InvalidTTCN3Type

        TTCN3SimpleType.__init__(self, aValue, aRestrictions)

    def __eq__(self, aOther):
        if isinstance(aOther, Boolean):
            return self.mValue == aOther.mValue
        else:
            raise InvalidTTCN3TypeInComparison

class Integer(TTCN3SimpleType):
    def __init__(self, aValue, aRestrictions=[]):
        if type(aValue) is not int:
            raise InvalidTTCN3Type

        TTCN3SimpleType.__init__(self, aValue, aRestrictions)

    def __eq__(self, aOther):
        if isinstance(aOther, Integer):
            return self.mValue == aOther.mValue
        elif isinstance(aOther, TTCN3SpecialSymbolType):
            return aOther == self
        else:
            raise InvalidTTCN3TypeInComparison

class Float(TTCN3SimpleType):
    def __init__(self, aValue, aRestrictions=[]):
        if type(aValue) is not float:
            raise InvalidTTCN3Type

        TTCN3SimpleType.__init__(self, aValue, aRestrictions)

    def __eq__(self, aOther):
        if isinstance(aOther, Float):
            return self.mValue == aOther.mValue
        else:
            raise InvalidTTCN3TypeInComparison

class Charstring(TTCN3SimpleType):
    def __init__(self, aValue, aRestrictions=[]):
        if type(aValue) is not str:
            raise InvalidTTCN3Type

        TTCN3SimpleType.__init__(self, aValue, aRestrictions)

    def __eq__(self, aOther):
        if isinstance(aOther, Charstring):
            return self.mValue == aOther.mValue
        else:
            raise InvalidTTCN3TypeInComparison

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
# Structured types.
#
class Enumeration(TTCN3StructuredType):
    pass

class Record(TTCN3StructuredType):
    def __init__(self, aValue={}, aRestrictions=[]):
        if type(aValue) is not dict:
            raise InvalidTTCN3Type

        for value in aValue.values():
            if not isinstance(value, TTCN3Type):
                raise InvalidTTCN3Type

        TTCN3StructuredType.__init__(self, aValue, aRestrictions)

    def __eq__(self, aOther):
        if isinstance(aOther, Record):
            if len(self.mValue) != len(aOther.mValue):
                return False

            for key in self.mValue.keys():
                if not key in aOther.mValue:
                    return False
                else:
                    if self.mValue[key] != aOther.mValue[key]:
                        return False
            return True
        else:
            return False

class Set(TTCN3StructuredType):
    pass

class Union(TTCN3StructuredType):
    pass

class RecordOf(TTCN3StructuredType):
    pass

class Array(TTCN3StructuredType):
    pass

class MultiDimensionalArray(TTCN3StructuredType):
    pass

class SetOf(TTCN3StructuredType):
    pass

#
# Special symbols.
#
class TTCN3SpecialSymbolType(TTCN3Type):
    def __init__(self, aValue, aRestrictions):
        TTCN3Type.__init__(self, aValue, aRestrictions)

#
# Special symbols used instead of values.
#
class TTCN3SpecialSymbolUsedInsteadOfAValueType(TTCN3SpecialSymbolType):
    pass

class Any(TTCN3SpecialSymbolUsedInsteadOfAValueType):
    def __init__(self, aValue=None, aRestrictions=[]):
        if aValue is not None or aRestrictions != []:
            raise InvalidTTCN3Type
        TTCN3SpecialSymbolType.__init__(self, aValue, aRestrictions)

    def __eq__(self, aOther):
        if isinstance(aOther, TTCN3Type):
            # TODO: Empty values.
            return True
        else:
            raise InvalidTTCN3Type

class AnyOrNone(TTCN3SpecialSymbolUsedInsteadOfAValueType):
    def __init__(self, aValue=None, aRestrictions=[]):
        if aValue is not None or aRestrictions != []:
            raise InvalidTTCN3Type
        TTCN3SpecialSymbolType.__init__(self, aValue, aRestrictions)

    def __eq__(self, aOther):
        if isinstance(aOther, TTCN3Type):
            return True
        else:
            raise InvalidTTCN3Type

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
