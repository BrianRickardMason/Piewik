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
# NOTE: The types are not initialized with a default value.
#

class TypeSystemException(Exception):
    pass

class InvalidTypeInAssignment(TypeSystemException):
    pass

class InvalidTypeInValueAssignment(TypeSystemException):
    pass

class InvalidTypeInComparison(TypeSystemException):
    pass

class InvalidTypeInCtor(TypeSystemException):
    pass

class LookupErrorMissingField(TypeSystemException):
    pass

#
# The values are needed to overload __eq__, etc... in a clean way.
#
class Value(object):
    def __eq__(self, aOther):
        raise NotImplementedError

    def __ne__(self, aOther):
        return not self.__eq__(aOther)

    def __gt__(self, aOther):
        raise NotImplementedError

    def __ge__(self, aOther):
        raise NotImplementedError

    def __lt__(self, aOther):
        raise NotImplementedError

    def __le__(self, aOther):
        raise NotImplementedError

class BooleanValue(Value):
    def __init__(self, aValue):
        if not type(aValue) is bool:
            raise InvalidTypeInValueAssignment
        self.mValue = aValue

    def __eq__(self, aOther):
        if isinstance(aOther, BooleanValue):
            return self.mValue == aOther.mValue
        elif isinstance(aOther, AnyValue):
            return aOther.__eq__(self)
        else:
            raise InvalidTypeInComparison

class IntegerValue(Value):
    def __init__(self, aValue):
        if not type(aValue) is int:
            raise InvalidTypeInValueAssignment
        self.mValue = aValue

    def __eq__(self, aOther):
        if isinstance(aOther, IntegerValue):
            return self.mValue == aOther.mValue
        elif isinstance(aOther, AnyValue):
            return aOther.__eq__(self)
        else:
            raise InvalidTypeInComparison

    def __gt__(self, aOther):
        if isinstance(aOther, IntegerValue):
            return self.mValue > aOther.mValue
        else:
            raise InvalidTypeInComparison

    def __ge__(self, aOther):
        if isinstance(aOther, IntegerValue):
            return self.mValue >= aOther.mValue
        else:
            raise InvalidTypeInComparison

    def __lt__(self, aOther):
        return not self.__ge__(aOther)

    def __le__(self, aOther):
        return not self.__gt__(aOther)

class FloatValue(Value):
    def __init__(self, aValue):
        if not type(aValue) is float:
            raise InvalidTypeInValueAssignment
        self.mValue = aValue

    def __eq__(self, aOther):
        if isinstance(aOther, FloatValue):
            return self.mValue == aOther.mValue
        elif isinstance(aOther, AnyValue):
            return aOther.__eq__(self)
        else:
            raise InvalidTypeInComparison

    def __gt__(self, aOther):
        if isinstance(aOther, FloatValue):
            return self.mValue > aOther.mValue
        else:
            raise InvalidTypeInComparison

    def __ge__(self, aOther):
        if isinstance(aOther, FloatValue):
            return self.mValue >= aOther.mValue
        else:
            raise InvalidTypeInComparison

    def __lt__(self, aOther):
        return not self.__ge__(aOther)

    def __le__(self, aOther):
        return not self.__gt__(aOther)

class CharstringValue(Value):
    def __init__(self, aValue):
        if not type(aValue) is str:
            raise InvalidTypeInValueAssignment
        self.mValue = aValue

    def __eq__(self, aOther):
        if isinstance(aOther, CharstringValue):
            return self.mValue == aOther.mValue
        elif isinstance(aOther, AnyValue):
            return aOther.__eq__(self)
        else:
            raise InvalidTypeInComparison

class AnyValue(Value):
    def __eq__(self, aOther):
        return True

class Type(object):
    def __eq__(self, aOther):
        raise NotImplementedError

    def __ne__(self, aOther):
        raise NotImplementedError

    def accept(self, aValue):
        raise NotImplementedError

    def assign(self, aValue):
        raise NotImplementedError

    def value(self):
        raise NotImplementedError

class SimpleType(Type):
    def __eq__(self, aOther):
        raise NotImplementedError

    def __ne__(self, aOther):
        raise NotImplementedError

    def accept(self, aValue):
        raise NotImplementedError

    def assign(self, aValue):
        raise NotImplementedError

    def value(self):
        raise NotImplementedError

class TypeDecorator(Type):
    def __init__(self, aDecoratedType):
        self.mDecoratedType = aDecoratedType

    def __eq__(self, aOther):
        if isinstance(aOther, TypeDecorator):
            return self.mValue == aOther.mValue
        else:
            raise InvalidTypeInComparison

    def __ne__(self, aOther):
        return not self.__eq__(aOther)

    def accept(self, aValue):
        raise NotImplementedError

    def assign(self, aValue):
        if not self.accept(aValue):
            raise InvalidTypeInAssignment
        self.mValue = aValue
        return self

    def value(self):
        return self.mValue

class Boolean(TypeDecorator):
    def __init__(self, aDecoratedType):
        TypeDecorator.__init__(self, aDecoratedType)

    def accept(self, aValue):
        return type(aValue) is BooleanValue

class Integer(TypeDecorator):
    def __init__(self, aDecoratedType):
        TypeDecorator.__init__(self, aDecoratedType)

    def accept(self, aValue):
        return type(aValue) is IntegerValue

class Float(TypeDecorator):
    def __init__(self, aDecoratedType):
        TypeDecorator.__init__(self, aDecoratedType)

    def accept(self, aValue):
        return type(aValue) is FloatValue

class Charstring(TypeDecorator):
    def __init__(self, aDecoratedType):
        TypeDecorator.__init__(self, aDecoratedType)

    def accept(self, aValue):
        return type(aValue) is CharstringValue

class Record(TypeDecorator):
    def __init__(self, aDecoratedType, aDictionary={}):
        if type(aDictionary) is not dict:
            raise InvalidTypeInCtor
        TypeDecorator.__init__(self, aDecoratedType)
        for key in aDictionary:
            if type(key) is not str:
                raise InvalidTypeInCtor
        for typeName in aDictionary.values():
            if not issubclass(typeName, TypeDecorator):
                raise InvalidTypeInCtor
            if issubclass(typeName, TemplateType):
                raise InvalidTypeInCtor
        self.mDictionary = aDictionary
        self.mValue = None

    # NOTE: Actually we should only make sure that we are comparing the record of the same types.
    #       All other checks should be redundant.
    def __eq__(self, aOther):
        # Make sure you compare only with a record...
        if not isinstance(aOther, Record):
            raise InvalidTypeInComparison
        # ...that is of the same type...
        if type(self) is not type(aOther):
            raise InvalidTypeInComparison
        # ...of the same length...
        if len(self.mValue) != len(aOther.mValue):
            raise InvalidTypeInComparison
        # ...which has mine keys...
        for key in self.mValue:
            if not key in aOther.mValue:
                raise InvalidTypeInComparison
        # ...and which's keys I have...
        for key in aOther.mValue:
            if not key in self.mValue:
                raise InvalidTypeInComparison
        # TODO: Remove me once TemplateRecord is introduced.
        #       This "for" statement is redundant (first condition checks it well enough).
        for value in aOther.mValue.values():
            # ...and that has only TypeDecorator values...
            if not isinstance(value, TypeDecorator):
                raise InvalidTypeInComparison
            # ...and that has not any TemplateType values...
            if isinstance(value, TemplateType):
                raise InvalidTypeInComparison
        # ...and which's values underneath keys are the same as mine...
        for key in self.mValue:
            if not isinstance(aOther.mValue[key], self.mDictionary[key]):
                raise InvalidTypeInComparison
        # ...and then compare...
        for key in self.mValue:
            if not self.mValue[key] == aOther.mValue[key]:
                return False
        return True

    def accept(self, aValue):
        if type(aValue) is not dict:
            return False
        if len(self.mDictionary) != len(aValue):
            return False
        for key in self.mDictionary:
            if not key in aValue:
                return False
        for key in aValue:
            if not key in self.mDictionary:
                return False
        for value in aValue.values():
            if not isinstance(value, TypeDecorator):
                return False
            if isinstance(value, TemplateType):
                return False
        for key in self.mDictionary:
            if not isinstance(aValue[key], self.mDictionary[key]):
                return False
        for key in self.mDictionary:
            if issubclass(self.mDictionary[key], Record):
                if aValue[key].mValue == None:
                    return False
        return True

    def getField(self, aName):
        if aName in self.mValue:
            return self.mValue[aName]
        else:
            raise LookupErrorMissingField

class BoundedType(TypeDecorator):
    def __init__(self, aDecoratedType, aLowerBoundary, aUpperBoundary):
        TypeDecorator.__init__(self, aDecoratedType)
        self.mLowerBoundary = aLowerBoundary
        self.mUpperBoundary = aUpperBoundary

    def accept(self, aValue):
        return self.mDecoratedType.accept(aValue) and \
               aValue >= self.mLowerBoundary      and \
               aValue <= self.mUpperBoundary

class TemplateType(TypeDecorator):
    def __init__(self, aDecoratedType):
        TypeDecorator.__init__(self, aDecoratedType)

    def accept(self, aValue):
        return self.mDecoratedType.accept(aValue) or \
               type(aValue) is AnyValue
