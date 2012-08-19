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

class NewTypeSystem_Boolean_Ctor(unittest.TestCase):
    def test_Ctor(self):
        Boolean(SimpleType())

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
                Record.__init__(self, SimpleType(), {})
        type = MyRecord()

    def test_Ctor_WithDictionary(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer, 'bar': Charstring})
        type = MyRecord()

    def test_CtorRaisesAnExceptionOnAnInvalidValue_InvalidKey(self):
        with self.assertRaises(InvalidTypeInCtor):
            class MyRecord(Record):
                def __init__(self):
                    Record.__init__(self, SimpleType(), {1: Integer, 'bar': Charstring})
            type = MyRecord()

    def test_CtorRaisesAnExceptionOnAnInvalidValue_InvalidType_BuiltIn(self):
        for type in [True, 1, 1.0, "WAX", [1, 2], (1, 2)]:
            with self.assertRaises(InvalidTypeInCtor):
                class MyRecord(Record):
                    def __init__(self):
                        Record.__init__(self, SimpleType(), type)
                type = MyRecord()

    def test_CtorRaisesAnExceptionOnAnInvalidValue_InvalidType_Special(self):
        with self.assertRaises(InvalidTypeInCtor):
            class MyRecord(Record):
                def __init__(self):
                    Record.__init__(self, SimpleType(), {'foo': Integer, 'bar': AnyValue})
            type = MyRecord()

    def test_CtorRaisesAnExceptionOnAnInvalidValue_InvalidType_AnyOfNestedTypesIsATemplateLikeType(self):
        with self.assertRaises(InvalidTypeInCtor):
            class MyRecord(Record):
                def __init__(self):
                    Record.__init__(self, SimpleType(), {'foo': Integer, 'bar': TemplateType})
            type = MyRecord()

class NewTypeSystem_Record_Accept(unittest.TestCase):
    def test_AcceptReturnsTrueOnAValidValue_TheSameTypes(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer, 'bar': Charstring})
        type = MyRecord()
        value = {'foo': Integer(SimpleType()).assign(IntegerValue(1)),
                 'bar': Charstring(SimpleType()).assign(CharstringValue("WAX"))}
        self.assertTrue(type.accept(value))

    def test_AcceptReturnsTrueOnAValidValue_CompatibleTypes(self):
        self.skipTest("Not implemented yet.")
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer, 'bar': Charstring})
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
                Record.__init__(self, SimpleType(), {'foo': Integer, 'bar': Charstring})
        class ExternalRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer, 'bar': InternalRecord})
        valueInternal = {'foo': Integer(SimpleType()).assign(IntegerValue(1)),
                         'bar': Charstring(SimpleType()).assign(CharstringValue("WAX"))}
        internalRecord = InternalRecord().assign(valueInternal)
        valueExternal = {'foo': Integer(SimpleType()).assign(IntegerValue(2)),
                         'bar': internalRecord}
        externalRecord = ExternalRecord()
        self.assertTrue(externalRecord.accept(valueExternal))

    def test_AcceptReturnsFalseOnAnInvalidValue_InvalidType_BuiltIn(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer, 'bar': Charstring})
        type = MyRecord()
        for value in [True, 1, 1.0, "WAX", [1, 2], (1, 2)]:
            self.assertFalse(type.accept(value))

    def test_AcceptReturnsFalseOnAnInvalidValue_InvalidType_Special(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer, 'bar': Charstring})
        type = MyRecord()
        value = {'foo': Integer(SimpleType()).assign(IntegerValue(1)),
                 'bar': AnyValue()}
        self.assertFalse(type.accept(value))

    def test_AcceptReturnsFalseOnAnInvalidValue_InvalidType_AnyOfNestedTypesIsATemplateLikeType(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer, 'bar': Charstring})
        type = MyRecord()
        value = {'foo': Integer(SimpleType()).assign(IntegerValue(1)),
                 'bar': TemplateType(Charstring(SimpleType)).assign(AnyValue())}
        self.assertFalse(type.accept(value))

    def test_AcceptReturnsFalseOnAnInvalidValue_IncompatibleDictionaries_AssignedEmpty(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer, 'bar': Charstring})
        type = MyRecord()
        self.assertFalse(type.accept({}))

    def test_AcceptReturnsFalseOnAnInvalidValue_IncompatibleDictionaries_AssignedTooSmall(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer, 'bar': Charstring})
        type = MyRecord()
        value = {'foo': Integer(SimpleType()).assign(IntegerValue(1))}
        self.assertFalse(type.accept(value))

    def test_AcceptReturnsFalseOnAnInvalidValue_IncompatibleDictionaries_AssignedTooBig(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer, 'bar': Charstring})
        type = MyRecord()
        value = {'foo': Integer(SimpleType()).assign(IntegerValue(1)),
                 'bar': Charstring(SimpleType()).assign(CharstringValue("WAX")),
                 'baz': Integer(SimpleType()).assign(IntegerValue(2))}
        self.assertFalse(type.accept(value))

    def test_AcceptReturnsFalseOnAnInvalidValue_IncompatibleDictionaries_AssignedHasDifferentKeys(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer, 'bar': Charstring})
        type = MyRecord()
        value = {'foo': Integer(SimpleType()).assign(IntegerValue(1)),
                 'baz': Charstring(SimpleType()).assign(CharstringValue("WAX"))}
        self.assertFalse(type.accept(value))

    def test_AcceptReturnsFalseOnAnInvalidValue_IncompatibleDictionaries_AssignedHasChangedKeys(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer, 'bar': Charstring})
        type = MyRecord()
        value = {'bar': Integer(SimpleType()).assign(IntegerValue(1)),
                 'foo': Charstring(SimpleType()).assign(CharstringValue("WAX"))}
        self.assertFalse(type.accept(value))

    def test_AcceptReturnsFalseOnAnInvalidValue_NotInitializedNestedRecord(self):
        class InternalRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer, 'bar': Charstring})
        class ExternalRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer, 'bar': InternalRecord})
        internalRecord = InternalRecord()
        valueExternal = {'foo': Integer(SimpleType()).assign(IntegerValue(2)),
                         'bar': internalRecord}
        externalRecord = ExternalRecord()
        self.assertFalse(externalRecord.accept(valueExternal))

class NewTypeSystem_Record_Assign(unittest.TestCase):
    def test_AssignAssignsOnAValidValue_TheSameTypes(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer, 'bar': Charstring})
        type = MyRecord()
        value = {'foo': Integer(SimpleType()).assign(IntegerValue(1)),
                 'bar': Charstring(SimpleType()).assign(CharstringValue("WAX"))}
        self.assertTrue(type.assign(value))

    def test_AssignAssignsOnAValidValue_CompatibleTypes(self):
        self.skipTest("Not implemented yet.")
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer, 'bar': Charstring})
        type = MyRecord()
        value = {'foo': BoundedType(
                            Integer(SimpleType()),
                            IntegerValue(0),
                            IntegerValue(10)
                        ).assign(IntegerValue(1)),
                 'bar': Charstring(SimpleType()).assign(CharstringValue("WAX"))}
        self.assertTrue(type.assign(value))

    def test_AcceptReturnsTrueOnAValidValue_NestedRecords(self):
        class InternalRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer, 'bar': Charstring})
        class ExternalRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer, 'bar': InternalRecord})
        valueInternal = {'foo': Integer(SimpleType()).assign(IntegerValue(1)),
                         'bar': Charstring(SimpleType()).assign(CharstringValue("WAX"))}
        internalRecord = InternalRecord().assign(valueInternal)
        valueExternal = {'foo': Integer(SimpleType()).assign(IntegerValue(2)),
                         'bar': internalRecord}
        externalRecord = ExternalRecord()
        externalRecord.assign(valueExternal)

    def test_AssignRaisesAnExceptionOnAnInvalidValue_InvalidType_BuiltIn(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer, 'bar': Charstring})
        type = MyRecord()
        for value in [True, 1, 1.0, "WAX", [1, 2], (1, 2)]:
            with self.assertRaises(InvalidTypeInAssignment):
                type.assign(value)

    def test_AssignRaisesAnExceptionOnAnInvalidValue_InvalidType_Special(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer, 'bar': Charstring})
        type = MyRecord()
        value = {'foo': Integer(SimpleType()).assign(IntegerValue(1)),
                 'bar': AnyValue()}
        with self.assertRaises(InvalidTypeInAssignment):
            type.assign(value)

    def test_AssignRaisesAnExceptionOnAnInvalidValue_IncompatibleDictionaries_AssignedEmpty(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer, 'bar': Charstring})
        type = MyRecord()
        with self.assertRaises(InvalidTypeInAssignment):
            type.assign({})

    def test_AssignRaisesAnExceptionOnAnInvalidValue_IncompatibleDictionaries_AssignedTooSmall(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer, 'bar': Charstring})
        type = MyRecord()
        value = {'foo': Integer(SimpleType()).assign(IntegerValue(1))}
        with self.assertRaises(InvalidTypeInAssignment):
            type.assign(value)

    def test_AssignRaisesAnExceptionOnAnInvalidValue_IncompatibleDictionaries_AssignedTooBig(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer, 'bar': Charstring})
        type = MyRecord()
        value = {'foo': Integer(SimpleType()).assign(IntegerValue(1)),
                 'bar': Charstring(SimpleType()).assign(CharstringValue("WAX")),
                 'baz': Integer(SimpleType()).assign(IntegerValue(2))}
        with self.assertRaises(InvalidTypeInAssignment):
            type.assign(value)

    def test_AssignRaisesAnExceptionOnAnInvalidValue_IncompatibleDictionaries_AssignedHasDifferentKeys(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer, 'bar': Charstring})
        type = MyRecord()
        value = {'foo': Integer(SimpleType()).assign(IntegerValue(1)),
                 'baz': Charstring(SimpleType()).assign(CharstringValue("WAX"))}
        with self.assertRaises(InvalidTypeInAssignment):
            type.assign(value)

    def test_AssignRaisesAnExceptionOnAnInvalidValue_IncompatibleDictionaries_AssignedHasChangedKeys(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer, 'bar': Charstring})
        type = MyRecord()
        value = {'bar': Integer(SimpleType()).assign(IntegerValue(1)),
                 'foo': Charstring(SimpleType()).assign(CharstringValue("WAX"))}
        with self.assertRaises(InvalidTypeInAssignment):
            type.assign(value)

    def test_AcceptReturnsFalseOnAnInvalidValue_NotInitializedNestedRecord(self):
        class InternalRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer, 'bar': Charstring})
        class ExternalRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer, 'bar': InternalRecord})
        internalRecord = InternalRecord()
        valueExternal = {'foo': Integer(SimpleType()).assign(IntegerValue(2)),
                         'bar': internalRecord}
        externalRecord = ExternalRecord()
        with self.assertRaises(InvalidTypeInAssignment):
            externalRecord.assign(valueExternal)

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
                Record.__init__(self, SimpleType(), {'foo': Integer, 'bar': Charstring})
        value = {'foo': Integer(SimpleType()).assign(IntegerValue(1)),
                 'bar': Charstring(SimpleType()).assign(CharstringValue("WAX"))}
        record1 = MyRecord().assign(value)
        record2 = MyRecord().assign(value)
        self.assertTrue(record1 == record2)

    def test_EqReturnsTrueOnSameValues_NestedRecords(self):
        class InternalRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer, 'bar': Charstring})
        class ExternalRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer, 'bar': InternalRecord})
        valueInternal = {'foo': Integer(SimpleType()).assign(IntegerValue(1)),
                         'bar': Charstring(SimpleType()).assign(CharstringValue("WAX"))}
        internalRecord = InternalRecord().assign(valueInternal)
        valueExternal = {'foo': Integer(SimpleType()).assign(IntegerValue(2)),
                         'bar': internalRecord}
        externalRecord1 = ExternalRecord()
        externalRecord2 = ExternalRecord()
        externalRecord1.assign(valueExternal)
        externalRecord2.assign(valueExternal)
        self.assertTrue(externalRecord1 == externalRecord2)

    def test_EqRaisesAnExceptionOnAnInvalidValue_InvalidType_BuiltIn(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer, 'bar': Charstring})
        value = {'foo': Integer(SimpleType()).assign(IntegerValue(1)),
                 'bar': Charstring(SimpleType()).assign(CharstringValue("WAX"))}
        record = MyRecord().assign(value)
        for value in [True, 1, 1.0, "WAX", [1, 2], (1, 2)]:
            with self.assertRaises(InvalidTypeInComparison):
                record == value

    def test_EqRaisesAnExceptionOnAnInvalidValue_InvalidType_Special(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer, 'bar': Charstring})
        value = {'foo': Integer(SimpleType()).assign(IntegerValue(1)),
                 'bar': Charstring(SimpleType()).assign(CharstringValue("WAX"))}
        record = MyRecord().assign(value)
        for value in [AnyValue()]:
            with self.assertRaises(InvalidTypeInComparison):
                record == value

    def test_EqRaisesAnExceptionOnAnInvalidValue_InvalidType_DifferentType(self):
        class MyRecord1(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer, 'bar': Charstring})
        class MyRecord2(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer, 'bar': Charstring})
        value1 = {'foo': Integer(SimpleType()).assign(IntegerValue(1)),
                  'bar': Charstring(SimpleType()).assign(CharstringValue("WAX"))}
        value2 = {'foo': Integer(SimpleType()).assign(IntegerValue(1)),
                  'bar': Charstring(SimpleType()).assign(CharstringValue("WAX"))}
        record1 = MyRecord1().assign(value1)
        record2 = MyRecord2().assign(value2)
        with self.assertRaises(InvalidTypeInComparison):
            record1 == record2

    def test_EqRaisesAnExceptionOnAnInvalidValue_IncompatibleDictionaries_SecondEmpty(self):
        record1 = Record(SimpleType(), {'foo': Integer, 'bar': Charstring})
        record2 = Record(SimpleType(), {})
        value1 = {'foo': Integer(SimpleType()).assign(IntegerValue(1)),
                  'bar': Charstring(SimpleType()).assign(CharstringValue("WAX"))}
        record1.assign(value1)
        record2.assign({})
        with self.assertRaises(InvalidTypeInComparison):
            record1 == record2

    def test_EqRaisesAnExceptionOnAnInvalidValue_IncompatibleDictionaries_SecondTooSmall(self):
        record1 = Record(SimpleType(), {'foo': Integer, 'bar': Charstring})
        record2 = Record(SimpleType(), {'foo': Integer})
        value1 = {'foo': Integer(SimpleType()).assign(IntegerValue(1)),
                  'bar': Charstring(SimpleType()).assign(CharstringValue("WAX"))}
        value2 = {'foo': Integer(SimpleType()).assign(IntegerValue(1))}
        record1.assign(value1)
        record2.assign(value2)
        with self.assertRaises(InvalidTypeInComparison):
            record1 == record2

    def test_EqRaisesAnExceptionOnAnInvalidValue_IncompatibleDictionaries_SecondTooBig(self):
        record1 = Record(SimpleType(), {'foo': Integer, 'bar': Charstring})
        record2 = Record(SimpleType(), {'foo': Integer, 'bar': Charstring, 'baz': Integer})
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
        record1 = Record(SimpleType(), {'foo': Integer, 'bar': Charstring})
        record2 = Record(SimpleType(), {'foo': Integer, 'baz': Charstring})
        value1 = {'foo': Integer(SimpleType()).assign(IntegerValue(1)),
                  'bar': Charstring(SimpleType()).assign(CharstringValue("WAX"))}
        value2 = {'foo': Integer(SimpleType()).assign(IntegerValue(1)),
                  'baz': Charstring(SimpleType()).assign(CharstringValue("WAX"))}
        record1.assign(value1)
        record2.assign(value2)
        with self.assertRaises(InvalidTypeInComparison):
            record1 == record2

    def test_AssignRaisesAnExceptionOnAnInvalidValue_IncompatibleDictionaries_AssignedHasChangedKeys(self):
        record1 = Record(SimpleType(), {'foo': Integer, 'bar': Charstring})
        record2 = Record(SimpleType(), {'bar': Integer, 'foo': Charstring})
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
                Record.__init__(self, SimpleType(), {'foo': Integer, 'bar': Charstring})
        value = {'foo': Integer(SimpleType()).assign(IntegerValue(1)),
                 'bar': Charstring(SimpleType()).assign(CharstringValue("WAX"))}
        record = MyRecord().assign(value)
        self.assertEqual(record.getField('foo'), Integer(SimpleType()).assign(IntegerValue(1)))
        self.assertEqual(record.getField('bar'), Charstring(SimpleType).assign(CharstringValue("WAX")))

    def test_GetFieldRaisesAnExceptionOnAnInvalidField(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, SimpleType(), {'foo': Integer, 'bar': Charstring})
        value = {'foo': Integer(SimpleType()).assign(IntegerValue(1)),
                 'bar': Charstring(SimpleType()).assign(CharstringValue("WAX"))}
        record = MyRecord().assign(value)
        with self.assertRaises(LookupErrorMissingField):
            record.getField('baz')

if __name__ == '__main__':
    unittest.main()
