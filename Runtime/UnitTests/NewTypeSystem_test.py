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

class TypeSystem_Integer_Accept(unittest.TestCase):
    def test_AcceptReturnsTrueOnAValidValue(self):
        typeInstance = Integer()
        for valueType in [IntegerValue(-1), IntegerValue(0), IntegerValue(1)]:
            self.assertTrue(typeInstance.accept(valueType))

    def test_AcceptReturnsFalseOnAnInvalidValue_BuiltIn(self):
        typeInstance = Integer()
        for valueType in [True, 1.0, "WAX"]:
            self.assertFalse(typeInstance.accept(valueType))

    def test_AcceptReturnsFalseOnAnInvalidValue_Special(self):
        typeInstance = Integer()
        for valueType in [AnyValue()]:
            self.assertFalse(typeInstance.accept(valueType))

class TypeSystem_Integer_AssignValueType(unittest.TestCase):
    def test_AssignValueTypeAssignsOnAValidValue(self):
        typeInstance = Integer()
        for valueType in [IntegerValue(-1), IntegerValue(0), IntegerValue(1)]:
            self.assertEqual(typeInstance.assignValueType(valueType).valueType(), valueType)

    def test_AssignValueTypeRaisesAnExceptionOnAnInvalidValue_BuiltIn(self):
        typeInstance = Integer()
        for valueType in [True, 1.0, "WAX"]:
            with self.assertRaises(InvalidTypeInValueTypeAssignment):
                typeInstance.assignValueType(valueType)

    def test_AssignValueTypeRaisesAnExceptionOnAnInvalidValue_Special(self):
        typeInstance = Integer()
        for valueType in [AnyValue()]:
            with self.assertRaises(InvalidTypeInValueTypeAssignment):
                typeInstance.assignValueType(valueType)

class TypeSystem_Integer_Eq(unittest.TestCase):
    def test_EqReturnsTrueOnSameValues_SameTypes(self):
        self.assertTrue(Integer().assignValueType(IntegerValue(1)) == Integer().assignValueType(IntegerValue(1)))

    def test_EqReturnsTrueOnSameValues_CompatibleTypes(self):
        typeInstance = Integer().assignValueType(IntegerValue(1))
        for value in [
            Integer().addAcceptDecorator(RangedAcceptDecorator, {'lowerBoundary': IntegerValue(0),
                                                                 'upperBoundary': IntegerValue(10)}).assignValueType(IntegerValue(1)),
            Integer().addAcceptDecorator(TemplateAcceptDecorator, {}).assignValueType(IntegerValue(1))
        ]:
            self.assertTrue(typeInstance == value)

    def test_EqReturnsFalseOnDifferentValues_SameTypes(self):
        self.assertFalse(Integer().assignValueType(IntegerValue(1)) == Integer().assignValueType(IntegerValue(2)))

    def test_EqReturnsFalseOnDifferentValues_CompatibleTypes(self):
        typeInstance = Integer().assignValueType(IntegerValue(1))
        for value in [
            Integer().addAcceptDecorator(RangedAcceptDecorator, {'lowerBoundary': IntegerValue(0),
                                                                 'upperBoundary': IntegerValue(10)}).assignValueType(IntegerValue(2)),
            Integer().addAcceptDecorator(TemplateAcceptDecorator, {}).assignValueType(IntegerValue(2))
        ]:
            self.assertFalse(typeInstance == value)

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

class TypeSystem_Integer_Ranged_Accept(unittest.TestCase):
    def test_AcceptReturnsTrueOnAValidValue(self):
        typeInstance = Integer().addAcceptDecorator(RangedAcceptDecorator, {'lowerBoundary': IntegerValue(0),
                                                                            'upperBoundary': IntegerValue(10)}).assignValueType(IntegerValue(1))
        for valueType in [IntegerValue(0), IntegerValue(1), IntegerValue(10)]:
            self.assertTrue(typeInstance.accept(valueType))

    def test_AcceptReturnsFalseOnAnInvalidValue(self):
        typeInstance = Integer().addAcceptDecorator(RangedAcceptDecorator, {'lowerBoundary': IntegerValue(0),
                                                                            'upperBoundary': IntegerValue(10)}).assignValueType(IntegerValue(1))
        for valueType in [IntegerValue(-1), IntegerValue(11)]:
            self.assertFalse(typeInstance.accept(valueType))

    def test_AcceptReturnsFalseOnAnInvalidValue_BuiltIn(self):
        typeInstance = Integer().addAcceptDecorator(RangedAcceptDecorator, {'lowerBoundary': IntegerValue(0),
                                                                            'upperBoundary': IntegerValue(10)}).assignValueType(IntegerValue(1))
        for valueType in [True, 1.0, "WAX"]:
            self.assertFalse(typeInstance.accept(valueType))

    def test_AcceptReturnsFalseOnAnInvalidValue_Special(self):
        typeInstance = Integer().addAcceptDecorator(RangedAcceptDecorator, {'lowerBoundary': IntegerValue(0),
                                                                            'upperBoundary': IntegerValue(10)}).assignValueType(IntegerValue(1))
        for valueType in [AnyValue()]:
            self.assertFalse(typeInstance.accept(valueType))

class TypeSystem_Integer_Ranged_Subtyped_Accept(unittest.TestCase):
    def test_AcceptReturnsTrueOnAValidValue(self):
        class MyInteger(Integer):
            def __init__(self):
                Integer.__init__(self)
                self.mAcceptDecorator = RangedAcceptDecorator(self.mAcceptDecorator, {'lowerBoundary': IntegerValue(0),
                                                                                      'upperBoundary': IntegerValue(10)})
        typeInstance = MyInteger().assignValueType(IntegerValue(1))
        for valueType in [IntegerValue(0), IntegerValue(1), IntegerValue(10)]:
            self.assertTrue(typeInstance.accept(valueType))

    def test_AcceptReturnsFalseOnAnInvalidValue(self):
        class MyInteger(Integer):
            def __init__(self):
                Integer.__init__(self)
                self.mAcceptDecorator = RangedAcceptDecorator(self.mAcceptDecorator, {'lowerBoundary': IntegerValue(0),
                                                                                      'upperBoundary': IntegerValue(10)})
        typeInstance = MyInteger().assignValueType(IntegerValue(1))
        for valueType in [IntegerValue(-1), IntegerValue(11)]:
            self.assertFalse(typeInstance.accept(valueType))

    def test_AcceptReturnsFalseOnAnInvalidValue_BuiltIn(self):
        class MyInteger(Integer):
            def __init__(self):
                Integer.__init__(self)
                self.mAcceptDecorator = RangedAcceptDecorator(self.mAcceptDecorator, {'lowerBoundary': IntegerValue(0),
                                                                                      'upperBoundary': IntegerValue(10)})
        typeInstance = MyInteger().assignValueType(IntegerValue(1))
        for valueType in [True, 1.0, "WAX"]:
            self.assertFalse(typeInstance.accept(valueType))

    def test_AcceptReturnsFalseOnAnInvalidValue_Special(self):
        class MyInteger(Integer):
            def __init__(self):
                Integer.__init__(self)
                self.mAcceptDecorator = RangedAcceptDecorator(self.mAcceptDecorator, {'lowerBoundary': IntegerValue(0),
                                                                                      'upperBoundary': IntegerValue(10)})
        typeInstance = MyInteger().assignValueType(IntegerValue(1))
        for valueType in [AnyValue()]:
            self.assertFalse(typeInstance.accept(valueType))

class TypeSystem_Integer_Ranged_AssignValueType(unittest.TestCase):
    def test_AssignValueTypeAssignsOnAValidValue(self):
        typeInstance = Integer().addAcceptDecorator(RangedAcceptDecorator, {'lowerBoundary': IntegerValue(0),
                                                                            'upperBoundary': IntegerValue(10)}).assignValueType(IntegerValue(1))
        for valueType in [IntegerValue(0), IntegerValue(1), IntegerValue(10)]:
            self.assertEqual(typeInstance.assignValueType(valueType).valueType(), valueType)

    def test_AssignValueRaisesAnExceptionOnAnInvalidValue_Boundary(self):
        typeInstance = Integer().addAcceptDecorator(RangedAcceptDecorator, {'lowerBoundary': IntegerValue(0),
                                                                            'upperBoundary': IntegerValue(10)}).assignValueType(IntegerValue(1))
        for valueType in [IntegerValue(-1), IntegerValue(11)]:
            with self.assertRaises(InvalidTypeInValueTypeAssignment):
                typeInstance.assignValueType(valueType)

    def test_AssignValueTypeRaisesAnExceptionOnAnInvalidValue_BuiltIn(self):
        typeInstance = Integer().addAcceptDecorator(RangedAcceptDecorator, {'lowerBoundary': IntegerValue(0),
                                                                            'upperBoundary': IntegerValue(10)}).assignValueType(IntegerValue(1))
        for valueType in [True, 1.0, "WAX"]:
            with self.assertRaises(InvalidTypeInValueTypeAssignment):
                typeInstance.assignValueType(valueType)

    def test_AssignValueTypeRaisesAnExceptionOnAnInvalidValue_Special(self):
        typeInstance = Integer().addAcceptDecorator(RangedAcceptDecorator, {'lowerBoundary': IntegerValue(0),
                                                                            'upperBoundary': IntegerValue(10)}).assignValueType(IntegerValue(1))
        for valueType in [AnyValue()]:
            with self.assertRaises(InvalidTypeInValueTypeAssignment):
                typeInstance.assignValueType(valueType)

class TypeSystem_Integer_Ranged_Subtyped_AssignValueType(unittest.TestCase):
    def test_AssignValueTypeAssignsOnAValidValue(self):
        class MyInteger(Integer):
            def __init__(self):
                Integer.__init__(self)
                self.mAcceptDecorator = RangedAcceptDecorator(self.mAcceptDecorator, {'lowerBoundary': IntegerValue(0),
                                                                                      'upperBoundary': IntegerValue(10)})
        typeInstance = MyInteger().assignValueType(IntegerValue(1))
        for valueType in [IntegerValue(0), IntegerValue(1), IntegerValue(10)]:
            self.assertEqual(typeInstance.assignValueType(valueType).valueType(), valueType)

    def test_AssignValueRaisesAnExceptionOnAnInvalidValue_Boundary(self):
        class MyInteger(Integer):
            def __init__(self):
                Integer.__init__(self)
                self.mAcceptDecorator = RangedAcceptDecorator(self.mAcceptDecorator, {'lowerBoundary': IntegerValue(0),
                                                                                      'upperBoundary': IntegerValue(10)})
        typeInstance = MyInteger().assignValueType(IntegerValue(1))
        for valueType in [IntegerValue(-1), IntegerValue(11)]:
            with self.assertRaises(InvalidTypeInValueTypeAssignment):
                typeInstance.assignValueType(valueType)

    def test_AssignValueTypeRaisesAnExceptionOnAnInvalidValue_BuiltIn(self):
        class MyInteger(Integer):
            def __init__(self):
                Integer.__init__(self)
                self.mAcceptDecorator = RangedAcceptDecorator(self.mAcceptDecorator, {'lowerBoundary': IntegerValue(0),
                                                                                      'upperBoundary': IntegerValue(10)})
        typeInstance = MyInteger().assignValueType(IntegerValue(1))
        for valueType in [True, 1.0, "WAX"]:
            with self.assertRaises(InvalidTypeInValueTypeAssignment):
                typeInstance.assignValueType(valueType)

    def test_AssignValueTypeRaisesAnExceptionOnAnInvalidValue_Special(self):
        class MyInteger(Integer):
            def __init__(self):
                Integer.__init__(self)
                self.mAcceptDecorator = RangedAcceptDecorator(self.mAcceptDecorator, {'lowerBoundary': IntegerValue(0),
                                                                                      'upperBoundary': IntegerValue(10)})
        typeInstance = MyInteger().assignValueType(IntegerValue(1))
        for valueType in [AnyValue()]:
            with self.assertRaises(InvalidTypeInValueTypeAssignment):
                typeInstance.assignValueType(valueType)

class TypeSystem_Integer_Ranged_Eq(unittest.TestCase):
    def test_EqReturnsTrueOnSameValues_SameTypes(self):
        typeInstance1 = Integer().addAcceptDecorator(RangedAcceptDecorator, {'lowerBoundary': IntegerValue(0),
                                                                             'upperBoundary': IntegerValue(10)}).assignValueType(IntegerValue(1))
        typeInstance2 = Integer().addAcceptDecorator(RangedAcceptDecorator, {'lowerBoundary': IntegerValue(0),
                                                                             'upperBoundary': IntegerValue(10)}).assignValueType(IntegerValue(1))
        self.assertTrue(typeInstance1 == typeInstance2)

    def test_EqReturnsTrueOnSameValues_CompatibleTypes(self):
        typeInstance = Integer().addAcceptDecorator(RangedAcceptDecorator, {'lowerBoundary': IntegerValue(0),
                                                                            'upperBoundary': IntegerValue(10)}).assignValueType(IntegerValue(1))
        for value in [
            Integer().assignValueType(IntegerValue(1)),
            Integer().addAcceptDecorator(TemplateAcceptDecorator, {}).assignValueType(IntegerValue(1))
        ]:
            self.assertTrue(typeInstance == value)

    def test_EqReturnsFalseOnDifferentValues_SameTypes(self):
        typeInstance1 = Integer().addAcceptDecorator(RangedAcceptDecorator, {'lowerBoundary': IntegerValue(0),
                                                                             'upperBoundary': IntegerValue(10)}).assignValueType(IntegerValue(1))
        typeInstance2 = Integer().addAcceptDecorator(RangedAcceptDecorator, {'lowerBoundary': IntegerValue(0),
                                                                             'upperBoundary': IntegerValue(10)}).assignValueType(IntegerValue(2))
        self.assertFalse(typeInstance1 == typeInstance2)

    def test_EqReturnsFalseOnDifferentValues_CompatibleTypes(self):
        typeInstance = Integer().addAcceptDecorator(RangedAcceptDecorator, {'lowerBoundary': IntegerValue(0),
                                                                            'upperBoundary': IntegerValue(10)}).assignValueType(IntegerValue(1))
        for value in [
            Integer().assignValueType(IntegerValue(2)),
            Integer().addAcceptDecorator(TemplateAcceptDecorator, {}).assignValueType(IntegerValue(2))
        ]:
            self.assertFalse(typeInstance == value)

    def test_EqRaisesAnExceptionOnAnInvalidType_BuiltIn(self):
        typeInstance = Integer().addAcceptDecorator(RangedAcceptDecorator, {'lowerBoundary': IntegerValue(0),
                                                                            'upperBoundary': IntegerValue(10)}).assignValueType(IntegerValue(1))
        for valueType in [True, 1.0, "WAX"]:
            with self.assertRaises(InvalidTypeInComparison):
                typeInstance == valueType

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

    def test_EqReturnsTrueOnSameValues_CompatibleTypes(self):
        class MyInteger(Integer):
            def __init__(self):
                Integer.__init__(self)
                self.mAcceptDecorator = RangedAcceptDecorator(self.mAcceptDecorator, {'lowerBoundary': IntegerValue(0),
                                                                                      'upperBoundary': IntegerValue(10)})
        typeInstance = MyInteger().assignValueType(IntegerValue(1))
        for value in [
            Integer().assignValueType(IntegerValue(1)),
            Integer().addAcceptDecorator(TemplateAcceptDecorator, {}).assignValueType(IntegerValue(1))
        ]:
            self.assertTrue(typeInstance == value)

    def test_EqReturnsFalseOnDifferentValues_SameTypes(self):
        class MyInteger(Integer):
            def __init__(self):
                Integer.__init__(self)
                self.mAcceptDecorator = RangedAcceptDecorator(self.mAcceptDecorator, {'lowerBoundary': IntegerValue(0),
                                                                                      'upperBoundary': IntegerValue(10)})
        typeInstance1 = MyInteger().assignValueType(IntegerValue(1))
        typeInstance2 = MyInteger().assignValueType(IntegerValue(2))
        self.assertFalse(typeInstance1 == typeInstance2)

    def test_EqReturnsFalseOnDifferentValues_CompatibleTypes(self):
        class MyInteger(Integer):
            def __init__(self):
                Integer.__init__(self)
                self.mAcceptDecorator = RangedAcceptDecorator(self.mAcceptDecorator, {'lowerBoundary': IntegerValue(0),
                                                                                      'upperBoundary': IntegerValue(10)})
        typeInstance = MyInteger().assignValueType(IntegerValue(1))
        for value in [
            Integer().assignValueType(IntegerValue(2)),
            Integer().addAcceptDecorator(TemplateAcceptDecorator, {}).assignValueType(IntegerValue(2))
        ]:
            self.assertFalse(typeInstance == value)

    def test_EqRaisesAnExceptionOnAnInvalidType_BuiltIn(self):
        class MyInteger(Integer):
            def __init__(self):
                Integer.__init__(self)
                self.mAcceptDecorator = RangedAcceptDecorator(self.mAcceptDecorator, {'lowerBoundary': IntegerValue(0),
                                                                                      'upperBoundary': IntegerValue(10)})
        typeInstance = MyInteger().assignValueType(IntegerValue(1))
        for valueType in [True, 1.0, "WAX"]:
            with self.assertRaises(InvalidTypeInComparison):
                typeInstance == valueType

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

if __name__ == '__main__':
    unittest.main()
