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

import unittest

from Runtime.NewTypeSystem import *

# Helpers.

class TemplateInteger(Integer):
    def __init__(self):
        Integer.__init__(self)
        self.mAcceptDecorator = TemplateAcceptDecorator(self.mAcceptDecorator, {})

# Tests.

class TypeSystem_Integer_Ctor(unittest.TestCase):
    def test_Ctor(self):
        Integer()

class TypeSystem_Integer_IsCompatible(unittest.TestCase):
    def test_IsCompatibleReturnsFlaseOnAnIncompatibleType_Self_NotInitialized(self):
        typeInstance = Integer()
        self.assertFalse(typeInstance.isCompatible(typeInstance))

    def test_IsCompatibleReturnsCorrectValue_Self_Mixed(self):
        typeInstance1 = Integer()
        typeInstance2 = Integer().assignValueType(IntegerValue(1))
        self.assertTrue(typeInstance1.isCompatible(typeInstance2))
        self.assertFalse(typeInstance2.isCompatible(typeInstance1))

    def test_IsCompatibleReturnsTrueOnACompatibleType_Self_Initialized(self):
        typeInstance = Integer().assignValueType(IntegerValue(1))
        self.assertTrue(typeInstance.isCompatible(typeInstance))

    def test_IsCompatibleReturnsTrueOnACompatibleType_RangedType(self):
        typeInstance1 = Integer().assignValueType(IntegerValue(1))
        typeInstance2 = Integer()
        typeInstance2.addAcceptDecorator(RangedAcceptDecorator, {'lowerBoundary': IntegerValue(0),
                                                                 'upperBoundary': IntegerValue(10)})
        typeInstance2.assignValueType(IntegerValue(1))
        self.assertTrue(typeInstance1.isCompatible(typeInstance2))
        self.assertTrue(typeInstance2.isCompatible(typeInstance1))

    def test_IsCompatibleReturnsTrueOnACompatibleType_Subtyped(self):
        typeInstance1 = Integer().assignValueType(IntegerValue(1))
        class MyInteger(Integer):
            def __init__(self):
                Integer.__init__(self)
        typeInstance2 = MyInteger().assignValueType(IntegerValue(1))
        self.assertTrue(typeInstance1.isCompatible(typeInstance2))
        self.assertTrue(typeInstance2.isCompatible(typeInstance1))

    def test_IsCompatibleReturnsTrueOnACompatibleType_DoubleSubtyped(self):
        typeInstance1 = Integer().assignValueType(IntegerValue(1))
        class MyInteger(Integer):
            def __init__(self):
                Integer.__init__(self, )
        class MyInteger2(MyInteger):
            def __init__(self):
                MyInteger.__init__(self)
        typeInstance2 = MyInteger2().assignValueType(IntegerValue(1))
        self.assertTrue(typeInstance1.isCompatible(typeInstance2))
        self.assertTrue(typeInstance2.isCompatible(typeInstance1))

    def test_IsCompatibleReturnsTrueOnACompatibleType_Template_WithoutSpecialValues(self):
        typeInstance1 = Integer().assignValueType(IntegerValue(1))
        typeInstance2 = Integer()
        typeInstance2.addAcceptDecorator(TemplateAcceptDecorator, {})
        typeInstance2.assignValueType(IntegerValue(1))
        self.assertTrue(typeInstance1.isCompatible(typeInstance2))
        self.assertTrue(typeInstance2.isCompatible(typeInstance1))

    def test_IsCompatibleReturnsFalseOnAnIncompatibleType_Template_WithSpecialValues(self):
        typeInstance1 = Integer().assignValueType(IntegerValue(1))
        typeInstance2 = Integer()
        typeInstance2.addAcceptDecorator(TemplateAcceptDecorator, {})
        typeInstance2.assignValueType(AnyValue())
        self.assertFalse(typeInstance1.isCompatible(typeInstance2))
        self.assertTrue(typeInstance2.isCompatible(typeInstance1))

    def test_IsCompatibleReturnsFalseOnAnIncompatibleType_BuiltIn(self):
        typeInstance1 = Integer()
        for typeInstance2 in [True, 1.0, "WAX"]:
            self.assertFalse(typeInstance1.isCompatible(typeInstance2))

    def test_IsCompatibleReturnsFalseOnAnIncompatibleType_Regular(self):
        self.skipTest("Not implemented yet.")

    def test_IsCompatibleReturnsFalseOnAnIncompatibleType_Special(self):
        typeInstance1 = Integer()
        for typeInstance2 in [AnyValue()]:
            self.assertFalse(typeInstance1.isCompatible(typeInstance2))

class TypeSystem_Integer_Ranged_IsCompatible(unittest.TestCase):
    def test_IsCompatibleReturnsFlaseOnAnIncompatibleType_Self_NotInitialized(self):
        typeInstance = Integer().addAcceptDecorator(RangedAcceptDecorator, {'lowerBoundary': IntegerValue(0),
                                                                            'upperBoundary': IntegerValue(10)})
        self.assertFalse(typeInstance.isCompatible(typeInstance))

    def test_IsCompatibleReturnsCorrectValue_Self_Mixed(self):
        typeInstance1 = Integer().addAcceptDecorator(RangedAcceptDecorator, {'lowerBoundary': IntegerValue(0),
                                                                             'upperBoundary': IntegerValue(10)})
        typeInstance2 = Integer().addAcceptDecorator(RangedAcceptDecorator, {'lowerBoundary': IntegerValue(0),
                                                                             'upperBoundary': IntegerValue(10)}).assignValueType(IntegerValue(1))
        self.assertTrue(typeInstance1.isCompatible(typeInstance2))
        self.assertFalse(typeInstance2.isCompatible(typeInstance1))

    def test_IsCompatibleReturnsTrueOnACompatibleType_Self_Initialized(self):
        typeInstance = Integer().addAcceptDecorator(RangedAcceptDecorator, {'lowerBoundary': IntegerValue(0),
                                                                            'upperBoundary': IntegerValue(10)}).assignValueType(IntegerValue(1))
        self.assertTrue(typeInstance.isCompatible(typeInstance))

    def test_IsCompatibleReturnsTrueOnACompatibleType_Subtyped(self):
        typeInstance1 = Integer().addAcceptDecorator(RangedAcceptDecorator, {'lowerBoundary': IntegerValue(0),
                                                                             'upperBoundary': IntegerValue(10)}).assignValueType(IntegerValue(1))
        class MyInteger(Integer):
            def __init__(self):
                Integer.__init__(self)
                self.mAcceptDecorator = RangedAcceptDecorator(self.mAcceptDecorator, {'lowerBoundary': IntegerValue(0),
                                                                                      'upperBoundary': IntegerValue(10)})
        typeInstance2 = MyInteger().assignValueType(IntegerValue(1))
        self.assertTrue(typeInstance1.isCompatible(typeInstance2))
        self.assertTrue(typeInstance2.isCompatible(typeInstance1))

    def test_IsCompatibleReturnsTrueOnACompatibleType_DoubleSubtyped(self):
        typeInstance1 = Integer().addAcceptDecorator(RangedAcceptDecorator, {'lowerBoundary': IntegerValue(0),
                                                                             'upperBoundary': IntegerValue(10)}).assignValueType(IntegerValue(1))
        class MyInteger(Integer):
            def __init__(self):
                Integer.__init__(self)
                self.mAcceptDecorator = RangedAcceptDecorator(self.mAcceptDecorator, {'lowerBoundary': IntegerValue(0),
                                                                                      'upperBoundary': IntegerValue(10)})
        class MyInteger2(MyInteger):
            def __init__(self):
                MyInteger.__init__(self)
        typeInstance2 = MyInteger2().assignValueType(IntegerValue(1))
        self.assertTrue(typeInstance1.isCompatible(typeInstance2))
        self.assertTrue(typeInstance2.isCompatible(typeInstance1))

    def test_IsCompatibleReturnsTrueOnACompatibleType_Template_WithoutSpecialValues(self):
        typeInstance1 = Integer().addAcceptDecorator(RangedAcceptDecorator, {'lowerBoundary': IntegerValue(0),
                                                                             'upperBoundary': IntegerValue(10)}).assignValueType(IntegerValue(1))
        typeInstance2 = Integer().addAcceptDecorator(RangedAcceptDecorator, {'lowerBoundary': IntegerValue(0),
                                                                             'upperBoundary': IntegerValue(10)}).\
                                  addAcceptDecorator(TemplateAcceptDecorator, {}).\
                                  assignValueType(IntegerValue(1))
        self.assertTrue(typeInstance1.isCompatible(typeInstance2))
        self.assertTrue(typeInstance2.isCompatible(typeInstance1))

    def test_IsCompatibleReturnsFalseOnAnIncompatibleType_Template_WithSpecialValues(self):
        typeInstance1 = Integer().addAcceptDecorator(RangedAcceptDecorator, {'lowerBoundary': IntegerValue(0),
                                                                             'upperBoundary': IntegerValue(10)}).assignValueType(IntegerValue(1))
        typeInstance2 = Integer().addAcceptDecorator(RangedAcceptDecorator, {'lowerBoundary': IntegerValue(0),
                                                                             'upperBoundary': IntegerValue(10)}).\
                                  addAcceptDecorator(TemplateAcceptDecorator, {}).\
                                  assignValueType(AnyValue())
        self.assertFalse(typeInstance1.isCompatible(typeInstance2))
        self.assertTrue(typeInstance2.isCompatible(typeInstance1))

    def test_IsCompatibleReturnsFalseOnAnIncompatibleType_BuiltIn(self):
        typeInstance1 = Integer().addAcceptDecorator(RangedAcceptDecorator, {'lowerBoundary': IntegerValue(0),
                                                                             'upperBoundary': IntegerValue(10)}).assignValueType(IntegerValue(1))
        for typeInstance2 in [True, 1.0, "WAX"]:
            self.assertFalse(typeInstance1.isCompatible(typeInstance2))

    def test_IsCompatibleReturnsFalseOnAnIncompatibleType_Regular(self):
        self.skipTest("Not implemented yet.")

    def test_IsCompatibleReturnsFalseOnAnIncompatibleType_Special(self):
        typeInstance1 = Integer().addAcceptDecorator(RangedAcceptDecorator, {'lowerBoundary': IntegerValue(0),
                                                                             'upperBoundary': IntegerValue(10)}).assignValueType(IntegerValue(1))
        for typeInstance2 in [AnyValue()]:
            self.assertFalse(typeInstance1.isCompatible(typeInstance2))

class TypeSystem_Integer_Template_IsCompatible(unittest.TestCase):
    def test_IsCompatibleReturnsFlaseOnAnIncompatibleType_Self_NotInitialized(self):
        typeInstance = Integer().addAcceptDecorator(TemplateAcceptDecorator, {})
        self.assertFalse(typeInstance.isCompatible(typeInstance))

    def test_IsCompatibleReturnsCorrectValue_Self_Mixed(self):
        typeInstance1 = Integer().addAcceptDecorator(TemplateAcceptDecorator, {})
        typeInstance2 = Integer().addAcceptDecorator(TemplateAcceptDecorator, {}).assignValueType(IntegerValue(1))
        self.assertTrue(typeInstance1.isCompatible(typeInstance2))
        self.assertFalse(typeInstance2.isCompatible(typeInstance1))

    def test_IsCompatibleReturnsTrueOnACompatibleType_Self_Initialized(self):
        typeInstance = Integer().addAcceptDecorator(TemplateAcceptDecorator, {}).assignValueType(IntegerValue(1))
        self.assertTrue(typeInstance.isCompatible(typeInstance))

    def test_IsCompatibleReturnsTrueOnACompatibleType_Subtyped(self):
        typeInstance1 = Integer().addAcceptDecorator(TemplateAcceptDecorator, {}).assignValueType(IntegerValue(1))
        class MyInteger(Integer):
            def __init__(self):
                Integer.__init__(self)
                self.mAcceptDecorator = TemplateAcceptDecorator(self.mAcceptDecorator, {})
        typeInstance2 = MyInteger().assignValueType(IntegerValue(1))
        self.assertTrue(typeInstance1.isCompatible(typeInstance2))
        self.assertTrue(typeInstance2.isCompatible(typeInstance1))

    def test_IsCompatibleReturnsTrueOnACompatibleType_DoubleSubtyped(self):
        typeInstance1 = Integer().addAcceptDecorator(TemplateAcceptDecorator, {}).assignValueType(IntegerValue(1))
        class MyInteger(Integer):
            def __init__(self):
                Integer.__init__(self)
                self.mAcceptDecorator = TemplateAcceptDecorator(self.mAcceptDecorator, {})
        class MyInteger2(MyInteger):
            def __init__(self):
                MyInteger.__init__(self)
        typeInstance2 = MyInteger2().assignValueType(IntegerValue(1))
        self.assertTrue(typeInstance1.isCompatible(typeInstance2))
        self.assertTrue(typeInstance2.isCompatible(typeInstance1))

    def test_IsCompatibleReturnsTrueOnACompatibleType_Bounded(self):
        typeInstance1 = Integer().addAcceptDecorator(TemplateAcceptDecorator, {}).assignValueType(IntegerValue(1))
        typeInstance2 = Integer().addAcceptDecorator(RangedAcceptDecorator, {'lowerBoundary': IntegerValue(0),
                                                                             'upperBoundary': IntegerValue(10)}).\
                                  assignValueType(IntegerValue(1))
        self.assertTrue(typeInstance1.isCompatible(typeInstance2))
        self.assertTrue(typeInstance2.isCompatible(typeInstance1))

    def test_IsCompatibleReturnsFalseOnAnIncompatibleType_BuiltIn(self):
        typeInstance1 = Integer().addAcceptDecorator(TemplateAcceptDecorator, {}).assignValueType(IntegerValue(1))
        for typeInstance2 in [True, 1.0, "WAX"]:
            self.assertFalse(typeInstance1.isCompatible(typeInstance2))

    def test_IsCompatibleReturnsFalseOnAnIncompatibleType_Regular(self):
        self.skipTest("Not implemented yet.")

    def test_IsCompatibleReturnsFalseOnAnIncompatibleType_Special(self):
        typeInstance1 = Integer().addAcceptDecorator(TemplateAcceptDecorator, {}).assignValueType(IntegerValue(1))
        for typeInstance2 in [AnyValue()]:
            self.assertFalse(typeInstance1.isCompatible(typeInstance2))

class TypeSystem_Integer_Accept(unittest.TestCase):
    def test_AcceptReturnsTrueOnAValidValueType(self):
        typeInstance = Integer()
        for valueType in [IntegerValue(-1), IntegerValue(0), IntegerValue(1)]:
            self.assertTrue(typeInstance.accept(valueType))

    def test_AcceptReturnsFalseOnAnInvalidValueType_BuiltIn(self):
        typeInstance = Integer()
        for valueType in [True, 1.0, "WAX"]:
            self.assertFalse(typeInstance.accept(valueType))

    def test_AcceptReturnsFalseOnAnInvalidValueType_Special(self):
        typeInstance = Integer()
        for valueType in [AnyValue()]:
            self.assertFalse(typeInstance.accept(valueType))

class TypeSystem_Integer_Ranged_Accept(unittest.TestCase):
    def test_AcceptReturnsTrueOnAValidValueType(self):
        typeInstance = Integer().addAcceptDecorator(RangedAcceptDecorator, {'lowerBoundary': IntegerValue(0),
                                                                            'upperBoundary': IntegerValue(10)}).assignValueType(IntegerValue(1))
        for valueType in [IntegerValue(0), IntegerValue(1), IntegerValue(10)]:
            self.assertTrue(typeInstance.accept(valueType))

    def test_AcceptReturnsFalseOnAnInvalidValueType_Boundary(self):
        typeInstance = Integer().addAcceptDecorator(RangedAcceptDecorator, {'lowerBoundary': IntegerValue(0),
                                                                            'upperBoundary': IntegerValue(10)}).assignValueType(IntegerValue(1))
        for valueType in [IntegerValue(-1), IntegerValue(11)]:
            self.assertFalse(typeInstance.accept(valueType))

    def test_AcceptReturnsFalseOnAnInvalidValueType_BuiltIn(self):
        typeInstance = Integer().addAcceptDecorator(RangedAcceptDecorator, {'lowerBoundary': IntegerValue(0),
                                                                            'upperBoundary': IntegerValue(10)}).assignValueType(IntegerValue(1))
        for valueType in [True, 1.0, "WAX"]:
            self.assertFalse(typeInstance.accept(valueType))

    def test_AcceptReturnsFalseOnAnInvalidValueType_Special(self):
        typeInstance = Integer().addAcceptDecorator(RangedAcceptDecorator, {'lowerBoundary': IntegerValue(0),
                                                                            'upperBoundary': IntegerValue(10)}).assignValueType(IntegerValue(1))
        for valueType in [AnyValue()]:
            self.assertFalse(typeInstance.accept(valueType))

class TypeSystem_Integer_Ranged_Subtyped_Accept(unittest.TestCase):
    def test_AcceptReturnsTrueOnAValidValueType(self):
        class MyInteger(Integer):
            def __init__(self):
                Integer.__init__(self)
                self.mAcceptDecorator = RangedAcceptDecorator(self.mAcceptDecorator, {'lowerBoundary': IntegerValue(0),
                                                                                      'upperBoundary': IntegerValue(10)})
        typeInstance = MyInteger().assignValueType(IntegerValue(1))
        for valueType in [IntegerValue(0), IntegerValue(1), IntegerValue(10)]:
            self.assertTrue(typeInstance.accept(valueType))

    def test_AcceptReturnsFalseOnAnInvalidValueType_Boundary(self):
        class MyInteger(Integer):
            def __init__(self):
                Integer.__init__(self)
                self.mAcceptDecorator = RangedAcceptDecorator(self.mAcceptDecorator, {'lowerBoundary': IntegerValue(0),
                                                                                      'upperBoundary': IntegerValue(10)})
        typeInstance = MyInteger().assignValueType(IntegerValue(1))
        for valueType in [IntegerValue(-1), IntegerValue(11)]:
            self.assertFalse(typeInstance.accept(valueType))

    def test_AcceptReturnsFalseOnAnInvalidValueType_BuiltIn(self):
        class MyInteger(Integer):
            def __init__(self):
                Integer.__init__(self)
                self.mAcceptDecorator = RangedAcceptDecorator(self.mAcceptDecorator, {'lowerBoundary': IntegerValue(0),
                                                                                      'upperBoundary': IntegerValue(10)})
        typeInstance = MyInteger().assignValueType(IntegerValue(1))
        for valueType in [True, 1.0, "WAX"]:
            self.assertFalse(typeInstance.accept(valueType))

    def test_AcceptReturnsFalseOnAnInvalidValueType_Special(self):
        class MyInteger(Integer):
            def __init__(self):
                Integer.__init__(self)
                self.mAcceptDecorator = RangedAcceptDecorator(self.mAcceptDecorator, {'lowerBoundary': IntegerValue(0),
                                                                                      'upperBoundary': IntegerValue(10)})
        typeInstance = MyInteger().assignValueType(IntegerValue(1))
        for valueType in [AnyValue()]:
            self.assertFalse(typeInstance.accept(valueType))

class TypeSystem_Integer_Template_Accept(unittest.TestCase):
    def test_AcceptReturnsTrueOnAValidValueType(self):
        typeInstance = Integer().addAcceptDecorator(TemplateAcceptDecorator, {})
        for valueType in [IntegerValue(-1), IntegerValue(0), IntegerValue(1), AnyValue()]:
            self.assertTrue(typeInstance.accept(valueType))

    def test_AcceptReturnsFalseOnAnInvalidValueType_BuiltIn(self):
        typeInstance = Integer().addAcceptDecorator(TemplateAcceptDecorator, {})
        for valueType in [True, 1.0, "WAX"]:
            self.assertFalse(typeInstance.accept(valueType))

class TypeSystem_Integer_Template_Subtyped_Accept(unittest.TestCase):
    def test_AcceptReturnsTrueOnAValidValueType(self):
        class MyInteger(Integer):
            def __init__(self):
                Integer.__init__(self)
                self.mAcceptDecorator = TemplateAcceptDecorator(self.mAcceptDecorator, {})
        typeInstance = MyInteger().assignValueType(IntegerValue(1))
        for valueType in [IntegerValue(-1), IntegerValue(0), IntegerValue(1), AnyValue()]:
            self.assertTrue(typeInstance.accept(valueType))

    def test_AcceptReturnsFalseOnAnInvalidValueType_BuiltIn(self):
        class MyInteger(Integer):
            def __init__(self):
                Integer.__init__(self)
                self.mAcceptDecorator = TemplateAcceptDecorator(self.mAcceptDecorator, {})
        typeInstance = MyInteger().assignValueType(IntegerValue(1))
        for valueType in [True, 1.0, "WAX"]:
            self.assertFalse(typeInstance.accept(valueType))

class TypeSystem_Integer_AssignValueType(unittest.TestCase):
    def test_AssignValueTypeAssignsOnAValidValueType(self):
        typeInstance = Integer()
        for valueType in [IntegerValue(-1), IntegerValue(0), IntegerValue(1)]:
            self.assertEqual(typeInstance.assignValueType(valueType).valueType(), valueType)

    def test_AssignValueTypeRaisesAnExceptionOnAnInvalidValueType_BuiltIn(self):
        typeInstance = Integer()
        for valueType in [True, 1.0, "WAX"]:
            with self.assertRaises(InvalidTypeInValueTypeAssignment):
                typeInstance.assignValueType(valueType)

    def test_AssignValueTypeRaisesAnExceptionOnAnInvalidValueType_Special(self):
        typeInstance = Integer()
        for valueType in [AnyValue()]:
            with self.assertRaises(InvalidTypeInValueTypeAssignment):
                typeInstance.assignValueType(valueType)

class TypeSystem_Integer_Ranged_AssignValueType(unittest.TestCase):
    def test_AssignValueTypeAssignsOnAValidValueType(self):
        typeInstance = Integer().addAcceptDecorator(RangedAcceptDecorator, {'lowerBoundary': IntegerValue(0),
                                                                            'upperBoundary': IntegerValue(10)}).assignValueType(IntegerValue(1))
        for valueType in [IntegerValue(0), IntegerValue(1), IntegerValue(10)]:
            self.assertEqual(typeInstance.assignValueType(valueType).valueType(), valueType)

    def test_AssignValueRaisesAnExceptionOnAnInvalidValueType_Boundary(self):
        typeInstance = Integer().addAcceptDecorator(RangedAcceptDecorator, {'lowerBoundary': IntegerValue(0),
                                                                            'upperBoundary': IntegerValue(10)}).assignValueType(IntegerValue(1))
        for valueType in [IntegerValue(-1), IntegerValue(11)]:
            with self.assertRaises(InvalidTypeInValueTypeAssignment):
                typeInstance.assignValueType(valueType)

    def test_AssignValueTypeRaisesAnExceptionOnAnInvalidValueType_BuiltIn(self):
        typeInstance = Integer().addAcceptDecorator(RangedAcceptDecorator, {'lowerBoundary': IntegerValue(0),
                                                                            'upperBoundary': IntegerValue(10)}).assignValueType(IntegerValue(1))
        for valueType in [True, 1.0, "WAX"]:
            with self.assertRaises(InvalidTypeInValueTypeAssignment):
                typeInstance.assignValueType(valueType)

    def test_AssignValueTypeRaisesAnExceptionOnAnInvalidValueType_Special(self):
        typeInstance = Integer().addAcceptDecorator(RangedAcceptDecorator, {'lowerBoundary': IntegerValue(0),
                                                                            'upperBoundary': IntegerValue(10)}).assignValueType(IntegerValue(1))
        for valueType in [AnyValue()]:
            with self.assertRaises(InvalidTypeInValueTypeAssignment):
                typeInstance.assignValueType(valueType)

class TypeSystem_Integer_Ranged_Subtyped_AssignValueType(unittest.TestCase):
    def test_AssignValueTypeAssignsOnAValidValueType(self):
        class MyInteger(Integer):
            def __init__(self):
                Integer.__init__(self)
                self.mAcceptDecorator = RangedAcceptDecorator(self.mAcceptDecorator, {'lowerBoundary': IntegerValue(0),
                                                                                      'upperBoundary': IntegerValue(10)})
        typeInstance = MyInteger().assignValueType(IntegerValue(1))
        for valueType in [IntegerValue(0), IntegerValue(1), IntegerValue(10)]:
            self.assertEqual(typeInstance.assignValueType(valueType).valueType(), valueType)

    def test_AssignValueRaisesAnExceptionOnAnInvalidValueType_Boundary(self):
        class MyInteger(Integer):
            def __init__(self):
                Integer.__init__(self)
                self.mAcceptDecorator = RangedAcceptDecorator(self.mAcceptDecorator, {'lowerBoundary': IntegerValue(0),
                                                                                      'upperBoundary': IntegerValue(10)})
        typeInstance = MyInteger().assignValueType(IntegerValue(1))
        for valueType in [IntegerValue(-1), IntegerValue(11)]:
            with self.assertRaises(InvalidTypeInValueTypeAssignment):
                typeInstance.assignValueType(valueType)

    def test_AssignValueTypeRaisesAnExceptionOnAnInvalidValueType_BuiltIn(self):
        class MyInteger(Integer):
            def __init__(self):
                Integer.__init__(self)
                self.mAcceptDecorator = RangedAcceptDecorator(self.mAcceptDecorator, {'lowerBoundary': IntegerValue(0),
                                                                                      'upperBoundary': IntegerValue(10)})
        typeInstance = MyInteger().assignValueType(IntegerValue(1))
        for valueType in [True, 1.0, "WAX"]:
            with self.assertRaises(InvalidTypeInValueTypeAssignment):
                typeInstance.assignValueType(valueType)

    def test_AssignValueTypeRaisesAnExceptionOnAnInvalidValueType_Special(self):
        class MyInteger(Integer):
            def __init__(self):
                Integer.__init__(self)
                self.mAcceptDecorator = RangedAcceptDecorator(self.mAcceptDecorator, {'lowerBoundary': IntegerValue(0),
                                                                                      'upperBoundary': IntegerValue(10)})
        typeInstance = MyInteger().assignValueType(IntegerValue(1))
        for valueType in [AnyValue()]:
            with self.assertRaises(InvalidTypeInValueTypeAssignment):
                typeInstance.assignValueType(valueType)

class TypeSystem_Integer_Template_AssignValueType(unittest.TestCase):
    def test_AssignValueTypeAssignsOnAValidValueType(self):
        class MyInteger(Integer):
            def __init__(self):
                Integer.__init__(self)
                self.mAcceptDecorator = TemplateAcceptDecorator(self.mAcceptDecorator, {})
        typeInstance = MyInteger().assignValueType(IntegerValue(1))
        for valueType in [IntegerValue(-1), IntegerValue(0), IntegerValue(1), AnyValue()]:
            self.assertEqual(typeInstance.assignValueType(valueType).valueType(), valueType)

    def test_AssignValueTypeRaisesAnExceptionOnAnInvalidValueType_BuiltIn(self):
        class MyInteger(Integer):
            def __init__(self):
                Integer.__init__(self)
                self.mAcceptDecorator = TemplateAcceptDecorator(self.mAcceptDecorator, {})
        typeInstance = MyInteger().assignValueType(IntegerValue(1))
        for valueType in [True, 1.0, "WAX"]:
            with self.assertRaises(InvalidTypeInValueTypeAssignment):
                typeInstance.assignValueType(valueType)

class TypeSystem_Integer_Template_Subtyped_AssignValueType(unittest.TestCase):
    def test_AssignValueTypeAssignsOnAValidValueType(self):
        class MyInteger(Integer):
            def __init__(self):
                Integer.__init__(self)
                self.mAcceptDecorator = TemplateAcceptDecorator(self.mAcceptDecorator, {})
        typeInstance = MyInteger().assignValueType(IntegerValue(1))
        for valueType in [IntegerValue(-1), IntegerValue(0), IntegerValue(1), AnyValue()]:
            self.assertEqual(typeInstance.assignValueType(valueType).valueType(), valueType)

    def test_AssignValueTypeRaisesAnExceptionOnAnInvalidValueType_BuiltIn(self):
        class MyInteger(Integer):
            def __init__(self):
                Integer.__init__(self)
                self.mAcceptDecorator = TemplateAcceptDecorator(self.mAcceptDecorator, {})
        typeInstance = MyInteger().assignValueType(IntegerValue(1))
        for valueType in [True, 1.0, "WAX"]:
            with self.assertRaises(InvalidTypeInValueTypeAssignment):
                typeInstance.assignValueType(valueType)

class TypeSystem_Integer_Eq(unittest.TestCase):
    def test_EqReturnsTrueOnSameValues_SameTypes(self):
        self.assertTrue(Integer().assignValueType(IntegerValue(1)) == Integer().assignValueType(IntegerValue(1)))

    def test_EqReturnsTrueOnSameValues_CompatibleTypes(self):
        typeInstance1 = Integer().assignValueType(IntegerValue(1))
        for typeInstance2 in [
            Integer().addAcceptDecorator(RangedAcceptDecorator, {'lowerBoundary': IntegerValue(0),
                                                                 'upperBoundary': IntegerValue(10)}).assignValueType(IntegerValue(1)),
            Integer().addAcceptDecorator(TemplateAcceptDecorator, {}).assignValueType(IntegerValue(1))
        ]:
            self.assertTrue(typeInstance1 == typeInstance2)
            self.assertTrue(typeInstance2 == typeInstance1)

    def test_EqReturnsFalseOnDifferentValues_SameTypes(self):
        self.assertFalse(Integer().assignValueType(IntegerValue(1)) == Integer().assignValueType(IntegerValue(2)))

    def test_EqReturnsFalseOnDifferentValues_CompatibleTypes(self):
        typeInstance1 = Integer().assignValueType(IntegerValue(1))
        for typeInstance2 in [
            Integer().addAcceptDecorator(RangedAcceptDecorator, {'lowerBoundary': IntegerValue(0),
                                                                 'upperBoundary': IntegerValue(10)}).assignValueType(IntegerValue(2)),
            Integer().addAcceptDecorator(TemplateAcceptDecorator, {}).assignValueType(IntegerValue(2))
        ]:
            self.assertFalse(typeInstance1 == typeInstance2)
            self.assertFalse(typeInstance2 == typeInstance1)

    def test_EqRaisesAnExceptionOnAnInvalidType_BuiltIn(self):
        typeInstance = Integer().assignValueType(IntegerValue(1))
        for valueType in [True, 1.0, "WAX"]:
            with self.assertRaises(InvalidTypeInComparison):
                typeInstance == valueType

    def test_EqRaisesAnExceptionOnAnInvalidType_Regular(self):
        self.skipTest("Not implemented yet.")

    def test_EqRaisesAnExceptionOnAnInvalidType_Special(self):
        typeInstance = Integer().assignValueType(IntegerValue(1))
        for valueType in [AnyValue()]:
            with self.assertRaises(InvalidTypeInComparison):
                typeInstance == valueType

    def test_EqRaisesAnExceptionOnAnInvalidType_Template(self):
        self.skipTest("Not implemented yet.")

class TypeSystem_Integer_Ranged_Eq(unittest.TestCase):
    def test_EqReturnsTrueOnSameValues_SameTypes(self):
        typeInstance1 = Integer().addAcceptDecorator(RangedAcceptDecorator, {'lowerBoundary': IntegerValue(0),
                                                                             'upperBoundary': IntegerValue(10)}).assignValueType(IntegerValue(1))
        typeInstance2 = Integer().addAcceptDecorator(RangedAcceptDecorator, {'lowerBoundary': IntegerValue(0),
                                                                             'upperBoundary': IntegerValue(10)}).assignValueType(IntegerValue(1))
        self.assertTrue(typeInstance1 == typeInstance2)
        self.assertTrue(typeInstance2 == typeInstance1)

    def test_EqReturnsTrueOnSameValues_CompatibleTypes(self):
        typeInstance1 = Integer().addAcceptDecorator(RangedAcceptDecorator, {'lowerBoundary': IntegerValue(0),
                                                                            'upperBoundary': IntegerValue(10)}).assignValueType(IntegerValue(1))
        for typeInstance2 in [
            Integer().assignValueType(IntegerValue(1)),
            Integer().addAcceptDecorator(TemplateAcceptDecorator, {}).assignValueType(IntegerValue(1))
        ]:
            self.assertTrue(typeInstance1 == typeInstance2)
            self.assertTrue(typeInstance2 == typeInstance1)

    def test_EqReturnsFalseOnDifferentValues_SameTypes(self):
        typeInstance1 = Integer().addAcceptDecorator(RangedAcceptDecorator, {'lowerBoundary': IntegerValue(0),
                                                                             'upperBoundary': IntegerValue(10)}).assignValueType(IntegerValue(1))
        typeInstance2 = Integer().addAcceptDecorator(RangedAcceptDecorator, {'lowerBoundary': IntegerValue(0),
                                                                             'upperBoundary': IntegerValue(10)}).assignValueType(IntegerValue(2))
        self.assertFalse(typeInstance1 == typeInstance2)
        self.assertFalse(typeInstance2 == typeInstance1)

    def test_EqReturnsFalseOnDifferentValues_CompatibleTypes(self):
        typeInstance1 = Integer().addAcceptDecorator(RangedAcceptDecorator, {'lowerBoundary': IntegerValue(0),
                                                                            'upperBoundary': IntegerValue(10)}).assignValueType(IntegerValue(1))
        for typeInstance2 in [
            Integer().assignValueType(IntegerValue(2)),
            Integer().addAcceptDecorator(TemplateAcceptDecorator, {}).assignValueType(IntegerValue(2))
        ]:
            self.assertFalse(typeInstance1 == typeInstance2)
            self.assertFalse(typeInstance2 == typeInstance1)

    def test_EqRaisesAnExceptionOnAnInvalidType_BuiltIn(self):
        typeInstance = Integer().addAcceptDecorator(RangedAcceptDecorator, {'lowerBoundary': IntegerValue(0),
                                                                            'upperBoundary': IntegerValue(10)}).assignValueType(IntegerValue(1))
        for builtIn in [True, 1.0, "WAX"]:
            with self.assertRaises(InvalidTypeInComparison):
                typeInstance == builtIn

    def test_EqRaisesAnExceptionOnAnInvalidType_Regular(self):
        self.skipTest("Not implemented yet.")

    def test_EqRaisesAnExceptionOnAnInvalidType_Special(self):
        typeInstance = Integer().addAcceptDecorator(RangedAcceptDecorator, {'lowerBoundary': IntegerValue(0),
                                                                            'upperBoundary': IntegerValue(10)}).assignValueType(IntegerValue(1))
        for valueType in [AnyValue()]:
            with self.assertRaises(InvalidTypeInComparison):
                typeInstance == valueType

    def test_EqRaisesAnExceptionOnAnInvalidType_Template(self):
        self.skipTest("Not implemented yet.")

class TypeSystem_Integer_Ranged_Subtyped_Eq(unittest.TestCase):
    def test_EqReturnsTrueOnSameValues_SameTypes(self):
        class MyInteger(Integer):
            def __init__(self):
                Integer.__init__(self)
                self.mAcceptDecorator = RangedAcceptDecorator(self.mAcceptDecorator, {'lowerBoundary': IntegerValue(0),
                                                                                      'upperBoundary': IntegerValue(10)})
        typeInstance1 = MyInteger().assignValueType(IntegerValue(1))
        typeInstance2 = MyInteger().assignValueType(IntegerValue(1))
        self.assertTrue(typeInstance1 == typeInstance2)
        self.assertTrue(typeInstance2 == typeInstance1)

    def test_EqReturnsTrueOnSameValues_CompatibleTypes(self):
        class MyInteger(Integer):
            def __init__(self):
                Integer.__init__(self)
                self.mAcceptDecorator = RangedAcceptDecorator(self.mAcceptDecorator, {'lowerBoundary': IntegerValue(0),
                                                                                      'upperBoundary': IntegerValue(10)})
        typeInstance1 = MyInteger().assignValueType(IntegerValue(1))
        for typeInstance2 in [
            Integer().assignValueType(IntegerValue(1)),
            Integer().addAcceptDecorator(TemplateAcceptDecorator, {}).assignValueType(IntegerValue(1))
        ]:
            self.assertTrue(typeInstance1 == typeInstance2)
            self.assertTrue(typeInstance2 == typeInstance1)

    def test_EqReturnsFalseOnDifferentValues_SameTypes(self):
        class MyInteger(Integer):
            def __init__(self):
                Integer.__init__(self)
                self.mAcceptDecorator = RangedAcceptDecorator(self.mAcceptDecorator, {'lowerBoundary': IntegerValue(0),
                                                                                      'upperBoundary': IntegerValue(10)})
        typeInstance1 = MyInteger().assignValueType(IntegerValue(1))
        typeInstance2 = MyInteger().assignValueType(IntegerValue(2))
        self.assertFalse(typeInstance1 == typeInstance2)
        self.assertFalse(typeInstance2 == typeInstance1)

    def test_EqReturnsFalseOnDifferentValues_CompatibleTypes(self):
        class MyInteger(Integer):
            def __init__(self):
                Integer.__init__(self)
                self.mAcceptDecorator = RangedAcceptDecorator(self.mAcceptDecorator, {'lowerBoundary': IntegerValue(0),
                                                                                      'upperBoundary': IntegerValue(10)})
        typeInstance1 = MyInteger().assignValueType(IntegerValue(1))
        for typeInstance2 in [
            Integer().assignValueType(IntegerValue(2)),
            Integer().addAcceptDecorator(TemplateAcceptDecorator, {}).assignValueType(IntegerValue(2))
        ]:
            self.assertFalse(typeInstance1 == typeInstance2)
            self.assertFalse(typeInstance2 == typeInstance1)

    def test_EqRaisesAnExceptionOnAnInvalidType_BuiltIn(self):
        class MyInteger(Integer):
            def __init__(self):
                Integer.__init__(self)
                self.mAcceptDecorator = RangedAcceptDecorator(self.mAcceptDecorator, {'lowerBoundary': IntegerValue(0),
                                                                                      'upperBoundary': IntegerValue(10)})
        typeInstance = MyInteger().assignValueType(IntegerValue(1))
        for builtIn in [True, 1.0, "WAX"]:
            with self.assertRaises(InvalidTypeInComparison):
                typeInstance == builtIn

    def test_EqRaisesAnExceptionOnAnInvalidType_Regular(self):
        self.skipTest("Not implemented yet.")

    def test_EqRaisesAnExceptionOnAnInvalidType_Special(self):
        class MyInteger(Integer):
            def __init__(self):
                Integer.__init__(self)
                self.mAcceptDecorator = RangedAcceptDecorator(self.mAcceptDecorator, {'lowerBoundary': IntegerValue(0),
                                                                                      'upperBoundary': IntegerValue(10)})
        typeInstance = MyInteger().assignValueType(IntegerValue(1))
        for valueType in [AnyValue()]:
            with self.assertRaises(InvalidTypeInComparison):
                typeInstance == valueType

    def test_EqRaisesAnExceptionOnAnInvalidType_Template(self):
        self.skipTest("Not implemented yet.")

class TypeSystem_Integer_Template_Eq(unittest.TestCase):
    def test_EqReturnsTrueOnSameValues_SameTypes(self):
        typeInstance1 = Integer().addAcceptDecorator(TemplateAcceptDecorator, {}).assignValueType(IntegerValue(1))
        typeInstance2 = Integer().addAcceptDecorator(TemplateAcceptDecorator, {}).assignValueType(IntegerValue(1))
        self.assertTrue(typeInstance1 == typeInstance2)
        self.assertTrue(typeInstance2 == typeInstance1)

    def test_EqReturnsTrueOnSameValues_CompatibleTypes(self):
        typeInstance1 = Integer().addAcceptDecorator(TemplateAcceptDecorator, {}).assignValueType(IntegerValue(1))
        for typeInstance2 in [
            Integer().assignValueType(IntegerValue(1)),
            Integer().addAcceptDecorator(RangedAcceptDecorator, {'lowerBoundary': IntegerValue(0),
                                                                 'upperBoundary': IntegerValue(10)}).assignValueType(IntegerValue(1))
        ]:
            self.assertTrue(typeInstance1 == typeInstance2)
            self.assertTrue(typeInstance2 == typeInstance1)

    def test_EqReturnsFalseOnDifferentValues_SameTypes(self):
        typeInstance1 = Integer().addAcceptDecorator(TemplateAcceptDecorator, {}).assignValueType(IntegerValue(1))
        typeInstance2 = Integer().addAcceptDecorator(TemplateAcceptDecorator, {}).assignValueType(IntegerValue(2))
        self.assertFalse(typeInstance1 == typeInstance2)
        self.assertFalse(typeInstance2 == typeInstance1)

    def test_EqReturnsFalseOnDifferentValues_CompatibleTypes(self):
        typeInstance1 = Integer().addAcceptDecorator(TemplateAcceptDecorator, {}).assignValueType(IntegerValue(1))
        for typeInstance2 in [
            Integer().assignValueType(IntegerValue(2)),
            Integer().addAcceptDecorator(RangedAcceptDecorator, {'lowerBoundary': IntegerValue(0),
                                                                 'upperBoundary': IntegerValue(10)}).assignValueType(IntegerValue(2))
        ]:
            self.assertFalse(typeInstance1 == typeInstance2)
            self.assertFalse(typeInstance2 == typeInstance1)

    def test_EqRaisesAnExceptionOnAnInvalidType_BuiltIn(self):
        typeInstance = Integer().addAcceptDecorator(TemplateAcceptDecorator, {}).assignValueType(IntegerValue(1))
        for builtIn in [True, 1.0, "WAX"]:
            with self.assertRaises(InvalidTypeInComparison):
                typeInstance == builtIn

    def test_EqRaisesAnExceptionOnAnInvalidType_Regular(self):
        self.skipTest("Not implemented yet.")

    def test_EqRaisesAnExceptionOnAnInvalidType_Special(self):
        typeInstance = Integer().addAcceptDecorator(TemplateAcceptDecorator, {}).assignValueType(IntegerValue(1))
        for valueType in [AnyValue()]:
            with self.assertRaises(InvalidTypeInComparison):
                typeInstance == valueType

    def test_EqRaisesAnExceptionOnAnInvalidType_Template(self):
        self.skipTest("Not implemented yet.")

class TypeSystem_Integer_Template_Subtyped_Eq(unittest.TestCase):
    def test_EqReturnsTrueOnSameValues_SameTypes(self):
        class MyInteger(Integer):
            def __init__(self):
                Integer.__init__(self)
                self.mAcceptDecorator = TemplateAcceptDecorator(self.mAcceptDecorator, {})
        typeInstance1 = MyInteger().assignValueType(IntegerValue(1))
        typeInstance2 = MyInteger().assignValueType(IntegerValue(1))
        self.assertTrue(typeInstance1 == typeInstance2)
        self.assertTrue(typeInstance2 == typeInstance1)

    def test_EqReturnsTrueOnSameValues_CompatibleTypes(self):
        class MyInteger(Integer):
            def __init__(self):
                Integer.__init__(self)
                self.mAcceptDecorator = TemplateAcceptDecorator(self.mAcceptDecorator, {})
        typeInstance1 = MyInteger().assignValueType(IntegerValue(1))
        for typeInstance2 in [
            Integer().assignValueType(IntegerValue(1)),
            Integer().addAcceptDecorator(RangedAcceptDecorator, {'lowerBoundary': IntegerValue(0),
                                                                 'upperBoundary': IntegerValue(10)}).assignValueType(IntegerValue(1))
        ]:
            self.assertTrue(typeInstance1 == typeInstance2)
            self.assertTrue(typeInstance2 == typeInstance1)

    def test_EqReturnsFalseOnDifferentValues_SameTypes(self):
        class MyInteger(Integer):
            def __init__(self):
                Integer.__init__(self)
                self.mAcceptDecorator = TemplateAcceptDecorator(self.mAcceptDecorator, {})
        typeInstance1 = MyInteger().assignValueType(IntegerValue(1))
        typeInstance2 = MyInteger().assignValueType(IntegerValue(2))
        self.assertFalse(typeInstance1 == typeInstance2)
        self.assertFalse(typeInstance2 == typeInstance1)

    def test_EqReturnsFalseOnDifferentValues_CompatibleTypes(self):
        class MyInteger(Integer):
            def __init__(self):
                Integer.__init__(self)
                self.mAcceptDecorator = TemplateAcceptDecorator(self.mAcceptDecorator, {})
        typeInstance1 = MyInteger().assignValueType(IntegerValue(1))
        for typeInstance2 in [
            Integer().assignValueType(IntegerValue(2)),
            Integer().addAcceptDecorator(RangedAcceptDecorator, {'lowerBoundary': IntegerValue(0),
                                                                 'upperBoundary': IntegerValue(10)}).assignValueType(IntegerValue(2))
        ]:
            self.assertFalse(typeInstance1 == typeInstance2)
            self.assertFalse(typeInstance2 == typeInstance1)

    def test_EqRaisesAnExceptionOnAnInvalidType_BuiltIn(self):
        class MyInteger(Integer):
            def __init__(self):
                Integer.__init__(self)
                self.mAcceptDecorator = TemplateAcceptDecorator(self.mAcceptDecorator, {})
        typeInstance = MyInteger().assignValueType(IntegerValue(1))
        for builtIn in [True, 1.0, "WAX"]:
            with self.assertRaises(InvalidTypeInComparison):
                typeInstance == builtIn

    def test_EqRaisesAnExceptionOnAnInvalidType_Regular(self):
        self.skipTest("Not implemented yet.")

    def test_EqRaisesAnExceptionOnAnInvalidType_Special(self):
        class MyInteger(Integer):
            def __init__(self):
                Integer.__init__(self)
                self.mAcceptDecorator = TemplateAcceptDecorator(self.mAcceptDecorator, {})
        typeInstance = MyInteger().assignValueType(IntegerValue(1))
        for valueType in [AnyValue()]:
            with self.assertRaises(InvalidTypeInComparison):
                typeInstance == valueType

    def test_EqRaisesAnExceptionOnAnInvalidType_Template(self):
        self.skipTest("Not implemented yet.")

class TypeSystem_Record_Ctor(unittest.TestCase):
    def test_Ctor_Empty(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, {})
        typeInstance = MyRecord()

    def test_Ctor_NonEmpty(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, {'foo': Integer()})
        typeInstance = MyRecord()

class TypeSystem_Record_Template_Ctor(unittest.TestCase):
    def test_Ctor_Empty(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, {})
                self.mAcceptDecorator = TemplateAcceptDecorator(self.mAcceptDecorator, {})
        typeInstance = MyRecord()
        self.assertTrue(isinstance(typeInstance.mAcceptDecorator, TemplateAcceptDecorator))
        self.assertTrue(isinstance(typeInstance.mAcceptDecorator.mAcceptDecorator, RecordAcceptDecorator))

    def test_Ctor_NonEmpty(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, {'foo': Integer()})
                self.mAcceptDecorator = TemplateAcceptDecorator(self.mAcceptDecorator, {})
        typeInstance = MyRecord()
        self.assertTrue(isinstance(typeInstance.mAcceptDecorator, TemplateAcceptDecorator))
        self.assertTrue(isinstance(typeInstance.mAcceptDecorator.mAcceptDecorator, RecordAcceptDecorator))
        self.assertTrue(isinstance(typeInstance.mAcceptDecorator.mAcceptDecorator.mDescriptorDictionary['foo'].mAcceptDecorator, TemplateAcceptDecorator))
        self.assertTrue(isinstance(typeInstance.mAcceptDecorator.mAcceptDecorator.mDescriptorDictionary['foo'].mAcceptDecorator.mAcceptDecorator, TypeAcceptDecorator))
        self.assertTrue(issubclass(typeInstance.mAcceptDecorator.mAcceptDecorator.mDescriptorDictionary['foo'].mAcceptDecorator.mAcceptDecorator.mType, IntegerValue))

    def test_Ctor_Nested1(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, {'foo': Integer()})
        class MyRecord1(Record):
            def __init__(self):
                Record.__init__(self, {'bar': MyRecord()})
                self.mAcceptDecorator = TemplateAcceptDecorator(self.mAcceptDecorator, {})
        typeInstance = MyRecord1()
        self.assertTrue(isinstance(typeInstance.mAcceptDecorator, TemplateAcceptDecorator))
        self.assertTrue(isinstance(typeInstance.mAcceptDecorator.mAcceptDecorator, RecordAcceptDecorator))
        self.assertTrue(isinstance(typeInstance.mAcceptDecorator.mAcceptDecorator.mDescriptorDictionary['bar'].mAcceptDecorator, TemplateAcceptDecorator))
        self.assertTrue(isinstance(typeInstance.mAcceptDecorator.mAcceptDecorator.mDescriptorDictionary['bar'].mAcceptDecorator.mAcceptDecorator, RecordAcceptDecorator))
        self.assertTrue(isinstance(typeInstance.mAcceptDecorator.mAcceptDecorator.mDescriptorDictionary['bar'].mAcceptDecorator.mAcceptDecorator.mDescriptorDictionary['foo'].mAcceptDecorator, TemplateAcceptDecorator))
        self.assertTrue(isinstance(typeInstance.mAcceptDecorator.mAcceptDecorator.mDescriptorDictionary['bar'].mAcceptDecorator.mAcceptDecorator.mDescriptorDictionary['foo'].mAcceptDecorator.mAcceptDecorator, TypeAcceptDecorator))
        self.assertTrue(issubclass(typeInstance.mAcceptDecorator.mAcceptDecorator.mDescriptorDictionary['bar'].mAcceptDecorator.mAcceptDecorator.mDescriptorDictionary['foo'].mAcceptDecorator.mAcceptDecorator.mType, IntegerValue))

    def test_Ctor_Nested2(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, {'foo': Integer()})
        class MyRecord1(Record):
            def __init__(self):
                Record.__init__(self, {'bar': MyRecord()})
        class MyRecord2(Record):
            def __init__(self):
                Record.__init__(self, {'baz1': MyRecord1(),
                                       'baz2': Integer()})
                self.mAcceptDecorator = TemplateAcceptDecorator(self.mAcceptDecorator, {})
        typeInstance = MyRecord2()
        self.assertTrue(isinstance(typeInstance.mAcceptDecorator, TemplateAcceptDecorator))
        self.assertTrue(isinstance(typeInstance.mAcceptDecorator.mAcceptDecorator, RecordAcceptDecorator))
        self.assertTrue(isinstance(typeInstance.mAcceptDecorator.mAcceptDecorator.mDescriptorDictionary['baz1'].mAcceptDecorator.mAcceptDecorator.mDescriptorDictionary['bar'].mAcceptDecorator, TemplateAcceptDecorator))
        self.assertTrue(isinstance(typeInstance.mAcceptDecorator.mAcceptDecorator.mDescriptorDictionary['baz1'].mAcceptDecorator.mAcceptDecorator.mDescriptorDictionary['bar'].mAcceptDecorator.mAcceptDecorator, RecordAcceptDecorator))
        self.assertTrue(isinstance(typeInstance.mAcceptDecorator.mAcceptDecorator.mDescriptorDictionary['baz1'].mAcceptDecorator.mAcceptDecorator.mDescriptorDictionary['bar'].mAcceptDecorator.mAcceptDecorator.mDescriptorDictionary['foo'].mAcceptDecorator, TemplateAcceptDecorator))
        self.assertTrue(isinstance(typeInstance.mAcceptDecorator.mAcceptDecorator.mDescriptorDictionary['baz1'].mAcceptDecorator.mAcceptDecorator.mDescriptorDictionary['bar'].mAcceptDecorator.mAcceptDecorator.mDescriptorDictionary['foo'].mAcceptDecorator.mAcceptDecorator, TypeAcceptDecorator))
        self.assertTrue(issubclass(typeInstance.mAcceptDecorator.mAcceptDecorator.mDescriptorDictionary['baz1'].mAcceptDecorator.mAcceptDecorator.mDescriptorDictionary['bar'].mAcceptDecorator.mAcceptDecorator.mDescriptorDictionary['foo'].mAcceptDecorator.mAcceptDecorator.mType, IntegerValue))

class TypeSystem_Record_RecordOf_Ctor(unittest.TestCase):
    def test_Ctor_Standalone(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, Integer())
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, {'foo': MyRecordOf()})
        typeInstance = MyRecord()

    def test_Ctor_WithOtherTypes(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, Integer())
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, {'foo': Integer(),
                                       'bar': MyRecordOf(),
                                       'baz': Integer()})
        typeInstance = MyRecord()

class TypeSystem_Record_RecordOf_Template_Ctor(unittest.TestCase):
    def test_Ctor_Standalone(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, Integer())
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, {'foo': MyRecordOf()})
                self.mAcceptDecorator = TemplateAcceptDecorator(self.mAcceptDecorator, {})
        typeInstance = MyRecord()
        self.assertTrue(isinstance(typeInstance.mAcceptDecorator, TemplateAcceptDecorator))
        self.assertTrue(isinstance(typeInstance.mAcceptDecorator.mAcceptDecorator, RecordAcceptDecorator))
        self.assertTrue(isinstance(typeInstance.mAcceptDecorator.mAcceptDecorator.mDescriptorDictionary['foo'].mAcceptDecorator, TemplateAcceptDecorator))
        self.assertTrue(isinstance(typeInstance.mAcceptDecorator.mAcceptDecorator.mDescriptorDictionary['foo'].mAcceptDecorator.mAcceptDecorator, RecordOfAcceptDecorator))
        self.assertTrue(isinstance(typeInstance.mAcceptDecorator.mAcceptDecorator.mDescriptorDictionary['foo'].mAcceptDecorator.mAcceptDecorator.mDescriptorType, Integer))
        self.assertTrue(isinstance(typeInstance.mAcceptDecorator.mAcceptDecorator.mDescriptorDictionary['foo'].mAcceptDecorator.mAcceptDecorator.mDescriptorType.mAcceptDecorator, TemplateAcceptDecorator))
        self.assertTrue(isinstance(typeInstance.mAcceptDecorator.mAcceptDecorator.mDescriptorDictionary['foo'].mAcceptDecorator.mAcceptDecorator.mDescriptorType.mAcceptDecorator.mAcceptDecorator, TypeAcceptDecorator))
        self.assertTrue(issubclass(typeInstance.mAcceptDecorator.mAcceptDecorator.mDescriptorDictionary['foo'].mAcceptDecorator.mAcceptDecorator.mDescriptorType.mAcceptDecorator.mAcceptDecorator.mType, IntegerValue))

    def test_Ctor_WithOtherTypes(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, Integer())
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, {'foo': Integer(),
                                       'bar': MyRecordOf(),
                                       'baz': Integer()})
                self.mAcceptDecorator = TemplateAcceptDecorator(self.mAcceptDecorator, {})
        typeInstance = MyRecord()
        self.assertTrue(isinstance(typeInstance.mAcceptDecorator, TemplateAcceptDecorator))
        self.assertTrue(isinstance(typeInstance.mAcceptDecorator.mAcceptDecorator, RecordAcceptDecorator))
        self.assertTrue(isinstance(typeInstance.mAcceptDecorator.mAcceptDecorator.mDescriptorDictionary['foo'].mAcceptDecorator, TemplateAcceptDecorator))
        self.assertTrue(isinstance(typeInstance.mAcceptDecorator.mAcceptDecorator.mDescriptorDictionary['foo'].mAcceptDecorator.mAcceptDecorator, TypeAcceptDecorator))
        self.assertTrue(issubclass(typeInstance.mAcceptDecorator.mAcceptDecorator.mDescriptorDictionary['foo'].mAcceptDecorator.mAcceptDecorator.mType, IntegerValue))
        self.assertTrue(isinstance(typeInstance.mAcceptDecorator.mAcceptDecorator.mDescriptorDictionary['bar'].mAcceptDecorator, TemplateAcceptDecorator))
        self.assertTrue(isinstance(typeInstance.mAcceptDecorator.mAcceptDecorator.mDescriptorDictionary['bar'].mAcceptDecorator.mAcceptDecorator, RecordOfAcceptDecorator))
        self.assertTrue(isinstance(typeInstance.mAcceptDecorator.mAcceptDecorator.mDescriptorDictionary['bar'].mAcceptDecorator.mAcceptDecorator.mDescriptorType, Integer))
        self.assertTrue(isinstance(typeInstance.mAcceptDecorator.mAcceptDecorator.mDescriptorDictionary['bar'].mAcceptDecorator.mAcceptDecorator.mDescriptorType.mAcceptDecorator, TemplateAcceptDecorator))
        self.assertTrue(isinstance(typeInstance.mAcceptDecorator.mAcceptDecorator.mDescriptorDictionary['bar'].mAcceptDecorator.mAcceptDecorator.mDescriptorType.mAcceptDecorator.mAcceptDecorator, TypeAcceptDecorator))
        self.assertTrue(issubclass(typeInstance.mAcceptDecorator.mAcceptDecorator.mDescriptorDictionary['bar'].mAcceptDecorator.mAcceptDecorator.mDescriptorType.mAcceptDecorator.mAcceptDecorator.mType, IntegerValue))
        self.assertTrue(isinstance(typeInstance.mAcceptDecorator.mAcceptDecorator.mDescriptorDictionary['baz'].mAcceptDecorator, TemplateAcceptDecorator))
        self.assertTrue(isinstance(typeInstance.mAcceptDecorator.mAcceptDecorator.mDescriptorDictionary['baz'].mAcceptDecorator.mAcceptDecorator, TypeAcceptDecorator))
        self.assertTrue(issubclass(typeInstance.mAcceptDecorator.mAcceptDecorator.mDescriptorDictionary['baz'].mAcceptDecorator.mAcceptDecorator.mType, IntegerValue))

class TypeSystem_Record_Accept(unittest.TestCase):
    def test_AcceptReturnsTrueOnAValidValueType_Empty(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, {})
        typeInstance = MyRecord()
        self.assertTrue(typeInstance.accept({}))

    def test_AcceptReturnsTrueOnAValidValueType_NonEmpty(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, {'foo': Integer()})
        typeInstance = MyRecord()
        self.assertTrue(typeInstance.accept({'foo': Integer().assignValueType(IntegerValue(1))}))

    def test_AcceptReturnsTrueOnAValidValueType_Nested1(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, {'foo': Integer()})
        class MyRecord1(Record):
            def __init__(self):
                Record.__init__(self, {'bar': MyRecord()})
        typeInstance = MyRecord1()
        self.assertTrue(typeInstance.accept({'bar': {'foo': Integer().assignValueType(IntegerValue(1))}}))

    def test_AcceptReturnsTrueOnAValidValueType_Nested2(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, {'foo': Integer()})
        class MyRecord1(Record):
            def __init__(self):
                Record.__init__(self, {'bar': MyRecord()})
        class MyRecord2(Record):
            def __init__(self):
                Record.__init__(self, {'baz1': MyRecord1(),
                                       'baz2': Integer()})
        typeInstance = MyRecord2()
        self.assertTrue(typeInstance.accept({'baz1': {'bar': {'foo': Integer().assignValueType(IntegerValue(1))}},
                                             'baz2': Integer().assignValueType(IntegerValue(1))}))

    def test_AcceptReturnsTrueOnAValidValueType_CompatibleType(self):
        self.skipTest("Not implemented yet.")

    def test_AcceptReturnsTrueOnAValidValueType_Subtyped(self):
        self.skipTest("Not implemented yet.")

    def test_AcceptReturnsTrueOnAValidValueType_DoubleSubtyped(self):
        self.skipTest("Not implemented yet.")

    def test_AcceptReturnsTrueOnAValidValueType_NonEmpty_AnyValue(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, {'foo': Integer()})
        typeInstance = MyRecord()
        self.assertFalse(typeInstance.accept(AnyValue()))

    def test_AcceptReturnsFalseOnAnInvalidValueType_InvalidNumberOfKeys_TooShort(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, {'foo': Integer().assignValueType(IntegerValue(1))})
        typeInstance = MyRecord()
        self.assertFalse(typeInstance.accept({}))

    def test_AcceptReturnsFalseOnAnInvalidValueType_InvalidNumberOfKeys_TooLong(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, {'foo': Integer().assignValueType(IntegerValue(1))})
        typeInstance = MyRecord()
        self.assertFalse(typeInstance.accept({'foo': Integer().assignValueType(IntegerValue(1)),
                                             'bar':  Integer().assignValueType(IntegerValue(1))}))

    def test_AcceptReturnsFalseOnAnInvalidValueType_InvalidKey(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, {'foo': Integer().assignValueType(IntegerValue(1))})
        typeInstance = MyRecord()
        self.assertFalse(typeInstance.accept({'bar': Integer().assignValueType(IntegerValue(1))}))

    def test_AcceptReturnsFalseOnAnInvalidValueType_InvalidValue(self):
        self.skipTest("Not implemented yet.")

class TypeSystem_Record_Template_Accept(unittest.TestCase):
    def test_AcceptReturnsTrueOnAValidValueType_Empty(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, {})
                self.mAcceptDecorator = TemplateAcceptDecorator(self.mAcceptDecorator, {})
        typeInstance = MyRecord()
        self.assertTrue(typeInstance.accept({}))

    def test_AcceptReturnsTrueOnAValidValueType_NonEmpty_AnyValue(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, {'foo': Integer()})
                self.mAcceptDecorator = TemplateAcceptDecorator(self.mAcceptDecorator, {})
        typeInstance = MyRecord()
        self.assertTrue(typeInstance.accept(AnyValue()))

    def test_AcceptReturnsTrueOnAValidValueType_NonEmpty_WithoutSpecialValueType(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, {'foo': Integer()})
                self.mAcceptDecorator = TemplateAcceptDecorator(self.mAcceptDecorator, {})
        typeInstance = MyRecord()
        self.assertTrue(typeInstance.accept({'foo': Integer().assignValueType(IntegerValue(1))}))

    def test_AcceptReturnsTrueOnAValidValueType_NonEmpty_WithSpecialValueType(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, {'foo': Integer()})
                self.mAcceptDecorator = TemplateAcceptDecorator(self.mAcceptDecorator, {})
        typeInstance = MyRecord()
        self.assertTrue(typeInstance.accept({'foo': TemplateInteger().assignValueType(AnyValue())}))

    def test_AcceptReturnsTrueOnAValidValueType_Nested1_WithoutSpecialValueType(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, {'foo': Integer()})
        class MyRecord1(Record):
            def __init__(self):
                Record.__init__(self, {'bar': MyRecord()})
                self.mAcceptDecorator = TemplateAcceptDecorator(self.mAcceptDecorator, {})
        typeInstance = MyRecord1()
        self.assertTrue(typeInstance.accept({'bar': {'foo': Integer().assignValueType(IntegerValue(1))}}))

    def test_AcceptReturnsTrueOnAValidValueType_Nested1_WithSpecialValueType(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, {'foo': Integer()})
        class MyRecord1(Record):
            def __init__(self):
                Record.__init__(self, {'bar': MyRecord()})
                self.mAcceptDecorator = TemplateAcceptDecorator(self.mAcceptDecorator, {})
        typeInstance = MyRecord1()
        self.assertTrue(typeInstance.accept({'bar': {'foo': TemplateInteger().assignValueType(AnyValue())}}))

    def test_AcceptReturnsTrueOnAValidValueType_Nested2_WithoutSpecialValueType(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, {'foo': Integer()})
        class MyRecord1(Record):
            def __init__(self):
                Record.__init__(self, {'bar': MyRecord()})
        class MyRecord2(Record):
            def __init__(self):
                Record.__init__(self, {'baz1': MyRecord1(),
                                       'baz2': Integer()})
                self.mAcceptDecorator = TemplateAcceptDecorator(self.mAcceptDecorator, {})
        typeInstance = MyRecord2()
        self.assertTrue(typeInstance.accept({'baz1': {'bar': {'foo': Integer().assignValueType(IntegerValue(1))}},
                                             'baz2': Integer().assignValueType(IntegerValue(1))}))

    def test_AcceptReturnsTrueOnAValidValueType_Nested2_WithSpecialValueType(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, {'foo': Integer()})
        class MyRecord1(Record):
            def __init__(self):
                Record.__init__(self, {'bar': MyRecord()})
        class MyRecord2(Record):
            def __init__(self):
                Record.__init__(self, {'baz1': MyRecord1(),
                                       'baz2': Integer()})
                self.mAcceptDecorator = TemplateAcceptDecorator(self.mAcceptDecorator, {})
        typeInstance = MyRecord2()
        self.assertTrue(typeInstance.accept({'baz1': {'bar': {'foo': TemplateInteger().assignValueType(AnyValue())}},
                                             'baz2': TemplateInteger().assignValueType(AnyValue())}))

    def test_AcceptReturnsTrueOnAValidValueType_CompatibleType(self):
        self.skipTest("Not implemented yet.")

    def test_AcceptReturnsTrueOnAValidValueType_Subtyped(self):
        self.skipTest("Not implemented yet.")

    def test_AcceptReturnsTrueOnAValidValueType_DoubleSubtyped(self):
        self.skipTest("Not implemented yet.")

    def test_AcceptReturnsFalseOnAnInvalidValueType_InvalidNumberOfKeys_TooShort(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, {'foo': Integer().assignValueType(IntegerValue(1))})
                self.mAcceptDecorator = TemplateAcceptDecorator(self.mAcceptDecorator, {})
        typeInstance = MyRecord()
        self.assertFalse(typeInstance.accept({}))

    def test_AcceptReturnsFalseOnAnInvalidValueType_InvalidNumberOfKeys_TooLong(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, {'foo': Integer().assignValueType(IntegerValue(1))})
                self.mAcceptDecorator = TemplateAcceptDecorator(self.mAcceptDecorator, {})
        typeInstance = MyRecord()
        self.assertFalse(typeInstance.accept({'foo': Integer().assignValueType(IntegerValue(1)),
                                              'bar': Integer().assignValueType(IntegerValue(1))}))

    def test_AcceptReturnsFalseOnAnInvalidValueType_InvalidKey(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, {'foo': Integer().assignValueType(IntegerValue(1))})
                self.mAcceptDecorator = TemplateAcceptDecorator(self.mAcceptDecorator, {})
        typeInstance = MyRecord()
        self.assertFalse(typeInstance.accept({'bar': Integer().assignValueType(IntegerValue(1))}))

    def test_AcceptReturnsFalseOnAnInvalidValueType_InvalidValue(self):
        self.skipTest("Not implemented yet.")

class TypeSystem_Record_RecordOf_Accept(unittest.TestCase):
    def test_AcceptReturnsTrueOnAValidValueType_Standalone_EmptyRecord(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, Integer())
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, {'foo': MyRecordOf()})
        valueTypeRecordOf = []
        valueTypeRecord = {'foo': valueTypeRecordOf}
        typeInstance = MyRecord()
        self.assertTrue(typeInstance.accept(valueTypeRecord))

    def test_AcceptReturnsTrueOnAValidValueType_Standalone_NonEmptyRecord(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, Integer())
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, {'foo': MyRecordOf()})
        valueTypeRecordOf = [Integer().assignValueType(IntegerValue(22))]
        valueTypeRecord = {'foo': valueTypeRecordOf}
        typeInstance = MyRecord()
        self.assertTrue(typeInstance.accept(valueTypeRecord))

    def test_AcceptReturnsTrueOnAValidValueType_WithOtherTypes_EmptyRecord(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, Integer())
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, {'foo': Integer(),
                                       'bar': MyRecordOf(),
                                       'baz': Integer()})
        typeInstance = MyRecord()
        valueTypeRecordOf = []
        valueTypeRecord = {'foo': Integer().assignValueType(IntegerValue(1)),
                           'bar': valueTypeRecordOf,
                           'baz': Integer().assignValueType(IntegerValue(2))}
        self.assertTrue(typeInstance.accept(valueTypeRecord))

    def test_AcceptReturnsTrueOnAValidValueType_WithOtherTypes_NonEmptyRecord(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, Integer())
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, {'foo': Integer(),
                                       'bar': MyRecordOf(),
                                       'baz': Integer()})
        typeInstance = MyRecord()
        valueTypeRecordOf = [Integer().assignValueType(IntegerValue(22))]
        valueTypeRecord = {'foo': Integer().assignValueType(IntegerValue(1)),
                           'bar': valueTypeRecordOf,
                           'baz': Integer().assignValueType(IntegerValue(2))}
        self.assertTrue(typeInstance.accept(valueTypeRecord))

    def test_AcceptReturnsFalseOnAnInvalidValueType_Standalone_RecordNotInitialized(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, Integer())
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, {'foo': MyRecordOf()})
        valueTypeRecordOf = [Integer()]
        valueTypeRecord = {'foo': valueTypeRecordOf}
        typeInstance = MyRecord()
        self.assertFalse(typeInstance.accept(valueTypeRecord))

    def test_AcceptReturnsFalseOnAnInvalidValueType_WithOtherTypes_RecordOfNotInitialized(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, Integer())
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, {'foo': Integer(),
                                       'bar': MyRecordOf(),
                                       'baz': Integer()})
        typeInstance = MyRecord()
        valueTypeRecordOf = [Integer()]
        valueTypeRecord = {'foo': Integer().assignValueType(IntegerValue(1)),
                           'bar': valueTypeRecordOf,
                           'baz': Integer().assignValueType(IntegerValue(2))}
        self.assertFalse(typeInstance.accept(valueTypeRecordOf))

    def test_AcceptReturnsFalseOnAnInvalidValueType_WithOtherTypes_AnyOtherTypeNotInitialized(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, Integer())
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, {'foo': Integer(),
                                       'bar': MyRecordOf(),
                                       'baz': Integer()})
        typeInstance = MyRecord()
        valueTypeRecordOf = [Integer().assignValueType(IntegerValue(22))]
        valueTypeRecord = {'foo': Integer().assignValueType(IntegerValue(1)),
                           'bar': valueTypeRecordOf,
                           'baz': Integer()}
        self.assertFalse(typeInstance.accept(valueTypeRecord))

    def test_AcceptReturnsFalseOnAnInvalidValueType_Standalone_WithSpecialValue(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, Integer())
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, {'foo': MyRecordOf()})
        valueTypeRecordOf = [TemplateInteger().assignValueType(AnyValue())]
        valueTypeRecord = {'foo': valueTypeRecordOf}
        typeInstance = MyRecord()
        self.assertFalse(typeInstance.accept(valueTypeRecord))

    def test_AcceptReturnsFalseOnAnInvalidValueType_WithOtherTypes_RecordOfWithSpecialValue(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, Integer())
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, {'foo': Integer(),
                                       'bar': MyRecordOf(),
                                       'baz': Integer()})
        typeInstance = MyRecord()
        valueTypeRecordOf = [TemplateInteger().assignValueType(AnyValue())]
        valueTypeRecord = {'foo': Integer().assignValueType(IntegerValue(1)),
                           'bar': valueTypeRecordOf,
                           'baz': Integer().assignValueType(IntegerValue(2))}
        self.assertFalse(typeInstance.accept(valueTypeRecordOf))

    def test_AcceptReturnsFalseOnAnInvalidValueType_WithOtherTypes_AnyOtherTypeWithSpecialValue(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, Integer())
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, {'foo': Integer(),
                                       'bar': MyRecordOf(),
                                       'baz': Integer()})
        typeInstance = MyRecord()
        valueTypeRecordOf = [Integer().assignValueType(IntegerValue(1))]
        valueTypeRecord = {'foo': TemplateInteger().assignValueType(AnyValue()),
                           'bar': valueTypeRecordOf,
                           'baz': Integer().assignValueType(IntegerValue(2))}
        self.assertFalse(typeInstance.accept(valueTypeRecordOf))

class TypeSystem_Record_RecordOf_Template_Accept(unittest.TestCase):
    def test_AcceptReturnsTrueOnAValidValueType_Standalone_EmptyRecord(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, Integer())
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, {'foo': MyRecordOf()})
                self.mAcceptDecorator = TemplateAcceptDecorator(self.mAcceptDecorator, {})
        valueTypeRecordOf = []
        valueTypeRecord = {'foo': valueTypeRecordOf}
        typeInstance = MyRecord()
        self.assertTrue(typeInstance.accept(valueTypeRecord))

    def test_AcceptReturnsTrueOnAValidValueType_Standalone_NonEmptyRecord(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, Integer())
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, {'foo': MyRecordOf()})
                self.mAcceptDecorator = TemplateAcceptDecorator(self.mAcceptDecorator, {})
        valueTypeRecordOf = [TemplateInteger().assignValueType(AnyValue())]
        valueTypeRecord = {'foo': valueTypeRecordOf}
        typeInstance = MyRecord()
        self.assertTrue(typeInstance.accept(valueTypeRecord))

    def test_AcceptReturnsTrueOnAValidValueType_WithOtherTypes_EmptyRecord(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, Integer())
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, {'foo': Integer(),
                                       'bar': MyRecordOf(),
                                       'baz': Integer()})
                self.mAcceptDecorator = TemplateAcceptDecorator(self.mAcceptDecorator, {})
        typeInstance = MyRecord()
        valueTypeRecordOf = []
        valueTypeRecord = {'foo': Integer().assignValueType(IntegerValue(1)),
                           'bar': valueTypeRecordOf,
                           'baz': Integer().assignValueType(IntegerValue(2))}
        self.assertTrue(typeInstance.accept(valueTypeRecord))

    def test_AcceptReturnsTrueOnAValidValueType_WithOtherTypes_NonEmptyRecord(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, Integer())
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, {'foo': Integer(),
                                       'bar': MyRecordOf(),
                                       'baz': Integer()})
                self.mAcceptDecorator = TemplateAcceptDecorator(self.mAcceptDecorator, {})
        typeInstance = MyRecord()
        valueTypeRecordOf = [TemplateInteger().assignValueType(AnyValue())]
        valueTypeRecord = {'foo': Integer().assignValueType(IntegerValue(1)),
                           'bar': valueTypeRecordOf,
                           'baz': Integer().assignValueType(IntegerValue(2))}
        self.assertTrue(typeInstance.accept(valueTypeRecord))

    def test_AcceptReturnsFalseOnAnInvalidValueType_Standalone_RecordNotInitialized(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, Integer())
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, {'foo': MyRecordOf()})
                self.mAcceptDecorator = TemplateAcceptDecorator(self.mAcceptDecorator, {})
        valueTypeRecordOf = [TemplateInteger()]
        valueTypeRecord = {'foo': valueTypeRecordOf}
        typeInstance = MyRecord()
        self.assertFalse(typeInstance.accept(valueTypeRecord))

    def test_AcceptReturnsFalseOnAnInvalidValueType_WithOtherTypes_RecordOfNotInitialized(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, Integer())
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, {'foo': Integer(),
                                       'bar': MyRecordOf(),
                                       'baz': Integer()})
                self.mAcceptDecorator = TemplateAcceptDecorator(self.mAcceptDecorator, {})
        typeInstance = MyRecord()
        valueTypeRecordOf = [TemplateInteger()]
        valueTypeRecord = {'foo': Integer().assignValueType(IntegerValue(1)),
                           'bar': valueTypeRecordOf,
                           'baz': Integer().assignValueType(IntegerValue(2))}
        self.assertFalse(typeInstance.accept(valueTypeRecordOf))

    def test_AcceptReturnsFalseOnAnInvalidValueType_WithOtherTypes_AnyOtherTypeNotInitialized(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, Integer())
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, {'foo': Integer(),
                                       'bar': MyRecordOf(),
                                       'baz': Integer()})
                self.mAcceptDecorator = TemplateAcceptDecorator(self.mAcceptDecorator, {})
        typeInstance = MyRecord()
        valueTypeRecordOf = [TemplateInteger().assignValueType(AnyValue())]
        valueTypeRecord = {'foo': Integer().assignValueType(IntegerValue(1)),
                           'bar': valueTypeRecordOf,
                           'baz': Integer()}
        self.assertFalse(typeInstance.accept(valueTypeRecord))

class TypeSystem_Record_AssignValueType(unittest.TestCase):
    def test_AssignValueTypeAssignsOnAValidValueType_Empty(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, {})
        typeInstance = MyRecord()
        self.assertEqual(typeInstance.assignValueType({}).valueType(), {})

    def test_AssignValueTypeAssignsOnAValidValueType_NonEmpty(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, {'foo': Integer()})
        typeInstance = MyRecord()
        valueType = {'foo': Integer().assignValueType(IntegerValue(1))}
        self.assertEqual(typeInstance.assignValueType(valueType).valueType(), valueType)

    def test_AssignValueTypeAssignsOnAValidValueType_Nested1(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, {'foo': Integer()})
        class MyRecord1(Record):
            def __init__(self):
                Record.__init__(self, {'bar': MyRecord()})
        typeInstance = MyRecord1()
        valueType = {'bar': {'foo': Integer().assignValueType(IntegerValue(1))}}
        self.assertEqual(typeInstance.assignValueType(valueType).valueType(), valueType)

    def test_AssignValueTypeAssignsOnAValidValueType_Nested2(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, {'foo': Integer()})
        class MyRecord1(Record):
            def __init__(self):
                Record.__init__(self, {'bar': MyRecord()})
        class MyRecord2(Record):
            def __init__(self):
                Record.__init__(self, {'baz1': MyRecord1(),
                                       'baz2': Integer()})
        typeInstance = MyRecord2()
        valueType = {'baz1': {'bar': {'foo': Integer().assignValueType(IntegerValue(1))}},
                                      'baz2': Integer().assignValueType(IntegerValue(1))}
        self.assertEqual(typeInstance.assignValueType(valueType).valueType(), valueType)

    def test_AssignValueTypeAssignsOnAValidValueType_CompatibleType(self):
        self.skipTest("Not implemented yet.")

    def test_AssignValueTypeAssignsOnAValidValueType_Subtyped(self):
        self.skipTest("Not implemented yet.")

    def test_AssignValueTypeAssignsOnAValidValueType_DoubleSubtyped(self):
        self.skipTest("Not implemented yet.")

    def test_AssignValueTypeRaisesAnExceptionOnAnInvalidType_InvalidNumberOfKeys_TooShort(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, {'foo': Integer().assignValueType(IntegerValue(1))})
        typeInstance = MyRecord()
        with self.assertRaises(InvalidTypeInValueTypeAssignment):
            typeInstance.assignValueType({})

    def test_AssignValueTypeRaisesAnExceptionOnAnInvalidType_InvalidNumberOfKeys_TooLong(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, {'foo': Integer().assignValueType(IntegerValue(1))})
        typeInstance = MyRecord()
        with self.assertRaises(InvalidTypeInValueTypeAssignment):
            typeInstance.assignValueType({'foo': Integer().assignValueType(IntegerValue(1)),
                                          'bar':  Integer().assignValueType(IntegerValue(1))})

    def test_AssignValueTypeRaisesAnExceptionOnAnInvalidType_InvalidKey(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, {'foo': Integer().assignValueType(IntegerValue(1))})
        typeInstance = MyRecord()
        with self.assertRaises(InvalidTypeInValueTypeAssignment):
            typeInstance.assignValueType({'bar': Integer().assignValueType(IntegerValue(1))})

    def test_AssignValueTypeRaisesAnExceptionOnAnInvalidType_InvalidValue(self):
        self.skipTest("Not implemented yet.")

class TypeSystem_Record_Template_AssignValueType(unittest.TestCase):
    def test_AssignValueTypeAssignsOnAValidValueType_Empty(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, {})
                self.mAcceptDecorator = TemplateAcceptDecorator(self.mAcceptDecorator, {})
        typeInstance = MyRecord()
        self.assertEqual(typeInstance.assignValueType({}).valueType(), {})

    def test_AssignValueTypeAssignsOnAValidValueType_NonEmpty_AnyValue(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, {'foo': Integer()})
                self.mAcceptDecorator = TemplateAcceptDecorator(self.mAcceptDecorator, {})
        typeInstance1 = MyRecord()
        typeInstance2 = MyRecord()
        typeInstance2.assignValueType({
            'foo': TemplateInteger().assignValueType(AnyValue())
        })
        self.assertEqual(typeInstance1.assignValueType(AnyValue()).valueType(), typeInstance2)

    def test_AssignValueTypeAssignsOnAValidValueType_NonEmpty_WithoutSpecialValueType(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, {'foo': Integer()})
                self.mAcceptDecorator = TemplateAcceptDecorator(self.mAcceptDecorator, {})
        typeInstance = MyRecord()
        valueType = {'foo': Integer().assignValueType(IntegerValue(1))}
        self.assertEqual(typeInstance.assignValueType(valueType).valueType(), valueType)

    def test_AssignValueTypeAssignsOnAValidValueType_NonEmpty_WithSpecialValueType(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, {'foo': Integer()})
                self.mAcceptDecorator = TemplateAcceptDecorator(self.mAcceptDecorator, {})
        typeInstance = MyRecord()
        valueType = {'foo': TemplateInteger().assignValueType(AnyValue())}
        self.assertEqual(typeInstance.assignValueType(valueType).valueType(), valueType)

    def test_AssignValueTypeAssignsOnAValidValueType_Nested1_WithoutSpecialValueType(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, {'foo': Integer()})
        class MyRecord1(Record):
            def __init__(self):
                Record.__init__(self, {'bar': MyRecord()})
                self.mAcceptDecorator = TemplateAcceptDecorator(self.mAcceptDecorator, {})
        typeInstance = MyRecord1()
        valueType = {'bar': {'foo': Integer().assignValueType(IntegerValue(1))}}
        self.assertEqual(typeInstance.assignValueType(valueType).valueType(), valueType)

    def test_AssignValueTypeAssignsOnAValidValueType_Nested1_WithSpecialValueType(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, {'foo': Integer()})
        class MyRecord1(Record):
            def __init__(self):
                Record.__init__(self, {'bar': MyRecord()})
                self.mAcceptDecorator = TemplateAcceptDecorator(self.mAcceptDecorator, {})
        typeInstance = MyRecord1()
        valueType = {'bar': {'foo': TemplateInteger().assignValueType(AnyValue())}}
        self.assertEqual(typeInstance.assignValueType(valueType).valueType(), valueType)

    def test_AssignValueTypeAssignsOnAValidValueType_Nested2_WithoutSpecialValueType(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, {'foo': Integer()})
        class MyRecord1(Record):
            def __init__(self):
                Record.__init__(self, {'bar': MyRecord()})
        class MyRecord2(Record):
            def __init__(self):
                Record.__init__(self, {'baz1': MyRecord1(),
                                       'baz2': Integer()})
                self.mAcceptDecorator = TemplateAcceptDecorator(self.mAcceptDecorator, {})
        typeInstance = MyRecord2()
        valueType = {'baz1': {'bar': {'foo': Integer().assignValueType(IntegerValue(1))}},
                                      'baz2': Integer().assignValueType(IntegerValue(1))}
        self.assertEqual(typeInstance.assignValueType(valueType).valueType(), valueType)
#
    def test_AssignValueTypeAssignsOnAValidValueType_Nested2_WithSpecialValueType(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, {'foo': Integer()})
        class MyRecord1(Record):
            def __init__(self):
                Record.__init__(self, {'bar': MyRecord()})
        class MyRecord2(Record):
            def __init__(self):
                Record.__init__(self, {'baz1': MyRecord1(),
                                       'baz2': Integer()})
                self.mAcceptDecorator = TemplateAcceptDecorator(self.mAcceptDecorator, {})
        typeInstance = MyRecord2()
        valueType = {'baz1': {'bar': {'foo': TemplateInteger().assignValueType(AnyValue())}},
                                      'baz2': TemplateInteger().assignValueType(AnyValue())}
        self.assertEqual(typeInstance.assignValueType(valueType).valueType(), valueType)

    def test_AssignValueTypeAssignsOnAValidValueType_CompatibleType(self):
        self.skipTest("Not implemented yet.")

    def test_AssignValueTypeAssignsOnAValidValueType_Subtyped(self):
        self.skipTest("Not implemented yet.")

    def test_AssignValueTypeAssignsOnAValidValueType_DoubleSubtyped(self):
        self.skipTest("Not implemented yet.")

    def test_AssignValueTypeRaisesAnExceptionOnAnInvalidValueType_InvalidNumberOfKeys_TooShort(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, {'foo': Integer().assignValueType(IntegerValue(1))})
                self.mAcceptDecorator = TemplateAcceptDecorator(self.mAcceptDecorator, {})
        typeInstance = MyRecord()
        with self.assertRaises(InvalidTypeInValueTypeAssignment):
            typeInstance.assignValueType({})

    def test_AssignValueTypeRaisesAnExceptionOnAnInvalidValueType_InvalidNumberOfKeys_TooLong(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, {'foo': Integer().assignValueType(IntegerValue(1))})
                self.mAcceptDecorator = TemplateAcceptDecorator(self.mAcceptDecorator, {})
        typeInstance = MyRecord()
        with self.assertRaises(InvalidTypeInValueTypeAssignment):
            typeInstance.assignValueType({'foo': Integer().assignValueType(IntegerValue(1)),
                                          'bar': Integer().assignValueType(IntegerValue(1))})

    def test_AssignValueTypeRaisesAnExceptionOnAnInvalidValueType_InvalidKey(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, {'foo': Integer().assignValueType(IntegerValue(1))})
                self.mAcceptDecorator = TemplateAcceptDecorator(self.mAcceptDecorator, {})
        typeInstance = MyRecord()
        with self.assertRaises(InvalidTypeInValueTypeAssignment):
            typeInstance.assignValueType({'bar': Integer().assignValueType(IntegerValue(1))})

    def test_AssignValueTypeRaisesAnExceptionOnAnInvalidValueType_InvalidValue(self):
        self.skipTest("Not implemented yet.")

class TypeSystem_RecordOf_Ctor(unittest.TestCase):
    def test_Ctor(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, Integer())
        typeInstance = MyRecordOf()

    def test_Ctor_Nested1(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, Integer())
        class MyRecordOf1(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, MyRecordOf())
        typeInstance = MyRecordOf1()

    def test_Ctor_Nested2(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, Integer())
        class MyRecordOf1(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, MyRecordOf())
        class MyRecordOf2(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, MyRecordOf1())
        typeInstance = MyRecordOf2()

class TypeSystem_RecordOf_Template_Ctor(unittest.TestCase):
    def test_Ctor(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, Integer())
                self.mAcceptDecorator = TemplateAcceptDecorator(self.mAcceptDecorator, {})
        typeInstance = MyRecordOf()
        self.assertTrue(isinstance(typeInstance.mAcceptDecorator, TemplateAcceptDecorator))
        self.assertTrue(isinstance(typeInstance.mAcceptDecorator.mAcceptDecorator, RecordOfAcceptDecorator))
        self.assertTrue(isinstance(typeInstance.mAcceptDecorator.mAcceptDecorator.mDescriptorType, Integer))
        self.assertTrue(isinstance(typeInstance.mAcceptDecorator.mAcceptDecorator.mDescriptorType.mAcceptDecorator, TemplateAcceptDecorator))
        self.assertTrue(isinstance(typeInstance.mAcceptDecorator.mAcceptDecorator.mDescriptorType.mAcceptDecorator.mAcceptDecorator, TypeAcceptDecorator))
        self.assertTrue(issubclass(typeInstance.mAcceptDecorator.mAcceptDecorator.mDescriptorType.mAcceptDecorator.mAcceptDecorator.mType, IntegerValue))

    def test_Ctor_Nested1(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, Integer())
        class MyRecordOf1(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, MyRecordOf())
                self.mAcceptDecorator = TemplateAcceptDecorator(self.mAcceptDecorator, {})
        typeInstance = MyRecordOf1()
        self.assertTrue(isinstance(typeInstance.mAcceptDecorator, TemplateAcceptDecorator))
        self.assertTrue(isinstance(typeInstance.mAcceptDecorator.mAcceptDecorator, RecordOfAcceptDecorator))
        self.assertTrue(isinstance(typeInstance.mAcceptDecorator.mAcceptDecorator.mDescriptorType, MyRecordOf))
        self.assertTrue(isinstance(typeInstance.mAcceptDecorator.mAcceptDecorator.mDescriptorType.mAcceptDecorator, TemplateAcceptDecorator))
        self.assertTrue(isinstance(typeInstance.mAcceptDecorator.mAcceptDecorator.mDescriptorType.mAcceptDecorator.mAcceptDecorator, RecordOfAcceptDecorator))
        self.assertTrue(isinstance(typeInstance.mAcceptDecorator.mAcceptDecorator.mDescriptorType.mAcceptDecorator.mAcceptDecorator.mDescriptorType, Integer))
        self.assertTrue(isinstance(typeInstance.mAcceptDecorator.mAcceptDecorator.mDescriptorType.mAcceptDecorator.mAcceptDecorator.mDescriptorType.mAcceptDecorator, TemplateAcceptDecorator))
        self.assertTrue(isinstance(typeInstance.mAcceptDecorator.mAcceptDecorator.mDescriptorType.mAcceptDecorator.mAcceptDecorator.mDescriptorType.mAcceptDecorator.mAcceptDecorator, TypeAcceptDecorator))
        self.assertTrue(issubclass(typeInstance.mAcceptDecorator.mAcceptDecorator.mDescriptorType.mAcceptDecorator.mAcceptDecorator.mDescriptorType.mAcceptDecorator.mAcceptDecorator.mType, IntegerValue))

    def test_Ctor_Nested2(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, Integer())
        class MyRecordOf1(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, MyRecordOf())
        class MyRecordOf2(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, MyRecordOf1())
                self.mAcceptDecorator = TemplateAcceptDecorator(self.mAcceptDecorator, {})
        typeInstance = MyRecordOf2()
        self.assertTrue(isinstance(typeInstance.mAcceptDecorator, TemplateAcceptDecorator))
        self.assertTrue(isinstance(typeInstance.mAcceptDecorator.mAcceptDecorator, RecordOfAcceptDecorator))
        self.assertTrue(isinstance(typeInstance.mAcceptDecorator.mAcceptDecorator.mDescriptorType, MyRecordOf1))
        self.assertTrue(isinstance(typeInstance.mAcceptDecorator.mAcceptDecorator.mDescriptorType.mAcceptDecorator, TemplateAcceptDecorator))
        self.assertTrue(isinstance(typeInstance.mAcceptDecorator.mAcceptDecorator.mDescriptorType.mAcceptDecorator.mAcceptDecorator, RecordOfAcceptDecorator))
        self.assertTrue(isinstance(typeInstance.mAcceptDecorator.mAcceptDecorator.mDescriptorType.mAcceptDecorator.mAcceptDecorator.mDescriptorType, MyRecordOf))
        self.assertTrue(isinstance(typeInstance.mAcceptDecorator.mAcceptDecorator.mDescriptorType.mAcceptDecorator.mAcceptDecorator.mDescriptorType.mAcceptDecorator, TemplateAcceptDecorator))
        self.assertTrue(isinstance(typeInstance.mAcceptDecorator.mAcceptDecorator.mDescriptorType.mAcceptDecorator.mAcceptDecorator.mDescriptorType.mAcceptDecorator.mAcceptDecorator, RecordOfAcceptDecorator))
        self.assertTrue(isinstance(typeInstance.mAcceptDecorator.mAcceptDecorator.mDescriptorType.mAcceptDecorator.mAcceptDecorator.mDescriptorType.mAcceptDecorator.mAcceptDecorator.mDescriptorType, Integer))
        self.assertTrue(isinstance(typeInstance.mAcceptDecorator.mAcceptDecorator.mDescriptorType.mAcceptDecorator.mAcceptDecorator.mDescriptorType.mAcceptDecorator.mAcceptDecorator.mDescriptorType.mAcceptDecorator, TemplateAcceptDecorator))
        self.assertTrue(isinstance(typeInstance.mAcceptDecorator.mAcceptDecorator.mDescriptorType.mAcceptDecorator.mAcceptDecorator.mDescriptorType.mAcceptDecorator.mAcceptDecorator.mDescriptorType.mAcceptDecorator.mAcceptDecorator, TypeAcceptDecorator))
        self.assertTrue(issubclass(typeInstance.mAcceptDecorator.mAcceptDecorator.mDescriptorType.mAcceptDecorator.mAcceptDecorator.mDescriptorType.mAcceptDecorator.mAcceptDecorator.mDescriptorType.mAcceptDecorator.mAcceptDecorator.mType, IntegerValue))

class TypeSystem_RecordOf_Accept(unittest.TestCase):
    def test_AcceptReturnsTrueOnAValidValue_AnEmptyList(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, Integer())
        instance = MyRecordOf()
        valueType = []
        self.assertTrue(instance.accept(valueType))

    def test_AcceptReturnsTrueOnAValidValue_ASingleElementList(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, Integer())
        instance = MyRecordOf()
        valueType = [Integer().assignValueType(IntegerValue(1))]
        self.assertTrue(instance.accept(valueType))

    def test_AcceptReturnsTrueOnAValidValue_AManyElementsList(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, Integer())
        instance = MyRecordOf()
        valueType = [Integer().assignValueType(IntegerValue(1)), Integer().assignValueType(IntegerValue(2))]
        self.assertTrue(instance.accept(valueType))

    def test_AcceptReturnsTrueOnAValidValue_AnyOfValuesIsATemplateLikeType_WithoutSpecialValueType(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, Integer())
        instance = MyRecordOf()
        valueType = [Integer().assignValueType(IntegerValue(1)),
                     TemplateInteger().assignValueType(IntegerValue(2))]
        self.assertTrue(instance.accept(valueType))

    def test_AcceptReturnsFalseOnAnInvalidValue_InvalidValue_AnyValue(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, Integer())
        instance = MyRecordOf()
        self.assertFalse(instance.accept(AnyValue()))

    def test_AcceptReturnsFalseOnAnInvalidValue_InvalidValue_AnyOfValuesIsATemplateLikeType_WithSpecialValueType(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, Integer())
        instance = MyRecordOf()
        valueType = [Integer().assignValueType(IntegerValue(1)),
                     TemplateInteger().assignValueType(AnyValue())]
        self.assertFalse(instance.accept(valueType))

    def test_AcceptReturnsFalseOnAnInvalidValue_InvalidType_BuiltIn(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, Integer())
        instance = MyRecordOf()
        for valueType in [True, 1, 1.0, "WAX", [1, 2], (1, 2)]:
            self.assertFalse(instance.accept(valueType))

    def test_AcceptReturnsFalseOnAnInvalidValue_InvalidType_Special(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, Integer())
        instance = MyRecordOf()
        for valueType in [[AnyValue()]]:
            self.assertFalse(instance.accept(valueType))

    def test_AcceptReturnsFalseOnAnInvalidValue_InvalidType_Template(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, Integer())
        instance = MyRecordOf()
        for valueType in [[TemplateInteger().assignValueType(IntegerValue(1)),
                           TemplateInteger().assignValueType(AnyValue())]]:
            self.assertFalse(instance.accept(valueType))

    def test_IsCompatibleReturnsFalseOnAnIncompatibleType_Regular(self):
        self.skipTest("Not implemented yet.")

class TypeSystem_RecordOf_Template_Accept(unittest.TestCase):
    def test_AcceptReturnsTrueOnAValidValue_AnEmptyList(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, Integer())
                self.mAcceptDecorator = TemplateAcceptDecorator(self.mAcceptDecorator, {})
        instance = MyRecordOf()
        valueType = []
        self.assertTrue(instance.accept(valueType))

    def test_AcceptReturnsTrueOnAVvalidValue_AnyValue(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, Integer())
                self.mAcceptDecorator = TemplateAcceptDecorator(self.mAcceptDecorator, {})
        instance = MyRecordOf()
        self.assertTrue(instance.accept(AnyValue()))

    def test_AcceptReturnsTrueOnAValidValue_ASingleElementList(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, Integer())
                self.mAcceptDecorator = TemplateAcceptDecorator(self.mAcceptDecorator, {})
        instance = MyRecordOf()
        valueType = [Integer().assignValueType(IntegerValue(1))]
        self.assertTrue(instance.accept(valueType))

    def test_AcceptReturnsTrueOnAValidValue_AManyElementsList(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, Integer())
                self.mAcceptDecorator = TemplateAcceptDecorator(self.mAcceptDecorator, {})
        instance = MyRecordOf()
        valueType = [Integer().assignValueType(IntegerValue(1)), Integer().assignValueType(IntegerValue(2))]
        self.assertTrue(instance.accept(valueType))

    def test_AcceptReturnsTrueOnAValidValue_AnyOfValuesIsATemplateLikeType_WithoutSpecialValueType(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, Integer())
                self.mAcceptDecorator = TemplateAcceptDecorator(self.mAcceptDecorator, {})
        instance = MyRecordOf()
        valueType = [Integer().assignValueType(IntegerValue(1)),
                     TemplateInteger().assignValueType(IntegerValue(2))]
        self.assertTrue(instance.accept(valueType))

    def test_AcceptReturnsTrueOnAValidValue_AnyOfValuesIsATemplateLikeType_WithSpecialValueType(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, Integer())
                self.mAcceptDecorator = TemplateAcceptDecorator(self.mAcceptDecorator, {})
        instance = MyRecordOf()
        valueType = [Integer().assignValueType(IntegerValue(1)),
                     TemplateInteger().assignValueType(AnyValue())]
        self.assertTrue(instance.accept(valueType))

    def test_AcceptReturnsFalseOnAnInvalidValue_InvalidType_BuiltIn(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, Integer())
                self.mAcceptDecorator = TemplateAcceptDecorator(self.mAcceptDecorator, {})
        instance = MyRecordOf()
        for valueType in [True, 1, 1.0, "WAX", [1, 2], (1, 2)]:
            self.assertFalse(instance.accept(valueType))

    def test_AcceptReturnsFalseOnAnInvalidValue_InvalidType_Special(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, Integer())
                self.mAcceptDecorator = TemplateAcceptDecorator(self.mAcceptDecorator, {})
        instance = MyRecordOf()
        for valueType in [[AnyValue()]]:
            self.assertFalse(instance.accept(valueType))

    def test_IsCompatibleReturnsFalseOnAnIncompatibleType_Regular(self):
        self.skipTest("Not implemented yet.")

class TypeSystem_RecordOf_AssignValueType(unittest.TestCase):
    def test_AssignValueTypeAssignsOnAValidValue_AnEmptyList(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, Integer())
        instanceType = MyRecordOf()
        valueType = []
        self.assertEqual(instanceType.assignValueType(valueType).valueType(), valueType)

    def test_AssignValueTypeAssignsOnAValidValue_ASingleElementList(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, Integer())
        instanceType = MyRecordOf()
        valueType = [Integer().assignValueType(IntegerValue(1))]
        self.assertEqual(instanceType.assignValueType(valueType).valueType(), valueType)

    def test_AssignValueTypeAssignsOnAValidValue_AManyElementsList(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, Integer())
        instanceType = MyRecordOf()
        valueType = [Integer().assignValueType(IntegerValue(1)), Integer().assignValueType(IntegerValue(2))]
        self.assertEqual(instanceType.assignValueType(valueType).valueType(), valueType)

    def test_AssignValueTypeAssignsOnAValidValue_AnyOfValuesIsATemplateLikeType_WithoutSpecialValueType(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, Integer())
        instanceType = MyRecordOf()
        valueType = [Integer().assignValueType(IntegerValue(1)),
                     TemplateInteger().assignValueType(IntegerValue(2))]
        self.assertEqual(instanceType.assignValueType(valueType).valueType(), valueType)

    def test_AssignValueTypeRaisesAnExceptionOnAnInvalidValue_InvalidValue_AnyOfValuesIsATemplateLikeType_WithSpecialValueType(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, Integer())
        instanceType = MyRecordOf()
        valueType = [Integer().assignValueType(IntegerValue(1)),
                     TemplateInteger().assignValueType(AnyValue())]
        with self.assertRaises(InvalidTypeInValueTypeAssignment):
            instanceType.assignValueType(valueType)

    def test_AssignValueTypeRaisesAnExceptionOnAnInvalidValue_InvalidType_BuiltIn(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, Integer())
        instanceType = MyRecordOf()
        for valueType in [True, 1, 1.0, "WAX", [1, 2], (1, 2)]:
            with self.assertRaises(InvalidTypeInValueTypeAssignment):
                instanceType.assignValueType(valueType)

    def test_AssignValueTypeRaisesAnExceptionOnAnInvalidValue_InvalidType_Special(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, Integer())
        instanceType = MyRecordOf()
        for valueType in [[AnyValue()]]:
            with self.assertRaises(InvalidTypeInValueTypeAssignment):
                instanceType.assignValueType(valueType)

    def test_AssignValueTypeRaisesAnExceptionOnAnInvalidValue_InvalidType_Template(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, Integer())
        instanceType = MyRecordOf()
        for valueType in [[TemplateInteger().assignValueType(IntegerValue(1)),
                           TemplateInteger().assignValueType(AnyValue())]]:
            with self.assertRaises(InvalidTypeInValueTypeAssignment):
                instanceType.assignValueType(valueType)

    def test_IsCompatibleReturnsFalseOnAnIncompatibleType_Regular(self):
        self.skipTest("Not implemented yet.")

class TypeSystem_RecordOf_Template_AssignValueType(unittest.TestCase):
    def test_AssignValueTypeAssignsOnAValidValue_AnEmptyList(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, Integer())
                self.mAcceptDecorator = TemplateAcceptDecorator(self.mAcceptDecorator, {})
        instanceType = MyRecordOf()
        valueType = []
        self.assertEqual(instanceType.assignValueType(valueType).valueType(), valueType)

    def test_AssignValueTypeAssignsOnAValidValue_ASingleElementList(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, Integer())
                self.mAcceptDecorator = TemplateAcceptDecorator(self.mAcceptDecorator, {})
        instanceType = MyRecordOf()
        valueType = [Integer().assignValueType(IntegerValue(1))]
        self.assertEqual(instanceType.assignValueType(valueType).valueType(), valueType)

    def test_AssignValueTypeAssignsOnAValidValue_AManyElementsList(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, Integer())
                self.mAcceptDecorator = TemplateAcceptDecorator(self.mAcceptDecorator, {})
        instanceType = MyRecordOf()
        valueType = [Integer().assignValueType(IntegerValue(1)), Integer().assignValueType(IntegerValue(2))]
        self.assertEqual(instanceType.assignValueType(valueType).valueType(), valueType)

    def test_AssignValueTypeAssignsOnAValidValue_AnyOfValuesIsATemplateLikeType_WithoutSpecialValueType(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, Integer())
                self.mAcceptDecorator = TemplateAcceptDecorator(self.mAcceptDecorator, {})
        instanceType = MyRecordOf()
        valueType = [Integer().assignValueType(IntegerValue(1)),
                     TemplateInteger().assignValueType(IntegerValue(2))]
        self.assertEqual(instanceType.assignValueType(valueType).valueType(), valueType)

    def test_AssignValueTypeAssignsOnAValidValue_AnyOfValuesIsATemplateLikeType_WithSpecialValueType(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, Integer())
                self.mAcceptDecorator = TemplateAcceptDecorator(self.mAcceptDecorator, {})
        instanceType = MyRecordOf()
        valueType = [Integer().assignValueType(IntegerValue(1)),
                     TemplateInteger().assignValueType(AnyValue())]
        self.assertEqual(instanceType.assignValueType(valueType).valueType(), valueType)

    def test_AssignValueTypeRaisesAnExceptionOnAnInvalidValue_InvalidType_BuiltIn(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, Integer())
                self.mAcceptDecorator = TemplateAcceptDecorator(self.mAcceptDecorator, {})
        instanceType = MyRecordOf()
        for valueType in [True, 1, 1.0, "WAX", [1, 2], (1, 2)]:
            with self.assertRaises(InvalidTypeInValueTypeAssignment):
                instanceType.assignValueType(valueType)

    def test_AssignValueTypeRaisesAnExceptionOnAnInvalidValue_InvalidType_Special(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, Integer())
                self.mAcceptDecorator = TemplateAcceptDecorator(self.mAcceptDecorator, {})
        instanceType = MyRecordOf()
        for valueType in [[AnyValue()]]:
            with self.assertRaises(InvalidTypeInValueTypeAssignment):
                instanceType.assignValueType(valueType)

    def test_IsCompatibleReturnsFalseOnAnIncompatibleType_Regular(self):
        self.skipTest("Not implemented yet.")

class TypeSystem_RecordOf_Template_Eq(unittest.TestCase):
    def test_EqReturnsTrueOnSameValues_Self(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, Integer())
                self.mAcceptDecorator = TemplateAcceptDecorator(self.mAcceptDecorator, {})
        instanceType = MyRecordOf()
        instanceType.assignValueType(AnyValue())
        self.assertTrue(instanceType == instanceType)

    def test_EqReturnsTrueOnSameValues_TemplateWithNonTemplate_Empty(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, Integer())
                self.mAcceptDecorator = TemplateAcceptDecorator(self.mAcceptDecorator, {})
        instanceType1 = MyRecordOf()
        instanceType1.assignValueType(AnyValue())
        instanceType2 = MyRecordOf()
        instanceType2.assignValueType([])
        self.assertTrue(instanceType1 == instanceType2)

    def test_EqReturnsTrueOnSameValues_TemplateWithNonTemplate_OneElement(self):
        class MyRecordOf1(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, Integer())
                self.mAcceptDecorator = TemplateAcceptDecorator(self.mAcceptDecorator, {})
        class MyRecordOf2(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, Integer())
        instanceType1 = MyRecordOf1()
        instanceType1.assignValueType(AnyValue())
        instanceType2 = MyRecordOf2()
        instanceType2.assignValueType([
            Integer().assignValueType(IntegerValue(1))
        ])
        self.assertTrue(instanceType1 == instanceType2)

    def test_EqReturnsTrueOnSameValues_TemplateWithNonTemplate_ManyElements(self):
        class MyRecordOf1(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, Integer())
                self.mAcceptDecorator = TemplateAcceptDecorator(self.mAcceptDecorator, {})
        class MyRecordOf2(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, Integer())
        instanceType1 = MyRecordOf1()
        instanceType1.assignValueType(AnyValue())
        instanceType2 = MyRecordOf2()
        instanceType2.assignValueType([
            Integer().assignValueType(IntegerValue(1)),
            Integer().assignValueType(IntegerValue(2)),
            Integer().assignValueType(IntegerValue(3))
        ])
        self.assertTrue(instanceType1 == instanceType2)

    def test_EqReturnsTrueOnSameValues_TemplateWithTemplate_Empty(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, Integer())
                self.mAcceptDecorator = TemplateAcceptDecorator(self.mAcceptDecorator, {})
        instanceType1 = MyRecordOf()
        instanceType1.assignValueType(AnyValue())
        instanceType2 = MyRecordOf()
        instanceType2.assignValueType([])
        self.assertTrue(instanceType1 == instanceType2)

    def test_EqReturnsTrueOnSameValues_TemplateWithTemplate_OneElement_WithoutSpecialValue(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, Integer())
                self.mAcceptDecorator = TemplateAcceptDecorator(self.mAcceptDecorator, {})
        instanceType1 = MyRecordOf()
        instanceType1.assignValueType(AnyValue())
        instanceType2 = MyRecordOf()
        instanceType2.assignValueType([
            Integer().assignValueType(IntegerValue(1))
        ])
        self.assertTrue(instanceType1 == instanceType2)

    def test_EqReturnsTrueOnSameValues_TemplateWithTemplate_OneElement_WithSpecialValue(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, Integer())
                self.mAcceptDecorator = TemplateAcceptDecorator(self.mAcceptDecorator, {})
        instanceType1 = MyRecordOf()
        instanceType1.assignValueType(AnyValue())
        instanceType2 = MyRecordOf()
        instanceType2.assignValueType([
            TemplateInteger().assignValueType(AnyValue())
        ])
        self.assertTrue(instanceType1 == instanceType2)

    def test_EqReturnsTrueOnSameValues_TemplateWithTemplate_ManyElements_WithoutSpecialValue(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, Integer())
                self.mAcceptDecorator = TemplateAcceptDecorator(self.mAcceptDecorator, {})
        instanceType1 = MyRecordOf()
        instanceType1.assignValueType(AnyValue())
        instanceType2 = MyRecordOf()
        instanceType2.assignValueType([
            Integer().assignValueType(IntegerValue(1)),
            Integer().assignValueType(IntegerValue(2)),
            Integer().assignValueType(IntegerValue(3))
        ])
        self.assertTrue(instanceType1 == instanceType2)

    def test_EqReturnsTrueOnSameValues_TemplateWithTemplate_ManyElements_WithSpecialValue(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, Integer())
                self.mAcceptDecorator = TemplateAcceptDecorator(self.mAcceptDecorator, {})
        instanceType1 = MyRecordOf()
        instanceType1.assignValueType(AnyValue())
        instanceType2 = MyRecordOf()
        instanceType2.assignValueType([
            TemplateInteger().assignValueType(AnyValue()),
            TemplateInteger().assignValueType(IntegerValue(2)),
            TemplateInteger().assignValueType(AnyValue())
        ])
        self.assertTrue(instanceType1 == instanceType2)

if __name__ == '__main__':
    unittest.main()
