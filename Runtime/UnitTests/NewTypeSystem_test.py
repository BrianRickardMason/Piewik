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

class NewTypeSystem_Integer_Ctor(unittest.TestCase):
    def test_Ctor(self):
        Integer(SimpleType())

class NewTypeSystem_Integer_Accept(unittest.TestCase):
    def test_AcceptRetursTrueOnAValidValue(self):
        type = Integer(SimpleType())
        for value in [IntegerValue(-1), IntegerValue(0), IntegerValue(1)]:
            self.assertTrue(type.accept(value))

    def test_AcceptRetursFalseOnAnInvalidValue(self):
        type = Integer(SimpleType())
        for value in [True, 1.0, "WAX"]:
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

class NewTypeSystem_Integer_Eq(unittest.TestCase):
    def test_EqReturnsTrueForSameValues(self):
        self.assertTrue(Integer(SimpleType()).assign(IntegerValue(1)) == Integer(SimpleType()).assign(IntegerValue(1)))

    def test_EqReturnsFalseForDifferentValues(self):
        self.assertFalse(Integer(SimpleType()).assign(IntegerValue(1)) == Integer(SimpleType()).assign(IntegerValue(2)))

    def test_EqRaisesAnExceptionForAnInvalidType(self):
        type = Integer(SimpleType()).assign(IntegerValue(1))
        for value in [True, 1.0, "WAX"]:
            with self.assertRaises(InvalidTypeInComparison):
                type == value

class NewTypeSystem_Integer_BoundedType_Ctor(unittest.TestCase):
    def test_Ctor(self):
        BoundedType(Integer(SimpleType()), IntegerValue(0), IntegerValue(10))

class NewTypeSystem_Integer_BoundedType_Accept(unittest.TestCase):
    def test_AcceptRetursTrueOnAValidValue(self):
        type = BoundedType(Integer(SimpleType()), IntegerValue(0), IntegerValue(10))
        for value in [IntegerValue(0), IntegerValue(1), IntegerValue(10)]:
            self.assertTrue(type.accept(value))

    def test_AcceptRetursFalseOnAnInvalidValue_InvalidType(self):
        type = BoundedType(Integer(SimpleType()), IntegerValue(0), IntegerValue(10))
        for value in [True, 1.0, "WAX"]:
            self.assertFalse(type.accept(value))

    def test_AcceptRetursFalseOnAnInvalidValue_InvalidValue(self):
        type = BoundedType(Integer(SimpleType()), IntegerValue(0), IntegerValue(10))
        for value in [IntegerValue(-1), IntegerValue(11)]:
            self.assertFalse(type.accept(value))

class NewTypeSystem_Integer_BoundedType_Assign(unittest.TestCase):
    def test_AssignAssignsOnAValidValue(self):
        type = BoundedType(Integer(SimpleType()), IntegerValue(0), IntegerValue(10))
        for value in [IntegerValue(0), IntegerValue(1), IntegerValue(10)]:
            self.assertEqual(type.assign(value).value(), value)

    def test_AssignRaisesAnExceptionOnAnInvalidValue_BuiltIn(self):
        type = BoundedType(Integer(SimpleType()), IntegerValue(0), IntegerValue(10))
        for value in [True, 1.0, "WAX"]:
            with self.assertRaises(InvalidTypeInAssignment):
                type.assign(value)

    def test_AssignRaisesAnExceptionOnAnInvalidValue_InvalidValue(self):
        type = BoundedType(Integer(SimpleType()), IntegerValue(0), IntegerValue(10))
        for value in [IntegerValue(-1), IntegerValue(11)]:
            with self.assertRaises(InvalidTypeInAssignment):
                type.assign(value)

class NewTypeSystem_Integer_BoundedType_Eq(unittest.TestCase):
    def test_EqReturnsTrueForSameValues(self):
        self.assertTrue(   BoundedType(Integer(SimpleType()), IntegerValue(0), IntegerValue(10)).assign(IntegerValue(1))
                        == BoundedType(Integer(SimpleType()), IntegerValue(0), IntegerValue(10)).assign(IntegerValue(1)))

    def test_EqReturnsFalseForDifferentValues(self):
        self.assertFalse(   BoundedType(Integer(SimpleType()), IntegerValue(0), IntegerValue(10)).assign(IntegerValue(1))
                         == BoundedType(Integer(SimpleType()), IntegerValue(0), IntegerValue(10)).assign(IntegerValue(2)))

    def test_EqRaisesAnExceptionForAnInvalidType(self):
        type = BoundedType(Integer(SimpleType()), IntegerValue(0), IntegerValue(10)).assign(IntegerValue(1))
        for value in [True, 1.0, "WAX"]:
            with self.assertRaises(InvalidTypeInComparison):
                type == value

class NewTypeSystem_Integer_TemplateType_Ctor(unittest.TestCase):
    def test_Ctor(self):
        TemplateType(Integer(SimpleType()))

class NewTypeSystem_Integer_TemplateType_Accept(unittest.TestCase):
    def test_AcceptRetursTrueOnAValidValue(self):
        type = TemplateType(Integer(SimpleType()))
        for value in [IntegerValue(-1), IntegerValue(0), IntegerValue(10), AnyValue()]:
            self.assertTrue(type.accept(value))

    def test_AcceptRetursFalseOnAnInvalidValue_InvalidType(self):
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
    def test_EqReturnsTrueForSameValues(self):
        for values in [(IntegerValue(1), IntegerValue(1)),
                       (IntegerValue(1), AnyValue()),
                       (AnyValue(), IntegerValue(1)),
                       (AnyValue(), AnyValue())]:
            self.assertTrue(   TemplateType(Integer(SimpleType())).assign(values[0])
                            == TemplateType(Integer(SimpleType())).assign(values[1]))

    def test_EqReturnsFalseForDifferentValues(self):
        self.assertFalse(   TemplateType(Integer(SimpleType())).assign(IntegerValue(1))
                         == TemplateType(Integer(SimpleType())).assign(IntegerValue(2)))

    def test_EqRaisesAnExceptionForAnInvalidType(self):
        type = TemplateType(Integer(SimpleType())).assign(IntegerValue(1))
        for value in [True, 1.0, "WAX"]:
            with self.assertRaises(InvalidTypeInComparison):
                type == value

if __name__ == '__main__':
    unittest.main()