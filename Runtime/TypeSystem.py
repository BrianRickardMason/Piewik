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
# NOTES:
#
# The types are not initialized with a default value.
#

#
# TODO: Change isinstance to isOfType.
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

    def value(self):
        return self.mValue

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

    def value(self):
        return self

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
        raise NotImplementedError

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

    def isOfType(self, aType):
        if isinstance(self, aType):
            return True
        elif isinstance(self.mDecoratedType, aType):
            return True
        elif isinstance(self.mDecoratedType, SimpleType):
            return False
        else:
            return self.mDecoratedType.isOfType(aType)

class Boolean(TypeDecorator):
    def __init__(self, aDecoratedType):
        if not isinstance(aDecoratedType, SimpleType):
            raise InvalidTypeInCtor
        TypeDecorator.__init__(self, aDecoratedType)

    def __eq__(self, aOther):
        if not isinstance(aOther, TypeDecorator):
            raise InvalidTypeInComparison
        if aOther.isOfType(Boolean):
            return self.value() == aOther.value()
        else:
            raise InvalidTypeInComparison

    def accept(self, aValue):
        return type(aValue) is BooleanValue

class Integer(TypeDecorator):
    def __init__(self, aDecoratedType):
        if not isinstance(aDecoratedType, SimpleType):
            raise InvalidTypeInCtor
        TypeDecorator.__init__(self, aDecoratedType)

    def __eq__(self, aOther):
        if not isinstance(aOther, TypeDecorator):
            raise InvalidTypeInComparison
        if aOther.isOfType(Integer):
            return self.value() == aOther.value()
        else:
            raise InvalidTypeInComparison

    def accept(self, aValue):
        return type(aValue) is IntegerValue

class Float(TypeDecorator):
    def __init__(self, aDecoratedType):
        if not isinstance(aDecoratedType, SimpleType):
            raise InvalidTypeInCtor
        TypeDecorator.__init__(self, aDecoratedType)

    def __eq__(self, aOther):
        if not isinstance(aOther, TypeDecorator):
            raise InvalidTypeInComparison
        if aOther.isOfType(Float):
            return self.value() == aOther.value()
        else:
            raise InvalidTypeInComparison

    def accept(self, aValue):
        return type(aValue) is FloatValue

class Charstring(TypeDecorator):
    def __init__(self, aDecoratedType):
        if not isinstance(aDecoratedType, SimpleType):
            raise InvalidTypeInCtor
        TypeDecorator.__init__(self, aDecoratedType)

    def __eq__(self, aOther):
        if not isinstance(aOther, TypeDecorator):
            raise InvalidTypeInComparison
        if aOther.isOfType(Charstring):
            return self.value() == aOther.value()
        else:
            raise InvalidTypeInComparison

    def accept(self, aValue):
        return type(aValue) is CharstringValue

class Record(TypeDecorator):
    def __init__(self, aDecoratedType, aDictionary={}):
        # TODO: Add checking of what can be decorated with this decorator.
        if type(aDictionary) is not dict:
            raise InvalidTypeInCtor
        TypeDecorator.__init__(self, aDecoratedType)
        for key in aDictionary:
            if type(key) is not str:
                raise InvalidTypeInCtor
        for typeName in aDictionary.values():
            if not isinstance(typeName, TypeDecorator):
                raise InvalidTypeInCtor
            if isinstance(typeName, TemplateType):
                raise InvalidTypeInCtor
        self.mDictionary = aDictionary
        self.mValue = None

    def __eq__(self, aOther):
        if not isinstance(aOther, TypeDecorator):
            raise InvalidTypeInComparison
        # TODO: Consider moving it to simple types (different trees of inheritance).
        if aOther.isOfType(type(self)):
            return self.value() == aOther.value()
        else:
            raise InvalidTypeInComparison

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
        for key in self.mDictionary:
            if self.mDictionary[key].isOfType(Record):
                if not self.mDictionary[key].accept(aValue[key]):
                    return False
            elif self.mDictionary[key].isOfType(RecordOf):
                if not self.mDictionary[key].accept(aValue[key]):
                    return False
            elif self.mDictionary[key].isOfType(TypeDecorator):
                if isinstance(aValue[key], TypeDecorator):
                    if not self.mDictionary[key].accept(aValue[key].value()):
                        return False
                else:
                    return False
            else:
                return False
        return True

    def assign(self, aValue):
        if not self.accept(aValue):
            raise InvalidTypeInAssignment
        tmpValue = {}
        for key in aValue:
            if isinstance(self.mDictionary[key], Record):
                tmpValue[key] = type(self.mDictionary[key])().assign(aValue[key])
            elif isinstance(self.mDictionary[key], RecordOf):
                tmpValue[key] = type(self.mDictionary[key])().assign(aValue[key])
            else:
                tmpValue[key] = aValue[key]
        self.mValue = tmpValue
        return self

    def getField(self, aName):
        if aName in self.mValue:
            return self.mValue[aName]
        else:
            raise LookupErrorMissingField

class RecordOf(TypeDecorator):
    def __init__(self, aDecoratedType, aInstance):
        # TODO: Add checking of what can be decorated with this decorator.
        # Make sure the type is TypeDecorator...
        if not isinstance(aInstance, TypeDecorator):
            raise InvalidTypeInCtor
        # ...and the type is not any TemplateType...
        # TODO: (this should be done recursively for all decorated types to be 100% bullet proof)...
        if isinstance(aInstance, TemplateType):
            raise InvalidTypeInCtor
        TypeDecorator.__init__(self, aDecoratedType)
        self.mType = aInstance
        self.mValue = None

    def __eq__(self, aOther):
        if not isinstance(aOther, TypeDecorator):
            raise InvalidTypeInComparison
        # TODO: Consider moving it to simple types (different trees of inheritance).
        if aOther.isOfType(type(self)):
            return self.value() == aOther.value()
        else:
            raise InvalidTypeInComparison

    def accept(self, aValue):
        if type(aValue) is not list:
            return False
        for value in aValue:
            if self.mType.isOfType(Record):
                if not self.mType.accept(value):
                    return False
            elif self.mType.isOfType(RecordOf):
                if not self.mType.accept(value):
                    return False
            elif self.mType.isOfType(TypeDecorator):
                if isinstance(value, TypeDecorator):
                    if isinstance(value, TemplateType):
                        if self.mType.isOfType(TemplateRecordOf) or \
                           self.mType.isOfType(TemplateRecord)   or \
                           self.mType.isOfType(TemplateType)        :
                            if not self.mType.accept(value.value()):
                                return False
                        else:
                            return False
                    else:
                        if not self.mType.accept(value.value()):
                            return False
                else:
                    return False
            else:
                return False
        return True

    def assign(self, aValue):
        if not self.accept(aValue):
            raise InvalidTypeInAssignment
        tmpValue = []
        for value in aValue:
            # TODO: Check it out again!
            if isinstance(self.mType, Record):
                if not type(value) is dict:
                    raise InvalidTypeInAssignment
                tmpValue.append(type(self.mType)().assign(value))
            elif isinstance(value, RecordOf):
                if not type(value) is list:
                    raise InvalidTypeInAssignment
                tmpValue.append(type(self.mType)().assign(value))
            else:
                tmpValue.append(value)
        self.mValue = tmpValue
        return self

    def getField(self, aIndex):
        try:
            return self.mValue[aIndex]
        except:
            raise LookupErrorMissingField

class BoundedType(TypeDecorator):
    def __init__(self, aDecoratedType, aLowerBoundary, aUpperBoundary):
        # TODO: Add checking of what can be decorated with this decorator.
        TypeDecorator.__init__(self, aDecoratedType)
        self.mLowerBoundary = aLowerBoundary
        self.mUpperBoundary = aUpperBoundary

    def __eq__(self, aOther):
        return self.mDecoratedType.__eq__(aOther)

    def accept(self, aValue):
        return self.mDecoratedType.accept(aValue) and \
               aValue >= self.mLowerBoundary      and \
               aValue <= self.mUpperBoundary

    def assign(self, aValue):
        if not self.accept(aValue):
            raise InvalidTypeInAssignment
        self.mDecoratedType.mValue = aValue
        return self

    def value(self):
        return self.mDecoratedType.value()

class TemplateType(TypeDecorator):
    def __init__(self, aDecoratedType):
        # TODO: Add checking of what can be decorated with this decorator.
        TypeDecorator.__init__(self, aDecoratedType)

    def __eq__(self, aOther):
        return self.mDecoratedType.__eq__(aOther)

    def accept(self, aValue):
        return self.mDecoratedType.accept(aValue) or \
               type(aValue) is AnyValue

    def assign(self, aValue):
        if not self.accept(aValue):
            raise InvalidTypeInAssignment
        self.mDecoratedType.mValue = aValue
        return self

    def value(self):
        return self.mDecoratedType.value()

class TemplateRecord(TypeDecorator):
    def __init__(self, aDecoratedType):
        if not isinstance(aDecoratedType, Record):
            raise InvalidTypeInCtor
        if isinstance(aDecoratedType, TemplateRecord):
            raise InvalidTypeInCtor
        # ...enforce the decoration of all types...
        for key in aDecoratedType.mDictionary:
            if aDecoratedType.mDictionary[key].isOfType(Record):
                aDecoratedType.mDictionary[key] = TemplateRecord(aDecoratedType.mDictionary[key])
            elif aDecoratedType.mDictionary[key].isOfType(RecordOf):
                aDecoratedType.mDictionary[key] = TemplateRecordOf(aDecoratedType.mDictionary[key])
            elif aDecoratedType.mDictionary[key].isOfType(Boolean   ) or \
                 aDecoratedType.mDictionary[key].isOfType(Integer   ) or \
                 aDecoratedType.mDictionary[key].isOfType(Float     ) or \
                 aDecoratedType.mDictionary[key].isOfType(Charstring)    :
                aDecoratedType.mDictionary[key] = TemplateType(aDecoratedType.mDictionary[key])
            else:
                # TODO: A meaningful exception.
                raise Exception
        TypeDecorator.__init__(self, aDecoratedType)

    def __eq__(self, aOther):
        return self.mDecoratedType.__eq__(aOther)

    def accept(self, aValue):
        return self.mDecoratedType.accept(aValue)

    def assign(self, aValue):
        if not self.accept(aValue):
            raise InvalidTypeInAssignment
        self.mDecoratedType.mValue = aValue
        return self

    def value(self):
        return self.mDecoratedType.value()

    def getField(self, aName):
        if aName in self.value():
            return self.value()[aName]
        else:
            raise LookupErrorMissingField

class TemplateRecordOf(TypeDecorator):
    def __init__(self, aDecoratedType):
        # TODO: Add checking of what can be decorated with this decorator.
        # Make sure the type is TypeDecorator...
        if not isinstance(aDecoratedType, RecordOf):
            raise InvalidTypeInCtor
        if isinstance(aDecoratedType, TemplateRecordOf):
            raise InvalidTypeInCtor
        # ...enforce the decoration of the type...
        if aDecoratedType.mType.isOfType(Record):
            aDecoratedType.mType = TemplateRecord(aDecoratedType.mType)
        elif aDecoratedType.mType.isOfType(RecordOf):
            aDecoratedType.mType = TemplateRecordOf(aDecoratedType.mType)
        elif aDecoratedType.mType.isOfType(Boolean   ) or \
             aDecoratedType.mType.isOfType(Integer   ) or \
             aDecoratedType.mType.isOfType(Float     ) or \
             aDecoratedType.mType.isOfType(Charstring)    :
            aDecoratedType.mType = TemplateType(aDecoratedType.mType)
        else:
            # TODO: A meaningful exception.
            raise Exception
        TypeDecorator.__init__(self, aDecoratedType)

    def __eq__(self, aOther):
        if not isinstance(aOther, TypeDecorator):
            raise InvalidTypeInComparison
        # TODO: Consider moving it to simple types (different trees of inheritance).
        if aOther.isOfType(type(self)):
            return self.value() == aOther.value()
        else:
            raise InvalidTypeInComparison

    def accept(self, aValue):
        return self.mDecoratedType.accept(aValue)

    def getField(self, aIndex):
        try:
            return self.mValue[aIndex]
        except:
            raise LookupErrorMissingField
