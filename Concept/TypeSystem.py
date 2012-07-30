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
# Part: Types.
#

#
# Exceptions used in Piewik type system.
#
class TypeSystemException(Exception):
    pass

class InvalidTTCN3TypeInAssignment(TypeSystemException):
    pass

class InvalidTTCN3TypeInBoundaryAssignment(TypeSystemException):
    pass

class InvalidTTCN3TypeValueNotInConstraint(TypeSystemException):
    pass

class LookupErrorMissingField(TypeSystemException):
    pass

class InvalidTTCN3TypeInCtor(TypeSystemException):
    pass

class InvalidTTCN3TypeInComparison(TypeSystemException):
    pass

class InvalidTypeOfDictionaryKey(TypeSystemException):
    pass

class InvalidTTCN3ValueInAssignment(TypeSystemException):
    pass

class InvalidTypeOfBoundary(TypeSystemException):
    pass

class InvalidTypeOfList(TypeSystemException):
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

    def accept(self, aValue):
        raise NotImplementedError

class TTCN3SimpleType(TTCN3Type):
    def __init__(self, aValue):
        TTCN3Type.__init__(self, aValue)

class TTCN3StructuredType(TTCN3Type):
    def __init__(self, aValue):
        TTCN3Type.__init__(self, aValue)

#
# Simple types.
#
class Boolean(TTCN3SimpleType):
    def __init__(self):
        TTCN3SimpleType.__init__(self, False)

    def __eq__(self, aOther):
        if isinstance(aOther, Boolean):
            return self.mValue == aOther.mValue
        else:
            raise InvalidTTCN3TypeInComparison

    def assign(self, aValue):
        if type(aValue) is not bool:
            raise InvalidTTCN3TypeInAssignment
        self.mValue = aValue
        return self

    def accept(self, aValue):
        return type(aValue) is bool

class Integer(TTCN3SimpleType):
    def __init__(self):
        TTCN3SimpleType.__init__(self, 0)

    def __eq__(self, aOther):
        if isinstance(aOther, Integer):
            return self.mValue == aOther.mValue
        else:
            raise InvalidTTCN3TypeInComparison

    def assign(self, aValue):
        if type(aValue) is not int:
            raise InvalidTTCN3TypeInAssignment
        self.mValue = aValue
        return self

    def accept(self, aValue):
        return type(aValue) is int

class Float(TTCN3SimpleType):
    def __init__(self):
        TTCN3SimpleType.__init__(self, 0.0)

    def __eq__(self, aOther):
        if isinstance(aOther, Float):
            return self.mValue == aOther.mValue
        else:
            raise InvalidTTCN3TypeInComparison

    def assign(self, aValue):
        if type(aValue) is not float:
            raise InvalidTTCN3TypeInAssignment
        self.mValue = aValue
        return self

    def accept(self, aValue):
        return type(aValue) is float

class Charstring(TTCN3SimpleType):
    def __init__(self):
        TTCN3SimpleType.__init__(self, "")

    def __eq__(self, aOther):
        if isinstance(aOther, Charstring):
            return self.mValue == aOther.mValue
        else:
            raise InvalidTTCN3TypeInComparison

    def assign(self, aValue):
        if type(aValue) is not str:
            raise InvalidTTCN3TypeInAssignment
        self.mValue = aValue
        return self

    def accept(self, aValue):
        return type(aValue) is str

#
# Structured types.
#
class Record(TTCN3StructuredType):
    def __init__(self, aDictionary={}):
        if type(aDictionary) is not dict:
            raise InvalidTTCN3TypeInCtor

        TTCN3StructuredType.__init__(self, {})

        # Keys may only be strings.
        for key in aDictionary:
            if type(key) is not str:
                raise InvalidTypeOfDictionaryKey

        # Values must be subtypes of TTCN3Type.
        for typeName in aDictionary.values():
            if not issubclass(typeName, TTCN3Type):
                raise InvalidTTCN3TypeInCtor

        self.mDictionary = aDictionary

    def __eq__(self, aOther):
        # TODO: Implement me.
        raise NotImplementedError

    def assign(self, aValue):
        if type(aValue) is not dict:
            raise InvalidTTCN3TypeInAssignement

        # TODO: Implement the verification of the assignment.
        self.mValue = aValue

    def accept(self, aValue):
        return type(aValue) is dict

    def value(self):
        raise NotImplementedError

    def getField(self, aName):
        if aName in self.mValue:
            return self.mValue[aName]
        else:
            raise LookupErrorMissingField

#
# Part: Subtypes.
#

#
# Boundaries.
#
class Boundary(object):
    pass

class BoundaryInteger(Boundary):
    def __init__(self, aValue, aClosed):
        if type(aValue)  is int  and \
           type(aClosed) is bool     :
            self.mValue  = aValue
            self.mClosed = aClosed
        else:
            raise InvalidTTCN3TypeInBoundaryAssignment

    def acceptLowerBoundary(self, aValue):
        if self.mClosed:
            return aValue >= self.mValue
        else:
            return aValue >  self.mValue

    def acceptUpperBoundary(self, aValue):
        if self.mClosed:
            return aValue <= self.mValue
        else:
            return aValue <  self.mValue

class BoundaryFloat(Boundary):
    def __init__(self, aValue, aClosed):
        if type(aValue)  is float and \
           type(aClosed) is bool      :
            self.mValue  = aValue
            self.mClosed = aClosed
        else:
            raise InvalidTTCN3TypeInBoundaryAssignment

    def acceptLowerBoundary(self, aValue):
        if self.mClosed:
            return aValue >= self.mValue
        else:
            return aValue >  self.mValue

    def acceptUpperBoundary(self, aValue):
        if self.mClosed:
            return aValue <= self.mValue
        else:
            return aValue <  self.mValue

#
# Subtypes.
#
class SubtypeOfSimpleType(object):
    pass

class ListOfTemplates(SubtypeOfSimpleType):
    # TODO: Check on assignment if all types are the same.
    def __init__(self, aList):
        if type(aList) is list:
            for item in aList:
                if not isinstance(item, TTCN3Type):
                    raise InvalidTTCN3TypeInCtor
            self.mList = aList
        else:
            raise InvalidTypeOfList

    def accept(self, aValue):
        for item in self.mList:
            if item.value() == aValue:
                return True
        return False

class ListOfTypes(SubtypeOfSimpleType):
    # TODO: Check on assignment if all types are the same.
    def __init__(self, aList):
        if type(aList) is list:
            for item in aList:
                if not isinstance(item, TTCN3Type):
                    raise InvalidTTCN3TypeInCtor
            self.mList = aList
        else:
            raise InvalidTypeOfList

    def accept(self, aValue):
        for item in self.mList:
            if item.accept(aValue):
                return True
        return False

class Range(SubtypeOfSimpleType):
    def __init__(self, aLowerBoundary, aUpperBoundary):
        if isinstance(aLowerBoundary, Boundary) and \
           isinstance(aUpperBoundary, Boundary)     :
            self.mLowerBoundary = aLowerBoundary
            self.mUpperBoundary = aUpperBoundary
        else:
            raise InvalidTypeOfBoundary

    def accept(self, aValue):
        if self.mLowerBoundary.acceptLowerBoundary(aValue) and \
           self.mUpperBoundary.acceptUpperBoundary(aValue)     :
            return True
        else:
            return False

class StringLength(SubtypeOfSimpleType):
    pass

class StringPattern(SubtypeOfSimpleType):
    pass
