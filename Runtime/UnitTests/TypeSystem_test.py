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
# TODO: Tests for RecordOf of RecordOf.
# TODO: More tests for RecordOf of Record.
# TODO: More tests for Record of RecordOf.
# TODO: Add exemplary module showing examples of anything that needs calling: class Foo(Bar):...
#       Example: calling class MyInteger(Integer):... to get a type alias.
# TODO: More tests for template types without special values
#       (TemplateType(Integer(SimpleType())).assign(IntegerValue(1))
# TODO: DifferentType tests for basic types.
#

import unittest

from Runtime.TypeSystem import *

class TypeSystem_TypeDecorator_IsOfType(unittest.TestCase):
    def test_IsOfTypeReturnsTrueForAValidType(self):
        instance = Boolean(SimpleType())
        self.assertFalse(instance.isOfType(TemplateType))
        self.assertTrue(instance.isOfType(Boolean))
        self.assertTrue(instance.isOfType(SimpleType))
        self.assertFalse(instance.isOfType(Integer))
        instance = TemplateType(Boolean(SimpleType()))
        self.assertTrue(instance.isOfType(TemplateType))
        self.assertTrue(instance.isOfType(Boolean))
        self.assertTrue(instance.isOfType(SimpleType))
        self.assertFalse(instance.isOfType(Integer))
        class MyRecord1(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': Charstring(SimpleType())})
        instance = MyRecord1()
        self.assertTrue(instance.isOfType(MyRecord1))
        self.assertTrue(instance.isOfType(Record))
        self.assertTrue(instance.isOfType(SimpleType))
        class MyRecord2(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': Charstring(SimpleType())})
        class MyWrappedRecord(MyRecord2):
            def __init__(self):
                MyRecord2.__init__(self)
        instance = MyWrappedRecord()
        self.assertTrue(instance.isOfType(MyWrappedRecord))
        self.assertTrue(instance.isOfType(MyRecord2))
        self.assertTrue(instance.isOfType(Record))
        self.assertTrue(instance.isOfType(SimpleType))

class TypeSystem_Boolean_Ctor(unittest.TestCase):
    def test_Ctor(self):
        Boolean(SimpleType())

    def test_CtorRaisesAnExceptionOnAnInvalidType_BuiltIn(self):
        for instance in [True, 1, 1.0, "WAX", {}, [], ()]:
            with self.assertRaises(InvalidTypeInCtor):
                Boolean(instance)

    def test_CtorRaisesAnExceptionOnAnInvalidType_Regular(self):
        for instance in [Boolean(SimpleType()), Integer(SimpleType()), Float(SimpleType()), Charstring(SimpleType())]:
            with self.assertRaises(InvalidTypeInCtor):
                Boolean(instance)

    def test_CtorRaisesAnExceptionOnAnInvalidType_Special(self):
        for instance in [AnyValue()]:
            with self.assertRaises(InvalidTypeInCtor):
                Boolean(instance)

    def test_CtorRaisesAnExceptionOnAnInvalidType_Template(self):
        for instance in [TemplateType(Boolean(SimpleType()))]:
            with self.assertRaises(InvalidTypeInCtor):
                Boolean(instance)

class TypeSystem_Boolean_Accept(unittest.TestCase):
    def test_AcceptReturnsTrueOnAValidValue(self):
        instance = Boolean(SimpleType())
        for value in [BooleanValue(True), BooleanValue(False)]:
            self.assertTrue(instance.accept(value))

    def test_AcceptReturnsFalseOnAnInvalidValue_BuiltIn(self):
        instance = Boolean(SimpleType())
        for value in [True, 1.0, "WAX"]:
            self.assertFalse(instance.accept(value))

    def test_AcceptReturnsFalseOnAnInvalidValue_Special(self):
        instance = Boolean(SimpleType())
        for value in [AnyValue()]:
            self.assertFalse(instance.accept(value))

class TypeSystem_Boolean_Assign(unittest.TestCase):
    def test_AssignAssignsOnAValidValue(self):
        instance = Boolean(SimpleType())
        for value in [BooleanValue(True), BooleanValue(False)]:
            self.assertEqual(instance.assign(value).value(), value)

    def test_AssignRaisesAnExceptionOnAnInvalidValue_BuiltIn(self):
        instance = Boolean(SimpleType())
        for value in [True, 1.0, "WAX"]:
            with self.assertRaises(InvalidTypeInAssignment):
                instance.assign(value)

    def test_AssignRaisesAnExceptionOnAnInvalidValue_Special(self):
        instance = Boolean(SimpleType())
        for value in [AnyValue()]:
            with self.assertRaises(InvalidTypeInAssignment):
                instance.assign(value)

class TypeSystem_Boolean_Eq(unittest.TestCase):
    def test_EqReturnsTrueOnSameValues_SameTypes(self):
        self.assertTrue(   Boolean(SimpleType()).assign(BooleanValue(True))
                        == Boolean(SimpleType()).assign(BooleanValue(True)))

    def test_EqReturnsTrueOnSameValues_CompatibleTypes(self):
        type = Boolean(SimpleType()).assign(BooleanValue(True))
        for value in [
            TemplateType(Boolean(SimpleType())).assign(BooleanValue(True))
        ]:
            self.assertTrue(type == value)

    def test_EqReturnsFalseOnDifferentValues(self):
        self.assertFalse(   Boolean(SimpleType()).assign(BooleanValue(True))
                         == Boolean(SimpleType()).assign(BooleanValue(False)))

    def test_EqRaisesAnExceptionOnAnInvalidType_BuiltIn(self):
        type = Boolean(SimpleType()).assign(BooleanValue(True))
        for value in [True, 1.0, "WAX"]:
            with self.assertRaises(InvalidTypeInComparison):
                type == value

    def test_EqRaisesAnExceptionOnAnInvalidType_Regular(self):
        type = Boolean(SimpleType()).assign(BooleanValue(True))
        for value in [
            Integer(SimpleType()).assign(IntegerValue(1)),
            Float(SimpleType()).assign(FloatValue(1.0)),
            Charstring(SimpleType()).assign(CharstringValue("WAX"))
        ]:
            with self.assertRaises(InvalidTypeInComparison):
                type == value

    def test_EqRaisesAnExceptionOnAnInvalidType_Special(self):
        type = Boolean(SimpleType()).assign(BooleanValue(True))
        for value in [AnyValue()]:
            with self.assertRaises(InvalidTypeInComparison):
                type == value

    def test_EqRaisesAnExceptionOnAnInvalidType_Template(self):
        type = Boolean(SimpleType()).assign(BooleanValue(True))
        for value in [
            TemplateType(Integer(SimpleType())).assign(IntegerValue(1)),
            TemplateType(Float(SimpleType())).assign(FloatValue(1.0)),
            TemplateType(Charstring(SimpleType())).assign(CharstringValue("WAX"))
        ]:
            with self.assertRaises(InvalidTypeInComparison):
                type == value

class TypeSystem_Boolean_IsCompatible(unittest.TestCase):
    def test_IsCompatibleReturnsTrueOnACompatibleType_Self(self):
        instance = Boolean(SimpleType()).assign(BooleanValue(True))
        self.assertTrue(instance.isCompatible(instance))

    def test_IsCompatibleReturnsTrueOnACompatibleType_Subtyped(self):
        instance1 = Boolean(SimpleType()).assign(BooleanValue(True))
        class MyBoolean(Boolean):
            def __init__(self):
                Boolean.__init__(self, SimpleType())
        instance2 = MyBoolean().assign(BooleanValue(True))
        self.assertTrue(instance1.isCompatible(instance2))
        self.assertTrue(instance2.isCompatible(instance1))

    def test_IsCompatibleReturnsTrueOnACompatibleType_DoubleSubtyped(self):
        instance1 = Boolean(SimpleType()).assign(BooleanValue(True))
        class MyBoolean(Boolean):
            def __init__(self):
                Boolean.__init__(self, SimpleType())
        class MyBoolean2(MyBoolean):
            def __init__(self):
                MyBoolean.__init__(self)
        instance2 = MyBoolean2().assign(BooleanValue(True))
        self.assertTrue(instance1.isCompatible(instance2))
        self.assertTrue(instance2.isCompatible(instance1))

    def test_IsCompatibleReturnsTrueOnACompatibleType_Template(self):
        instance1 = Boolean(SimpleType()).assign(BooleanValue(True))
        instance2 = TemplateType(Boolean(SimpleType())).assign(BooleanValue(True))
        self.assertTrue(instance1.isCompatible(instance2))
        self.assertTrue(instance2.isCompatible(instance1))

    def test_IsCompatibleReturnsFalseOnAnIncompatibleType_BuiltIn(self):
        instance1 = Boolean(SimpleType()).assign(BooleanValue(True))
        for instance2 in [True, 1.0, "WAX"]:
            self.assertFalse(instance1.isCompatible(instance2))

    def test_IsCompatibleReturnsFalseOnAnIncompatibleType_Regular(self):
        instance1 = Boolean(SimpleType()).assign(BooleanValue(True))
        for instance2 in [
            Integer(SimpleType()).assign(IntegerValue(1)),
            Float(SimpleType()).assign(FloatValue(1.0)),
            Charstring(SimpleType()).assign(CharstringValue("WAX"))
        ]:
            self.assertFalse(instance1.isCompatible(instance2))
            self.assertFalse(instance2.isCompatible(instance1))

    def test_IsCompatibleReturnsFalseOnAnIncompatibleType_Special(self):
        instance1 = Boolean(SimpleType()).assign(BooleanValue(True))
        for instance2 in [AnyValue()]:
            self.assertFalse(instance1.isCompatible(instance2))

    def test_IsCompatibleReturnsFalseOnAnIncompatibleType_TemplateWithSpecial(self):
        instance1 = Boolean(SimpleType()).assign(BooleanValue(True))
        instance2 = TemplateType(Boolean(SimpleType())).assign(AnyValue())
        self.assertFalse(instance1.isCompatible(instance2))
        self.assertTrue(instance2.isCompatible(instance1))

class TypeSystem_Boolean_TemplateType_Ctor(unittest.TestCase):
    def test_Ctor(self):
        TemplateType(Boolean(SimpleType()))

class TypeSystem_Boolean_TemplateType_Accept(unittest.TestCase):
    def test_AcceptReturnsTrueOnAValidValue(self):
        type = TemplateType(Boolean(SimpleType()))
        for value in [BooleanValue(True), BooleanValue(False), AnyValue()]:
            self.assertTrue(type.accept(value))

    def test_AcceptReturnsFalseOnAnInvalidValue_InvalidType(self):
        type = TemplateType(Boolean(SimpleType()))
        for value in [True, 1.0, "WAX"]:
            self.assertFalse(type.accept(value))

class TypeSystem_Boolean_TemplateType_Assign(unittest.TestCase):
    def test_AssignAssignsOnAValidValue(self):
        type = TemplateType(Boolean(SimpleType()))
        for value in [BooleanValue(True), BooleanValue(False), AnyValue()]:
            self.assertEqual(type.assign(value).value(), value)

    def test_AssignRaisesAnExceptionOnAnInvalidValue(self):
        type = TemplateType(Boolean(SimpleType()))
        for value in [True, 1.0, "WAX"]:
            with self.assertRaises(InvalidTypeInAssignment):
                type.assign(value)

class TypeSystem_Boolean_TemplateType_Eq(unittest.TestCase):
    def test_EqReturnsTrueOnSameValues(self):
        for values in [(BooleanValue(True), BooleanValue(True)),
                       (BooleanValue(True), AnyValue()),
                       (AnyValue(), BooleanValue(True)),
                       (AnyValue(), AnyValue())]:
            self.assertTrue(   TemplateType(Boolean(SimpleType())).assign(values[0])
                            == TemplateType(Boolean(SimpleType())).assign(values[1]))

    def test_EqReturnsFalseOnDifferentValues(self):
        self.assertFalse(   TemplateType(Boolean(SimpleType())).assign(BooleanValue(True))
                         == TemplateType(Boolean(SimpleType())).assign(BooleanValue(False)))

    def test_EqRaisesAnExceptionOnAnInvalidType_BuiltIn(self):
        type = TemplateType(Boolean(SimpleType())).assign(BooleanValue(True))
        for value in [True, 1.0, "WAX"]:
            with self.assertRaises(InvalidTypeInComparison):
                type == value

    def test_EqRaisesAnExceptionOnAnInvalidType_Regular(self):
        type = TemplateType(Boolean(SimpleType())).assign(BooleanValue(True))
        for value in [
            Integer(SimpleType()).assign(IntegerValue(1)),
            Float(SimpleType()).assign(FloatValue(1.0)),
            Charstring(SimpleType()).assign(CharstringValue("WAX"))
        ]:
            with self.assertRaises(InvalidTypeInComparison):
                type == value

    def test_EqRaisesAnExceptionOnAnInvalidType_Special(self):
        type = TemplateType(Boolean(SimpleType())).assign(BooleanValue(True))
        for value in [AnyValue()]:
            with self.assertRaises(InvalidTypeInComparison):
                type == value

    def test_EqRaisesAnExceptionOnAnInvalidType_Template(self):
        type = TemplateType(Boolean(SimpleType())).assign(BooleanValue(True))
        for value in [
            TemplateType(Integer(SimpleType())).assign(IntegerValue(1)),
            TemplateType(Float(SimpleType())).assign(FloatValue(1.0)),
            TemplateType(Charstring(SimpleType())).assign(CharstringValue("WAX"))
        ]:
            with self.assertRaises(InvalidTypeInComparison):
                type == value

class TypeSystem_Integer_Ctor(unittest.TestCase):
    def test_Ctor(self):
        Integer(SimpleType())

    def test_CtorRaisesAnExceptionOnAnInvalidType_BuiltIn(self):
        for type in [True, 1, 1.0, "WAX", {}, [], ()]:
            with self.assertRaises(InvalidTypeInCtor):
                Integer(type)

    def test_CtorRaisesAnExceptionOnAnInvalidType_Regular(self):
        for type in [Boolean(SimpleType()), Integer(SimpleType()), Float(SimpleType()), Charstring(SimpleType())]:
            with self.assertRaises(InvalidTypeInCtor):
                Integer(type)

    def test_CtorRaisesAnExceptionOnAnInvalidType_Special(self):
        for type in [AnyValue()]:
            with self.assertRaises(InvalidTypeInCtor):
                Integer(type)

    def test_CtorRaisesAnExceptionOnAnInvalidType_Template(self):
        for type in [TemplateType(Integer(SimpleType()))]:
            with self.assertRaises(InvalidTypeInCtor):
                Integer(type)

class TypeSystem_Integer_Accept(unittest.TestCase):
    def test_AcceptReturnsTrueOnAValidValue(self):
        type = Integer(SimpleType())
        for value in [IntegerValue(-1), IntegerValue(0), IntegerValue(1)]:
            self.assertTrue(type.accept(value))

    def test_AcceptReturnsFalseOnAnInvalidValue_BuiltIn(self):
        type = Integer(SimpleType())
        for value in [True, 1.0, "WAX"]:
            self.assertFalse(type.accept(value))

    def test_AcceptReturnsFalseOnAnInvalidValue_Special(self):
        type = Integer(SimpleType())
        for value in [AnyValue()]:
            self.assertFalse(type.accept(value))

class TypeSystem_Integer_Assign(unittest.TestCase):
    def test_AssignAssignsOnAValidValue(self):
        type = Integer(SimpleType())
        for value in [IntegerValue(-1), IntegerValue(0), IntegerValue(1)]:
            self.assertEqual(type.assign(value).value(), value)

    def test_AssignRaisesAnExceptionOnAnInvalidValue_BuiltIn(self):
        type = Integer(SimpleType())
        for value in [True, 1.0, "WAX"]:
            with self.assertRaises(InvalidTypeInAssignment):
                type.assign(value)

    def test_AssignRaisesAnExceptionOnAnInvalidValue_Special(self):
        type = Integer(SimpleType())
        for value in [AnyValue()]:
            with self.assertRaises(InvalidTypeInAssignment):
                type.assign(value)

class TypeSystem_Integer_Eq(unittest.TestCase):
    def test_EqReturnsTrueOnSameValues_SameTypes(self):
        self.assertTrue(Integer(SimpleType()).assign(IntegerValue(1)) == Integer(SimpleType()).assign(IntegerValue(1)))

    def test_EqReturnsTrueOnSameValues_CompatibleTypes(self):
        type = Integer(SimpleType()).assign(IntegerValue(1))
        for value in [
            BoundedType(Integer(SimpleType()), IntegerValue(0), IntegerValue(10)).assign(IntegerValue(1)),
            TemplateType(Integer(SimpleType())).assign(IntegerValue(1))
        ]:
            self.assertTrue(type == value)

    def test_EqReturnsFalseOnDifferentValues(self):
        self.assertFalse(Integer(SimpleType()).assign(IntegerValue(1)) == Integer(SimpleType()).assign(IntegerValue(2)))

    def test_EqRaisesAnExceptionOnAnInvalidType_BuiltIn(self):
        type = Integer(SimpleType()).assign(IntegerValue(1))
        for value in [True, 1.0, "WAX"]:
            with self.assertRaises(InvalidTypeInComparison):
                type == value

    def test_EqRaisesAnExceptionOnAnInvalidType_Regular(self):
        type = Integer(SimpleType()).assign(IntegerValue(1))
        for value in [
            Boolean(SimpleType()).assign(BooleanValue(True)),
            Float(SimpleType()).assign(FloatValue(1.0)),
            Charstring(SimpleType()).assign(CharstringValue("WAX"))
        ]:
            with self.assertRaises(InvalidTypeInComparison):
                type == value

    def test_EqRaisesAnExceptionOnAnInvalidType_Special(self):
        type = Integer(SimpleType()).assign(IntegerValue(1))
        for value in [AnyValue()]:
            with self.assertRaises(InvalidTypeInComparison):
                type == value

    def test_EqRaisesAnExceptionOnAnInvalidType_Template(self):
        type = Integer(SimpleType()).assign(IntegerValue(1))
        for value in [
            TemplateType(Boolean(SimpleType())).assign(BooleanValue(True)),
            TemplateType(Float(SimpleType())).assign(FloatValue(1.0)),
            TemplateType(Charstring(SimpleType())).assign(CharstringValue("WAX"))
        ]:
            with self.assertRaises(InvalidTypeInComparison):
                type == value

class TypeSystem_Integer_IsCompatible(unittest.TestCase):
    def test_IsCompatibleReturnsTrueOnACompatibleType_Self(self):
        instance = Integer(SimpleType()).assign(IntegerValue(1))
        self.assertTrue(instance.isCompatible(instance))

    def test_IsCompatibleReturnsTrueOnACompatibleType_BoundedType(self):
        instance1 = Integer(SimpleType()).assign(IntegerValue(1))
        instance2 = BoundedType(Integer(SimpleType()), IntegerValue(0), IntegerValue(10)).assign(IntegerValue(1))
        self.assertTrue(instance1.isCompatible(instance2))
        self.assertTrue(instance2.isCompatible(instance1))

    def test_IsCompatibleReturnsTrueOnACompatibleType_Subtyped(self):
        instance1 = Integer(SimpleType()).assign(IntegerValue(1))
        class MyInteger(Integer):
            def __init__(self):
                Integer.__init__(self, SimpleType())
        instance2 = MyInteger().assign(IntegerValue(1))
        self.assertTrue(instance1.isCompatible(instance2))
        self.assertTrue(instance2.isCompatible(instance1))

    def test_IsCompatibleReturnsTrueOnACompatibleType_DoubleSubtyped(self):
        instance1 = Integer(SimpleType()).assign(IntegerValue(1))
        class MyInteger(Integer):
            def __init__(self):
                Integer.__init__(self, SimpleType())
        class MyInteger2(MyInteger):
            def __init__(self):
                MyInteger.__init__(self)
        instance2 = MyInteger2().assign(IntegerValue(1))
        self.assertTrue(instance1.isCompatible(instance2))
        self.assertTrue(instance2.isCompatible(instance1))

    def test_IsCompatibleReturnsTrueOnACompatibleType_Template(self):
        instance1 = Integer(SimpleType()).assign(IntegerValue(1))
        instance2 = TemplateType(Integer(SimpleType())).assign(IntegerValue(1))
        self.assertTrue(instance1.isCompatible(instance2))
        self.assertTrue(instance2.isCompatible(instance1))

    def test_IsCompatibleReturnsFalseOnAnIncompatibleType_BuiltIn(self):
        instance1 = Integer(SimpleType()).assign(IntegerValue(1))
        for instance2 in [True, 1.0, "WAX"]:
            self.assertFalse(instance1.isCompatible(instance2))

    def test_IsCompatibleReturnsFalseOnAnIncompatibleType_Regular(self):
        instance1 = Integer(SimpleType()).assign(IntegerValue(1))
        for instance2 in [
            Boolean(SimpleType()).assign(BooleanValue(True)),
            Float(SimpleType()).assign(FloatValue(1.0)),
            Charstring(SimpleType()).assign(CharstringValue("WAX"))
        ]:
            self.assertFalse(instance1.isCompatible(instance2))
            self.assertFalse(instance2.isCompatible(instance1))

    def test_IsCompatibleReturnsFalseOnAnIncompatibleType_Special(self):
        instance1 = Integer(SimpleType()).assign(IntegerValue(1))
        for instance2 in [AnyValue()]:
            self.assertFalse(instance1.isCompatible(instance2))

    def test_IsCompatibleReturnsFalseOnAnIncompatibleType_TemplateWithSpecial(self):
        instance1 = Integer(SimpleType()).assign(IntegerValue(1))
        instance2 = TemplateType(Integer(SimpleType())).assign(AnyValue())
        self.assertFalse(instance1.isCompatible(instance2))
        self.assertTrue(instance2.isCompatible(instance1))

class TypeSystem_Integer_BoundedType_Ctor(unittest.TestCase):
    def test_Ctor(self):
        BoundedType(Integer(SimpleType()), IntegerValue(0), IntegerValue(10))

class TypeSystem_Integer_BoundedType_Accept(unittest.TestCase):
    def test_AcceptReturnsTrueOnAValidValue(self):
        type = BoundedType(Integer(SimpleType()), IntegerValue(0), IntegerValue(10))
        for value in [IntegerValue(0), IntegerValue(1), IntegerValue(10)]:
            self.assertTrue(type.accept(value))

    def test_AcceptReturnsFalseOnAnInvalidValue_InvalidType_BuiltIn(self):
        type = BoundedType(Integer(SimpleType()), IntegerValue(0), IntegerValue(10))
        for value in [True, 1.0, "WAX"]:
            self.assertFalse(type.accept(value))

    def test_AcceptReturnsFalseOnAnInvalidValue_InvalidType_Special(self):
        type = BoundedType(Integer(SimpleType()), IntegerValue(0), IntegerValue(10))
        for value in [AnyValue()]:
            self.assertFalse(type.accept(value))

    def test_AcceptReturnsFalseOnAnInvalidValue_InvalidValue(self):
        type = BoundedType(Integer(SimpleType()), IntegerValue(0), IntegerValue(10))
        for value in [IntegerValue(-1), IntegerValue(11)]:
            self.assertFalse(type.accept(value))

class TypeSystem_Integer_BoundedType_Assign(unittest.TestCase):
    def test_AssignAssignsOnAValidValue(self):
        type = BoundedType(Integer(SimpleType()), IntegerValue(0), IntegerValue(10))
        for value in [IntegerValue(0), IntegerValue(1), IntegerValue(10)]:
            self.assertEqual(type.assign(value).value(), value)

    def test_AssignRaisesAnExceptionOnAnInvalidValue_InvalidType_BuiltIn(self):
        type = BoundedType(Integer(SimpleType()), IntegerValue(0), IntegerValue(10))
        for value in [True, 1.0, "WAX"]:
            with self.assertRaises(InvalidTypeInAssignment):
                type.assign(value)

    def test_AssignRaisesAnExceptionOnAnInvalidValue_InvalidType_Special(self):
        type = BoundedType(Integer(SimpleType()), IntegerValue(0), IntegerValue(10))
        for value in [AnyValue()]:
            with self.assertRaises(InvalidTypeInAssignment):
                type.assign(value)

    def test_AssignRaisesAnExceptionOnAnInvalidValue_InvalidValue(self):
        type = BoundedType(Integer(SimpleType()), IntegerValue(0), IntegerValue(10))
        for value in [IntegerValue(-1), IntegerValue(11)]:
            with self.assertRaises(InvalidTypeInAssignment):
                type.assign(value)

class TypeSystem_Integer_BoundedType_Eq(unittest.TestCase):
    def test_EqReturnsTrueOnSameValues(self):
        self.assertTrue(
               BoundedType(Integer(SimpleType()), IntegerValue(0), IntegerValue(10)).assign(IntegerValue(1))
            == BoundedType(Integer(SimpleType()), IntegerValue(0), IntegerValue(10)).assign(IntegerValue(1)))

    def test_EqReturnsFalseOnDifferentValues(self):
        self.assertFalse(
               BoundedType(Integer(SimpleType()), IntegerValue(0), IntegerValue(10)).assign(IntegerValue(1))
            == BoundedType(Integer(SimpleType()), IntegerValue(0), IntegerValue(10)).assign(IntegerValue(2)))

    def test_EqRaisesAnExceptionOnAnInvalidType_BuiltIn(self):
        type = BoundedType(Integer(SimpleType()), IntegerValue(0), IntegerValue(10)).assign(IntegerValue(1))
        for value in [True, 1.0, "WAX"]:
            with self.assertRaises(InvalidTypeInComparison):
                type == value

    def test_EqRaisesAnExceptionOnAnInvalidType_Regular(self):
        type = BoundedType(Integer(SimpleType()), IntegerValue(0), IntegerValue(10)).assign(IntegerValue(1))
        for value in [
            Boolean(SimpleType()).assign(BooleanValue(True)),
            Float(SimpleType()).assign(FloatValue(1.0)),
            Charstring(SimpleType()).assign(CharstringValue("WAX"))
        ]:
            with self.assertRaises(InvalidTypeInComparison):
                type == value

    def test_EqRaisesAnExceptionOnAnInvalidType_Special(self):
        type = BoundedType(Integer(SimpleType()), IntegerValue(0), IntegerValue(10)).assign(IntegerValue(1))
        for value in [AnyValue()]:
            with self.assertRaises(InvalidTypeInComparison):
                type == value

    def test_EqRaisesAnExceptionOnAnInvalidType_Template(self):
        type = BoundedType(Integer(SimpleType()), IntegerValue(0), IntegerValue(10)).assign(IntegerValue(1))
        for value in [
            TemplateType(Boolean(SimpleType())).assign(BooleanValue(True)),
            TemplateType(Float(SimpleType())).assign(FloatValue(1.0)),
            TemplateType(Charstring(SimpleType())).assign(CharstringValue("WAX"))
        ]:
            with self.assertRaises(InvalidTypeInComparison):
                type == value

class TypeSystem_Integer_TemplateType_Ctor(unittest.TestCase):
    def test_Ctor(self):
        TemplateType(Integer(SimpleType()))

class TypeSystem_Integer_TemplateType_Accept(unittest.TestCase):
    def test_AcceptReturnsTrueOnAValidValue(self):
        type = TemplateType(Integer(SimpleType()))
        for value in [IntegerValue(-1), IntegerValue(0), IntegerValue(10), AnyValue()]:
            self.assertTrue(type.accept(value))

    def test_AcceptReturnsFalseOnAnInvalidValue_InvalidType(self):
        type = TemplateType(Integer(SimpleType()))
        for value in [True, 1.0, "WAX"]:
            self.assertFalse(type.accept(value))

class TypeSystem_Integer_TemplateType_Assign(unittest.TestCase):
    def test_AssignAssignsOnAValidValue(self):
        type = TemplateType(Integer(SimpleType()))
        for value in [IntegerValue(-1), IntegerValue(0), IntegerValue(10), AnyValue()]:
            self.assertEqual(type.assign(value).value(), value)

    def test_AssignRaisesAnExceptionOnAnInvalidValue(self):
        type = TemplateType(Integer(SimpleType()))
        for value in [True, 1.0, "WAX"]:
            with self.assertRaises(InvalidTypeInAssignment):
                type.assign(value)

class TypeSystem_Integer_TemplateType_Eq(unittest.TestCase):
    def test_EqReturnsTrueOnSameValues(self):
        for values in [(IntegerValue(1), IntegerValue(1)),
                       (IntegerValue(1), AnyValue()),
                       (AnyValue(), IntegerValue(1)),
                       (AnyValue(), AnyValue())]:
            self.assertTrue(   TemplateType(Integer(SimpleType())).assign(values[0])
                            == TemplateType(Integer(SimpleType())).assign(values[1]))

    def test_EqReturnsFalseOnDifferentValues(self):
        self.assertFalse(   TemplateType(Integer(SimpleType())).assign(IntegerValue(1))
                         == TemplateType(Integer(SimpleType())).assign(IntegerValue(2)))

    def test_EqRaisesAnExceptionOnAnInvalidType_BuiltIn(self):
        type = TemplateType(Integer(SimpleType())).assign(IntegerValue(1))
        for value in [True, 1.0, "WAX"]:
            with self.assertRaises(InvalidTypeInComparison):
                type == value

    def test_EqRaisesAnExceptionOnAnInvalidType_Regular(self):
        type = TemplateType(Integer(SimpleType())).assign(IntegerValue(1))
        for value in [
            Boolean(SimpleType()).assign(BooleanValue(True)),
            Float(SimpleType()).assign(FloatValue(1.0)),
            Charstring(SimpleType()).assign(CharstringValue("WAX"))
        ]:
            with self.assertRaises(InvalidTypeInComparison):
                type == value

    def test_EqRaisesAnExceptionOnAnInvalidType_Special(self):
        type = TemplateType(Integer(SimpleType())).assign(IntegerValue(1))
        for value in [AnyValue()]:
            with self.assertRaises(InvalidTypeInComparison):
                type == value

    def test_EqRaisesAnExceptionOnAnInvalidType_Template(self):
        type = TemplateType(Integer(SimpleType())).assign(IntegerValue(1))
        for value in [
            TemplateType(Boolean(SimpleType())).assign(BooleanValue(True)),
            TemplateType(Float(SimpleType())).assign(FloatValue(1.0)),
            TemplateType(Charstring(SimpleType())).assign(CharstringValue("WAX"))
        ]:
            with self.assertRaises(InvalidTypeInComparison):
                type == value

class TypeSystem_Float_Ctor(unittest.TestCase):
    def test_Ctor(self):
        Float(SimpleType())

    def test_CtorRaisesAnExceptionOnAnInvalidType_BuiltIn(self):
        for type in [True, 1, 1.0, "WAX", {}, [], ()]:
            with self.assertRaises(InvalidTypeInCtor):
                Float(type)

    def test_CtorRaisesAnExceptionOnAnInvalidType_Regular(self):
        for type in [Boolean(SimpleType()), Integer(SimpleType()), Float(SimpleType()), Charstring(SimpleType())]:
            with self.assertRaises(InvalidTypeInCtor):
                Float(type)

    def test_CtorRaisesAnExceptionOnAnInvalidType_Special(self):
        for type in [AnyValue()]:
            with self.assertRaises(InvalidTypeInCtor):
                Float(type)

    def test_CtorRaisesAnExceptionOnAnInvalidType_Template(self):
        for type in [TemplateType(Float(SimpleType()))]:
            with self.assertRaises(InvalidTypeInCtor):
                Float(type)

class TypeSystem_Float_Accept(unittest.TestCase):
    def test_AcceptReturnsTrueOnAValidValue(self):
        type = Float(SimpleType())
        for value in [FloatValue(-1.0), FloatValue(0.0), FloatValue(1.0)]:
            self.assertTrue(type.accept(value))

    def test_AcceptReturnsFalseOnAnInvalidValue_BuiltIn(self):
        type = Float(SimpleType())
        for value in [True, 1, "WAX"]:
            self.assertFalse(type.accept(value))

    def test_AcceptReturnsFalseOnAnInvalidValue_Special(self):
        type = Float(SimpleType())
        for value in [AnyValue()]:
            self.assertFalse(type.accept(value))

class TypeSystem_Float_Assign(unittest.TestCase):
    def test_AssignAssignsOnAValidValue(self):
        type = Float(SimpleType())
        for value in [FloatValue(-1.0), FloatValue(0.0), FloatValue(1.0)]:
            self.assertEqual(type.assign(value).value(), value)

    def test_AssignRaisesAnExceptionOnAnInvalidValue_BuiltIn(self):
        type = Float(SimpleType())
        for value in [AnyValue()]:
            with self.assertRaises(InvalidTypeInAssignment):
                type.assign(value)

    def test_AssignRaisesAnExceptionOnAnInvalidValue_Special(self):
        type = Float(SimpleType())
        for value in [AnyValue()]:
            with self.assertRaises(InvalidTypeInAssignment):
                type.assign(value)

class TypeSystem_Float_Eq(unittest.TestCase):
    def test_EqReturnsTrueOnSameValues_SameTypes(self):
        self.assertTrue(Float(SimpleType()).assign(FloatValue(1.0)) == Float(SimpleType()).assign(FloatValue(1.0)))

    def test_EqReturnsTrueOnSameValues_CompatibleTypes(self):
        type = Float(SimpleType()).assign(FloatValue(1.0))
        for value in [
            BoundedType(Float(SimpleType()), FloatValue(0.0), FloatValue(10.0)).assign(FloatValue(1.0)),
            TemplateType(Float(SimpleType())).assign(FloatValue(1.0))
        ]:
            self.assertTrue(type == value)

    def test_EqReturnsFalseOnDifferentValues(self):
        self.assertFalse(Float(SimpleType()).assign(FloatValue(1.0)) == Float(SimpleType()).assign(FloatValue(2.0)))

    def test_EqRaisesAnExceptionOnAnInvalidType_BuiltIn(self):
        type = Float(SimpleType()).assign(FloatValue(1.0))
        for value in [True, 1.0, "WAX"]:
            with self.assertRaises(InvalidTypeInComparison):
                type == value

    def test_EqRaisesAnExceptionOnAnInvalidType_Regular(self):
        type = Float(SimpleType()).assign(FloatValue(1.0))
        for value in [
            Boolean(SimpleType()).assign(BooleanValue(True)),
            Integer(SimpleType()).assign(IntegerValue(1)),
            Charstring(SimpleType()).assign(CharstringValue("WAX"))
        ]:
            with self.assertRaises(InvalidTypeInComparison):
                type == value

    def test_EqRaisesAnExceptionOnAnInvalidType_Special(self):
        type = Float(SimpleType()).assign(FloatValue(1.0))
        for value in [AnyValue()]:
            with self.assertRaises(InvalidTypeInComparison):
                type == value

    def test_EqRaisesAnExceptionOnAnInvalidType_Template(self):
        type = Float(SimpleType()).assign(FloatValue(1.0))
        for value in [
            TemplateType(Boolean(SimpleType())).assign(BooleanValue(True)),
            TemplateType(Integer(SimpleType())).assign(IntegerValue(1)),
            TemplateType(Charstring(SimpleType())).assign(CharstringValue("WAX"))
        ]:
            with self.assertRaises(InvalidTypeInComparison):
                type == value

class TypeSystem_Float_IsCompatible(unittest.TestCase):
    def test_IsCompatibleReturnsTrueOnACompatibleType_Self(self):
        instance = Float(SimpleType()).assign(FloatValue(1.0))
        self.assertTrue(instance.isCompatible(instance))

    def test_IsCompatibleReturnsTrueOnACompatibleType_BoundedType(self):
        instance1 = Float(SimpleType()).assign(FloatValue(1.0))
        instance2 = BoundedType(Float(SimpleType()), FloatValue(0.0), FloatValue(10.0)).assign(FloatValue(1.0))
        self.assertTrue(instance1.isCompatible(instance2))
        self.assertTrue(instance2.isCompatible(instance1))

    def test_IsCompatibleReturnsTrueOnACompatibleType_Subtyped(self):
        instance1 = Float(SimpleType()).assign(FloatValue(1.0))
        class MyFloat(Float):
            def __init__(self):
                Float.__init__(self, SimpleType())
        instance2 = MyFloat().assign(FloatValue(1.0))
        self.assertTrue(instance1.isCompatible(instance2))
        self.assertTrue(instance2.isCompatible(instance1))

    def test_IsCompatibleReturnsTrueOnACompatibleType_DoubleSubtyped(self):
        instance1 = Float(SimpleType()).assign(FloatValue(1.0))
        class MyFloat(Float):
            def __init__(self):
                Float.__init__(self, SimpleType())
        class MyFloat2(MyFloat):
            def __init__(self):
                MyFloat.__init__(self)
        instance2 = MyFloat2().assign(FloatValue(1.0))
        self.assertTrue(instance1.isCompatible(instance2))
        self.assertTrue(instance2.isCompatible(instance1))

    def test_IsCompatibleReturnsTrueOnACompatibleType_Template(self):
        instance1 = Float(SimpleType()).assign(FloatValue(1.0))
        instance2 = TemplateType(Float(SimpleType())).assign(FloatValue(1.0))
        self.assertTrue(instance1.isCompatible(instance2))
        self.assertTrue(instance2.isCompatible(instance1))

    def test_IsCompatibleReturnsFalseOnAnIncompatibleType_BuiltIn(self):
        instance1 = Float(SimpleType()).assign(FloatValue(1.0))
        for instance2 in [True, 1.0, "WAX"]:
            self.assertFalse(instance1.isCompatible(instance2))

    def test_IsCompatibleReturnsFalseOnAnIncompatibleType_Regular(self):
        instance1 = Float(SimpleType()).assign(FloatValue(1.0))
        for instance2 in [
            Boolean(SimpleType()).assign(BooleanValue(True)),
            Integer(SimpleType()).assign(IntegerValue(1)),
            Charstring(SimpleType()).assign(CharstringValue("WAX"))
        ]:
            self.assertFalse(instance1.isCompatible(instance2))
            self.assertFalse(instance2.isCompatible(instance1))

    def test_IsCompatibleReturnsFalseOnAnIncompatibleType_Special(self):
        instance1 = Float(SimpleType()).assign(FloatValue(1.0))
        for instance2 in [AnyValue()]:
            self.assertFalse(instance1.isCompatible(instance2))

    def test_IsCompatibleReturnsFalseOnAnIncompatibleType_TemplateWithSpecial(self):
        instance1 = Float(SimpleType()).assign(FloatValue(1.0))
        instance2 = TemplateType(Float(SimpleType())).assign(AnyValue())
        self.assertFalse(instance1.isCompatible(instance2))
        self.assertTrue(instance2.isCompatible(instance1))

class TypeSystem_Float_BoundedType_Ctor(unittest.TestCase):
    def test_Ctor(self):
        BoundedType(Float(SimpleType()), FloatValue(0.0), FloatValue(10.0))

class TypeSystem_Float_BoundedType_Accept(unittest.TestCase):
    def test_AcceptReturnsTrueOnAValidValue(self):
        type = BoundedType(Float(SimpleType()), FloatValue(0.0), FloatValue(10.0)).assign(FloatValue(1.0))
        for value in [FloatValue(0.0), FloatValue(1.0), FloatValue(1.0)]:
            self.assertTrue(type.accept(value))

    def test_AcceptReturnsFalseOnAnInvalidValue_InvalidType_BuiltIn(self):
        type = BoundedType(Float(SimpleType()), FloatValue(0.0), FloatValue(10.0)).assign(FloatValue(1.0))
        for value in [True, 1, "WAX"]:
            self.assertFalse(type.accept(value))

    def test_AcceptReturnsFalseOnAnInvalidValue_InvalidType_Special(self):
        type = BoundedType(Float(SimpleType()), FloatValue(0.0), FloatValue(10.0)).assign(FloatValue(1.0))
        for value in [AnyValue()]:
            self.assertFalse(type.accept(value))

    def test_AcceptReturnsFalseOnAnInvalidValue_InvalidValue(self):
        type = BoundedType(Float(SimpleType()), FloatValue(0.0), FloatValue(10.0)).assign(FloatValue(1.0))
        for value in [FloatValue(-1.0), FloatValue(11.0)]:
            self.assertFalse(type.accept(value))

class TypeSystem_Float_BoundedType_Assign(unittest.TestCase):
    def test_AssignAssignsOnAValidValue(self):
        type = BoundedType(Float(SimpleType()), FloatValue(0.0), FloatValue(10.0)).assign(FloatValue(1.0))
        for value in [FloatValue(0.0), FloatValue(1.0), FloatValue(1.0)]:
            self.assertEqual(type.assign(value).value(), value)

    def test_AssignRaisesAnExceptionOnAnInvalidValue_InvalidType_BuiltIn(self):
        type = BoundedType(Float(SimpleType()), FloatValue(0.0), FloatValue(10.0)).assign(FloatValue(1.0))
        for value in [True, 1, "WAX"]:
            with self.assertRaises(InvalidTypeInAssignment):
                type.assign(value)

    def test_AssignRaisesAnExceptionOnAnInvalidValue_InvalidType_Special(self):
        type = BoundedType(Float(SimpleType()), FloatValue(0.0), FloatValue(10.0)).assign(FloatValue(1.0))
        for value in [AnyValue()]:
            with self.assertRaises(InvalidTypeInAssignment):
                type.assign(value)

    def test_AssignRaisesAnExceptionOnAnInvalidValue_InvalidValue(self):
        type = BoundedType(Float(SimpleType()), FloatValue(0.0), FloatValue(10.0)).assign(FloatValue(1.0))
        for value in [FloatValue(-1.0), FloatValue(11.0)]:
            with self.assertRaises(InvalidTypeInAssignment):
                type.assign(value)

class TypeSystem_Float_BoundedType_Eq(unittest.TestCase):
    def test_EqReturnsTrueOnSameValues(self):
        self.assertTrue(
               BoundedType(Float(SimpleType()), FloatValue(0.0), FloatValue(10.0)).assign(FloatValue(1.0))
            == BoundedType(Float(SimpleType()), FloatValue(0.0), FloatValue(10.0)).assign(FloatValue(1.0)))

    def test_EqReturnsFalseOnDifferentValues(self):
        self.assertFalse(
               BoundedType(Float(SimpleType()), FloatValue(0.0), FloatValue(10.0)).assign(FloatValue(1.0))
            == BoundedType(Float(SimpleType()), FloatValue(0.0), FloatValue(10.0)).assign(FloatValue(2.0)))

    def test_EqRaisesAnExceptionOnAnInvalidType_BuiltIn(self):
        type = BoundedType(Float(SimpleType()), FloatValue(0.0), FloatValue(10.0)).assign(FloatValue(1.0))
        for value in [True, 1.0, "WAX"]:
            with self.assertRaises(InvalidTypeInComparison):
                type == value

    def test_EqRaisesAnExceptionOnAnInvalidType_Regular(self):
        type = BoundedType(Float(SimpleType()), FloatValue(0.0), FloatValue(10.0)).assign(FloatValue(1.0))
        for value in [
            Boolean(SimpleType()).assign(BooleanValue(True)),
            Integer(SimpleType()).assign(IntegerValue(1)),
            Charstring(SimpleType()).assign(CharstringValue("WAX"))
        ]:
            with self.assertRaises(InvalidTypeInComparison):
                type == value

    def test_EqRaisesAnExceptionOnAnInvalidType_Special(self):
        type = BoundedType(Float(SimpleType()), FloatValue(0.0), FloatValue(10.0)).assign(FloatValue(1.0))
        for value in [AnyValue()]:
            with self.assertRaises(InvalidTypeInComparison):
                type == value

    def test_EqRaisesAnExceptionOnAnInvalidType_Template(self):
        type = BoundedType(Float(SimpleType()), FloatValue(0.0), FloatValue(10.0)).assign(FloatValue(1.0))
        for value in [
            TemplateType(Boolean(SimpleType())).assign(BooleanValue(True)),
            TemplateType(Integer(SimpleType())).assign(IntegerValue(1)),
            TemplateType(Charstring(SimpleType())).assign(CharstringValue("WAX"))
        ]:
            with self.assertRaises(InvalidTypeInComparison):
                type == value

class TypeSystem_Float_TemplateType_Ctor(unittest.TestCase):
    def test_Ctor(self):
        TemplateType(Float(SimpleType()))

class TypeSystem_Float_TemplateType_Accept(unittest.TestCase):
    def test_AcceptReturnsTrueOnAValidValue(self):
        type = TemplateType(Float(SimpleType()))
        for value in [FloatValue(-1.0), FloatValue(0.0), FloatValue(10.0), AnyValue()]:
            self.assertTrue(type.accept(value))

    def test_AcceptReturnsFalseOnAnInvalidValue_InvalidType(self):
        type = TemplateType(Float(SimpleType()))
        for value in [True, 1, "WAX"]:
            self.assertFalse(type.accept(value))

class TypeSystem_Float_TemplateType_Assign(unittest.TestCase):
    def test_AssignAssignsOnAValidValue(self):
        type = TemplateType(Float(SimpleType()))
        for value in [FloatValue(-1.0), FloatValue(0.0), FloatValue(10.0), AnyValue()]:
            self.assertEqual(type.assign(value).value(), value)

    def test_AssignRaisesAnExceptionOnAnInvalidValue(self):
        type = TemplateType(Float(SimpleType()))
        for value in [True, 1, "WAX"]:
            with self.assertRaises(InvalidTypeInAssignment):
                type.assign(value)

class TypeSystem_Float_TemplateType_Eq(unittest.TestCase):
    def test_EqReturnsTrueOnSameValues(self):
        for values in [(FloatValue(1.0), FloatValue(1.0)),
                       (FloatValue(1.0), AnyValue()),
                       (AnyValue(), FloatValue(1.0)),
                       (AnyValue(), AnyValue())]:
            self.assertTrue(   TemplateType(Float(SimpleType())).assign(values[0])
                            == TemplateType(Float(SimpleType())).assign(values[1]))

    def test_EqReturnsFalseOnDifferentValues(self):
        self.assertFalse(   TemplateType(Float(SimpleType())).assign(FloatValue(1.0))
                         == TemplateType(Float(SimpleType())).assign(FloatValue(2.0)))

    def test_EqRaisesAnExceptionOnAnInvalidType_BuiltIn(self):
        type = TemplateType(Float(SimpleType())).assign(FloatValue(1.0))
        for value in [True, 1.0, "WAX"]:
            with self.assertRaises(InvalidTypeInComparison):
                type == value

    def test_EqRaisesAnExceptionOnAnInvalidType_Regular(self):
        type = TemplateType(Float(SimpleType())).assign(FloatValue(1.0))
        for value in [
            Boolean(SimpleType()).assign(BooleanValue(True)),
            Integer(SimpleType()).assign(IntegerValue(1)),
            Charstring(SimpleType()).assign(CharstringValue("WAX"))
        ]:
            with self.assertRaises(InvalidTypeInComparison):
                type == value

    def test_EqRaisesAnExceptionOnAnInvalidType_Special(self):
        type = TemplateType(Float(SimpleType())).assign(FloatValue(1.0))
        for value in [AnyValue()]:
            with self.assertRaises(InvalidTypeInComparison):
                type == value

    def test_EqRaisesAnExceptionOnAnInvalidType_Template(self):
        type = TemplateType(Float(SimpleType())).assign(FloatValue(1.0))
        for value in [
            TemplateType(Boolean(SimpleType())).assign(BooleanValue(True)),
            TemplateType(Integer(SimpleType())).assign(IntegerValue(1)),
            TemplateType(Charstring(SimpleType())).assign(CharstringValue("WAX"))
        ]:
            with self.assertRaises(InvalidTypeInComparison):
                type == value

class TypeSystem_Charstring_Ctor(unittest.TestCase):
    def test_Ctor(self):
        Charstring(SimpleType())

    def test_CtorRaisesAnExceptionOnAnInvalidType_BuiltIn(self):
        for type in [True, 1, 1.0, "WAX", {}, [], ()]:
            with self.assertRaises(InvalidTypeInCtor):
                Charstring(type)

    def test_CtorRaisesAnExceptionOnAnInvalidType_Regular(self):
        for type in [Boolean(SimpleType()), Integer(SimpleType()), Float(SimpleType()), Charstring(SimpleType())]:
            with self.assertRaises(InvalidTypeInCtor):
                Charstring(type)

    def test_CtorRaisesAnExceptionOnAnInvalidType_Special(self):
        for type in [AnyValue()]:
            with self.assertRaises(InvalidTypeInCtor):
                Charstring(type)

    def test_CtorRaisesAnExceptionOnAnInvalidType_Template(self):
        for type in [TemplateType(Charstring(SimpleType()))]:
            with self.assertRaises(InvalidTypeInCtor):
                Charstring(type)

class TypeSystem_Charstring_Accept(unittest.TestCase):
    def test_AcceptReturnsTrueOnAValidValue(self):
        type = Charstring(SimpleType())
        for value in [CharstringValue(""), CharstringValue("WAX")]:
            self.assertTrue(type.accept(value))

    def test_AcceptReturnsFalseOnAnInvalidValue_BuiltIn(self):
        type = Charstring(SimpleType())
        for value in [True, 1, 1.0]:
            self.assertFalse(type.accept(value))

    def test_AcceptReturnsFalseOnAnInvalidValue_Special(self):
        type = Charstring(SimpleType())
        for value in [AnyValue()]:
            self.assertFalse(type.accept(value))

class TypeSystem_Charstring_Assign(unittest.TestCase):
    def test_AssignAssignsOnAValidValue(self):
        type = Charstring(SimpleType())
        for value in [CharstringValue(""), CharstringValue("WAX")]:
            self.assertEqual(type.assign(value).value(), value)

    def test_AssignRaisesAnExceptionOnAnInvalidValue_BuiltIn(self):
        type = Charstring(SimpleType())
        for value in [True, 1, 1.0]:
            with self.assertRaises(InvalidTypeInAssignment):
                type.assign(value)

    def test_AssignRaisesAnExceptionOnAnInvalidValue_Special(self):
        type = Charstring(SimpleType())
        for value in [AnyValue()]:
            with self.assertRaises(InvalidTypeInAssignment):
                type.assign(value)

class TypeSystem_Charstring_Eq(unittest.TestCase):
    def test_EqReturnsTrueOnSameValues_SameTypes(self):
        for values in [(CharstringValue(""), CharstringValue("")),
                       (CharstringValue("WAX"), CharstringValue("WAX"))]:
            self.assertTrue(   TemplateType(Charstring(SimpleType())).assign(values[0])
                            == TemplateType(Charstring(SimpleType())).assign(values[1]))

    def test_EqReturnsTrueOnSameValues_CompatibleTypes(self):
        type = Charstring(SimpleType()).assign(CharstringValue("WAX"))
        for value in [
            TemplateType(Charstring(SimpleType())).assign(CharstringValue("WAX"))
        ]:
            self.assertTrue(type == value)

    def test_EqReturnsFalseOnDifferentValues(self):
        self.assertFalse(   Charstring(SimpleType()).assign(CharstringValue("WAX"))
                         == Charstring(SimpleType()).assign(CharstringValue("WAS")))

    def test_EqRaisesAnExceptionOnAnInvalidType_BuiltIn(self):
        type = Charstring(SimpleType()).assign(CharstringValue("WAX"))
        for value in [True, 1.0, "WAX"]:
            with self.assertRaises(InvalidTypeInComparison):
                type == value

    def test_EqRaisesAnExceptionOnAnInvalidType_Regular(self):
        type = Charstring(SimpleType()).assign(CharstringValue("WAX"))
        for value in [
            Boolean(SimpleType()).assign(BooleanValue(True)),
            Integer(SimpleType()).assign(IntegerValue(1)),
            Float(SimpleType()).assign(FloatValue(1.0))
        ]:
            with self.assertRaises(InvalidTypeInComparison):
                type == value

    def test_EqRaisesAnExceptionOnAnInvalidType_Special(self):
        type = Charstring(SimpleType()).assign(CharstringValue("WAX"))
        for value in [AnyValue()]:
            with self.assertRaises(InvalidTypeInComparison):
                type == value

    def test_EqRaisesAnExceptionOnAnInvalidType_Template(self):
        type = Charstring(SimpleType()).assign(CharstringValue("WAX"))
        for value in [
            TemplateType(Boolean(SimpleType())).assign(BooleanValue(True)),
            TemplateType(Integer(SimpleType())).assign(IntegerValue(1)),
            TemplateType(Float(SimpleType())).assign(FloatValue(1.0))
        ]:
            with self.assertRaises(InvalidTypeInComparison):
                type == value

class TypeSystem_Charstring_IsCompatible(unittest.TestCase):
    def test_IsCompatibleReturnsTrueOnACompatibleType_Self(self):
        instance = Charstring(SimpleType()).assign(CharstringValue("WAX"))
        self.assertTrue(instance.isCompatible(instance))

    def test_IsCompatibleReturnsTrueOnACompatibleType_Subtyped(self):
        instance1 = Charstring(SimpleType()).assign(CharstringValue("WAX"))
        class MyCharstring(Charstring):
            def __init__(self):
                Charstring.__init__(self, SimpleType())
        instance2 = MyCharstring().assign(CharstringValue("WAX"))
        self.assertTrue(instance1.isCompatible(instance2))
        self.assertTrue(instance2.isCompatible(instance1))

    def test_IsCompatibleReturnsTrueOnACompatibleType_DoubleSubtyped(self):
        instance1 = Charstring(SimpleType()).assign(CharstringValue("WAX"))
        class MyCharstring(Charstring):
            def __init__(self):
                Charstring.__init__(self, SimpleType())
        class MyCharstring2(MyCharstring):
            def __init__(self):
                MyCharstring.__init__(self)
        instance2 = MyCharstring2().assign(CharstringValue("WAX"))
        self.assertTrue(instance1.isCompatible(instance2))
        self.assertTrue(instance2.isCompatible(instance1))

    def test_IsCompatibleReturnsTrueOnACompatibleType_Template(self):
        instance1 = Charstring(SimpleType()).assign(CharstringValue("WAX"))
        instance2 = TemplateType(Charstring(SimpleType())).assign(CharstringValue("WAX"))
        self.assertTrue(instance1.isCompatible(instance2))
        self.assertTrue(instance2.isCompatible(instance1))

    def test_IsCompatibleReturnsFalseOnAnIncompatibleType_BuiltIn(self):
        instance1 = Charstring(SimpleType()).assign(CharstringValue("WAX"))
        for instance2 in [True, 1.0, "WAX"]:
            self.assertFalse(instance1.isCompatible(instance2))

    def test_IsCompatibleReturnsFalseOnAnIncompatibleType_Regular(self):
        instance1 = Charstring(SimpleType()).assign(CharstringValue("WAX"))
        for instance2 in [
            Boolean(SimpleType()).assign(BooleanValue(True)),
            Integer(SimpleType()).assign(IntegerValue(1)),
            Float(SimpleType()).assign(FloatValue(1.0)),
        ]:
            self.assertFalse(instance1.isCompatible(instance2))
            self.assertFalse(instance2.isCompatible(instance1))

    def test_IsCompatibleReturnsFalseOnAnIncompatibleType_Special(self):
        instance1 = Charstring(SimpleType()).assign(CharstringValue("WAX"))
        for instance2 in [AnyValue()]:
            self.assertFalse(instance1.isCompatible(instance2))

    def test_IsCompatibleReturnsFalseOnAnIncompatibleType_TemplateWithSpecial(self):
        instance1 = Charstring(SimpleType()).assign(CharstringValue("WAX"))
        instance2 = TemplateType(Charstring(SimpleType())).assign(AnyValue())
        self.assertFalse(instance1.isCompatible(instance2))
        self.assertTrue(instance2.isCompatible(instance1))

class TypeSystem_Charstring_TemplateType_Ctor(unittest.TestCase):
    def test_Ctor(self):
        TemplateType(Charstring(SimpleType()))

class TypeSystem_Charstring_TemplateType_Accept(unittest.TestCase):
    def test_AcceptReturnsTrueOnAValidValue(self):
        type = TemplateType(Charstring(SimpleType()))
        for value in [CharstringValue(""), CharstringValue("WAX"), AnyValue()]:
            self.assertTrue(type.accept(value))

    def test_AcceptReturnsFalseOnAnInvalidValue_InvalidType(self):
        type = TemplateType(Charstring(SimpleType()))
        for value in [True, 1, 1.0]:
            self.assertFalse(type.accept(value))

class TypeSystem_Charstring_TemplateType_Assign(unittest.TestCase):
    def test_AssignAssignsOnAValidValue(self):
        type = TemplateType(Charstring(SimpleType()))
        for value in [CharstringValue(""), CharstringValue("WAX"), AnyValue()]:
            self.assertEqual(type.assign(value).value(), value)

    def test_AssignRaisesAnExceptionOnAnInvalidValue(self):
        type = TemplateType(Charstring(SimpleType()))
        for value in [True, 1, 1.0]:
            with self.assertRaises(InvalidTypeInAssignment):
                type.assign(value)

class TypeSystem_Charstring_TemplateType_Eq(unittest.TestCase):
    def test_EqReturnsTrueOnSameValues(self):
        for values in [(CharstringValue(""), CharstringValue("")),
                       (CharstringValue("WAX"), CharstringValue("WAX")),
                       (CharstringValue("WAX"), AnyValue()),
                       (AnyValue(), CharstringValue("WAX")),
                       (AnyValue(), AnyValue())]:
            self.assertTrue(   TemplateType(Charstring(SimpleType())).assign(values[0])
                            == TemplateType(Charstring(SimpleType())).assign(values[1]))

    def test_EqReturnsFalseOnDifferentValues(self):
        self.assertFalse(   TemplateType(Charstring(SimpleType())).assign(CharstringValue("WAX"))
                         == TemplateType(Charstring(SimpleType())).assign(CharstringValue("WAS")))

    def test_EqRaisesAnExceptionOnAnInvalidType_BuiltIn(self):
        type = TemplateType(Charstring(SimpleType())).assign(CharstringValue("WAX"))
        for value in [True, 1.0, "WAX"]:
            with self.assertRaises(InvalidTypeInComparison):
                type == value

    def test_EqRaisesAnExceptionOnAnInvalidType_Regular(self):
        type = TemplateType(Charstring(SimpleType())).assign(CharstringValue("WAX"))
        for value in [
            Boolean(SimpleType()).assign(BooleanValue(True)),
            Integer(SimpleType()).assign(IntegerValue(1)),
            Float(SimpleType()).assign(FloatValue(1.0))
        ]:
            with self.assertRaises(InvalidTypeInComparison):
                type == value

    def test_EqRaisesAnExceptionOnAnInvalidType_Special(self):
        type = TemplateType(Charstring(SimpleType())).assign(CharstringValue("WAX"))
        for value in [AnyValue()]:
            with self.assertRaises(InvalidTypeInComparison):
                type == value

    def test_EqRaisesAnExceptionOnAnInvalidType_Template(self):
        type = TemplateType(Charstring(SimpleType())).assign(CharstringValue("WAX"))
        for value in [
            TemplateType(Boolean(SimpleType())).assign(BooleanValue(True)),
            TemplateType(Integer(SimpleType())).assign(IntegerValue(1)),
            TemplateType(Float(SimpleType())).assign(FloatValue(1.0))
        ]:
            with self.assertRaises(InvalidTypeInComparison):
                type == value

class TypeSystem_Record_Ctor(unittest.TestCase):
    def test_Ctor_WithoutDictionary(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType())
        type = MyRecord()

    def test_Ctor_WithDictionary_Empty(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {})
        type = MyRecord()

    def test_Ctor_WithDictionary_NonEmpty(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': Charstring(SimpleType())})
        type = MyRecord()

    def test_CtorRaisesAnExceptionOnAnInvalidValue_InvalidKey(self):
        with self.assertRaises(InvalidTypeInCtor):
            class MyRecord(Record):
                def __init__(self):
                    Record.__init__(self, SimpleType(), {1: Integer(SimpleType()), 'bar': Charstring(SimpleType())})
            type = MyRecord()

    def test_CtorRaisesAnExceptionOnAnInvalidValue_InvalidType_BuiltIn(self):
        for type in [True, 1, 1.0, "WAX", [1, 2], (1, 2)]:
            with self.assertRaises(InvalidTypeInCtor):
                class MyRecord(Record):
                    def __init__(self):
                        Record.__init__(self, SimpleType(), type)
                type = MyRecord()

    def test_CtorRaisesAnExceptionOnAnInvalidValue_InvalidType_Special(self):
        for type in [AnyValue()]:
            with self.assertRaises(InvalidTypeInCtor):
                class MyRecord(Record):
                    def __init__(self):
                        Record.__init__(self, SimpleType(), type)
                type = MyRecord()

    def test_CtorRaisesAnExceptionOnAnInvalidValue_InvalidType_Template(self):
        for type in [TemplateType(Integer(SimpleType()))]:
            with self.assertRaises(InvalidTypeInCtor):
                class MyRecord(Record):
                    def __init__(self):
                        Record.__init__(self, SimpleType(), type)
                type = MyRecord()

    def test_CtorRaisesAnExceptionOnAnInvalidValue_InvalidType_AnyOfNestedTypesIsASpecialType(self):
        with self.assertRaises(InvalidTypeInCtor):
            class MyRecord(Record):
                def __init__(self):
                    Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': AnyValue()})
            type = MyRecord()

    def test_CtorRaisesAnExceptionOnAnInvalidValue_InvalidType_AnyOfNestedTypesIsATemplateLikeType(self):
        with self.assertRaises(InvalidTypeInCtor):
            class MyRecord(Record):
                def __init__(self):
                    Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()),
                                                         'bar': TemplateType(Integer(SimpleType()))})
            type = MyRecord()

class TypeSystem_Record_Accept(unittest.TestCase):
    def test_AcceptReturnsTrueOnAValidValue_TheSameTypes(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': Charstring(SimpleType())})
        type = MyRecord()
        value = {'foo': Integer(SimpleType()).assign(IntegerValue(1)),
                 'bar': Charstring(SimpleType()).assign(CharstringValue("WAX"))}
        self.assertTrue(type.accept(value))

    def test_AcceptReturnsTrueOnAValidValue_CompatibleTypes(self):
        self.skipTest("Not implemented yet.")
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': Charstring(SimpleType())})
        type = MyRecord()
        value = {'foo': BoundedType(
                            Integer(SimpleType()),
                            IntegerValue(0),
                            IntegerValue(10)
                        ).assign(IntegerValue(1)),
                 'bar': Charstring(SimpleType()).assign(CharstringValue("WAX"))}
        self.assertTrue(type.accept(value))

    def test_AcceptReturnsTrueOnAValidValue_NestedRecords(self):
        class InternalRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': Charstring(SimpleType())})
        class ExternalRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': InternalRecord()})
        internalValue = {'foo': Integer(SimpleType()).assign(IntegerValue(1)),
                         'bar': Charstring(SimpleType()).assign(CharstringValue("WAX"))}
        externalValue = {'foo': Integer(SimpleType()).assign(IntegerValue(2)),
                         'bar': internalValue}
        externalRecord = ExternalRecord()
        self.assertTrue(externalRecord.accept(externalValue))

    def test_AcceptReturnsTrueOnAValidValue_RecordWithNestedRecordOf(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer(SimpleType()))
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': MyRecordOf()})
        type = MyRecord()
        value = {'foo': Integer(SimpleType()).assign(IntegerValue(1)),
                 'bar': [Integer(SimpleType()).assign(IntegerValue(1)), Integer(SimpleType()).assign(IntegerValue(2))]}
        self.assertTrue(type.accept(value))

    def test_AcceptReturnsFalseOnAnInvalidValue_InvalidType_BuiltIn(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': Charstring(SimpleType())})
        type = MyRecord()
        for value in [True, 1, 1.0, "WAX", [1, 2], (1, 2)]:
            self.assertFalse(type.accept(value))

    def test_AcceptReturnsFalseOnAnInvalidValue_InvalidType_Special(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': Charstring(SimpleType())})
        type = MyRecord()
        value = {'foo': Integer(SimpleType()).assign(IntegerValue(1)),
                 'bar': AnyValue()}
        self.assertFalse(type.accept(value))

    def test_AcceptReturnsFalseOnAnInvalidValue_InvalidType_AnyOfNestedTypesIsATemplateLikeType(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': Charstring(SimpleType())})
        type = MyRecord()
        value = {'foo': Integer(SimpleType()).assign(IntegerValue(1)),
                 'bar': TemplateType(Charstring(SimpleType())).assign(AnyValue())}
        self.assertFalse(type.accept(value))

    def test_AcceptReturnsFalseOnAnInvalidValue_IncompatibleDictionaries_AssignedEmpty(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': Charstring(SimpleType())})
        type = MyRecord()
        self.assertFalse(type.accept({}))

    def test_AcceptReturnsFalseOnAnInvalidValue_IncompatibleDictionaries_AssignedTooSmall(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': Charstring(SimpleType())})
        type = MyRecord()
        value = {'foo': Integer(SimpleType()).assign(IntegerValue(1))}
        self.assertFalse(type.accept(value))

    def test_AcceptReturnsFalseOnAnInvalidValue_IncompatibleDictionaries_AssignedTooBig(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': Charstring(SimpleType())})
        type = MyRecord()
        value = {'foo': Integer(SimpleType()).assign(IntegerValue(1)),
                 'bar': Charstring(SimpleType()).assign(CharstringValue("WAX")),
                 'baz': Integer(SimpleType()).assign(IntegerValue(2))}
        self.assertFalse(type.accept(value))

    def test_AcceptReturnsFalseOnAnInvalidValue_IncompatibleDictionaries_AssignedHasDifferentKeys(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': Charstring(SimpleType())})
        type = MyRecord()
        value = {'foo': Integer(SimpleType()).assign(IntegerValue(1)),
                 'baz': Charstring(SimpleType()).assign(CharstringValue("WAX"))}
        self.assertFalse(type.accept(value))

    def test_AcceptReturnsFalseOnAnInvalidValue_IncompatibleDictionaries_AssignedHasChangedKeys(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': Charstring(SimpleType())})
        type = MyRecord()
        value = {'bar': Integer(SimpleType()).assign(IntegerValue(1)),
                 'foo': Charstring(SimpleType()).assign(CharstringValue("WAX"))}
        self.assertFalse(type.accept(value))

    def test_AcceptReturnsFalseOnAnInvalidValue_NestedRecords_WithSpecialTypes(self):
        class InternalRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': Charstring(SimpleType())})
        class ExternalRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': InternalRecord()})
        internalValue = {'foo': TemplateType(Integer(SimpleType())).assign(AnyValue()),
                         'bar': Charstring(SimpleType()).assign(CharstringValue("WAX"))}
        externalValue = {'foo': Integer(SimpleType()).assign(IntegerValue(1)),
                         'bar': internalValue}
        externalRecord = ExternalRecord()
        self.assertFalse(externalRecord.accept(externalValue))

class TypeSystem_Record_Assign(unittest.TestCase):
    def test_AssignAssignsOnAValidValue_TheSameTypes(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': Charstring(SimpleType())})
        type = MyRecord()
        value = {'foo': Integer(SimpleType()).assign(IntegerValue(1)),
                 'bar': Charstring(SimpleType()).assign(CharstringValue("WAX"))}
        type.assign(value)

    def test_AssignAssignsOnAValidValue_CompatibleTypes(self):
        self.skipTest("Not implemented yet.")
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': Charstring(SimpleType())})
        type = MyRecord()
        value = {'foo': BoundedType(
                            Integer(SimpleType()),
                            IntegerValue(0),
                            IntegerValue(10)
                        ).assign(IntegerValue(1)),
                 'bar': Charstring(SimpleType()).assign(CharstringValue("WAX"))}
        type.assign(value)

    def test_AssignAssignsOnAValidValue_NestedRecords(self):
        class InternalRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': Charstring(SimpleType())})
        class ExternalRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': InternalRecord()})
        internalValue = {'foo': Integer(SimpleType()).assign(IntegerValue(1)),
                         'bar': Charstring(SimpleType()).assign(CharstringValue("WAX"))}
        externalValue = {'foo': Integer(SimpleType()).assign(IntegerValue(2)),
                         'bar': internalValue}
        externalRecord = ExternalRecord()
        externalRecord.assign(externalValue)

    def test_AssignAssignsOnAValidValue_RecordWithNestedRecordOf(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer(SimpleType()))
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': MyRecordOf()})
        type = MyRecord()
        value = {'foo': Integer(SimpleType()).assign(IntegerValue(1)),
                 'bar': [Integer(SimpleType()).assign(IntegerValue(1)), Integer(SimpleType()).assign(IntegerValue(2))]}
        type.assign(value)
        self.assertTrue(type.getField('bar').getField(0) == Integer(SimpleType()).assign(IntegerValue(1)))
        self.assertTrue(type.getField('bar').getField(1) == Integer(SimpleType()).assign(IntegerValue(2)))

    def test_AssignRaisesAnExceptionOnAnInvalidValue_InvalidType_BuiltIn(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': Charstring(SimpleType())})
        type = MyRecord()
        for value in [True, 1, 1.0, "WAX", [1, 2], (1, 2)]:
            with self.assertRaises(InvalidTypeInAssignment):
                type.assign(value)

    def test_AssignRaisesAnExceptionOnAnInvalidValue_InvalidType_Special(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': Charstring(SimpleType())})
        type = MyRecord()
        value = {'foo': Integer(SimpleType()).assign(IntegerValue(1)),
                 'bar': AnyValue()}
        with self.assertRaises(InvalidTypeInAssignment):
            type.assign(value)

    def test_AssignRaisesAnExceptionOnAnInvalidValue_IncompatibleDictionaries_AssignedEmpty(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': Charstring(SimpleType())})
        type = MyRecord()
        with self.assertRaises(InvalidTypeInAssignment):
            type.assign({})

    def test_AssignRaisesAnExceptionOnAnInvalidValue_IncompatibleDictionaries_AssignedTooSmall(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': Charstring(SimpleType())})
        type = MyRecord()
        value = {'foo': Integer(SimpleType()).assign(IntegerValue(1))}
        with self.assertRaises(InvalidTypeInAssignment):
            type.assign(value)

    def test_AssignRaisesAnExceptionOnAnInvalidValue_IncompatibleDictionaries_AssignedTooBig(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': Charstring(SimpleType())})
        type = MyRecord()
        value = {'foo': Integer(SimpleType()).assign(IntegerValue(1)),
                 'bar': Charstring(SimpleType()).assign(CharstringValue("WAX")),
                 'baz': Integer(SimpleType()).assign(IntegerValue(2))}
        with self.assertRaises(InvalidTypeInAssignment):
            type.assign(value)

    def test_AssignRaisesAnExceptionOnAnInvalidValue_IncompatibleDictionaries_AssignedHasDifferentKeys(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': Charstring(SimpleType())})
        type = MyRecord()
        value = {'foo': Integer(SimpleType()).assign(IntegerValue(1)),
                 'baz': Charstring(SimpleType()).assign(CharstringValue("WAX"))}
        with self.assertRaises(InvalidTypeInAssignment):
            type.assign(value)

    def test_AssignRaisesAnExceptionOnAnInvalidValue_IncompatibleDictionaries_AssignedHasChangedKeys(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': Charstring(SimpleType())})
        type = MyRecord()
        value = {'bar': Integer(SimpleType()).assign(IntegerValue(1)),
                 'foo': Charstring(SimpleType()).assign(CharstringValue("WAX"))}
        with self.assertRaises(InvalidTypeInAssignment):
            type.assign(value)

class TypeSystem_Record_Eq(unittest.TestCase):
    def test_EqReturnsTrueOnSameValues_EmptyRecord(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {})
        record1 = MyRecord().assign({})
        record2 = MyRecord().assign({})
        self.assertTrue(record1 == record2)
        self.assertTrue(record2 == record1)

    def test_EqReturnsTrueOnSameValues_NonEmptyRecord(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': Charstring(SimpleType())})
        value = {'foo': Integer(SimpleType()).assign(IntegerValue(1)),
                 'bar': Charstring(SimpleType()).assign(CharstringValue("WAX"))}
        record1 = MyRecord().assign(value)
        record2 = MyRecord().assign(value)
        self.assertTrue(record1 == record2)
        self.assertTrue(record2 == record1)

    def test_EqReturnsTrueOnSameValues_NestedRecords(self):
        class InternalRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': Charstring(SimpleType())})
        class ExternalRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': InternalRecord()})
        internalValue1 = {'foo': Integer(SimpleType()).assign(IntegerValue(1)),
                          'bar': Charstring(SimpleType()).assign(CharstringValue("WAX"))}
        internalValue2 = {'foo': Integer(SimpleType()).assign(IntegerValue(1)),
                          'bar': Charstring(SimpleType()).assign(CharstringValue("WAX"))}
        externalValue1 = {'foo': Integer(SimpleType()).assign(IntegerValue(2)),
                          'bar': internalValue1}
        externalValue2 = {'foo': Integer(SimpleType()).assign(IntegerValue(2)),
                          'bar': internalValue2}
        externalRecord1 = ExternalRecord()
        externalRecord2 = ExternalRecord()
        externalRecord1.assign(externalValue1)
        externalRecord2.assign(externalValue2)
        self.assertTrue(externalRecord1 == externalRecord2)
        self.assertTrue(externalRecord2 == externalRecord1)

    def test_EqReturnsFalseOnDifferentValues_NonEmptyRecord(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': Charstring(SimpleType())})
        value1 = {'foo': Integer(SimpleType()).assign(IntegerValue(1)),
                  'bar': Charstring(SimpleType()).assign(CharstringValue("WAX"))}
        value2 = {'foo': Integer(SimpleType()).assign(IntegerValue(2)),
                  'bar': Charstring(SimpleType()).assign(CharstringValue("WAX"))}
        record1 = MyRecord().assign(value1)
        record2 = MyRecord().assign(value2)
        self.assertFalse(record1 == record2)
        self.assertFalse(record2 == record1)

    def test_EqReturnsFalseOnDifferentValues_NestedRecords(self):
        class InternalRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': Charstring(SimpleType())})
        class ExternalRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': InternalRecord()})
        internalValue1 = {'foo': Integer(SimpleType()).assign(IntegerValue(1)),
                          'bar': Charstring(SimpleType()).assign(CharstringValue("WAX"))}
        internalValue2 = {'foo': Integer(SimpleType()).assign(IntegerValue(2)),
                          'bar': Charstring(SimpleType()).assign(CharstringValue("WAX"))}
        externalValue1 = {'foo': Integer(SimpleType()).assign(IntegerValue(2)),
                          'bar': internalValue1}
        externalValue2 = {'foo': Integer(SimpleType()).assign(IntegerValue(2)),
                          'bar': internalValue2}
        externalRecord1 = ExternalRecord()
        externalRecord2 = ExternalRecord()
        externalRecord1.assign(externalValue1)
        externalRecord2.assign(externalValue2)
        self.assertFalse(externalRecord1 == externalRecord2)
        self.assertFalse(externalRecord2 == externalRecord1)

    def test_EqRaisesAnExceptionOnAnInvalidValue_InvalidType_BuiltIn(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': Charstring(SimpleType())})
        value = {'foo': Integer(SimpleType()).assign(IntegerValue(1)),
                 'bar': Charstring(SimpleType()).assign(CharstringValue("WAX"))}
        record = MyRecord().assign(value)
        for value in [True, 1, 1.0, "WAX", [1, 2], (1, 2)]:
            with self.assertRaises(InvalidTypeInComparison):
                record == value

    def test_EqRaisesAnExceptionOnAnInvalidValue_InvalidType_Special(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': Charstring(SimpleType())})
        value = {'foo': Integer(SimpleType()).assign(IntegerValue(1)),
                 'bar': Charstring(SimpleType()).assign(CharstringValue("WAX"))}
        record = MyRecord().assign(value)
        for value in [AnyValue()]:
            with self.assertRaises(InvalidTypeInComparison):
                record == value

    def test_EqRaisesAnExceptionOnAnInvalidValue_InvalidType_Template(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': Charstring(SimpleType())})
        value = {'foo': Integer(SimpleType()).assign(IntegerValue(1)),
                 'bar': Charstring(SimpleType()).assign(CharstringValue("WAX"))}
        record = MyRecord().assign(value)
        for value in [TemplateType(Integer(SimpleType())).assign(IntegerValue(1))]:
            with self.assertRaises(InvalidTypeInComparison):
                record == value

    def test_EqRaisesAnExceptionOnAnInvalidValue_InvalidType_DifferentType(self):
        class MyRecord1(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': Charstring(SimpleType())})
        class MyRecord2(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': Charstring(SimpleType())})
        value1 = {'foo': Integer(SimpleType()).assign(IntegerValue(1)),
                  'bar': Charstring(SimpleType()).assign(CharstringValue("WAX"))}
        value2 = {'foo': Integer(SimpleType()).assign(IntegerValue(1)),
                  'bar': Charstring(SimpleType()).assign(CharstringValue("WAX"))}
        record1 = MyRecord1().assign(value1)
        record2 = MyRecord2().assign(value2)
        with self.assertRaises(InvalidTypeInComparison):
            record1 == record2

class TypeSystem_Record_GetField(unittest.TestCase):
    def test_GetFieldReturnsTheValueOfTheFieldOnAValidField(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': Charstring(SimpleType())})
        value = {'foo': Integer(SimpleType()).assign(IntegerValue(1)),
                 'bar': Charstring(SimpleType()).assign(CharstringValue("WAX"))}
        record = MyRecord().assign(value)
        self.assertEqual(record.getField('foo'), Integer(SimpleType()).assign(IntegerValue(1)))
        self.assertEqual(record.getField('bar'), Charstring(SimpleType()).assign(CharstringValue("WAX")))

    def test_GetFieldRaisesAnExceptionOnAnInvalidField(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': Charstring(SimpleType())})
        value = {'foo': Integer(SimpleType()).assign(IntegerValue(1)),
                 'bar': Charstring(SimpleType()).assign(CharstringValue("WAX"))}
        record = MyRecord().assign(value)
        with self.assertRaises(LookupErrorMissingField):
            record.getField('baz')

class TypeSystem_Record_TemplateRecord_Ctor(unittest.TestCase):
    def test_Ctor_WithoutDictionary(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType())
        class MyTemplateRecord(TemplateRecord):
            def __init__(self):
                TemplateRecord.__init__(self, MyRecord())
        type = MyTemplateRecord()

    def test_Ctor_WithDictionary(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': Charstring(SimpleType())})
        class MyTemplateRecord(TemplateRecord):
            def __init__(self):
                TemplateRecord.__init__(self, MyRecord())
        type = MyTemplateRecord()

    def test_CtorRaisesAnExceptionOnAnInvalidValue_DoubleWrap(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': Charstring(SimpleType())})
        class MyTemplateRecord1(TemplateRecord):
            def __init__(self):
                TemplateRecord.__init__(self, MyRecord())
        class MyTemplateRecord2(TemplateRecord):
            def __init__(self):
                TemplateRecord.__init__(self, MyTemplateRecord1())
        with self.assertRaises(InvalidTypeInCtor):
            type = MyTemplateRecord2()

    def test_CtorRaisesAnExceptionOnAnInvalidValue_InvalidType_BuiltIn(self):
        for type in [True, 1, 1.0, "WAX", [1, 2], (1, 2)]:
            with self.assertRaises(InvalidTypeInCtor):
                class MyTemplateRecord(TemplateRecord):
                    def __init__(self):
                        TemplateRecord.__init__(self, type)
                type = MyTemplateRecord()

    def test_CtorRaisesAnExceptionOnAnInvalidValue_InvalidType_Regular(self):
        for type in [Boolean(SimpleType()), Integer(SimpleType()), Float(SimpleType()), Charstring(SimpleType())]:
            with self.assertRaises(InvalidTypeInCtor):
                class MyTemplateRecord(TemplateRecord):
                    def __init__(self):
                        TemplateRecord.__init__(self, type)
                type = MyTemplateRecord()

    def test_CtorRaisesAnExceptionOnAnInvalidValue_InvalidType_Special(self):
        for type in [AnyValue()]:
            with self.assertRaises(InvalidTypeInCtor):
                class MyTemplateRecord(TemplateRecord):
                    def __init__(self):
                        TemplateRecord.__init__(self, type)
                type = MyTemplateRecord()

    def test_CtorRaisesAnExceptionOnAnInvalidValue_InvalidType_Template(self):
        for type in [TemplateType(Integer(SimpleType()))]:
            with self.assertRaises(InvalidTypeInCtor):
                class MyTemplateRecord(TemplateRecord):
                    def __init__(self):
                        TemplateRecord.__init__(self, type)
                type = MyTemplateRecord()

    def test_Ctor_ConvertsTypesToTemplateTypes_SimpleTypes(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': Charstring(SimpleType())})
        class MyTemplateRecord(TemplateRecord):
            def __init__(self):
                TemplateRecord.__init__(self, MyRecord())
        type = MyTemplateRecord()
        self.assertTrue(type.mDecoratedType.mDictionary['foo'].isOfType(Integer))
        self.assertTrue(type.mDecoratedType.mDictionary['foo'].isOfType(TemplateType))
        self.assertTrue(type.mDecoratedType.mDictionary['bar'].isOfType(Charstring))
        self.assertTrue(type.mDecoratedType.mDictionary['bar'].isOfType(TemplateType))

    def test_Ctor_ConvertsTypesToTemplateTypes_NestedRecord(self):
        class InternalRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': Charstring(SimpleType())})
        class ExternalRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': InternalRecord()})
        class MyTemplateRecord(TemplateRecord):
            def __init__(self):
                TemplateRecord.__init__(self, ExternalRecord())
        type = MyTemplateRecord()
        self.assertTrue(type.mDecoratedType.mDictionary['foo'].isOfType(Integer))
        self.assertTrue(type.mDecoratedType.mDictionary['foo'].isOfType(TemplateType))
        self.assertTrue(type.mDecoratedType.mDictionary['bar'].isOfType(Record))
        self.assertTrue(type.mDecoratedType.mDictionary['bar'].isOfType(InternalRecord))
        self.assertTrue(type.mDecoratedType.mDictionary['bar'].isOfType(TemplateRecord))
        self.assertTrue(type.mDecoratedType.mDictionary['bar'].mDecoratedType.mDictionary['foo'].isOfType(Integer))
        self.assertTrue(type.mDecoratedType.mDictionary['bar'].mDecoratedType.mDictionary['foo'].isOfType(TemplateType))
        self.assertTrue(type.mDecoratedType.mDictionary['bar'].mDecoratedType.mDictionary['bar'].isOfType(Charstring))
        self.assertTrue(type.mDecoratedType.mDictionary['bar'].mDecoratedType.mDictionary['bar'].isOfType(TemplateType))

    def test_Ctor_ConvertsTypesToTemplateTypes_RecordWithNestedRecordOf(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer(SimpleType()))
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': MyRecordOf()})
        class MyTemplateRecord(TemplateRecord):
            def __init__(self):
                TemplateRecord.__init__(self, MyRecord())
        myTemplateRecord = MyTemplateRecord()
        self.assertTrue(myTemplateRecord.mDecoratedType.mDictionary['foo'].isOfType(TemplateType))
        self.assertTrue(myTemplateRecord.mDecoratedType.mDictionary['foo'].isOfType(Integer))
        self.assertTrue(myTemplateRecord.mDecoratedType.mDictionary['bar'].isOfType(TemplateRecordOf))
        self.assertTrue(myTemplateRecord.mDecoratedType.mDictionary['bar'].isOfType(MyRecordOf))
        self.assertTrue(myTemplateRecord.mDecoratedType.mDictionary['bar'].isOfType(RecordOf))
        self.assertTrue(myTemplateRecord.mDecoratedType.mDictionary['bar'].mDecoratedType.mType.isOfType(TemplateType))
        self.assertTrue(myTemplateRecord.mDecoratedType.mDictionary['bar'].mDecoratedType.mType.isOfType(Integer))

class TypeSystem_Record_TemplateRecord_Accept(unittest.TestCase):
    def test_AcceptReturnsTrueOnAValidValue_TheSameTypes_WithoutSpecial(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': Charstring(SimpleType())})
        class MyTemplateRecord(TemplateRecord):
            def __init__(self):
                TemplateRecord.__init__(self, MyRecord())
        type = MyTemplateRecord()
        value = {'foo': Integer(SimpleType()).assign(IntegerValue(1)),
                 'bar': Charstring(SimpleType()).assign(CharstringValue("WAX"))}
        self.assertTrue(type.accept(value))

    def test_AcceptReturnsTrueOnAValidValue_TheSameTypes_WithSpecial(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': Charstring(SimpleType())})
        class MyTemplateRecord(TemplateRecord):
            def __init__(self):
                TemplateRecord.__init__(self, MyRecord())
        type = MyTemplateRecord()
        value = {'foo': Integer(SimpleType()).assign(IntegerValue(1)),
                 'bar': TemplateType(Charstring(SimpleType())).assign(AnyValue())}
        self.assertTrue(type.accept(value))

    def test_AcceptReturnsTrueOnAValidValue_CompatibleTypes(self):
        self.skipTest("Not implemented yet.")
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': Charstring(SimpleType())})
        class MyTemplateRecord(TemplateRecord):
            def __init__(self):
                TemplateRecord.__init__(self, MyRecord())
        type = MyTemplateRecord()
        value = {'foo': BoundedType(
                            Integer(SimpleType()),
                            IntegerValue(0),
                            IntegerValue(10)
                        ).assign(IntegerValue(1)),
                 'bar': TemplateType(Charstring(SimpleType())).assign(AnyValue())}
        self.assertTrue(type.accept(value))

    def test_AcceptReturnsTrueOnAValidValue_NestedRecords(self):
        class InternalRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': Charstring(SimpleType())})
        class ExternalRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': InternalRecord()})
        class MyTemplateRecord(TemplateRecord):
            def __init__(self):
                TemplateRecord.__init__(self, ExternalRecord())
        internalValue = {'foo': Integer(SimpleType()).assign(IntegerValue(1)),
                         'bar': Charstring(SimpleType()).assign(CharstringValue("WAX"))}
        externalValue = {'foo': TemplateType(Integer(SimpleType())).assign(AnyValue()),
                         'bar': internalValue}
        type = MyTemplateRecord()
        self.assertTrue(type.accept(externalValue))

    def test_AcceptReturnsTrueOnAValidValue_NestedRecords_Recursively(self):
        class InternalRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': Charstring(SimpleType())})
        class ExternalRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': InternalRecord()})
        class MyTemplateRecord(TemplateRecord):
            def __init__(self):
                TemplateRecord.__init__(self, ExternalRecord())
        internalValue = {'foo': TemplateType(Integer(SimpleType())).assign(AnyValue()),
                         'bar': Charstring(SimpleType()).assign(CharstringValue("WAX"))}
        externalValue = {'foo': TemplateType(Integer(SimpleType())).assign(AnyValue()),
                         'bar': internalValue}
        type = MyTemplateRecord()
        self.assertTrue(type.accept(externalValue))

    def test_AcceptReturnsTrueOnAValidValue_RecordWithNestedRecordOf_WithoutSpecial(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer(SimpleType()))
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': MyRecordOf()})
        class MyTemplateRecord(TemplateRecord):
            def __init__(self):
                TemplateRecord.__init__(self, MyRecord())
        myTemplateRecord = MyTemplateRecord()
        value = {'foo': Integer(SimpleType()).assign(IntegerValue(1)),
                 'bar': [Integer(SimpleType()).assign(IntegerValue(1)),
                         Integer(SimpleType()).assign(IntegerValue(1))]}
        self.assertTrue(myTemplateRecord.accept(value))

    def test_AcceptReturnsTrueOnAValidValue_RecordWithNestedRecordOf_WithSpecial(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer(SimpleType()))
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': MyRecordOf()})
        class MyTemplateRecord(TemplateRecord):
            def __init__(self):
                TemplateRecord.__init__(self, MyRecord())
        myTemplateRecord = MyTemplateRecord()
        value = {'foo': TemplateType(Integer(SimpleType())).assign(AnyValue()),
                 'bar': [Integer(SimpleType()).assign(IntegerValue(1)),
                         TemplateType(Integer(SimpleType())).assign(AnyValue())]}
        self.assertTrue(myTemplateRecord.accept(value))

    def test_AcceptReturnsFalseOnAnInvalidValue_InvalidType_BuiltIn(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': Charstring(SimpleType())})
        class MyTemplateRecord(TemplateRecord):
            def __init__(self):
                TemplateRecord.__init__(self, MyRecord())
        type = MyTemplateRecord()
        for value in [True, 1, 1.0, "WAX", [1, 2], (1, 2)]:
            self.assertFalse(type.accept(value))

    def test_AcceptReturnsFalseOnAnInvalidValue_InvalidType_Special(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': Charstring(SimpleType())})
        class MyTemplateRecord(TemplateRecord):
            def __init__(self):
                TemplateRecord.__init__(self, MyRecord())
        type = MyTemplateRecord()
        value = {'foo': Integer(SimpleType()).assign(IntegerValue(1)),
                 'bar': AnyValue()}
        self.assertFalse(type.accept(value))

    def test_AcceptReturnsFalseOnAnInvalidValue_IncompatibleDictionaries_AssignedEmpty(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': Charstring(SimpleType())})
        class MyTemplateRecord(TemplateRecord):
            def __init__(self):
                TemplateRecord.__init__(self, MyRecord())
        type = MyTemplateRecord()
        self.assertFalse(type.accept({}))

    def test_AcceptReturnsFalseOnAnInvalidValue_IncompatibleDictionaries_AssignedTooSmall(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': Charstring(SimpleType())})
        class MyTemplateRecord(TemplateRecord):
            def __init__(self):
                TemplateRecord.__init__(self, MyRecord())
        type = MyTemplateRecord()
        value = {'foo': Integer(SimpleType()).assign(IntegerValue(1))}
        self.assertFalse(type.accept(value))

    def test_AcceptReturnsFalseOnAnInvalidValue_IncompatibleDictionaries_AssignedTooBig(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': Charstring(SimpleType())})
        class MyTemplateRecord(TemplateRecord):
            def __init__(self):
                TemplateRecord.__init__(self, MyRecord())
        type = MyTemplateRecord()
        value = {'foo': Integer(SimpleType()).assign(IntegerValue(1)),
                 'bar': Charstring(SimpleType()).assign(CharstringValue("WAX")),
                 'baz': Integer(SimpleType()).assign(IntegerValue(2))}
        self.assertFalse(type.accept(value))

    def test_AcceptReturnsFalseOnAnInvalidValue_IncompatibleDictionaries_AssignedHasDifferentKeys(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': Charstring(SimpleType())})
        class MyTemplateRecord(TemplateRecord):
            def __init__(self):
                TemplateRecord.__init__(self, MyRecord())
        type = MyTemplateRecord()
        value = {'foo': Integer(SimpleType()).assign(IntegerValue(1)),
                 'baz': Charstring(SimpleType()).assign(CharstringValue("WAX"))}
        self.assertFalse(type.accept(value))

    def test_AcceptReturnsFalseOnAnInvalidValue_IncompatibleDictionaries_AssignedHasChangedKeys(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': Charstring(SimpleType())})
        class MyTemplateRecord(TemplateRecord):
            def __init__(self):
                TemplateRecord.__init__(self, MyRecord())
        type = MyTemplateRecord()
        value = {'bar': Integer(SimpleType()).assign(IntegerValue(1)),
                 'foo': Charstring(SimpleType()).assign(CharstringValue("WAX"))}
        self.assertFalse(type.accept(value))

class TypeSystem_Record_TemplateRecord_Assign(unittest.TestCase):
    def test_AssignAssignsOnAValidValue_TheSameTypes_WithoutSpecial(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': Charstring(SimpleType())})
        class MyTemplateRecord(TemplateRecord):
            def __init__(self):
                TemplateRecord.__init__(self, MyRecord())
        type = MyTemplateRecord()
        value = {'foo': Integer(SimpleType()).assign(IntegerValue(1)),
                 'bar': Charstring(SimpleType()).assign(CharstringValue("WAX"))}
        type.assign(value)

    def test_AssignAssignsOnAValidValue_TheSameTypes_WithSpecial(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': Charstring(SimpleType())})
        class MyTemplateRecord(TemplateRecord):
            def __init__(self):
                TemplateRecord.__init__(self, MyRecord())
        type = MyTemplateRecord()
        value = {'foo': Integer(SimpleType()).assign(IntegerValue(1)),
                 'bar': TemplateType(Charstring(SimpleType())).assign(AnyValue())}
        type.assign(value)

    def test_AssignAssignsOnAValidValue_CompatibleTypes(self):
        self.skipTest("Not implemented yet.")
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': Charstring(SimpleType())})
        class MyTemplateRecord(TemplateRecord):
            def __init__(self):
                TemplateRecord.__init__(self, MyRecord())
        type = MyTemplateRecord()
        value = {'foo': BoundedType(
                            Integer(SimpleType()),
                            IntegerValue(0),
                            IntegerValue(10)
                        ).assign(IntegerValue(1)),
                 'bar': TemplateType(Charstring(SimpleType())).assign(AnyValue())}
        type.assign(value)

    def test_AssignAssignsOnAValidValue_NestedRecords(self):
        class InternalRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': Charstring(SimpleType())})
        class ExternalRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': InternalRecord()})
        class MyTemplateRecord(TemplateRecord):
            def __init__(self):
                TemplateRecord.__init__(self, ExternalRecord())
        internalValue = {'foo': Integer(SimpleType()).assign(IntegerValue(1)),
                         'bar': Charstring(SimpleType()).assign(CharstringValue("WAX"))}
        externalValue = {'foo': TemplateType(Integer(SimpleType())).assign(AnyValue()),
                         'bar': internalValue}
        type = MyTemplateRecord()
        type.assign(externalValue)

    def test_AssignAssignsOnAValidValue_NestedRecords_Recursively(self):
        class InternalRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': Charstring(SimpleType())})
        class ExternalRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': InternalRecord()})
        class MyTemplateRecord(TemplateRecord):
            def __init__(self):
                TemplateRecord.__init__(self, ExternalRecord())
        internalValue = {'foo': TemplateType(Integer(SimpleType())).assign(AnyValue()),
                         'bar': Charstring(SimpleType()).assign(CharstringValue("WAX"))}
        externalValue = {'foo': TemplateType(Integer(SimpleType())).assign(AnyValue()),
                         'bar': internalValue}
        type = MyTemplateRecord()
        type.assign(externalValue)

    def test_AssignRaisesAnExceptionOnAnInvalidValue_InvalidType_BuiltIn(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': Charstring(SimpleType())})
        class MyTemplateRecord(TemplateRecord):
            def __init__(self):
                TemplateRecord.__init__(self, MyRecord())
        type = MyTemplateRecord()
        for value in [True, 1, 1.0, "WAX", [1, 2], (1, 2)]:
            with self.assertRaises(InvalidTypeInAssignment):
                type.assign(value)

    def test_AssignRaisesAnExceptionOnAnInvalidValue_InvalidType_Special(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': Charstring(SimpleType())})
        class MyTemplateRecord(TemplateRecord):
            def __init__(self):
                TemplateRecord.__init__(self, MyRecord())
        type = MyTemplateRecord()
        value = {'foo': Integer(SimpleType()).assign(IntegerValue(1)),
                 'bar': AnyValue()}
        with self.assertRaises(InvalidTypeInAssignment):
            type.assign(value)

    def test_AssignRaisesAnExceptionOnAnInvalidValue_IncompatibleDictionaries_AssignedEmpty(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': Charstring(SimpleType())})
        class MyTemplateRecord(TemplateRecord):
            def __init__(self):
                TemplateRecord.__init__(self, MyRecord())
        type = MyTemplateRecord()
        with self.assertRaises(InvalidTypeInAssignment):
            type.assign({})

    def test_AssignRaisesAnExceptionOnAnInvalidValue_IncompatibleDictionaries_AssignedTooSmall(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': Charstring(SimpleType())})
        class MyTemplateRecord(TemplateRecord):
            def __init__(self):
                TemplateRecord.__init__(self, MyRecord())
        type = MyTemplateRecord()
        value = {'foo': Integer(SimpleType()).assign(IntegerValue(1))}
        with self.assertRaises(InvalidTypeInAssignment):
            type.assign(value)

    def test_AssignRaisesAnExceptionOnAnInvalidValue_IncompatibleDictionaries_AssignedTooBig(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': Charstring(SimpleType())})
        class MyTemplateRecord(TemplateRecord):
            def __init__(self):
                TemplateRecord.__init__(self, MyRecord())
        type = MyTemplateRecord()
        value = {'foo': Integer(SimpleType()).assign(IntegerValue(1)),
                 'bar': Charstring(SimpleType()).assign(CharstringValue("WAX")),
                 'baz': Integer(SimpleType()).assign(IntegerValue(2))}
        with self.assertRaises(InvalidTypeInAssignment):
            type.assign(value)

    def test_AssignRaisesAnExceptionOnAnInvalidValue_IncompatibleDictionaries_AssignedHasDifferentKeys(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': Charstring(SimpleType())})
        class MyTemplateRecord(TemplateRecord):
            def __init__(self):
                TemplateRecord.__init__(self, MyRecord())
        type = MyTemplateRecord()
        value = {'foo': Integer(SimpleType()).assign(IntegerValue(1)),
                 'baz': Charstring(SimpleType()).assign(CharstringValue("WAX"))}
        with self.assertRaises(InvalidTypeInAssignment):
            type.assign(value)

    def test_AssignRaisesAnExceptionOnAnInvalidValue_IncompatibleDictionaries_AssignedHasChangedKeys(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': Charstring(SimpleType())})
        class MyTemplateRecord(TemplateRecord):
            def __init__(self):
                TemplateRecord.__init__(self, MyRecord())
        type = MyTemplateRecord()
        value = {'bar': Integer(SimpleType()).assign(IntegerValue(1)),
                 'foo': Charstring(SimpleType()).assign(CharstringValue("WAX"))}
        with self.assertRaises(InvalidTypeInAssignment):
            type.assign(value)

class TypeSystem_Record_TemplateRecord_Eq(unittest.TestCase):
    def test_EqReturnsTrueOnSameValues_EmptyRecord(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {})
        class MyTemplateRecord(TemplateRecord):
            def __init__(self):
                TemplateRecord.__init__(self, MyRecord())
        record1 = MyTemplateRecord().assign({})
        record2 = MyTemplateRecord().assign({})
        self.assertTrue(record1 == record2)
        self.assertTrue(record2 == record1)

    def test_EqReturnsTrueOnSameValues_NonEmptyRecord(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': Charstring(SimpleType())})
        class MyTemplateRecord(TemplateRecord):
            def __init__(self):
                TemplateRecord.__init__(self, MyRecord())
        value = {'foo': Integer(SimpleType()).assign(IntegerValue(1)),
                 'bar': Charstring(SimpleType()).assign(CharstringValue("WAX"))}
        record1 = MyTemplateRecord().assign(value)
        record2 = MyTemplateRecord().assign(value)
        self.assertTrue(record1 == record2)
        self.assertTrue(record2 == record1)

    def test_EqReturnsTrueOnSameValues_NonEmptyRecord_WithSpecialValues(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': Charstring(SimpleType())})
        class MyTemplateRecord(TemplateRecord):
            def __init__(self):
                TemplateRecord.__init__(self, MyRecord())
        value1 = {'foo': TemplateType(Integer(SimpleType())).assign(AnyValue()),
                  'bar': Charstring(SimpleType()).assign(CharstringValue("WAX"))}
        value2 = {'foo': Integer(SimpleType()).assign(IntegerValue(1)),
                  'bar': Charstring(SimpleType()).assign(CharstringValue("WAX"))}
        record1 = MyTemplateRecord().assign(value1)
        record2 = MyTemplateRecord().assign(value2)
        self.assertTrue(record1 == record2)
        with self.assertRaises(InvalidTypeInComparison):
            record2 == record1

    # TODO: Moar!

    def test_EqReturnsTrueOnSameValues_NestedRecords(self):
        class InternalRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': Charstring(SimpleType())})
        class ExternalRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': InternalRecord()})
        class MyTemplateRecord(TemplateRecord):
            def __init__(self):
                TemplateRecord.__init__(self, ExternalRecord())
        internalValue = {'foo': Integer(SimpleType()).assign(IntegerValue(1)),
                         'bar': Charstring(SimpleType()).assign(CharstringValue("WAX"))}
        externalValue = {'foo': TemplateType(Integer(SimpleType())).assign(AnyValue()),
                         'bar': internalValue}
        record1 = MyTemplateRecord()
        record2 = MyTemplateRecord()
        record1.assign(externalValue)
        record2.assign(externalValue)
        self.assertTrue(record1 == record2)
        self.assertTrue(record2 == record1)

    # TODO: Moar!

    def test_EqReturnsFalseOnDifferentValues_NonEmptyRecord(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': Charstring(SimpleType())})
        class MyTemplateRecord(TemplateRecord):
            def __init__(self):
                TemplateRecord.__init__(self, MyRecord())
        type = MyTemplateRecord()
        value1 = {'foo': Integer(SimpleType()).assign(IntegerValue(1)),
                  'bar': Charstring(SimpleType()).assign(CharstringValue("WAX"))}
        value2 = {'foo': Integer(SimpleType()).assign(IntegerValue(1)),
                  'bar': Charstring(SimpleType()).assign(CharstringValue("WAS"))}
        record1 = MyTemplateRecord().assign(value1)
        record2 = MyTemplateRecord().assign(value2)
        self.assertFalse(record1 == record2)
        self.assertFalse(record2 == record1)

    def test_EqReturnsFalseOnDifferentValues_NestedRecords(self):
        class InternalRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': Charstring(SimpleType())})
        class ExternalRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': InternalRecord()})
        class MyTemplateRecord(TemplateRecord):
            def __init__(self):
                TemplateRecord.__init__(self, ExternalRecord())
        internalValue1 = {'foo': Integer(SimpleType()).assign(IntegerValue(1)),
                          'bar': Charstring(SimpleType()).assign(CharstringValue("WAX"))}
        internalValue2 = {'foo': Integer(SimpleType()).assign(IntegerValue(1)),
                          'bar': Charstring(SimpleType()).assign(CharstringValue("WAS"))}
        externalValue1 = {'foo': TemplateType(Integer(SimpleType())).assign(AnyValue()),
                          'bar': internalValue1}
        externalValue2 = {'foo': TemplateType(Integer(SimpleType())).assign(AnyValue()),
                          'bar': internalValue2}
        record1 = MyTemplateRecord()
        record2 = MyTemplateRecord()
        record1.assign(externalValue1)
        record2.assign(externalValue2)
        self.assertFalse(record1 == record2)
        self.assertFalse(record2 == record1)

    def test_EqRaisesAnExceptionOnAnInvalidValue_InvalidType_DifferentType(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': Charstring(SimpleType())})
        class MyTemplateRecord1(TemplateRecord):
            def __init__(self):
                TemplateRecord.__init__(self, MyRecord())
        class MyTemplateRecord2(TemplateRecord):
            def __init__(self):
                TemplateRecord.__init__(self, MyRecord())
        value1 = {'foo': Integer(SimpleType()).assign(IntegerValue(1)),
                  'bar': Charstring(SimpleType()).assign(CharstringValue("WAX"))}
        value2 = {'foo': Integer(SimpleType()).assign(IntegerValue(1)),
                  'bar': Charstring(SimpleType()).assign(CharstringValue("WAX"))}
        record1 = MyTemplateRecord1().assign(value1)
        record2 = MyTemplateRecord2().assign(value2)
        with self.assertRaises(InvalidTypeInComparison):
            record1 == record2

class TypeSystem_Record_TemplateRecord_GetField(unittest.TestCase):
    def test_GetFieldReturnsTheValueOfTheFieldOnAValidField(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': Charstring(SimpleType())})
        class MyTemplateRecord(TemplateRecord):
            def __init__(self):
                TemplateRecord.__init__(self, MyRecord())
        value = {'foo': Integer(SimpleType()).assign(IntegerValue(1)),
                 'bar': Charstring(SimpleType()).assign(CharstringValue("WAX"))}
        type = MyTemplateRecord().assign(value)
        self.assertEqual(type.getField('foo'), Integer(SimpleType()).assign(IntegerValue(1)))
        self.assertEqual(type.getField('bar'), Charstring(SimpleType()).assign(CharstringValue("WAX")))

    def test_GetFieldRaisesAnExceptionOnAnInvalidField(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': Charstring(SimpleType())})
        class MyTemplateRecord(TemplateRecord):
            def __init__(self):
                TemplateRecord.__init__(self, MyRecord())
        value = {'foo': Integer(SimpleType()).assign(IntegerValue(1)),
                 'bar': Charstring(SimpleType()).assign(CharstringValue("WAX"))}
        type = MyTemplateRecord().assign(value)
        with self.assertRaises(LookupErrorMissingField):
            type.getField('baz')

class TypeSystem_RecordOf_Ctor(unittest.TestCase):
    def test_Ctor(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer(SimpleType()))
        type = MyRecordOf()

    def test_CtorRaisesAnExceptionOnAnInvalidValue_InvalidType_BuiltIn(self):
        for type in [bool, int, float, str, dict, list, tuple]:
            with self.assertRaises(InvalidTypeInCtor):
                class MyRecordOf(RecordOf):
                    def __init__(self):
                        RecordOf.__init__(self, SimpleType(), type)
                type = MyRecordOf()

    def test_CtorRaisesAnExceptionOnAnInvalidValue_InvalidType_Special(self):
        for type in [AnyValue]:
            with self.assertRaises(InvalidTypeInCtor):
                class MyRecordOf(RecordOf):
                    def __init__(self):
                        RecordOf.__init__(self, SimpleType(), type)
                type = MyRecordOf()

    def test_CtorRaisesAnExceptionOnAnInvalidValue_InvalidType_Template(self):
        for type in [TemplateType]:
            with self.assertRaises(InvalidTypeInCtor):
                class MyRecordOf(RecordOf):
                    def __init__(self):
                        RecordOf.__init__(self, SimpleType(), type)
                type = MyRecordOf()

class TypeSystem_RecordOf_Accept(unittest.TestCase):
    def test_AcceptReturnsTrueOnAValidValue_TheSameTypes_AnEmptyList(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer(SimpleType()))
        type = MyRecordOf()
        value = []
        self.assertTrue(type.accept(value))

    def test_AcceptReturnsTrueOnAValidValue_TheSameTypes_ASingleElementList(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer(SimpleType()))
        type = MyRecordOf()
        value = [Integer(SimpleType()).assign(IntegerValue(1))]
        self.assertTrue(type.accept(value))

    def test_AcceptReturnsTrueOnAValidValue_TheSameTypes_AManyElementsList(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer(SimpleType()))
        type = MyRecordOf()
        value = [Integer(SimpleType()).assign(IntegerValue(1)), Integer(SimpleType()).assign(IntegerValue(2))]
        self.assertTrue(type.accept(value))

    def test_AcceptReturnsFalseOnAnInvalidValue_InvalidType_BuiltIn(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer(SimpleType()))
        type = MyRecordOf()
        for value in [True, 1, 1.0, "WAX", [1, 2], (1, 2)]:
            self.assertFalse(type.accept(value))

    def test_AcceptReturnsFalseOnAnInvalidValue_InvalidType_Special(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer(SimpleType()))
        type = MyRecordOf()
        for value in [[AnyValue()]]:
            self.assertFalse(type.accept(value))

    def test_AcceptReturnsFalseOnAnInvalidValue_InvalidType_Template(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer(SimpleType()))
        type = MyRecordOf()
        for value in [[TemplateType(Integer(SimpleType())).assign(IntegerValue(1)),
                       TemplateType(Integer(SimpleType())).assign(AnyValue())]]:
            self.assertFalse(type.accept(value))

    def test_AcceptReturnsFalseOnAnInvalidValue_InvalidType_OtherType(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer(SimpleType()))
        type = MyRecordOf()
        for value in [[Float(SimpleType()).assign(FloatValue(1.0))]]:
            self.assertFalse(type.accept(value))

    def test_AcceptReturnsFalseOnAnInvalidValue_InvalidValue_AnyOfValuesIsATemplateLikeType(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer(SimpleType()))
        type = MyRecordOf()
        value = [Integer(SimpleType()).assign(IntegerValue(1)),
                 TemplateType(Integer(SimpleType()).assign(IntegerValue(2)))]
        self.assertFalse(type.accept(value))

class TypeSystem_RecordOf_Assign(unittest.TestCase):
    def test_AssignAssignsOnAValidValue_TheSameTypes_AnEmptyList(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer(SimpleType()))
        type = MyRecordOf()
        value = []
        type.assign(value)

    def test_AssignAssignsOnAValidValue_TheSameTypes_ASingleElementList(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer(SimpleType()))
        type = MyRecordOf()
        value = [Integer(SimpleType()).assign(IntegerValue(1))]
        type.assign(value)

    def test_AssignAssignsOnAValidValue_TheSameTypes_AManyElementsList(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer(SimpleType()))
        type = MyRecordOf()
        value = [Integer(SimpleType()).assign(IntegerValue(1)), Integer(SimpleType()).assign(IntegerValue(2))]
        type.assign(value)

    def test_AssignAssignsOnAValidValue_RecordOfWithNestedRecord(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': Charstring(SimpleType())})
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), MyRecord())
        type = MyRecordOf()
        value = [
            {'foo': Integer(SimpleType()).assign(IntegerValue(1)),
             'bar': Charstring(SimpleType()).assign(CharstringValue("WAX"))},
            {'foo': Integer(SimpleType()).assign(IntegerValue(2)),
             'bar': Charstring(SimpleType()).assign(CharstringValue("WAS"))}
        ]
        type.assign(value)
        self.assertTrue(type.getField(0).getField('foo') == Integer(SimpleType()).assign(IntegerValue(1)))
        self.assertTrue(type.getField(0).getField('bar') == Charstring(SimpleType()).assign(CharstringValue("WAX")))
        self.assertTrue(type.getField(1).getField('foo') == Integer(SimpleType()).assign(IntegerValue(2)))
        self.assertTrue(type.getField(1).getField('bar') == Charstring(SimpleType()).assign(CharstringValue("WAS")))

    def test_AssignRaisesAnExceptionOnAnInvalidValue_InvalidType_BuiltIn(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer(SimpleType()))
        type = MyRecordOf()
        for value in [True, 1, 1.0, "WAX", [1, 2], (1, 2)]:
            with self.assertRaises(InvalidTypeInAssignment):
                type.assign(value)

    def test_AssignRaisesAnExceptionOnAnInvalidValue_InvalidType_Special(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer(SimpleType()))
        type = MyRecordOf()
        for value in [[AnyValue()]]:
            with self.assertRaises(InvalidTypeInAssignment):
                type.assign(value)

    def test_AssignRaisesAnExceptionOnAnInvalidValue_InvalidType_Template(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer(SimpleType()))
        type = MyRecordOf()
        for value in [[TemplateType(Integer(SimpleType()))]]:
            with self.assertRaises(InvalidTypeInAssignment):
                type.assign(value)

    def test_AssignRaisesAnExceptionOnAnInvalidValue_InvalidType_OtherType(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer(SimpleType()))
        type = MyRecordOf()
        for value in [[Float(SimpleType()).assign(FloatValue(1.0))]]:
            with self.assertRaises(InvalidTypeInAssignment):
                type.assign(value)

    def test_AssignRaisesAnExceptionOnAnInvalidValue_InvalidValue_AnyOfValuesIsATemplateLikeType(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer(SimpleType()))
        type = MyRecordOf()
        value = [Integer(SimpleType()).assign(IntegerValue(1)),
                 TemplateType(Integer(SimpleType()).assign(IntegerValue(2)))]
        with self.assertRaises(InvalidTypeInAssignment):
            type.assign(value)

class TypeSystem_RecordOF_Eq(unittest.TestCase):
    def test_EqReturnsTrueOnSameValues_EmptyRecordOf(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer(SimpleType()))
        record1 = MyRecordOf().assign([])
        record2 = MyRecordOf().assign([])
        self.assertTrue(record1 == record2)

    def test_EqReturnsTrueOnSameValues_OneElement(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer(SimpleType()))
        record1 = MyRecordOf().assign([Integer(SimpleType()).assign(IntegerValue(1))])
        record2 = MyRecordOf().assign([Integer(SimpleType()).assign(IntegerValue(1))])
        self.assertTrue(record1 == record2)

    def test_EqReturnsTrueOnSameValues_ManyElements(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer(SimpleType()))
        record1 = MyRecordOf().assign([Integer(SimpleType()).assign(IntegerValue(1)),
                                       Integer(SimpleType()).assign(IntegerValue(2)),
                                       Integer(SimpleType()).assign(IntegerValue(3))])
        record2 = MyRecordOf().assign([Integer(SimpleType()).assign(IntegerValue(1)),
                                       Integer(SimpleType()).assign(IntegerValue(2)),
                                       Integer(SimpleType()).assign(IntegerValue(3))])
        self.assertTrue(record1 == record2)

    def test_EqReturnsFalseOnDifferentValues_OneElement(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer(SimpleType()))
        record1 = MyRecordOf().assign([Integer(SimpleType()).assign(IntegerValue(1))])
        record2 = MyRecordOf().assign([Integer(SimpleType()).assign(IntegerValue(2))])
        self.assertFalse(record1 == record2)

    def test_EqReturnsFalseOnDifferentValues_ManyElements(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer(SimpleType()))
        record1 = MyRecordOf().assign([Integer(SimpleType()).assign(IntegerValue(1)),
                                       Integer(SimpleType()).assign(IntegerValue(2)),
                                       Integer(SimpleType()).assign(IntegerValue(3))])
        record2 = MyRecordOf().assign([Integer(SimpleType()).assign(IntegerValue(1)),
                                       Integer(SimpleType()).assign(IntegerValue(3)),
                                       Integer(SimpleType()).assign(IntegerValue(3))])
        self.assertFalse(record1 == record2)

    def test_EqReturnsFalseOnDifferentValues_DiffentSize_SmallerBigger(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer(SimpleType()))
        record1 = MyRecordOf().assign([Integer(SimpleType()).assign(IntegerValue(1)),
                                       Integer(SimpleType()).assign(IntegerValue(2))])
        record2 = MyRecordOf().assign([Integer(SimpleType()).assign(IntegerValue(1)),
                                       Integer(SimpleType()).assign(IntegerValue(2)),
                                       Integer(SimpleType()).assign(IntegerValue(3))])
        self.assertFalse(record1 == record2)

    def test_EqReturnsFalseOnDifferentValues_DiffentSize_BiggerSmaller(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer(SimpleType()))
        record1 = MyRecordOf().assign([Integer(SimpleType()).assign(IntegerValue(1)),
                                       Integer(SimpleType()).assign(IntegerValue(2)),
                                       Integer(SimpleType()).assign(IntegerValue(3))])
        record2 = MyRecordOf().assign([Integer(SimpleType()).assign(IntegerValue(1)),
                                       Integer(SimpleType()).assign(IntegerValue(2))])
        self.assertFalse(record1 == record2)

    def test_EqReturnsFalseOnDifferentValues_SequenceMatters(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer(SimpleType()))
        record1 = MyRecordOf().assign([Integer(SimpleType()).assign(IntegerValue(1)),
                                       Integer(SimpleType()).assign(IntegerValue(2)),
                                       Integer(SimpleType()).assign(IntegerValue(3))])
        record2 = MyRecordOf().assign([Integer(SimpleType()).assign(IntegerValue(1)),
                                       Integer(SimpleType()).assign(IntegerValue(3)),
                                       Integer(SimpleType()).assign(IntegerValue(2))])
        self.assertFalse(record1 == record2)

    def test_EqRaisesAnExceptionOnAnInvalidValue_InvalidType_BuiltIn(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer(SimpleType()))
        record = MyRecordOf().assign([Integer(SimpleType()).assign(IntegerValue(1))])
        for value in [True, 1, 1.0, "WAX", [1, 2], (1, 2)]:
            with self.assertRaises(InvalidTypeInComparison):
                record == value

    def test_EqRaisesAnExceptionOnAnInvalidValue_InvalidType_Special(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer(SimpleType()))
        record = MyRecordOf().assign([Integer(SimpleType()).assign(IntegerValue(1))])
        for value in [AnyValue()]:
            with self.assertRaises(InvalidTypeInComparison):
                record == value

    def test_EqRaisesAnExceptionOnAnInvalidValue_InvalidType_Template(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer(SimpleType()))
        record = MyRecordOf().assign([Integer(SimpleType()).assign(IntegerValue(1))])
        for value in [TemplateType(Integer(SimpleType())).assign(IntegerValue(1))]:
            with self.assertRaises(InvalidTypeInComparison):
                record == value

    def test_EqRaisesAnExceptionOnAnInvalidValue_InvalidType_DifferentType(self):
        class MyRecordOf1(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer(SimpleType()))
        class MyRecordOf2(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer(SimpleType()))
        record1 = MyRecordOf1().assign([Integer(SimpleType()).assign(IntegerValue(1))])
        record2 = MyRecordOf2().assign([Integer(SimpleType()).assign(IntegerValue(1))])
        with self.assertRaises(InvalidTypeInComparison):
            record1 == record2

class TypeSystem_RecordOf_GetField(unittest.TestCase):
    def test_GetFieldReturnsTheValueOfTheFieldOnAValidField(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer(SimpleType()))
        record = MyRecordOf().assign([Integer(SimpleType()).assign(IntegerValue(1)),
                                      Integer(SimpleType()).assign(IntegerValue(2)),
                                      Integer(SimpleType()).assign(IntegerValue(3))])
        self.assertEqual(record.getField(1), Integer(SimpleType()).assign(IntegerValue(2)))

    def test_GetFieldRaisesAnExceptionOnAnInvalidField(self):
        with self.assertRaises(LookupErrorMissingField):
            class MyRecordOf(RecordOf):
                def __init__(self):
                    RecordOf.__init__(self, SimpleType(), Integer(SimpleType()))
            record = MyRecordOf().assign([Integer(SimpleType()).assign(IntegerValue(1)),
                                          Integer(SimpleType()).assign(IntegerValue(2)),
                                          Integer(SimpleType()).assign(IntegerValue(3))])
            record.getField(4)

class TypeSystem_RecordOf_TemplateRecordOf_Ctor(unittest.TestCase):
    def test_Ctor(self):
        for type in [Boolean(SimpleType()), Integer(SimpleType()), Float(SimpleType()), Charstring(SimpleType())]:
            class MyRecordOf(RecordOf):
                def __init__(self):
                    RecordOf.__init__(self, SimpleType(), type)
            class MyTemplateRecordOf(TemplateRecordOf):
                def __init__(self):
                    TemplateRecordOf.__init__(self, MyRecordOf())
            type = MyTemplateRecordOf()

    def test_CtorRaisesAnExceptionOnAnInvalidValue_DoubleWrap(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer(SimpleType()))
        class MyTemplateRecordOf1(TemplateRecordOf):
            def __init__(self):
                TemplateRecordOf.__init__(self, MyRecordOf())
        class MyTemplateRecordOf2(TemplateRecordOf):
            def __init__(self):
                TemplateRecordOf.__init__(self, MyTemplateRecordOf1())
        with self.assertRaises(InvalidTypeInCtor):
            type = MyTemplateRecordOf2()

    def test_CtorRaisesAnExceptionOnAnInvalidValue_InvalidType_BuiltIn(self):
        for type in [True, 1, 1.0, "WAX", [1, 2], (1, 2)]:
            with self.assertRaises(InvalidTypeInCtor):
                class MyRecordOf(RecordOf):
                    def __init__(self):
                        RecordOf.__init__(self, SimpleType(), type)
                class MyTemplateRecordOf(TemplateRecordOf):
                    def __init__(self):
                        TemplateRecordOf.__init__(self, MyRecordOf())
                type = MyTemplateRecordOf()

    def test_CtorRaisesAnExceptionOnAnInvalidValue_InvalidType_Special(self):
        for type in [AnyValue()]:
            with self.assertRaises(InvalidTypeInCtor):
                class MyRecordOf(RecordOf):
                    def __init__(self):
                        RecordOf.__init__(self, SimpleType(), type)
                class MyTemplateRecordOf(TemplateRecordOf):
                    def __init__(self):
                        TemplateRecordOf.__init__(self, MyRecordOf())
                type = MyTemplateRecordOf()

    def test_CtorRaisesAnExceptionOnAnInvalidValue_InvalidType_Template(self):
        with self.assertRaises(InvalidTypeInCtor):
            for type in [TemplateType(Integer(SimpleType))]:
                class MyRecordOf(RecordOf):
                    def __init__(self):
                        RecordOf.__init__(self, SimpleType(), type)
                class MyTemplateRecordOf(MyRecordOf):
                    def __init__(self):
                        MyRecordOf.__init__(self)
                type = MyTemplateRecordOf()

    def test_Ctor_ConvertsTypesToTemplateTypes_SimpleTypes(self):
        for type in [Boolean(SimpleType()), Integer(SimpleType()), Float(SimpleType()), Charstring(SimpleType())]:
            class MyRecordOf(RecordOf):
                def __init__(self):
                    RecordOf.__init__(self, SimpleType(), type)
            class MyTemplateRecordOf(TemplateRecordOf):
                def __init__(self):
                    TemplateRecordOf.__init__(self, MyRecordOf())
            type = MyTemplateRecordOf()
            self.assertTrue(type.mDecoratedType.mType.isOfType(TemplateType))

    def test_Ctor_ConvertsTypesToTemplateTypes_NestedRecordsOf(self):
        class MyInnerRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer(SimpleType()))
        class MyOuterRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), MyInnerRecordOf())
        class MyTemplateRecordOf(TemplateRecordOf):
            def __init__(self):
                TemplateRecordOf.__init__(self, MyOuterRecordOf())
        type = MyTemplateRecordOf()
        self.assertTrue(type.mDecoratedType.mType.isOfType(TemplateRecordOf))
        self.assertTrue(type.mDecoratedType.mType.mDecoratedType.mType.isOfType(TemplateType))

class TypeSystem_RecordOf_TemplateRecordOf_Accept(unittest.TestCase):
    def test_AcceptReturnsTrueOnAValidValue_TheSameTypes_AnEmptyList(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer(SimpleType()))
        class MyTemplateRecordOf(TemplateRecordOf):
            def __init__(self):
                TemplateRecordOf.__init__(self, MyRecordOf())
        type = MyTemplateRecordOf()
        value = []
        self.assertTrue(type.accept(value))

    def test_AcceptReturnsTrueOnAValidValue_TheSameTypes_ASingleElementList(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer(SimpleType()))
        class MyTemplateRecordOf(TemplateRecordOf):
            def __init__(self):
                TemplateRecordOf.__init__(self, MyRecordOf())
        type = MyTemplateRecordOf()
        value = [Integer(SimpleType()).assign(IntegerValue(1))]
        self.assertTrue(type.accept(value))

    def test_AcceptReturnsTrueOnAValidValue_TheSameTypes_AManyElementsList(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer(SimpleType()))
        class MyTemplateRecordOf(TemplateRecordOf):
            def __init__(self):
                TemplateRecordOf.__init__(self, MyRecordOf())
        type = MyTemplateRecordOf()
        value = [Integer(SimpleType()).assign(IntegerValue(1)), Integer(SimpleType()).assign(IntegerValue(2))]
        self.assertTrue(type.accept(value))

    def test_AcceptReturnsTrueOnAValidValue_TheSameTypes_Template(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer(SimpleType()))
        class MyTemplateRecordOf(TemplateRecordOf):
            def __init__(self):
                TemplateRecordOf.__init__(self, MyRecordOf())
        type = MyTemplateRecordOf()
        for value in [[TemplateType(Integer(SimpleType())).assign(IntegerValue(1))]]:
            self.assertTrue(type.accept(value))

    def test_AcceptReturnsTrueOnAValidValue_TheSameTypes_AnyOfValuesIsATemplateLikeType(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer(SimpleType()))
        class MyTemplateRecordOf(TemplateRecordOf):
            def __init__(self):
                TemplateRecordOf.__init__(self, MyRecordOf())
        type = MyTemplateRecordOf()
        value = [Integer(SimpleType()).assign(IntegerValue(1)),
                 TemplateType(Integer(SimpleType()).assign(IntegerValue(2)))]
        self.assertTrue(type.accept(value))

    def test_AcceptReturnsFalseOnAnInvalidValue_InvalidType_BuiltIn(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer(SimpleType()))
        class MyTemplateRecordOf(TemplateRecordOf):
            def __init__(self):
                TemplateRecordOf.__init__(self, MyRecordOf())
        type = MyTemplateRecordOf()
        for value in [True, 1, 1.0, "WAX", [1, 2], (1, 2)]:
            self.assertFalse(type.accept(value))

    def test_AcceptReturnsFalseOnAnInvalidValue_InvalidType_Special(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer(SimpleType()))
        class MyTemplateRecordOf(TemplateRecordOf):
            def __init__(self):
                TemplateRecordOf.__init__(self, MyRecordOf())
        type = MyTemplateRecordOf()
        for value in [[AnyValue()]]:
            self.assertFalse(type.accept(value))

    def test_AcceptReturnsFalseOnAnInvalidValue_InvalidType_OtherType(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer(SimpleType()))
        class MyTemplateRecordOf(TemplateRecordOf):
            def __init__(self):
                TemplateRecordOf.__init__(self, MyRecordOf())
        type = MyTemplateRecordOf()
        for value in [[Float(SimpleType()).assign(FloatValue(1.0))]]:
            self.assertFalse(type.accept(value))

class TypeSystem_RecordOf_TemplateRecordOf_Assign(unittest.TestCase):
    def test_AssignAssignsOnAValidValue_TheSameTypes_AnEmptyList(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer(SimpleType()))
        class MyTemplateRecordOf(TemplateRecordOf):
            def __init__(self):
                TemplateRecordOf.__init__(self, MyRecordOf())
        type = MyTemplateRecordOf()
        value = []
        type.assign(value)

    def test_AssignAssignsOnAValidValue_TheSameTypes_ASingleElementList(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer(SimpleType()))
        class MyTemplateRecordOf(TemplateRecordOf):
            def __init__(self):
                TemplateRecordOf.__init__(self, MyRecordOf())
        type = MyTemplateRecordOf()
        value = [Integer(SimpleType()).assign(IntegerValue(1))]
        type.assign(value)

    def test_AssignAssignsOnAValidValue_TheSameTypes_AManyElementsList(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer(SimpleType()))
        class MyTemplateRecordOf(TemplateRecordOf):
            def __init__(self):
                TemplateRecordOf.__init__(self, MyRecordOf())
        type = MyTemplateRecordOf()
        value = [Integer(SimpleType()).assign(IntegerValue(1)), Integer(SimpleType()).assign(IntegerValue(2))]
        type.assign(value)

    def test_AssignAssignsOnAValidValue_TheSameTypes_Template(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer(SimpleType()))
        class MyTemplateRecordOf(TemplateRecordOf):
            def __init__(self):
                TemplateRecordOf.__init__(self, MyRecordOf())
        type = MyTemplateRecordOf()
        for value in [[TemplateType(Integer(SimpleType())).assign(IntegerValue(1))],
                      [TemplateType(Integer(SimpleType())).assign(AnyValue())]]:
            type.assign(value)

    def test_AssignAssignsOnAValidValue_TheSameTypes_AnyOfValuesIsATemplateLikeType(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer(SimpleType()))
        class MyTemplateRecordOf(TemplateRecordOf):
            def __init__(self):
                TemplateRecordOf.__init__(self, MyRecordOf())
        type = MyTemplateRecordOf()
        value = [Integer(SimpleType()).assign(IntegerValue(1)),
                 TemplateType(Integer(SimpleType()).assign(IntegerValue(2)))]
        type.assign(value)

    def test_AssignRaisesAnExceptionOnAnInvalidValue_InvalidType_BuiltIn(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer(SimpleType()))
        class MyTemplateRecordOf(TemplateRecordOf):
            def __init__(self):
                TemplateRecordOf.__init__(self, MyRecordOf())
        type = MyTemplateRecordOf()
        for value in [True, 1, 1.0, "WAX", [1, 2], (1, 2)]:
            with self.assertRaises(InvalidTypeInAssignment):
                self.assertFalse(type.assign(value))

    def test_AssignRaisesAnExceptionOnAnInvalidValue_InvalidType_Special(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer(SimpleType()))
        class MyTemplateRecordOf(TemplateRecordOf):
            def __init__(self):
                TemplateRecordOf.__init__(self, MyRecordOf())
        type = MyTemplateRecordOf()
        for value in [[AnyValue()]]:
            with self.assertRaises(InvalidTypeInAssignment):
                self.assertFalse(type.assign(value))

    def test_AssignRaisesAnExceptionOnAnInvalidValue_InvalidType_OtherType(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer(SimpleType()))
        class MyTemplateRecordOf(TemplateRecordOf):
            def __init__(self):
                TemplateRecordOf.__init__(self, MyRecordOf())
        type = MyTemplateRecordOf()
        for value in [[Float(SimpleType()).assign(FloatValue(1.0))]]:
            with self.assertRaises(InvalidTypeInAssignment):
                self.assertFalse(type.assign(value))

class TypeSystem_RecordOF_TemplateRecordOf_Eq(unittest.TestCase):
    def test_EqReturnsTrueOnSameValues_EmptyRecordOf(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer(SimpleType()))
        class MyTemplateRecordOf(TemplateRecordOf):
            def __init__(self):
                TemplateRecordOf.__init__(self, MyRecordOf())
        record1 = MyTemplateRecordOf().assign([])
        record2 = MyTemplateRecordOf().assign([])
        self.assertTrue(record1 == record2)

    def test_EqReturnsTrueOnSameValues_OneElement_WithoutSpecial(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer(SimpleType()))
        class MyTemplateRecordOf(TemplateRecordOf):
            def __init__(self):
                TemplateRecordOf.__init__(self, MyRecordOf())
        record1 = MyTemplateRecordOf().assign([Integer(SimpleType()).assign(IntegerValue(1))])
        record2 = MyTemplateRecordOf().assign([Integer(SimpleType()).assign(IntegerValue(1))])
        self.assertTrue(record1 == record2)

    def test_EqReturnsTrueOnSameValues_OneElement_WithSpecial(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer(SimpleType()))
        class MyTemplateRecordOf(TemplateRecordOf):
            def __init__(self):
                TemplateRecordOf.__init__(self, MyRecordOf())
        record1 = MyTemplateRecordOf().assign([TemplateType(Integer(SimpleType())).assign(AnyValue())])
        record2 = MyTemplateRecordOf().assign([Integer(SimpleType()).assign(IntegerValue(1))])
        self.assertTrue(record1 == record2)

    def test_EqReturnsTrueOnSameValues_ManyElements_WithoutSpecial(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer(SimpleType()))
        class MyTemplateRecordOf(TemplateRecordOf):
            def __init__(self):
                TemplateRecordOf.__init__(self, MyRecordOf())
        record1 = MyTemplateRecordOf().assign([Integer(SimpleType()).assign(IntegerValue(1)),
                                               Integer(SimpleType()).assign(IntegerValue(2)),
                                               Integer(SimpleType()).assign(IntegerValue(3))])
        record2 = MyTemplateRecordOf().assign([Integer(SimpleType()).assign(IntegerValue(1)),
                                               Integer(SimpleType()).assign(IntegerValue(2)),
                                               Integer(SimpleType()).assign(IntegerValue(3))])
        self.assertTrue(record1 == record2)

    def test_EqReturnsTrueOnSameValues_ManyElements_WithSpecial(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer(SimpleType()))
        class MyTemplateRecordOf(TemplateRecordOf):
            def __init__(self):
                TemplateRecordOf.__init__(self, MyRecordOf())
        record1 = MyTemplateRecordOf().assign([Integer(SimpleType()).assign(IntegerValue(1)),
                                               TemplateType(Integer(SimpleType())).assign(AnyValue()),
                                               Integer(SimpleType()).assign(IntegerValue(3))])
        record2 = MyTemplateRecordOf().assign([Integer(SimpleType()).assign(IntegerValue(1)),
                                               Integer(SimpleType()).assign(IntegerValue(2)),
                                               Integer(SimpleType()).assign(IntegerValue(3))])
        self.assertTrue(record1 == record2)

    def test_EqReturnsFalseOnDifferentValues_OneElement(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer(SimpleType()))
        class MyTemplateRecordOf(TemplateRecordOf):
            def __init__(self):
                TemplateRecordOf.__init__(self, MyRecordOf())
        record1 = MyTemplateRecordOf().assign([Integer(SimpleType()).assign(IntegerValue(1))])
        record2 = MyTemplateRecordOf().assign([Integer(SimpleType()).assign(IntegerValue(2))])
        self.assertFalse(record1 == record2)

    def test_EqReturnsFalseOnDifferentValues_ManyElements(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer(SimpleType()))
        class MyTemplateRecordOf(TemplateRecordOf):
            def __init__(self):
                TemplateRecordOf.__init__(self, MyRecordOf())
        record1 = MyTemplateRecordOf().assign([Integer(SimpleType()).assign(IntegerValue(1)),
                                               Integer(SimpleType()).assign(IntegerValue(2)),
                                               Integer(SimpleType()).assign(IntegerValue(3))])
        record2 = MyTemplateRecordOf().assign([Integer(SimpleType()).assign(IntegerValue(1)),
                                               Integer(SimpleType()).assign(IntegerValue(3)),
                                               Integer(SimpleType()).assign(IntegerValue(3))])
        self.assertFalse(record1 == record2)

    def test_EqReturnsFalseOnDifferentValues_DiffentSize_SmallerBigger(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer(SimpleType()))
        class MyTemplateRecordOf(TemplateRecordOf):
            def __init__(self):
                TemplateRecordOf.__init__(self, MyRecordOf())
        record1 = MyTemplateRecordOf().assign([Integer(SimpleType()).assign(IntegerValue(1)),
                                               Integer(SimpleType()).assign(IntegerValue(2))])
        record2 = MyTemplateRecordOf().assign([Integer(SimpleType()).assign(IntegerValue(1)),
                                               Integer(SimpleType()).assign(IntegerValue(2)),
                                               Integer(SimpleType()).assign(IntegerValue(3))])
        self.assertFalse(record1 == record2)

    def test_EqReturnsFalseOnDifferentValues_DiffentSize_BiggerSmaller(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer(SimpleType()))
        class MyTemplateRecordOf(TemplateRecordOf):
            def __init__(self):
                TemplateRecordOf.__init__(self, MyRecordOf())
        record1 = MyTemplateRecordOf().assign([Integer(SimpleType()).assign(IntegerValue(1)),
                                               Integer(SimpleType()).assign(IntegerValue(2)),
                                               Integer(SimpleType()).assign(IntegerValue(3))])
        record2 = MyTemplateRecordOf().assign([Integer(SimpleType()).assign(IntegerValue(1)),
                                               Integer(SimpleType()).assign(IntegerValue(2))])
        self.assertFalse(record1 == record2)

    def test_EqReturnsFalseOnDifferentValues_SequenceMatters(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer(SimpleType()))
        class MyTemplateRecordOf(TemplateRecordOf):
            def __init__(self):
                TemplateRecordOf.__init__(self, MyRecordOf())
        record1 = MyTemplateRecordOf().assign([Integer(SimpleType()).assign(IntegerValue(1)),
                                               Integer(SimpleType()).assign(IntegerValue(2)),
                                               Integer(SimpleType()).assign(IntegerValue(3))])
        record2 = MyTemplateRecordOf().assign([Integer(SimpleType()).assign(IntegerValue(1)),
                                               Integer(SimpleType()).assign(IntegerValue(3)),
                                               Integer(SimpleType()).assign(IntegerValue(2))])
        self.assertFalse(record1 == record2)

    def test_EqRaisesAnExceptionOnAnInvalidValue_InvalidType_BuiltIn(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer(SimpleType()))
        class MyTemplateRecordOf(TemplateRecordOf):
            def __init__(self):
                TemplateRecordOf.__init__(self, MyRecordOf())
        record = MyTemplateRecordOf().assign([Integer(SimpleType()).assign(IntegerValue(1))])
        for value in [True, 1, 1.0, "WAX", [1, 2], (1, 2)]:
            with self.assertRaises(InvalidTypeInComparison):
                record == value

    def test_EqRaisesAnExceptionOnAnInvalidValue_InvalidType_Special(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer(SimpleType()))
        class MyTemplateRecordOf(TemplateRecordOf):
            def __init__(self):
                TemplateRecordOf.__init__(self, MyRecordOf())
        record = MyTemplateRecordOf().assign([Integer(SimpleType()).assign(IntegerValue(1))])
        for value in [AnyValue()]:
            with self.assertRaises(InvalidTypeInComparison):
                record == value

    def test_EqRaisesAnExceptionOnAnInvalidValue_InvalidType_Template(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer(SimpleType()))
        class MyTemplateRecordOf(TemplateRecordOf):
            def __init__(self):
                TemplateRecordOf.__init__(self, MyRecordOf())
        record = MyTemplateRecordOf().assign([Integer(SimpleType()).assign(IntegerValue(1))])
        for value in [TemplateType(Integer(SimpleType())).assign(IntegerValue(1))]:
            with self.assertRaises(InvalidTypeInComparison):
                record == value

    def test_EqRaisesAnExceptionOnAnInvalidValue_InvalidType_DifferentType(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer(SimpleType()))
        class MyTemplateRecordOf1(TemplateRecordOf):
            def __init__(self):
                TemplateRecordOf.__init__(self, MyRecordOf())
        class MyTemplateRecordOf2(TemplateRecordOf):
            def __init__(self):
                TemplateRecordOf.__init__(self, MyRecordOf())
        record1 = MyTemplateRecordOf1().assign([Integer(SimpleType()).assign(IntegerValue(1))])
        record2 = MyTemplateRecordOf2().assign([Integer(SimpleType()).assign(IntegerValue(1))])
        with self.assertRaises(InvalidTypeInComparison):
            record1 == record2

class TypeSystem_RecordOf_TemplateRecordOf_GetField(unittest.TestCase):
    def test_GetFieldReturnsTheValueOfTheFieldOnAValidField(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer(SimpleType()))
        class MyTemplateRecordOf(TemplateRecordOf):
            def __init__(self):
                TemplateRecordOf.__init__(self, MyRecordOf())
        record = MyTemplateRecordOf().assign([Integer(SimpleType()).assign(IntegerValue(1)),
                                              Integer(SimpleType()).assign(IntegerValue(2)),
                                              Integer(SimpleType()).assign(IntegerValue(3))])
        self.assertEqual(record.getField(1), Integer(SimpleType()).assign(IntegerValue(2)))

    def test_GetFieldRaisesAnExceptionOnAnInvalidField(self):
        with self.assertRaises(LookupErrorMissingField):
            class MyRecordOf(RecordOf):
                def __init__(self):
                    RecordOf.__init__(self, SimpleType(), Integer(SimpleType()))
            class MyTemplateRecordOf(TemplateRecordOf):
                def __init__(self):
                    TemplateRecordOf.__init__(self, MyRecordOf())
            record = MyTemplateRecordOf().assign([Integer(SimpleType()).assign(IntegerValue(1)),
                                                  Integer(SimpleType()).assign(IntegerValue(2)),
                                                  Integer(SimpleType()).assign(IntegerValue(3))])
            record.getField(4)

if __name__ == '__main__':
    unittest.main()
