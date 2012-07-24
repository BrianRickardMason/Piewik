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

from Type import *

class Type_Boolean(unittest.TestCase):

    # Positive construction.
    def testBooleanCtorSetsValueProperly(self):
        self.assertEqual(Boolean(True).value(), True)

    # Negative construction.
    def testBooleanCtorRaisesOnInvalidType_Integer(self):
        with self.assertRaises(InvalidTTCN3Type):
            Boolean(1)

    def testBooleanCtorRaisesOnInvalidType_Float(self):
        with self.assertRaises(InvalidTTCN3Type):
            Boolean(1.0)

    def testBooleanCtorRaisesOnInvalidType_Charstring(self):
        with self.assertRaises(InvalidTTCN3Type):
            Boolean("Charstring")

    # Positive matching.
    def testBooleanMatchReturnsTrueOnTheSameType(self):
        self.assertTrue(Boolean(True) == Boolean(True))

    # Negative matching.
    def testBooleanMatchReturnsFalseOnTheSameTypeAndDifferentValue(self):
        self.assertFalse(Boolean(True) == Boolean(False))

    def testBooleanMatchReturnsFalseOnDifferentType_Integer(self):
        self.assertFalse(Boolean(True) == Integer(1))

    def testBooleanMatchReturnsFalseOnDifferentType_Float(self):
        self.assertFalse(Boolean(True) == Float(1.0))

    def testBooleanMatchReturnsFalseOnDifferentType_Charstring(self):
        self.assertFalse(Boolean(True) == Charstring("qwe"))

    # Positive restrictions.
    def testBooleanCtorAllowsCreatingObjectWithRestriction_ValueList_OneElement(self):
        try:
            Boolean(True, [ValueList([Boolean(True)])])
        except:
            self.fail()

    def testBooleanCtorAllowsCreatingObjectWithRestriction_ValueList_ManyElements(self):
        try:
            Boolean(True,  [ValueList([Boolean(True), Boolean(False)])])
            Boolean(False, [ValueList([Boolean(True), Boolean(False)])])
        except:
            self.fail()

    # Negative restrictions.
    def testBooleanCtorRaisesOnInvalidRestriction_ValueList_OneElement(self):
        with self.assertRaises(UnmetRestriction):
            Boolean(True, [ValueList([Boolean(False)])])

class Type_Integer(unittest.TestCase):

    # Positive construction.
    def testIntegerCtorSetsValueProperly(self):
        self.assertEqual(Integer(1).value(), 1)

    # Negative construction.
    def testIntegerCtorRaisesOnInvalidType_Boolean(self):
        with self.assertRaises(InvalidTTCN3Type):
            Integer(True)

    def testIntegerCtorRaisesOnInvalidType_Float(self):
        with self.assertRaises(InvalidTTCN3Type):
            Integer(1.0)

    def testIntegerCtorRaisesOnInvalidType_Charstring(self):
        with self.assertRaises(InvalidTTCN3Type):
            Integer("Charstring")

    # Positive matching.
    def testIntegerMatchReturnsTrueOnTheSameType(self):
        self.assertTrue(Integer(1) == Integer(1))

    # Negative matching.
    def testIntegerMatchReturnsFalseOnTheSameTypeAndDifferentValue(self):
        self.assertFalse(Integer(1) == Integer(2))

    def testIntegerMatchReturnsFalseOnDifferentType_Boolean(self):
        self.assertFalse(Integer(1) == Boolean(False))

    def testIntegerMatchReturnsFalseOnDifferentType_Float(self):
        self.assertFalse(Integer(1) == Float(1.0))

    def testIntegerMatchReturnsFalseOnDifferentType_Charstring(self):
        self.assertFalse(Integer(1) == Charstring("poi"))

    # Positive restrictions.
    def testIntegerCtorAllowsCreatingObjectWithRestriction_ValueList_OneElement(self):
        try:
            Integer(1, [ValueList([Integer(1)])])
        except:
            self.fail()

    def testIntegerCtorAllowsCreatingObjectWithRestriction_ValueList_ManyElements(self):
        try:
            Integer(1, [ValueList([Integer(1), Integer(2), Integer(3)])])
            Integer(2, [ValueList([Integer(1), Integer(2), Integer(3)])])
            Integer(3, [ValueList([Integer(1), Integer(2), Integer(3)])])
        except:
            self.fail()

    # Negative restrictions.
    def testIntegerCtorRaisesOnInvalidRestriction_ValueList_OneElement(self):
        with self.assertRaises(UnmetRestriction):
            Integer(1, [ValueList([Integer(2)])])

    def testIntegerCtorRaisesOnInvalidRestriction_ValueList_ManyElements(self):
        with self.assertRaises(UnmetRestriction):
            Integer(1, [ValueList([Integer(2), Integer(3), Integer(4)])])

class Type_Float(unittest.TestCase):

    # Positive construction.
    def testFloatCtorSetsValueProperly(self):
        self.assertEqual(Float(1.0).value(), 1.0)

    # Negative construction.
    def testFloatCtorRaisesOnInvalidType_Boolean(self):
        with self.assertRaises(InvalidTTCN3Type):
            Float(True)

    def testFloatCtorRaisesOnInvalidType_Integer(self):
        with self.assertRaises(InvalidTTCN3Type):
            Float(1)

    def testFloatCtorRaisesOnInvalidType_Charstring(self):
        with self.assertRaises(InvalidTTCN3Type):
            Float("Charstring")

    # Positive matching.
    def testFloatMatchReturnsTrueOnTheSameType(self):
        self.assertTrue(Float(1.0) == Float(1.0))

    # Negative matching.
    def testFloatMatchReturnsFalseOnTheSameTypeAndDifferentValue(self):
        self.assertFalse(Float(1.0) == Float(2.0))

    def testFloatMatchReturnsFalseOnDifferentType_Boolean(self):
        self.assertFalse(Float(1.0) == Boolean(False))

    def testFloatMatchReturnsFalseOnDifferentType_Integer(self):
        self.assertFalse(Float(1.0) == Integer(1))

    def testFloatMatchReturnsFalseOnDifferentType_Charstring(self):
        self.assertFalse(Float(1.0) == Charstring("qwe"))

    # Positive restrictions.
    def testFloatCtorAllowsCreatingObjectWithRestriction_ValueList_OneElement(self):
        try:
            Float(1.0, [ValueList([Float(1.0)])])
        except:
            self.fail()

    def testFloatCtorAllowsCreatingObjectWithRestriction_ValueList_ManyElements(self):
        try:
            Float(1.0, [ValueList([Float(1.0), Float(2.0), Float(3.0)])])
            Float(2.0, [ValueList([Float(1.0), Float(2.0), Float(3.0)])])
            Float(3.0, [ValueList([Float(1.0), Float(2.0), Float(3.0)])])
        except:
            self.fail()

    # Negative restrictions.
    def testFloatCtorRaisesOnInvalidRestriction_ValueList_OneElement(self):
        with self.assertRaises(UnmetRestriction):
            Float(1.0, [ValueList([Float(2.0)])])

    def testFloatCtorRaisesOnInvalidRestriction_ValueList_ManyElements(self):
        with self.assertRaises(UnmetRestriction):
            Float(1.0, [ValueList([Float(2.0), Float(3.0), Float(4.0)])])

class Type_Charstring(unittest.TestCase):

    # Positive construction.
    def testCharstringCtorSetsValueProperly(self):
        self.assertEqual(Charstring("tyrytyr").value(), "tyrytyr")

    # Negative construction.
    def testCharstringCtorRaisesOnInvalidType_Boolean(self):
        with self.assertRaises(InvalidTTCN3Type):
            Charstring(True)

    def testCharstringCtorRaisesOnInvalidType_Integer(self):
        with self.assertRaises(InvalidTTCN3Type):
            Charstring(1)

    def testCharstringCtorRaisesOnInvalidType_Float(self):
        with self.assertRaises(InvalidTTCN3Type):
            Charstring(1.0)

    # Positive matching.
    def testCharstringMatchReturnsTrueOnTheSameType(self):
        self.assertTrue(Charstring("qwert") == Charstring("qwert"))

    # Negative matching.
    def testCharstringMatchReturnsFalseOnTheSameTypeAndDifferentValue(self):
        self.assertFalse(Charstring("qwert") == Charstring("yuiop"))

    def testCharstringMatchReturnsFalseOnDifferentType_Boolean(self):
        self.assertFalse(Charstring("qwert") == Boolean(False))

    def testCharstringMatchReturnsFalseOnDifferentType_Integer(self):
        self.assertFalse(Charstring("qwert") == Integer(1))

    def testCharstringMatchReturnsFalseOnDifferentType_Float(self):
        self.assertFalse(Charstring("qwert") == Float(1.0))

    # Positive restrictions.
    def testCharstringCtorAllowsCreatingObjectWithRestriction_ValueList_OneElement(self):
        try:
            Charstring("asdf", [ValueList([Charstring("asdf")])])
        except:
            self.fail()

    def testCharstringCtorAllowsCreatingObjectWithRestriction_ValueList_ManyElements(self):
        try:
            Charstring("asdf", [ValueList([Charstring("asdf"), Charstring("qwer"), Charstring("zxcv")])])
            Charstring("qwer", [ValueList([Charstring("asdf"), Charstring("qwer"), Charstring("zxcv")])])
            Charstring("zxcv", [ValueList([Charstring("asdf"), Charstring("qwer"), Charstring("zxcv")])])
        except:
            self.fail()

    # Negative restrictions.
    def testCharstringCtorRaisesOnInvalidRestriction_ValueList_OneElement(self):
        with self.assertRaises(UnmetRestriction):
            Charstring("asdf", [ValueList([Charstring("sdf")])])

    def testCharstringCtorRaisesOnInvalidRestriction_ValueList_ManyElements(self):
        with self.assertRaises(UnmetRestriction):
            Charstring("poiu", [ValueList([Charstring("asdf"), Charstring("qwer"), Charstring("zxcv")])])

class Type_Record(unittest.TestCase):

    # Positive construction.
    def testRecordCtorConstructsAnEmptyRecord(self):
        Record()

    def testRecordCtorConstructsANonEmptyRecord(self):
        Record({'foo': Integer(1), 'bar': Float(123.4)})

    def testRecordCtorConstructsANestedRecord(self):
        Record({'foo': Integer(1), 'bar': Float(123.4), 'baz': Record({'foo': Charstring("SD")})})

    # Negative construction.
    def testRecordCtorRaisesOnInvalidType_Boolean(self):
        with self.assertRaises(InvalidTTCN3Type):
            Record(True)

    def testRecordCtorRaisesOnInvalidType_AnyOfElementsIsAnInvalidPiewikType(self):
        with self.assertRaises(InvalidTTCN3Type):
            Record({'foo': Integer(1), 'bar': Float(True)})

    def testRecordCtorRaisesOnInvalidType_AnyOfElementsIsNotAPiewikType(self):
        with self.assertRaises(InvalidTTCN3Type):
            Record({'foo': Integer(1), 'bar': 12})

    # Positive matching.
    def testRecordMatchReturnsTrueOnTheSameType(self):
        record1 = Record({'foo': Integer(1), 'bar': Float(22.2)})
        record2 = Record({'foo': Integer(1), 'bar': Float(22.2)})
        self.assertTrue(record1 == record2)

    def testRecordMatchReturnsTrueOnTheSameType_OrderDoesNotMatter(self):
        record1 = Record({'foo': Integer(1), 'bar': Float(22.2)})
        record2 = Record({'bar': Float(22.2), 'foo': Integer(1)})
        self.assertTrue(record1 == record2)

    # Negative matching.
    def testRecordMatchReturnsFalseOnTheSameTypeAndDifferentValue(self):
        record1 = Record({'foo': Integer(1), 'bar': Float(22.2)})
        record2 = Record({'foo': Integer(1), 'bar': Float(24.2)})
        self.assertFalse(record1 == record2)

    def testRecordMatchReturnsFalseOnTheSameValues_FirstLonger(self):
        record1 = Record({'foo': Integer(1), 'bar': Float(22.2), 'baz': Charstring("Exist")})
        record2 = Record({'foo': Integer(1), 'bar': Float(22.2)})
        self.assertFalse(record1 == record2)

    def testRecordMatchReturnsFalseOnTheSameValues_SecondLonger(self):
        record1 = Record({'foo': Integer(1), 'bar': Float(22.2)})
        record2 = Record({'foo': Integer(1), 'bar': Float(22.2), 'baz': Charstring("Exist")})
        self.assertFalse(record1 == record2)

    def testRecordMatchReturnsFalseOnDifferentType_Boolean(self):
        self.assertFalse(Record({'foo': Integer(1), 'bar': Float(22.2)}) == Boolean(True))

if __name__ == '__main__':
    unittest.main()
