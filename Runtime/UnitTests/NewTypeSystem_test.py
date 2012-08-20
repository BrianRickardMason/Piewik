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
# TODO: Tests for RecordOf of Record.
# TODO: Tests for Record of RecordOf.
#

import unittest

from Runtime.NewTypeSystem import *

class NewTypeSystem_TypeDecorator_IsOfType(unittest.TestCase):
    def test_IsOfTypeReturnsTrueForAValidType(self):
        type = Boolean(SimpleType())
        self.assertFalse(type.isOfType(TemplateType))
        self.assertTrue(type.isOfType(Boolean))
        self.assertTrue(type.isOfType(SimpleType))
        self.assertFalse(type.isOfType(Integer))
        type = TemplateType(Boolean(SimpleType()))
        self.assertTrue(type.isOfType(TemplateType))
        self.assertTrue(type.isOfType(Boolean))
        self.assertTrue(type.isOfType(SimpleType))
        self.assertFalse(type.isOfType(Integer))
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': Charstring(SimpleType())})
        type = MyRecord()
        self.assertTrue(type.isOfType(Record))

class NewTypeSystem_Boolean_Ctor(unittest.TestCase):
    def test_Ctor(self):
        Boolean(SimpleType())

    def test_CtorRaisesAnExceptionOnAnInvalidType_BuiltIn(self):
        for type in [True, 1, 1.0, "WAX", {}, [], ()]:
            with self.assertRaises(InvalidTypeInCtor):
                Boolean(type)

    def test_CtorRaisesAnExceptionOnAnInvalidType_Regular(self):
        for type in [Boolean(SimpleType()), Integer(SimpleType()), Float(SimpleType()), Charstring(SimpleType())]:
            with self.assertRaises(InvalidTypeInCtor):
                Boolean(type)

    def test_CtorRaisesAnExceptionOnAnInvalidType_Special(self):
        for type in [AnyValue()]:
            with self.assertRaises(InvalidTypeInCtor):
                Boolean(type)

    def test_CtorRaisesAnExceptionOnAnInvalidType_Template(self):
        for type in [TemplateType(Boolean(SimpleType()))]:
            with self.assertRaises(InvalidTypeInCtor):
                Boolean(type)

class NewTypeSystem_Boolean_Accept(unittest.TestCase):
    def test_AcceptReturnsTrueOnAValidValue(self):
        type = Boolean(SimpleType())
        for value in [BooleanValue(True), BooleanValue(False)]:
            self.assertTrue(type.accept(value))

    def test_AcceptReturnsFalseOnAnInvalidValue_BuiltIn(self):
        type = Boolean(SimpleType())
        for value in [True, 1.0, "WAX"]:
            self.assertFalse(type.accept(value))

    def test_AcceptReturnsFalseOnAnInvalidValue_Special(self):
        type = Boolean(SimpleType())
        for value in [AnyValue()]:
            self.assertFalse(type.accept(value))

class NewTypeSystem_Boolean_Assign(unittest.TestCase):
    def test_AssignAssignsOnAValidValue(self):
        type = Boolean(SimpleType())
        for value in [BooleanValue(True), BooleanValue(False)]:
            self.assertEqual(type.assign(value).value(), value)

    def test_AssignRaisesAnExceptionOnAnInvalidValue_BuiltIn(self):
        type = Boolean(SimpleType())
        for value in [True, 1.0, "WAX"]:
            with self.assertRaises(InvalidTypeInAssignment):
                type.assign(value)

    def test_AssignRaisesAnExceptionOnAnInvalidValue_Special(self):
        type = Boolean(SimpleType())
        for value in [AnyValue()]:
            with self.assertRaises(InvalidTypeInAssignment):
                type.assign(value)

class NewTypeSystem_Boolean_Eq(unittest.TestCase):
    def test_EqReturnsTrueOnSameValues(self):
        self.assertTrue(   Boolean(SimpleType()).assign(BooleanValue(True))
                        == Boolean(SimpleType()).assign(BooleanValue(True)))

    def test_EqReturnsFalseOnDifferentValues(self):
        self.assertFalse(   Boolean(SimpleType()).assign(BooleanValue(True))
                         == Boolean(SimpleType()).assign(BooleanValue(False)))

    def test_EqRaisesAnExceptionOnAnInvalidType(self):
        type = Boolean(SimpleType()).assign(BooleanValue(True))
        for value in [True, 1.0, "WAX"]:
            with self.assertRaises(InvalidTypeInComparison):
                type == value

class NewTypeSystem_Boolean_TemplateType_Ctor(unittest.TestCase):
    def test_Ctor(self):
        TemplateType(Boolean(SimpleType()))

class NewTypeSystem_Boolean_TemplateType_Accept(unittest.TestCase):
    def test_AcceptReturnsTrueOnAValidValue(self):
        type = TemplateType(Boolean(SimpleType()))
        for value in [BooleanValue(True), BooleanValue(False), AnyValue()]:
            self.assertTrue(type.accept(value))

    def test_AcceptReturnsFalseOnAnInvalidValue_InvalidType(self):
        type = TemplateType(Boolean(SimpleType()))
        for value in [True, 1.0, "WAX"]:
            self.assertFalse(type.accept(value))

class NewTypeSystem_Boolean_TemplateType_Assign(unittest.TestCase):
    def test_AssignAssignsOnAValidValue(self):
        type = TemplateType(Boolean(SimpleType()))
        for value in [BooleanValue(True), BooleanValue(False), AnyValue()]:
            self.assertEqual(type.assign(value).value(), value)

    def test_AssignRaisesAnExceptionOnAnInvalidValue(self):
        type = TemplateType(Boolean(SimpleType()))
        for value in [True, 1.0, "WAX"]:
            with self.assertRaises(InvalidTypeInAssignment):
                type.assign(value)

class NewTypeSystem_Boolean_TemplateType_Eq(unittest.TestCase):
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

    def test_EqRaisesAnExceptionOnAnInvalidType(self):
        type = TemplateType(Boolean(SimpleType())).assign(BooleanValue(True))
        for value in [True, 1.0, "WAX"]:
            with self.assertRaises(InvalidTypeInComparison):
                type == value

class NewTypeSystem_Integer_Ctor(unittest.TestCase):
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

class NewTypeSystem_Integer_Accept(unittest.TestCase):
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

class NewTypeSystem_Integer_Assign(unittest.TestCase):
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

class NewTypeSystem_Integer_Eq(unittest.TestCase):
    def test_EqReturnsTrueOnSameValues(self):
        self.assertTrue(Integer(SimpleType()).assign(IntegerValue(1)) == Integer(SimpleType()).assign(IntegerValue(1)))

    def test_EqReturnsFalseOnDifferentValues(self):
        self.assertFalse(Integer(SimpleType()).assign(IntegerValue(1)) == Integer(SimpleType()).assign(IntegerValue(2)))

    def test_EqRaisesAnExceptionOnAnInvalidType(self):
        type = Integer(SimpleType()).assign(IntegerValue(1))
        for value in [True, 1.0, "WAX"]:
            with self.assertRaises(InvalidTypeInComparison):
                type == value

class NewTypeSystem_Integer_BoundedType_Ctor(unittest.TestCase):
    def test_Ctor(self):
        BoundedType(Integer(SimpleType()), IntegerValue(0), IntegerValue(10))

class NewTypeSystem_Integer_BoundedType_Accept(unittest.TestCase):
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

class NewTypeSystem_Integer_BoundedType_Assign(unittest.TestCase):
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

class NewTypeSystem_Integer_BoundedType_Eq(unittest.TestCase):
    def test_EqReturnsTrueOnSameValues(self):
        self.assertTrue(
               BoundedType(Integer(SimpleType()), IntegerValue(0), IntegerValue(10)).assign(IntegerValue(1))
            == BoundedType(Integer(SimpleType()), IntegerValue(0), IntegerValue(10)).assign(IntegerValue(1)))

    def test_EqReturnsFalseOnDifferentValues(self):
        self.assertFalse(
               BoundedType(Integer(SimpleType()), IntegerValue(0), IntegerValue(10)).assign(IntegerValue(1))
            == BoundedType(Integer(SimpleType()), IntegerValue(0), IntegerValue(10)).assign(IntegerValue(2)))

    def test_EqRaisesAnExceptionOnAnInvalidType(self):
        type = BoundedType(Integer(SimpleType()), IntegerValue(0), IntegerValue(10)).assign(IntegerValue(1))
        for value in [True, 1.0, "WAX"]:
            with self.assertRaises(InvalidTypeInComparison):
                type == value

class NewTypeSystem_Integer_TemplateType_Ctor(unittest.TestCase):
    def test_Ctor(self):
        TemplateType(Integer(SimpleType()))

class NewTypeSystem_Integer_TemplateType_Accept(unittest.TestCase):
    def test_AcceptReturnsTrueOnAValidValue(self):
        type = TemplateType(Integer(SimpleType()))
        for value in [IntegerValue(-1), IntegerValue(0), IntegerValue(10), AnyValue()]:
            self.assertTrue(type.accept(value))

    def test_AcceptReturnsFalseOnAnInvalidValue_InvalidType(self):
        type = TemplateType(Integer(SimpleType()))
        for value in [True, 1.0, "WAX"]:
            self.assertFalse(type.accept(value))

class NewTypeSystem_Integer_TemplateType_Assign(unittest.TestCase):
    def test_AssignAssignsOnAValidValue(self):
        type = TemplateType(Integer(SimpleType()))
        for value in [IntegerValue(-1), IntegerValue(0), IntegerValue(10), AnyValue()]:
            self.assertEqual(type.assign(value).value(), value)

    def test_AssignRaisesAnExceptionOnAnInvalidValue(self):
        type = TemplateType(Integer(SimpleType()))
        for value in [True, 1.0, "WAX"]:
            with self.assertRaises(InvalidTypeInAssignment):
                type.assign(value)

class NewTypeSystem_Integer_TemplateType_Eq(unittest.TestCase):
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

    def test_EqRaisesAnExceptionOnAnInvalidType(self):
        type = TemplateType(Integer(SimpleType())).assign(IntegerValue(1))
        for value in [True, 1.0, "WAX"]:
            with self.assertRaises(InvalidTypeInComparison):
                type == value

class NewTypeSystem_Float_Ctor(unittest.TestCase):
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

class NewTypeSystem_Float_Accept(unittest.TestCase):
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

class NewTypeSystem_Float_Assign(unittest.TestCase):
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

class NewTypeSystem_Float_Eq(unittest.TestCase):
    def test_EqReturnsTrueOnSameValues(self):
        self.assertTrue(Float(SimpleType()).assign(FloatValue(1.0)) == Float(SimpleType()).assign(FloatValue(1.0)))

    def test_EqReturnsFalseOnDifferentValues(self):
        self.assertFalse(Float(SimpleType()).assign(FloatValue(1.0)) == Float(SimpleType()).assign(FloatValue(2.0)))

    def test_EqRaisesAnExceptionOnAnInvalidType(self):
        type = Float(SimpleType()).assign(FloatValue(1.0))
        for value in [True, 1, "WAX"]:
            with self.assertRaises(InvalidTypeInComparison):
                type == value

class NewTypeSystem_Float_BoundedType_Ctor(unittest.TestCase):
    def test_Ctor(self):
        BoundedType(Float(SimpleType()), FloatValue(0.0), FloatValue(10.0))

class NewTypeSystem_Float_BoundedType_Accept(unittest.TestCase):
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

class NewTypeSystem_Float_BoundedType_Assign(unittest.TestCase):
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

class NewTypeSystem_Float_BoundedType_Eq(unittest.TestCase):
    def test_EqReturnsTrueOnSameValues(self):
        self.assertTrue(
               BoundedType(Float(SimpleType()), FloatValue(0.0), FloatValue(10.0)).assign(FloatValue(1.0))
            == BoundedType(Float(SimpleType()), FloatValue(0.0), FloatValue(10.0)).assign(FloatValue(1.0)))

    def test_EqReturnsFalseOnDifferentValues(self):
        self.assertFalse(
               BoundedType(Float(SimpleType()), FloatValue(0.0), FloatValue(10.0)).assign(FloatValue(1.0))
            == BoundedType(Float(SimpleType()), FloatValue(0.0), FloatValue(10.0)).assign(FloatValue(2.0)))

    def test_EqRaisesAnExceptionOnAnInvalidType(self):
        type = BoundedType(Float(SimpleType()), FloatValue(0.0), FloatValue(10.0)).assign(FloatValue(1.0))
        for value in [True, 1, "WAX"]:
            with self.assertRaises(InvalidTypeInComparison):
                type == value

class NewTypeSystem_Float_TemplateType_Ctor(unittest.TestCase):
    def test_Ctor(self):
        TemplateType(Float(SimpleType()))

class NewTypeSystem_Float_TemplateType_Accept(unittest.TestCase):
    def test_AcceptReturnsTrueOnAValidValue(self):
        type = TemplateType(Float(SimpleType()))
        for value in [FloatValue(-1.0), FloatValue(0.0), FloatValue(10.0), AnyValue()]:
            self.assertTrue(type.accept(value))

    def test_AcceptReturnsFalseOnAnInvalidValue_InvalidType(self):
        type = TemplateType(Float(SimpleType()))
        for value in [True, 1, "WAX"]:
            self.assertFalse(type.accept(value))

class NewTypeSystem_Float_TemplateType_Assign(unittest.TestCase):
    def test_AssignAssignsOnAValidValue(self):
        type = TemplateType(Float(SimpleType()))
        for value in [FloatValue(-1.0), FloatValue(0.0), FloatValue(10.0), AnyValue()]:
            self.assertEqual(type.assign(value).value(), value)

    def test_AssignRaisesAnExceptionOnAnInvalidValue(self):
        type = TemplateType(Float(SimpleType()))
        for value in [True, 1, "WAX"]:
            with self.assertRaises(InvalidTypeInAssignment):
                type.assign(value)

class NewTypeSystem_Float_TemplateType_Eq(unittest.TestCase):
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

    def test_EqRaisesAnExceptionOnAnInvalidType(self):
        type = TemplateType(Float(SimpleType())).assign(FloatValue(1.0))
        for value in [True, 1, "WAX"]:
            with self.assertRaises(InvalidTypeInComparison):
                type == value

class NewTypeSystem_Charstring_Ctor(unittest.TestCase):
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

class NewTypeSystem_Charstring_Accept(unittest.TestCase):
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

class NewTypeSystem_Charstring_Assign(unittest.TestCase):
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

class NewTypeSystem_Charstring_Eq(unittest.TestCase):
    def test_EqReturnsTrueOnSameValues(self):
        for values in [(CharstringValue(""), CharstringValue("")),
                       (CharstringValue("WAX"), CharstringValue("WAX"))]:
            self.assertTrue(   TemplateType(Charstring(SimpleType())).assign(values[0])
                            == TemplateType(Charstring(SimpleType())).assign(values[1]))

    def test_EqReturnsFalseOnDifferentValues(self):
        self.assertFalse(   Charstring(SimpleType()).assign(CharstringValue("WAX"))
                         == Charstring(SimpleType()).assign(CharstringValue("WAS")))

    def test_EqRaisesAnExceptionOnAnInvalidType(self):
        type = Charstring(SimpleType()).assign(CharstringValue("WAX"))
        for value in [True, 1, 1.0]:
            with self.assertRaises(InvalidTypeInComparison):
                type == value

class NewTypeSystem_Charstring_TemplateType_Ctor(unittest.TestCase):
    def test_Ctor(self):
        TemplateType(Charstring(SimpleType()))

class NewTypeSystem_Charstring_TemplateType_Accept(unittest.TestCase):
    def test_AcceptReturnsTrueOnAValidValue(self):
        type = TemplateType(Charstring(SimpleType()))
        for value in [CharstringValue(""), CharstringValue("WAX"), AnyValue()]:
            self.assertTrue(type.accept(value))

    def test_AcceptReturnsFalseOnAnInvalidValue_InvalidType(self):
        type = TemplateType(Charstring(SimpleType()))
        for value in [True, 1, 1.0]:
            self.assertFalse(type.accept(value))

class NewTypeSystem_Charstring_TemplateType_Assign(unittest.TestCase):
    def test_AssignAssignsOnAValidValue(self):
        type = TemplateType(Charstring(SimpleType()))
        for value in [CharstringValue(""), CharstringValue("WAX"), AnyValue()]:
            self.assertEqual(type.assign(value).value(), value)

    def test_AssignRaisesAnExceptionOnAnInvalidValue(self):
        type = TemplateType(Charstring(SimpleType()))
        for value in [True, 1, 1.0]:
            with self.assertRaises(InvalidTypeInAssignment):
                type.assign(value)

class NewTypeSystem_Charstring_TemplateType_Eq(unittest.TestCase):
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

    def test_EqRaisesAnExceptionOnAnInvalidType(self):
        type = TemplateType(Charstring(SimpleType())).assign(CharstringValue("WAX"))
        for value in [True, 1, 1.0]:
            with self.assertRaises(InvalidTypeInComparison):
                type == value

class NewTypeSystem_Record_Ctor(unittest.TestCase):
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

class NewTypeSystem_Record_Accept(unittest.TestCase):
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

class NewTypeSystem_Record_Assign(unittest.TestCase):
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
        externalRecord.assign(externalValue)

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

class NewTypeSystem_Record_Eq(unittest.TestCase):
    def test_EqReturnsTrueOnSameValues_EmptyRecord(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {})
        record1 = MyRecord().assign({})
        record2 = MyRecord().assign({})
        self.assertTrue(record1 == record2)

    def test_EqReturnsTrueOnSameValues_NonEmptyRecord(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': Charstring(SimpleType())})
        value = {'foo': Integer(SimpleType()).assign(IntegerValue(1)),
                 'bar': Charstring(SimpleType()).assign(CharstringValue("WAX"))}
        record1 = MyRecord().assign(value)
        record2 = MyRecord().assign(value)
        self.assertTrue(record1 == record2)

    def test_EqReturnsTrueOnSameValues_NestedRecords(self):
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
        externalRecord1 = ExternalRecord()
        externalRecord2 = ExternalRecord()
        externalRecord1.assign(externalValue)
        externalRecord2.assign(externalValue)
        self.assertTrue(externalRecord1 == externalRecord2)

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

    def test_EqRaisesAnExceptionOnAnInvalidValue_IncompatibleDictionaries_SecondEmpty(self):
        record1 = Record(SimpleType(), {'foo': Integer(SimpleType()), 'bar': Charstring(SimpleType())})
        record2 = Record(SimpleType(), {})
        value1 = {'foo': Integer(SimpleType()).assign(IntegerValue(1)),
                  'bar': Charstring(SimpleType()).assign(CharstringValue("WAX"))}
        record1.assign(value1)
        record2.assign({})
        with self.assertRaises(InvalidTypeInComparison):
            record1 == record2

    def test_EqRaisesAnExceptionOnAnInvalidValue_IncompatibleDictionaries_SecondTooSmall(self):
        record1 = Record(SimpleType(), {'foo': Integer(SimpleType()), 'bar': Charstring(SimpleType())})
        record2 = Record(SimpleType(), {'foo': Integer(SimpleType())})
        value1 = {'foo': Integer(SimpleType()).assign(IntegerValue(1)),
                  'bar': Charstring(SimpleType()).assign(CharstringValue("WAX"))}
        value2 = {'foo': Integer(SimpleType()).assign(IntegerValue(1))}
        record1.assign(value1)
        record2.assign(value2)
        with self.assertRaises(InvalidTypeInComparison):
            record1 == record2

    def test_EqRaisesAnExceptionOnAnInvalidValue_IncompatibleDictionaries_SecondTooBig(self):
        record1 = Record(SimpleType(), {'foo': Integer(SimpleType()), 'bar': Charstring(SimpleType())})
        record2 = Record(SimpleType(), {'foo': Integer(SimpleType()),
                                        'bar': Charstring(SimpleType()),
                                        'baz': Integer(SimpleType())})
        value1 = {'foo': Integer(SimpleType()).assign(IntegerValue(1)),
                  'bar': Charstring(SimpleType()).assign(CharstringValue("WAX"))}
        value2 = {'foo': Integer(SimpleType()).assign(IntegerValue(1)),
                  'bar': Charstring(SimpleType()).assign(CharstringValue("WAX")),
                  'baz': Integer(SimpleType()).assign(IntegerValue(2))}
        record1.assign(value1)
        record2.assign(value2)
        with self.assertRaises(InvalidTypeInComparison):
            record1 == record2

    def test_AssignRaisesAnExceptionOnAnInvalidValue_IncompatibleDictionaries_AssignedHasDifferentKeys(self):
        record1 = Record(SimpleType(), {'foo': Integer(SimpleType()), 'bar': Charstring(SimpleType())})
        record2 = Record(SimpleType(), {'foo': Integer(SimpleType()), 'baz': Charstring(SimpleType())})
        value1 = {'foo': Integer(SimpleType()).assign(IntegerValue(1)),
                  'bar': Charstring(SimpleType()).assign(CharstringValue("WAX"))}
        value2 = {'foo': Integer(SimpleType()).assign(IntegerValue(1)),
                  'baz': Charstring(SimpleType()).assign(CharstringValue("WAX"))}
        record1.assign(value1)
        record2.assign(value2)
        with self.assertRaises(InvalidTypeInComparison):
            record1 == record2

    def test_AssignRaisesAnExceptionOnAnInvalidValue_IncompatibleDictionaries_AssignedHasChangedKeys(self):
        record1 = Record(SimpleType(), {'foo': Integer(SimpleType()), 'bar': Charstring(SimpleType())})
        record2 = Record(SimpleType(), {'bar': Integer(SimpleType()), 'foo': Charstring(SimpleType())})
        value1 = {'foo': Integer(SimpleType()).assign(IntegerValue(1)),
                  'bar': Charstring(SimpleType()).assign(CharstringValue("WAX"))}
        value2 = {'bar': Integer(SimpleType()).assign(IntegerValue(1)),
                  'foo': Charstring(SimpleType()).assign(CharstringValue("WAX"))}
        record1.assign(value1)
        record2.assign(value2)
        with self.assertRaises(InvalidTypeInComparison):
            record1 == record2

class NewTypeSystem_Record_GetField(unittest.TestCase):
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

class NewTypeSystem_Record_TemplateRecord_Ctor(unittest.TestCase):
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

class NewTypeSystem_Record_TemplateRecord_Accept(unittest.TestCase):
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
        internalRecord = InternalRecord().assign(internalValue)
        externalValue = {'foo': TemplateType(Integer(SimpleType())).assign(AnyValue()),
                         'bar': internalRecord}
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

class NewTypeSystem_Record_TemplateRecord_Assign(unittest.TestCase):
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
        internalRecord = InternalRecord().assign(internalValue)
        externalValue = {'foo': TemplateType(Integer(SimpleType())).assign(AnyValue()),
                         'bar': internalRecord}
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

class NewTypeSystem_Record_TemplateRecord_Eq(unittest.TestCase):
    def test_EqReturnsTrueOnSameValues_EmptyRecord(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {})
        class MyTemplateRecord(TemplateRecord):
            def __init__(self):
                TemplateRecord.__init__(self, MyRecord())
        type = MyTemplateRecord()
        record1 = MyTemplateRecord().assign({})
        record2 = MyTemplateRecord().assign({})
        self.assertTrue(record1 == record2)

    def test_EqReturnsTrueOnSameValues_NonEmptyRecord(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': Charstring(SimpleType())})
        class MyTemplateRecord(TemplateRecord):
            def __init__(self):
                TemplateRecord.__init__(self, MyRecord())
        type = MyTemplateRecord()
        value = {'foo': Integer(SimpleType()).assign(IntegerValue(1)),
                 'bar': Charstring(SimpleType()).assign(CharstringValue("WAX"))}
        record1 = MyTemplateRecord().assign(value)
        record2 = MyTemplateRecord().assign(value)
        self.assertTrue(record1 == record2)

    def test_EqReturnsTrueOnSameValues_NonEmptyRecord_WithSpecialValues(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer(SimpleType()), 'bar': Charstring(SimpleType())})
        class MyTemplateRecord(TemplateRecord):
            def __init__(self):
                TemplateRecord.__init__(self, MyRecord())
        type = MyTemplateRecord()
        value1 = {'foo': Integer(SimpleType()).assign(IntegerValue(1)),
                  'bar': Charstring(SimpleType()).assign(CharstringValue("WAX"))}
        value2 = {'foo': TemplateType(Integer(SimpleType())).assign(AnyValue()),
                  'bar': Charstring(SimpleType()).assign(CharstringValue("WAX"))}
        record1 = MyTemplateRecord().assign(value1)
        record2 = MyTemplateRecord().assign(value2)
        self.assertTrue(record1 == record2)

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
        type1 = MyTemplateRecord()
        type2 = MyTemplateRecord()
        type1.assign(externalValue)
        type2.assign(externalValue)
        self.assertTrue(type1 == type2)

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
        type1 = MyTemplateRecord()
        type2 = MyTemplateRecord()
        type1.assign(externalValue1)
        type2.assign(externalValue2)
        self.assertFalse(type1 == type2)

class NewTypeSystem_Record_TemplateRecord_GetField(unittest.TestCase):
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

class NewTypeSystem_RecordOf_Ctor(unittest.TestCase):
    def test_Ctor(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer)
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

class NewTypeSystem_RecordOf_Accept(unittest.TestCase):
    def test_AcceptReturnsTrueOnAValidValue_TheSameTypes_AnEmptyList(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer)
        type = MyRecordOf()
        value = []
        self.assertTrue(type.accept(value))

    def test_AcceptReturnsTrueOnAValidValue_TheSameTypes_ASingleElementList(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer)
        type = MyRecordOf()
        value = [Integer(SimpleType()).assign(IntegerValue(1))]
        self.assertTrue(type.accept(value))

    def test_AcceptReturnsTrueOnAValidValue_TheSameTypes_AManyElementsList(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer)
        type = MyRecordOf()
        value = [Integer(SimpleType()).assign(IntegerValue(1)), Integer(SimpleType()).assign(IntegerValue(2))]
        self.assertTrue(type.accept(value))

    def test_AcceptReturnsFalseOnAnInvalidValue_InvalidType_BuiltIn(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer)
        type = MyRecordOf()
        for value in [True, 1, 1.0, "WAX", [1, 2], (1, 2)]:
            self.assertFalse(type.accept(value))

    def test_AcceptReturnsFalseOnAnInvalidValue_InvalidType_Special(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer)
        type = MyRecordOf()
        for value in [[AnyValue()]]:
            self.assertFalse(type.accept(value))

    def test_AcceptReturnsFalseOnAnInvalidValue_InvalidType_Template(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer)
        type = MyRecordOf()
        for value in [[TemplateType(Integer(SimpleType()))]]:
            self.assertFalse(type.accept(value))

    def test_AcceptReturnsFalseOnAnInvalidValue_InvalidType_OtherType(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer)
        type = MyRecordOf()
        for value in [[Float(SimpleType())]]:
            self.assertFalse(type.accept(value))

    def test_AcceptReturnsFalseOnAnInvalidValue_InvalidValue_AnyOfValuesIsATemplateLikeType(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer)
        type = MyRecordOf()
        value = [Integer(SimpleType()).assign(IntegerValue(1)),
                 TemplateType(Integer(SimpleType()).assign(IntegerValue(2)))]
        self.assertFalse(type.accept(value))

class NewTypeSystem_RecordOf_Assign(unittest.TestCase):
    def test_AcceptReturnsTrueOnAValidValue_TheSameTypes_AnEmptyList(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer)
        type = MyRecordOf()
        value = []
        type.assign(value)

    def test_AcceptReturnsTrueOnAValidValue_TheSameTypes_ASingleElementList(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer)
        type = MyRecordOf()
        value = [Integer(SimpleType()).assign(IntegerValue(1))]
        type.assign(value)

    def test_AcceptReturnsTrueOnAValidValue_TheSameTypes_AManyElementsList(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer)
        type = MyRecordOf()
        value = [Integer(SimpleType()).assign(IntegerValue(1)), Integer(SimpleType()).assign(IntegerValue(2))]
        type.assign(value)

    def test_AcceptReturnsFalseOnAnInvalidValue_InvalidType_BuiltIn(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer)
        type = MyRecordOf()
        for value in [True, 1, 1.0, "WAX", [1, 2], (1, 2)]:
            with self.assertRaises(InvalidTypeInAssignment):
                type.assign(value)

    def test_AcceptReturnsFalseOnAnInvalidValue_InvalidType_Special(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer)
        type = MyRecordOf()
        for value in [[AnyValue()]]:
            with self.assertRaises(InvalidTypeInAssignment):
                type.assign(value)

    def test_AcceptReturnsFalseOnAnInvalidValue_InvalidType_Template(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer)
        type = MyRecordOf()
        for value in [[TemplateType(Integer(SimpleType()))]]:
            with self.assertRaises(InvalidTypeInAssignment):
                type.assign(value)

    def test_AcceptReturnsFalseOnAnInvalidValue_InvalidType_OtherType(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer)
        type = MyRecordOf()
        for value in [[Float(SimpleType())]]:
            with self.assertRaises(InvalidTypeInAssignment):
                type.assign(value)

    def test_AcceptReturnsFalseOnAnInvalidValue_InvalidValue_AnyOfValuesIsATemplateLikeType(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer)
        type = MyRecordOf()
        value = [Integer(SimpleType()).assign(IntegerValue(1)),
                 TemplateType(Integer(SimpleType()).assign(IntegerValue(2)))]
        with self.assertRaises(InvalidTypeInAssignment):
            type.assign(value)

class NewTypeSystem_RecordOF_Eq(unittest.TestCase):
    def test_EqReturnsTrueOnSameValues_EmptyRecordOf(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer)
        record1 = MyRecordOf().assign([])
        record2 = MyRecordOf().assign([])
        self.assertTrue(record1 == record2)

    def test_EqReturnsTrueOnSameValues_OneElement(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer)
        record1 = MyRecordOf().assign([Integer(SimpleType()).assign(IntegerValue(1))])
        record2 = MyRecordOf().assign([Integer(SimpleType()).assign(IntegerValue(1))])
        self.assertTrue(record1 == record2)

    def test_EqReturnsTrueOnSameValues_ManyElements(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer)
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
                RecordOf.__init__(self, SimpleType(), Integer)
        record1 = MyRecordOf().assign([Integer(SimpleType()).assign(IntegerValue(1))])
        record2 = MyRecordOf().assign([Integer(SimpleType()).assign(IntegerValue(2))])
        self.assertFalse(record1 == record2)

    def test_EqReturnsFalseOnDifferentValues_ManyElements(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer)
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
                RecordOf.__init__(self, SimpleType(), Integer)
        record1 = MyRecordOf().assign([Integer(SimpleType()).assign(IntegerValue(1)),
                                       Integer(SimpleType()).assign(IntegerValue(2))])
        record2 = MyRecordOf().assign([Integer(SimpleType()).assign(IntegerValue(1)),
                                       Integer(SimpleType()).assign(IntegerValue(2)),
                                       Integer(SimpleType()).assign(IntegerValue(3))])
        self.assertFalse(record1 == record2)

    def test_EqReturnsFalseOnDifferentValues_DiffentSize_BiggerSmaller(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer)
        record1 = MyRecordOf().assign([Integer(SimpleType()).assign(IntegerValue(1)),
                                       Integer(SimpleType()).assign(IntegerValue(2)),
                                       Integer(SimpleType()).assign(IntegerValue(3))])
        record2 = MyRecordOf().assign([Integer(SimpleType()).assign(IntegerValue(1)),
                                       Integer(SimpleType()).assign(IntegerValue(2))])
        self.assertFalse(record1 == record2)

    def test_EqReturnsFalseOnDifferentValues_SequenceMatters(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer)
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
                RecordOf.__init__(self, SimpleType(), Integer)
        record = MyRecordOf().assign([Integer(SimpleType()).assign(IntegerValue(1))])
        for value in [True, 1, 1.0, "WAX", [1, 2], (1, 2)]:
            with self.assertRaises(InvalidTypeInComparison):
                record == value

    def test_EqRaisesAnExceptionOnAnInvalidValue_InvalidType_Special(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer)
        record = MyRecordOf().assign([Integer(SimpleType()).assign(IntegerValue(1))])
        for value in [AnyValue()]:
            with self.assertRaises(InvalidTypeInComparison):
                record == value

    def test_EqRaisesAnExceptionOnAnInvalidValue_InvalidType_Template(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer)
        record = MyRecordOf().assign([Integer(SimpleType()).assign(IntegerValue(1))])
        for value in [TemplateType(Integer(SimpleType())).assign(IntegerValue(1))]:
            with self.assertRaises(InvalidTypeInComparison):
                record == value

    def test_EqRaisesAnExceptionOnAnInvalidValue_InvalidType_DifferentType(self):
        class MyRecordOf1(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer)
        class MyRecordOf2(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer)
        record1 = MyRecordOf1().assign([Integer(SimpleType()).assign(IntegerValue(1))])
        record2 = MyRecordOf2().assign([Integer(SimpleType()).assign(IntegerValue(1))])
        with self.assertRaises(InvalidTypeInComparison):
            record1 == record2

class NewTypeSystem_RecordOf_GetField(unittest.TestCase):
    def test_GetFieldReturnsTheValueOfTheFieldOnAValidField(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, SimpleType(), Integer)
        record = MyRecordOf().assign([Integer(SimpleType()).assign(IntegerValue(1)),
                                      Integer(SimpleType()).assign(IntegerValue(2)),
                                      Integer(SimpleType()).assign(IntegerValue(3))])
        self.assertEqual(record.getField(1), Integer(SimpleType()).assign(IntegerValue(2)))

    def test_GetFieldRaisesAnExceptionOnAnInvalidField(self):
        with self.assertRaises(LookupErrorMissingField):
            class MyRecordOf(RecordOf):
                def __init__(self):
                    RecordOf.__init__(self, SimpleType(), Integer)
            record = MyRecordOf().assign([Integer(SimpleType()).assign(IntegerValue(1)),
                                          Integer(SimpleType()).assign(IntegerValue(2)),
                                          Integer(SimpleType()).assign(IntegerValue(3))])
            record.getField(4)

if __name__ == '__main__':
    unittest.main()
