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

# TODO: Add verification of decorated types in AcceptDecorators.

from copy import deepcopy

class TypeSystemException(Exception):
    pass

class InvalidTypeInAssignment(TypeSystemException):
    pass

class InvalidTypeInValueAssignment(TypeSystemException):
    pass

class InvalidTypeInValueTypeAssignment(TypeSystemException):
    pass

class InvalidTypeInTypeAssignment(TypeSystemException):
    pass

class InvalidTypeInComparison(TypeSystemException):
    pass

class InvalidTypeInValueComparison(TypeSystemException):
    pass

class LookupErrorMissingField(TypeSystemException):
    pass

class TemplateAcceptDecoratorAppliedForASecondTimeError(TypeSystemException):
    pass

#
# The values are needed to overload __eq__, etc... in a clean way.
#
class Value(object):
    def __eq__(self, aValue):
        raise NotImplementedError

    def __ne__(self, aValue):
        return not self.__eq__(aValue)

    def __gt__(self, aValue):
        raise NotImplementedError

    def __ge__(self, aValue):
        raise NotImplementedError

    def __lt__(self, aValue):
        raise NotImplementedError

    def __le__(self, aValue):
        raise NotImplementedError

    def value(self):
        return self.mValue

class BooleanValue(Value):
    def __init__(self, aValue):
        if not type(aValue) is bool:
            raise InvalidTypeInValueAssignment
        self.mValue = aValue

    def __eq__(self, aValue):
        if isinstance(aValue, BooleanValue):
            return self.mValue == aValue.mValue
        elif isinstance(aValue, AnyValue):
            return aValue.__eq__(self)
        else:
            raise InvalidTypeInValueComparison

class IntegerValue(Value):
    def __init__(self, aValue):
        if not type(aValue) is int:
            raise InvalidTypeInValueAssignment
        self.mValue = aValue

    def __eq__(self, aValue):
        if isinstance(aValue, IntegerValue):
            return self.mValue == aValue.mValue
        elif isinstance(aValue, AnyValue):
            return aValue.__eq__(self)
        else:
            raise InvalidTypeInValueComparison

    def __gt__(self, aValue):
        if isinstance(aValue, IntegerValue):
            return self.mValue > aValue.mValue
        else:
            raise InvalidTypeInValueComparison

    def __ge__(self, aValue):
        return self.__gt__(aValue) or \
               self.__eq__(aValue)

    def __lt__(self, aValue):
        return not self.__ge__(aValue)

    def __le__(self, aValue):
        return not self.__gt__(aValue)

class FloatValue(Value):
    def __init__(self, aValue):
        if not type(aValue) is float:
            raise InvalidTypeInValueAssignment
        self.mValue = aValue

    def __eq__(self, aValue):
        if isinstance(aValue, FloatValue):
            return self.mValue == aValue.mValue
        elif isinstance(aValue, AnyValue):
            return aValue.__eq__(self)
        else:
            raise InvalidTypeInValueComparison

    def __gt__(self, aValue):
        if isinstance(aValue, FloatValue):
            return self.mValue > aValue.mValue
        else:
            raise InvalidTypeInValueComparison

    def __ge__(self, aValue):
        if isinstance(aValue, FloatValue):
            return self.__gt__(aValue) or \
                   self.__eq__(aValue)
        else:
            raise InvalidTypeInValueComparison

    def __lt__(self, aValue):
        return not self.__ge__(aValue)

    def __le__(self, aValue):
        return not self.__gt__(aValue)

class CharstringValue(Value):
    def __init__(self, aValue):
        if not type(aValue) is str:
            raise InvalidTypeInValueAssignment
        self.mValue = aValue

    def __eq__(self, aValue):
        if isinstance(aValue, CharstringValue):
            return self.mValue == aValue.mValue
        elif isinstance(aValue, AnyValue):
            return aValue.__eq__(self)
        else:
            raise InvalidTypeInValueComparison

    def __gt__(self, aValue):
        if isinstance(aValue, CharstringValue):
            return self.mValue > aValue.mValue
        else:
            raise InvalidTypeInValueComparison

    def __ge__(self, aValue):
        return self.__gt__(aValue) or \
               self.__eq__(aValue)

    def __lt__(self, aValue):
        return not self.__ge__(aValue)

    def __le__(self, aValue):
        return not self.__gt__(aValue)

class AnyValue(Value):
    def __eq__(self, aValue):
        return True

    def value(self):
        return self

class Type(object):
    def __init__(self):
        self.mValueType = None

    def __eq__(self, aTypeInstance):
        raise NotImplementedError

    def __ne__(self, aTypeInstance):
        return not self.__eq__(aTypeInstance)

    def accept(self, aValueType):
        raise NotImplementedError

    def assignType(self, aTypeInstance):
        raise NotImplementedError

    def assignValueType(self, aValueType):
        raise NotImplementedError

    def isCompatible(self, aTypeInstance):
        raise NotImplementedError

    def valueType(self):
        return self.mValueType

    def addAcceptDecorator(self, aAcceptDecoratorType, aAcceptDecoratorParams):
        self.mAcceptDecorator = aAcceptDecoratorType(self.mAcceptDecorator, aAcceptDecoratorParams)
        return self

class Boolean(Type):
    def __init__(self):
        Type.__init__(self)
        self.mAcceptDecorator = TypeAcceptDecorator(AcceptDecorator(), {'type': BooleanValue})

    def __eq__(self, aTypeInstance):
        if self.isCompatible(aTypeInstance):
            return self.valueType() == aTypeInstance.valueType()
        else:
            raise InvalidTypeInComparison

    def accept(self, aValueType):
        return self.mAcceptDecorator.accept(aValueType)

    def assignType(self, aTypeInstance):
        if self.isCompatible(aTypeInstance):
            self.mValueType = aTypeInstance.valueType()
        else:
            raise InvalidTypeInTypeAssignment
        return self

    def assignValueType(self, aValueType):
        if self.accept(aValueType):
            self.mValueType = aValueType
        else:
            raise InvalidTypeInValueTypeAssignment
        return self

    def isCompatible(self, aTypeInstance):
        if not isinstance(aTypeInstance, Boolean):
            return False
        if not self.accept(aTypeInstance.valueType()):
            return False
        return True

class Integer(Type):
    def __init__(self):
        Type.__init__(self)
        self.mAcceptDecorator = TypeAcceptDecorator(AcceptDecorator(), {'type': IntegerValue})

    def __eq__(self, aTypeInstance):
        if self.isCompatible(aTypeInstance):
            return self.valueType() == aTypeInstance.valueType()
        else:
            raise InvalidTypeInComparison

    def accept(self, aValueType):
        return self.mAcceptDecorator.accept(aValueType)

    def assignType(self, aTypeInstance):
        if self.isCompatible(aTypeInstance):
            self.mValueType = aTypeInstance.valueType()
        else:
            raise InvalidTypeInTypeAssignment
        return self

    def assignValueType(self, aValueType):
        if self.accept(aValueType):
            self.mValueType = aValueType
        else:
            raise InvalidTypeInValueTypeAssignment
        return self

    def isCompatible(self, aTypeInstance):
        if not isinstance(aTypeInstance, Integer):
            return False
        if not self.accept(aTypeInstance.valueType()):
            return False
        return True

class Float(Type):
    def __init__(self):
        Type.__init__(self)
        self.mAcceptDecorator = TypeAcceptDecorator(AcceptDecorator(), {'type': FloatValue})

    def __eq__(self, aTypeInstance):
        if self.isCompatible(aTypeInstance):
            return self.valueType() == aTypeInstance.valueType()
        else:
            raise InvalidTypeInComparison

    def accept(self, aValueType):
        return self.mAcceptDecorator.accept(aValueType)

    def assignType(self, aTypeInstance):
        if self.isCompatible(aTypeInstance):
            self.mValueType = aTypeInstance.valueType()
        else:
            raise InvalidTypeInTypeAssignment
        return self

    def assignValueType(self, aValueType):
        if self.accept(aValueType):
            self.mValueType = aValueType
        else:
            raise InvalidTypeInValueTypeAssignment
        return self

    def isCompatible(self, aTypeInstance):
        if not isinstance(aTypeInstance, Float):
            return False
        if not self.accept(aTypeInstance.valueType()):
            return False
        return True

class Charstring(Type):
    def __init__(self):
        Type.__init__(self)
        self.mAcceptDecorator = TypeAcceptDecorator(AcceptDecorator(), {'type': CharstringValue})

    def __eq__(self, aTypeInstance):
        if self.isCompatible(aTypeInstance):
            return self.valueType() == aTypeInstance.valueType()
        else:
            raise InvalidTypeInComparison

    def accept(self, aValueType):
        return self.mAcceptDecorator.accept(aValueType)

    def assignType(self, aTypeInstance):
        if self.isCompatible(aTypeInstance):
            self.mValueType = aTypeInstance.valueType()
        else:
            raise InvalidTypeInTypeAssignment
        return self

    def assignValueType(self, aValueType):
        if self.accept(aValueType):
            self.mValueType = aValueType
        else:
            raise InvalidTypeInValueTypeAssignment
        return self

    def isCompatible(self, aTypeInstance):
        if not isinstance(aTypeInstance, Charstring):
            return False
        if not self.accept(aTypeInstance.valueType()):
            return False
        return True

class Record(Type):
    def __init__(self, aDescriptorDictionary):
        Type.__init__(self)
        self.mAcceptDecorator = RecordAcceptDecorator(AcceptDecorator(), {'descriptorDictionary': aDescriptorDictionary})

    def __eq__(self, aTypeInstance):
        if self.isCompatible(aTypeInstance):
            return self.valueType() == aTypeInstance.valueType()
        else:
            raise InvalidTypeInComparison

    def accept(self, aValueType):
        return self.mAcceptDecorator.accept(aValueType)

    def assignType(self, aTypeInstance):
        if self.isCompatible(aTypeInstance):
            self.mValue = aTypeInstance.value()
            self.mValueType = aTypeInstance.valueType()
        else:
            raise InvalidTypeInTypeAssignment
        return self

    def assignValueType(self, aValueType):
        if self.accept(aValueType):
            tmpValue = {}
            for key in aValueType:
                if isinstance(self.mAcceptDecorator.descriptorDictionary()[key], Record):
                    tmpValue[key] = deepcopy(self.mAcceptDecorator.descriptorDictionary()[key]).assignValueType(aValueType[key])
                elif isinstance(self.mAcceptDecorator.descriptorDictionary()[key], RecordOf):
                    tmpValue[key] = deepcopy(self.mAcceptDecorator.descriptorDictionary()[key]).assignValueType(aValueType[key])
                else:
                    tmpValue[key] = aValueType[key]
            self.mValue = tmpValue
            self.mValueType = aValueType
        else:
            raise InvalidTypeInValueTypeAssignment
        return self

    def isCompatible(self, aTypeInstance):
        if not isinstance(aTypeInstance, Record):
            return False
        if not self.accept(aTypeInstance.valueType()):
            return False
        return True

    def value(self):
        return self.mValue

    def getField(self, aName):
        if aName in self.mValue:
            return self.mValue[aName]
        else:
            raise LookupErrorMissingField

class RecordOf(Type):
    def __init__(self, aDescriptorType):
        Type.__init__(self)
        self.mAcceptDecorator = RecordOfAcceptDecorator(AcceptDecorator(), {'descriptorType': aDescriptorType})

    def __eq__(self, aTypeInstance):
        if self.isCompatible(aTypeInstance):
            return self.valueType() == aTypeInstance.valueType()
        else:
            raise InvalidTypeInComparison

    def accept(self, aValueType):
        return self.mAcceptDecorator.accept(aValueType)

    def assignType(self, aTypeInstance):
        if self.isCompatible(aTypeInstance):
            # TODO: Add test of assignment of an uninitalized type.
            self.mValue = aTypeInstance.value()
            self.mValueType = aTypeInstance.valueType()
        else:
            raise InvalidTypeInTypeAssignment
        return self

    def assignValueType(self, aValueType):
        if self.accept(aValueType):
            tmpValue = []
            for valueType in aValueType:
                if isinstance(self.mAcceptDecorator.descriptorType(), Record):
                    tmpValue.append(deepcopy(self.mAcceptDecorator.descriptorType()).assignValueType(valueType))
                elif isinstance(self.mAcceptDecorator.descriptorType(), RecordOf):
                    tmpValue.append(deepcopy(self.mAcceptDecorator.descriptorType()).assignValueType(valueType))
                else:
                    tmpValue.append(valueType)
            self.mValue = tmpValue
            self.mValueType = aValueType
        else:
            raise InvalidTypeInValueTypeAssignment
        return self

    def isCompatible(self, aTypeInstance):
        if not isinstance(aTypeInstance, RecordOf):
            return False
        if not self.accept(aTypeInstance.valueType()):
            return False
        return True

    def value(self):
        return self.mValue

    def getField(self, aIndex):
        try:
            return self.mValue[aIndex]
        except:
            raise LookupErrorMissingField

# TODO: Define and check the hierarchy of accept decorators.
class AcceptDecorator(object):
    def accept(self, aValueType):
        return True

    def descriptorDictionary(self):
        raise NotImplementedError

class TypeAcceptDecorator(AcceptDecorator):
    def __init__(self, aAcceptDecorator, aAcceptDecoratorParams):
        self.mAcceptDecorator = aAcceptDecorator
        self.mType = aAcceptDecoratorParams['type']

    def accept(self, aValueType):
        return self.mAcceptDecorator.accept(aValueType) and \
               type(aValueType) is self.mType

class RecordAcceptDecorator(AcceptDecorator):
    def __init__(self, aAcceptDecorator, aAcceptDecoratorParams):
        self.mAcceptDecorator = aAcceptDecorator
        self.mDescriptorDictionary = aAcceptDecoratorParams['descriptorDictionary']

    def accept(self, aValueType):
        if not self.mAcceptDecorator.accept(aValueType):
            return False
        if type(aValueType) is not dict:
            return False
        if len(self.mDescriptorDictionary) != len(aValueType):
            return False
        for key in self.mDescriptorDictionary:
            if not key in aValueType:
                return False
        for key in aValueType:
            if not key in self.mDescriptorDictionary:
                return False
        for key in self.mDescriptorDictionary:
            if isinstance(self.mDescriptorDictionary[key], Record):
                if not self.mDescriptorDictionary[key].accept(aValueType[key]):
                    return False
            elif isinstance(self.mDescriptorDictionary[key], RecordOf):
                if not self.mDescriptorDictionary[key].accept(aValueType[key]):
                    return False
            elif isinstance(self.mDescriptorDictionary[key], Type):
                if not self.mDescriptorDictionary[key].isCompatible(aValueType[key]):
                    return False
            else:
                return False
        return True

    def descriptorDictionary(self):
        return self.mDescriptorDictionary

class RecordOfAcceptDecorator(AcceptDecorator):
    def __init__(self, aAcceptDecorator, aAcceptDecoratorParams):
        self.mAcceptDecorator = aAcceptDecorator
        self.mDescriptorType = aAcceptDecoratorParams['descriptorType']

    def accept(self, aValueType):
        if not self.mAcceptDecorator.accept(aValueType):
            return False
        if type(aValueType) is not list:
            return False
        for valueType in aValueType:
            if isinstance(self.mDescriptorType, Record):
                if not self.mDescriptorType.accept(valueType):
                    return False
            elif isinstance(self.mDescriptorType, RecordOf):
                if not self.mDescriptorType.accept(valueType):
                    return False
            elif isinstance(self.mDescriptorType, Type):
                if not self.mDescriptorType.isCompatible(valueType):
                    return False
            else:
                return False
        return True

    def descriptorType(self):
        return self.mDescriptorType

class RangedAcceptDecorator(AcceptDecorator):
    def __init__(self, aAcceptDecorator, aAcceptDecoratorParams):
        self.mAcceptDecorator = aAcceptDecorator
        self.mLowerBoundary = aAcceptDecoratorParams['lowerBoundary']
        self.mUpperBoundary = aAcceptDecoratorParams['upperBoundary']

    def accept(self, aValueType):
        return self.mAcceptDecorator.accept(aValueType) and \
               aValueType >= self.mLowerBoundary        and \
               aValueType <= self.mUpperBoundary

class TemplateAcceptDecorator(AcceptDecorator):
    def __init__(self, aAcceptDecorator, aAcceptDecoratorParams):
        if isinstance(aAcceptDecorator, TemplateAcceptDecorator):
            raise TemplateAcceptDecoratorAppliedForASecondTimeError
        if isinstance(aAcceptDecorator, RecordAcceptDecorator):
            for key in aAcceptDecorator.mDescriptorDictionary:
                aAcceptDecorator.mDescriptorDictionary[key].addAcceptDecorator(TemplateAcceptDecorator, aAcceptDecoratorParams)
            self.mAcceptDecorator = aAcceptDecorator
        if isinstance(aAcceptDecorator, RecordOfAcceptDecorator):
            aAcceptDecorator.mDescriptorType.addAcceptDecorator(TemplateAcceptDecorator, aAcceptDecoratorParams)
            self.mAcceptDecorator = aAcceptDecorator
        else:
            self.mAcceptDecorator = aAcceptDecorator

    def accept(self, aValueType):
        if isinstance(self.mAcceptDecorator, RecordAcceptDecorator):
            return self.mAcceptDecorator.accept(aValueType)
        else:
            return self.mAcceptDecorator.accept(aValueType) or \
                   type(aValueType) is AnyValue

    def descriptorDictionary(self):
        return self.mAcceptDecorator.descriptorDictionary()

    def descriptorType(self):
        return self.mAcceptDecorator.descriptorType()
