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

from Runtime.TypeSystem import *

class TypeSystem_Boolean(unittest.TestCase):
    #
    # Constructions.
    #
    def test_CtorConstructsAProperVariableAndSetsProperDefaultValue(self):
        try:
            self.assertEqual(Boolean().value(), False)
        except:
            self.fail()

    #
    # Successful assignments.
    #
    def test_AssignAssignsProperValue_Boolean(self):
        self.assertEqual(Boolean().assign(True).value(), True)

    #
    # Unsuccessful assignments.
    #
    # TODO: All types.
    #
    def test_AssignRaisesAnExceptionIfCalledWithInvalidType_Integer(self):
        with self.assertRaises(InvalidTTCN3TypeInAssignment):
            Boolean().assign(1)

    def test_AssignRaisesAnExceptionIfCalledWithInvalidType_Float(self):
        with self.assertRaises(InvalidTTCN3TypeInAssignment):
            Boolean().assign(1.0)

    def test_AssignRaisesAnExceptionIfCalledWithInvalidType_String(self):
        with self.assertRaises(InvalidTTCN3TypeInAssignment):
            Boolean().assign("WAX")

    #
    # Successful matching.
    #
    def test_ComparisonReturnsTrueForTwoVariablesWithTheSameValue(self):
        self.assertTrue(Boolean().assign(True) == Boolean().assign(True))

    #
    # Unsuccessful matching.
    #
    def test_ComparisonReturnsFalseForTwoVariablesWithDifferentValues(self):
        self.assertFalse(Boolean().assign(True) == Boolean().assign(False))

    #
    # TODO: All types.
    #
    def test_ComparisonRaisesAnExceptionIfCalledWithInvalidType_Integer(self):
        with self.assertRaises(InvalidTTCN3TypeInComparison):
            Boolean().assign(True) == Integer().assign(1)

    def test_ComparisonRaisesAnExceptionIfCalledWithInvalidType_Float(self):
        with self.assertRaises(InvalidTTCN3TypeInComparison):
            Boolean().assign(True) == Float().assign(1.0)

    def test_ComparisonRaisesAnExceptionIfCalledWithInvalidType_Charstring(self):
        with self.assertRaises(InvalidTTCN3TypeInComparison):
            Boolean().assign(True) == Charstring().assign("WAX")

class TypeSystem_Integer(unittest.TestCase):
    #
    # Constructions.
    #
    def test_CtorConstructsAProperVariableAndSetsProperDefaultValue(self):
        try:
            self.assertEqual(Integer().value(), 0)
        except:
            self.fail()

    #
    # Successful assignments.
    #
    def test_AssignAssignsProperValue_Integer(self):
        self.assertEqual(Integer().assign(1).value(), 1)

    #
    # Unsuccessful assignments.
    #
    # TODO: All types.
    #
    def test_AssignRaisesAnExceptionIfCalledWithInvalidType_Boolean(self):
        with self.assertRaises(InvalidTTCN3TypeInAssignment):
            Integer().assign(True)

    def test_AssignRaisesAnExceptionIfCalledWithInvalidType_Float(self):
        with self.assertRaises(InvalidTTCN3TypeInAssignment):
            Integer().assign(1.0)

    def test_AssignRaisesAnExceptionIfCalledWithInvalidType_String(self):
        with self.assertRaises(InvalidTTCN3TypeInAssignment):
            Integer().assign("WAX")

    #
    # Successful matching.
    #
    def test_ComparisonReturnsTrueForTwoVariablesWithTheSameValue(self):
        self.assertTrue(Integer().assign(1) == Integer().assign(1))

    #
    # Unsuccessful matching.
    #
    def test_ComparisonReturnsFalseForTwoVariablesWithDifferentValues(self):
        self.assertFalse(Integer().assign(1) == Integer().assign(2))

    #
    # TODO: All types.
    #
    def test_ComparisonRaisesAnExceptionIfCalledWithInvalidType_Boolean(self):
        with self.assertRaises(InvalidTTCN3TypeInComparison):
            Integer().assign(1) == Boolean().assign(True)

    def test_ComparisonRaisesAnExceptionIfCalledWithInvalidType_Float(self):
        with self.assertRaises(InvalidTTCN3TypeInComparison):
            Integer().assign(1) == Float().assign(1.0)

    def test_ComparisonRaisesAnExceptionIfCalledWithInvalidType_Charstring(self):
        with self.assertRaises(InvalidTTCN3TypeInComparison):
            Integer().assign(1) == Charstring().assign("WAX")

    def test_ComparisonRaisesAnExceptionIfCalledWithInvalidType_AnyOrNone(self):
        with self.assertRaises(InvalidTTCN3TypeInComparison):
            self.assertTrue(Integer().assign(1) == AnyOrNone())

    def test_ComparisonRaisesAnExceptionIfCalledWithInvalidType_AnySingleElement(self):
        with self.assertRaises(InvalidTTCN3TypeInComparison):
            self.assertTrue(Integer().assign(1) == AnySingleElement())

class TypeSystem_Float(unittest.TestCase):
    #
    # Constructions.
    #
    def test_CtorConstructsAProperVariableAndSetsProperDefaultValue(self):
        try:
            self.assertEqual(Float().value(), 0.0)
        except:
            self.fail()

    #
    # Successful assignments.
    #
    def test_AssignAssignsProperValue(self):
        self.assertEqual(Float().assign(1.0).value(), 1.0)

    #
    # Unsuccessful assignments.
    #
    # TODO: All types.
    #
    def test_AssignRaisesAnExceptionIfCalledWithInvalidType_Boolean(self):
        with self.assertRaises(InvalidTTCN3TypeInAssignment):
            Float().assign(True)

    def test_AssignRaisesAnExceptionIfCalledWithInvalidType_Integer(self):
        with self.assertRaises(InvalidTTCN3TypeInAssignment):
            Float().assign(1)

    def test_AssignRaisesAnExceptionIfCalledWithInvalidType_String(self):
        with self.assertRaises(InvalidTTCN3TypeInAssignment):
            Float().assign("WAX")

    #
    # Successful matching.
    #
    def test_ComparisonReturnsTrueForTwoVariablesWithTheSameValue(self):
        self.assertTrue(Float().assign(1.0) == Float().assign(1.0))

    #
    # Unsuccessful matching.
    #
    def test_ComparisonReturnsFalseForTwoVariablesWithDifferentValues(self):
        self.assertFalse(Float().assign(1.0) == Float().assign(2.0))

    #
    # TODO: All types.
    #
    def test_ComparisonRaisesAnExceptionIfCalledWithInvalidType_Boolean(self):
        with self.assertRaises(InvalidTTCN3TypeInComparison):
            Float().assign(1.0) == Boolean().assign(True)

    def test_ComparisonRaisesAnExceptionIfCalledWithInvalidType_Integer(self):
        with self.assertRaises(InvalidTTCN3TypeInComparison):
            Float().assign(1.0) == Integer().assign(1)

    def test_ComparisonRaisesAnExceptionIfCalledWithInvalidType_Charstring(self):
        with self.assertRaises(InvalidTTCN3TypeInComparison):
            Float().assign(1.0) == Charstring().assign("WAX")

class TypeSystem_Charstring(unittest.TestCase):
    #
    # Constructions.
    #
    def test_CtorConstructsAProperVariableAndSetsProperDefaultValue(self):
        try:
            self.assertEqual(Charstring().value(), "")
        except:
            self.fail()

    #
    # Successful assignments.
    #
    def test_AssignAssignsProperValue_Charstring(self):
        self.assertEqual(Charstring().assign("WAX").value(), "WAX")

    #
    # Unsuccessful assignments.
    #
    # TODO: All types.
    #
    def test_AssignRaisesAnExceptionIfCalledWithInvalidType_Boolean(self):
        with self.assertRaises(InvalidTTCN3TypeInAssignment):
            Charstring().assign(True)

    def test_AssignRaisesAnExceptionIfCalledWithInvalidType_Integer(self):
        with self.assertRaises(InvalidTTCN3TypeInAssignment):
            Charstring().assign(1)

    def test_AssignRaisesAnExceptionIfCalledWithInvalidType_Float(self):
        with self.assertRaises(InvalidTTCN3TypeInAssignment):
            Charstring().assign(1.0)

    #
    # Successful matching.
    #
    def test_ComparisonReturnsTrueForTwoVariablesWithTheSameValue(self):
        self.assertTrue(Charstring().assign("WAX") == Charstring().assign("WAX"))

    #
    # Unsuccessful matching.
    #
    def test_ComparisonReturnsFalseForTwoVariablesWithDifferentValues(self):
        self.assertFalse(Charstring().assign("WAX") == Charstring().assign("XAW"))

    #
    # TODO: All types.
    #
    def test_ComparisonRaisesAnExceptionIfCalledWithInvalidType_Boolean(self):
        with self.assertRaises(InvalidTTCN3TypeInComparison):
            Charstring().assign("WAX") == Boolean().assign(True)

    def test_ComparisonRaisesAnExceptionIfCalledWithInvalidType_Integer(self):
        with self.assertRaises(InvalidTTCN3TypeInComparison):
            Charstring().assign("WAX") == Integer().assign(1)

    def test_ComparisonRaisesAnExceptionIfCalledWithInvalidType_Float(self):
        with self.assertRaises(InvalidTTCN3TypeInComparison):
            Charstring().assign("WAX") == Float().assign(1.0)

class TypeSystem_Record(unittest.TestCase):
    #
    # Successful constructions.
    #
    def test_CtorConstructsAProperVariableAndSetsProperValue_EmptyRecord(self):
        class myRecord(Record):
            def __init__(self):
                Record.__init__(self, {})
        myRecordInstance = myRecord()

    def test_CtorConstructsAProperVariableAndSetsProperValue_NonEmptyRecord(self):
        class myRecord(Record):
            def __init__(self):
                Record.__init__(self, {'field1': Integer, 'field2': Charstring})
        myRecordInstance = myRecord()

    #
    # Unsuccessful constructions.
    #
    def test_CtorRaisesAnExceptionForInvalidValue_NonTTCN3Type(self):
        class myRecord(Record):
            def __init__(self):
                Record.__init__(self, {'field1': int})
        with self.assertRaises(InvalidTTCN3TypeInCtor):
            myRecordInstance = myRecord()

    #
    # TODO: All types.
    #
    def test_CtorRaisesAnExceptionForInvalidValue_SpecialSymbolUsedInsteadOfValue(self):
        class myRecord(Record):
            def __init__(self):
                Record.__init__(self, {'field1': AnyOrNone})
        with self.assertRaises(InvalidTTCN3TypeInCtor):
            myRecordInstance = myRecord()

    #
    # Successful assignments.
    #
    def test_AssignmentOfAProperValue_EmptyRecord(self):
        class myRecord(Record):
            def __init__(self):
                Record.__init__(self, {})
        myRecordInstance = myRecord()
        myRecordInstance.assign({})

    def test_AssignmentOfAProperValue_NonEmptyRecord(self):
        class myRecord(Record):
            def __init__(self):
                Record.__init__(self, {'field1': Integer,
                                       'field2': Charstring})
        myRecordInstance = myRecord()
        myRecordInstance.assign({'field1': Integer().assign(1),
                                 'field2': Charstring().assign("QUARK")})
        self.assertEqual(myRecordInstance.getField('field1').value(), 1)
        self.assertEqual(myRecordInstance.getField('field2').value(), "QUARK")

    def test_AssignmentOfAProperValue_SpecialSymbolUsedInsideAValue_AnySingleElement(self):
        class myRecord(Record):
            def __init__(self):
                Record.__init__(self, {'field1': Integer,
                                       'field2': Charstring})
        myRecordInstance = myRecord()
        myRecordInstance.assign({'field1': AnySingleElement(),
                                 'field2': AnySingleElement()})

    #
    # Unsuccessful assignments.
    #
    def test_AssignmentRaisesAnExceptionForInvalidValue_AssigningNotADictionary(self):
        class myRecord(Record):
            def __init__(self):
                Record.__init__(self, {})
        myRecordInstance = myRecord()
        with self.assertRaises(InvalidTTCN3TypeInAssignment):
            myRecordInstance.assign(Integer().assign(1))

    def test_AssignmentRaisesAnExceptionForInvalidValue_AssigningNonEmptyRecordToAnEmptyRecord(self):
        class myRecord(Record):
            def __init__(self):
                Record.__init__(self, {})
        myRecordInstance = myRecord()
        with self.assertRaises(InvalidTTCN3TypeInAssignment):
            myRecordInstance.assign({'field1': Integer().assign(1)})

    def test_AssignmentRaisesAnExceptionForInvalidValue_AssigningAnEmptyRecordToANonEmptyRecord(self):
        class myRecord(Record):
            def __init__(self):
                Record.__init__(self, {'field1': Integer,
                                       'field2': Charstring})
        myRecordInstance = myRecord()
        with self.assertRaises(InvalidTTCN3TypeInAssignment):
            myRecordInstance.assign({})

    def test_AssignmentRaisesAnExceptionForInvalidValue_MissingFieldsOfTheRecord(self):
        class myRecord(Record):
            def __init__(self):
                Record.__init__(self, {'field1': Integer,
                                       'field2': Charstring})
        myRecordInstance = myRecord()
        with self.assertRaises(InvalidTTCN3TypeInAssignment):
            myRecordInstance.assign({'field1': Integer().assign(1)})

    def test_AssignmentRaisesAnExceptionForInvalidValue_ExtraneousFieldsOfTheRecord(self):
        class myRecord(Record):
            def __init__(self):
                Record.__init__(self, {'field1': Integer,
                                       'field2': Charstring})
        myRecordInstance = myRecord()
        with self.assertRaises(InvalidTTCN3TypeInAssignment):
            myRecordInstance.assign({'field1': Integer().assign(1),
                                     'field2': Charstring().assign("QUARK"),
                                     'field3': Integer().assign(3)})

    def test_AssignmentRaisesAnExceptionForInvalidValue_InvalidTypeOfTheRecordField(self):
        class myRecord(Record):
            def __init__(self):
                Record.__init__(self, {'field1': Integer,
                                       'field2': Charstring})
        myRecordInstance = myRecord()
        with self.assertRaises(InvalidTTCN3TypeInAssignment):
            myRecordInstance.assign({'field1': Integer().assign(1),
                                     'field2': Integer().assign(2)})

    def test_AssignmentRaisesAnExceptionForInvalidValue_ChangedTypesOfTheRecordField(self):
        class myRecord(Record):
            def __init__(self):
                Record.__init__(self, {'field1': Integer,
                                       'field2': Charstring})
        myRecordInstance = myRecord()
        with self.assertRaises(InvalidTTCN3TypeInAssignment):
            myRecordInstance.assign({'field2': Integer().assign(1),
                                     'field1': Charstring().assign("QUARK")})

    def test_AssignmentRaisesAnExceptionForInvalidValue_SpecialSymbolUsedInsteadOfAValueUsed(self):
        class myRecord(Record):
            def __init__(self):
                Record.__init__(self, {'field1': Integer,
                                       'field2': Charstring})
        myRecordInstance = myRecord()
        with self.assertRaises(InvalidTTCN3TypeInAssignment):
            myRecordInstance.assign({'field2': Integer().assign(1),
                                     'field1': AnyOrNone()})

    # TODO: Comparison with AnyOrNone, AnySingleElement.

class TypeSystem_RecordOf_Ctor(unittest.TestCase):
    #
    # Successful constructions.
    #
    # TODO: All types.
    #
    def test_CtorConstructsAProperVariable_Boolean(self):
        try:
            class MyRecordOf(RecordOf):
                def __init__(self):
                    RecordOf.__init__(self, Boolean)
            recordOf = MyRecordOf()
        except:
            self.fail()

    def test_CtorConstructsAProperVariable_Integer(self):
        try:
            class MyRecordOf(RecordOf):
                def __init__(self):
                    RecordOf.__init__(self, Integer)
            recordOf = MyRecordOf()
        except:
            self.fail()

    def test_CtorConstructsAProperVariable_Float(self):
        try:
            class MyRecordOf(RecordOf):
                def __init__(self):
                    RecordOf.__init__(self, Float)
            recordOf = MyRecordOf()
        except:
            self.fail()

    def test_CtorConstructsAProperVariable_Charstring(self):
        try:
            class MyRecordOf(RecordOf):
                def __init__(self):
                    RecordOf.__init__(self, Charstring)
            recordOf = MyRecordOf()
        except:
            self.fail()

    #
    # Unsuccessful constructions.
    #
    def test_CtorRaisesAnExceptionForInvalidValue(self):
        with self.assertRaises(InvalidTTCN3TypeInCtor):
            class MyRecordOf(RecordOf):
                def __init__(self):
                    RecordOf.__init__(self, int)
            recordOf = MyRecordOf()

class TypeSystem_RecordOf_Assign(unittest.TestCase):
    #
    # Successful assignments.
    #
    def test_AssignementOfProperValue_EmptyList(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, Boolean)
        myRecordOf = MyRecordOf()
        self.assertEqual(myRecordOf.assign([]).value(), [])

    def test_AssignementOfProperValue_NonEmptyList(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, Integer)
        myRecordOf = MyRecordOf()
        self.assertEqual(myRecordOf.assign([Integer().assign(1), Integer().assign(2)]).value(),
                         [Integer().assign(1), Integer().assign(2)])

    #
    # Unsuccessful assignments.
    #
    # TODO: All types.
    #
    def test_AssignRaisesAnExceptionIfCalledWithInvalidType_NotATTCN3Type(self):
        with self.assertRaises(InvalidTTCN3TypeInAssignment):
            class MyRecordOf(RecordOf):
                def __init__(self):
                    RecordOf.__init__(self, Integer)
            myRecordOf = MyRecordOf()
            myRecordOf.assign(True)

    def test_AssignRaisesAnExceptionIfCalledWithInvalidType_Boolean(self):
        with self.assertRaises(InvalidTTCN3TypeInAssignment):
            class MyRecordOf(RecordOf):
                def __init__(self):
                    RecordOf.__init__(self, Integer)
            myRecordOf = MyRecordOf()
            myRecordOf.assign(Boolean().assign(True))

    def test_AssignRaisesAnExceptionIfCalledWithInvalidType_Integer(self):
        with self.assertRaises(InvalidTTCN3TypeInAssignment):
            class MyRecordOf(RecordOf):
                def __init__(self):
                    RecordOf.__init__(self, Integer)
            myRecordOf = MyRecordOf()
            myRecordOf.assign(Integer().assign(1))

    def test_AssignRaisesAnExceptionIfCalledWithInvalidType_Float(self):
        with self.assertRaises(InvalidTTCN3TypeInAssignment):
            class MyRecordOf(RecordOf):
                def __init__(self):
                    RecordOf.__init__(self, Integer)
            myRecordOf = MyRecordOf()
            myRecordOf.assign(Float().assign(1.0))

    def test_AssignRaisesAnExceptionIfCalledWithInvalidType_Charstring(self):
        with self.assertRaises(InvalidTTCN3TypeInAssignment):
            class MyRecordOf(RecordOf):
                def __init__(self):
                    RecordOf.__init__(self, Integer)
            myRecordOf = MyRecordOf()
            myRecordOf.assign(Charstring().assign("WAX"))

    def test_AssignRaisesAnExceptionIfCalledWithInvalidType_ValidType_InvalidContent_OneElement(self):
        with self.assertRaises(InvalidTTCN3TypeInAssignment):
            class MyRecordOf(RecordOf):
                def __init__(self):
                    RecordOf.__init__(self, Integer)
            myRecordOf = MyRecordOf()
            myRecordOf.assign([Float().assign(1.0)])

    def test_AssignRaisesAnExceptionIfCalledWithInvalidType_ValidType_InvalidContent_OneOfElements(self):
        with self.assertRaises(InvalidTTCN3TypeInAssignment):
            class MyRecordOf(RecordOf):
                def __init__(self):
                    RecordOf.__init__(self, Integer)
            myRecordOf = MyRecordOf()
            myRecordOf.assign([Integer().assign(1), Float().assign(1.0), Integer().assign(2)])

class TypeSystem_RecordOf_GetField(unittest.TestCase):
    #
    # Getting a field.
    #
    def test_GetFieldReturnsTheValueOfTheField(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, Integer)
        myRecordOf = MyRecordOf()
        myRecordOf.assign([Integer().assign(1), Integer().assign(2), Integer().assign(3)])
        self.assertEqual(myRecordOf.getField(1), Integer().assign(2))


    def test_GetFieldRaisesAnExceptionForMissingField(self):
        with self.assertRaises(LookupErrorMissingField):
            class MyRecordOf(RecordOf):
                def __init__(self):
                    RecordOf.__init__(self, Integer)
            myRecordOf = MyRecordOf()
            myRecordOf.assign([Integer().assign(1), Integer().assign(2), Integer().assign(3)])
            myRecordOf.getField(4)

class TypeSystem_RecordOf_Eq(unittest.TestCase):
    #
    # Successful matching.
    #
    def test_ComparisonReturnsTrueForTwoVariablesWithTheSameValue_EmptyRecordsOf(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, Integer)
        myRecordOf1 = MyRecordOf()
        myRecordOf2 = MyRecordOf()
        self.assertTrue(myRecordOf1 == myRecordOf2)
        self.assertTrue(myRecordOf2 == myRecordOf1)

    def test_ComparisonReturnsTrueForTwoVariablesWithTheSameValue_OneElement(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, Integer)
        myRecordOf1 = MyRecordOf()
        myRecordOf2 = MyRecordOf()
        myRecordOf1.assign([Integer().assign(1)])
        myRecordOf2.assign([Integer().assign(1)])
        self.assertTrue(myRecordOf1 == myRecordOf2)
        self.assertTrue(myRecordOf2 == myRecordOf1)

    def test_ComparisonReturnsTrueForTwoVariablesWithTheSameValue_ManyElements(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, Integer)
        myRecordOf1 = MyRecordOf()
        myRecordOf2 = MyRecordOf()
        myRecordOf1.assign([Integer().assign(1), Integer().assign(2), Integer().assign(3)])
        myRecordOf2.assign([Integer().assign(1), Integer().assign(2), Integer().assign(3)])
        self.assertTrue(myRecordOf1 == myRecordOf2)
        self.assertTrue(myRecordOf2 == myRecordOf1)

    #
    # Unsuccessful matching.
    #
    def test_ComparisonReturnsFalseForTwoVariablesWithDifferentValues_OneElement(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, Integer)
        myRecordOf1 = MyRecordOf()
        myRecordOf2 = MyRecordOf()
        myRecordOf1.assign([Integer().assign(1)])
        myRecordOf2.assign([Integer().assign(2)])
        self.assertFalse(myRecordOf1 == myRecordOf2)
        self.assertFalse(myRecordOf2 == myRecordOf1)

    def test_ComparisonReturnsFalseForTwoVariablesWithDifferentValues_OneElement_DifferentLength(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, Integer)
        myRecordOf1 = MyRecordOf()
        myRecordOf2 = MyRecordOf()
        myRecordOf1.assign([Integer().assign(1)])
        myRecordOf2.assign([Integer().assign(1), Integer().assign(2)])
        self.assertFalse(myRecordOf1 == myRecordOf2)
        self.assertFalse(myRecordOf2 == myRecordOf1)

    def test_ComparisonReturnsFalseForTwoVariablesWithDifferentValues_OneElement_DifferentLength_OneEmpty(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, Integer)
        myRecordOf1 = MyRecordOf()
        myRecordOf2 = MyRecordOf()
        myRecordOf1.assign([])
        myRecordOf2.assign([Integer().assign(1), Integer().assign(2)])
        self.assertFalse(myRecordOf1 == myRecordOf2)
        self.assertFalse(myRecordOf2 == myRecordOf1)

    def test_ComparisonReturnsFalseForTwoVariablesWithDifferentValues_ManyElements(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, Integer)
        myRecordOf1 = MyRecordOf()
        myRecordOf2 = MyRecordOf()
        myRecordOf1.assign([Integer().assign(1), Integer().assign(2), Integer().assign(3)])
        myRecordOf2.assign([Integer().assign(1), Integer().assign(2), Integer().assign(4)])
        self.assertFalse(myRecordOf1 == myRecordOf2)
        self.assertFalse(myRecordOf2 == myRecordOf1)

    def test_ComparisonReturnsFalseForTwoVariablesWithDifferentValues_ManyElements_SequenceMatters(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, Integer)
        myRecordOf1 = MyRecordOf()
        myRecordOf2 = MyRecordOf()
        myRecordOf1.assign([Integer().assign(1), Integer().assign(2), Integer().assign(3)])
        myRecordOf2.assign([Integer().assign(1), Integer().assign(3), Integer().assign(2)])
        self.assertFalse(myRecordOf1 == myRecordOf2)
        self.assertFalse(myRecordOf2 == myRecordOf1)

    #
    # TODO: All types.
    #
    def test_ComparisonRaisesAnExceptionIfCalledWithInvalidType_Boolean(self):
        with self.assertRaises(InvalidTTCN3TypeInComparison):
            class MyRecordOf(RecordOf):
                def __init__(self):
                    RecordOf.__init__(self, Integer)
            myRecordOf = MyRecordOf()
            myRecordOf.assign([Integer().assign(1)])
            RecordOf(myRecordOf == Boolean().assign(True))

    def test_ComparisonRaisesAnExceptionIfCalledWithInvalidType_Integer(self):
        with self.assertRaises(InvalidTTCN3TypeInComparison):
            class MyRecordOf(RecordOf):
                def __init__(self):
                    RecordOf.__init__(self, Integer)
            myRecordOf = MyRecordOf()
            myRecordOf.assign([Integer().assign(1)])
            RecordOf(myRecordOf == Integer().assign(1))

    def test_ComparisonRaisesAnExceptionIfCalledWithInvalidType_Float(self):
        with self.assertRaises(InvalidTTCN3TypeInComparison):
            class MyRecordOf(RecordOf):
                def __init__(self):
                    RecordOf.__init__(self, Integer)
            myRecordOf = MyRecordOf()
            myRecordOf.assign([Integer().assign(1)])
            RecordOf(myRecordOf == Float().assign(1.0))

    #
    # Successful matching - special symbols.
    #
    # TODO: All types.
    #
    def test_ComparisonReturnsTrue_AnyOrNone(self):
        class MyRecordOf(RecordOf):
            def __init__(self):
                RecordOf.__init__(self, Integer)
        myRecordOf = MyRecordOf()
        myRecordOf.assign([Integer().assign(1)])
        self.assertTrue(myRecordOf == AnyOrNone())

    # TODO: Comparison with AnySingleElement?

class TypeSystem_TemplateBoolean_Ctor(unittest.TestCase):
    #
    # Successful constructions.
    #
    def test_CtorConstructsAProperVariable_Boolean(self):
        TemplateBoolean()

class TypeSystem_TemplateBoolean_Assign(unittest.TestCase):
    #
    # Successful assignments.
    #
    def test_AssignementOfProperValue_Boolean(self):
        self.assertEqual(TemplateBoolean().assign(True).value(), True)

    def test_AssignementOfProperValue_AnyOrNone(self):
        self.assertEqual(TemplateBoolean().assign(AnyOrNone()).value(), AnyOrNone())

    #
    # Unsuccessful assignments.
    #
    # TODO: All types.
    #
    def test_AssignRaisesAnExceptionIfCalledWithInvalidType_Integer(self):
        with self.assertRaises(InvalidTTCN3TypeInAssignment):
            TemplateBoolean().assign(1)

    def test_AssignRaisesAnExceptionIfCalledWithInvalidType_Float(self):
        with self.assertRaises(InvalidTTCN3TypeInAssignment):
            TemplateBoolean().assign(1.0)

    def test_AssignRaisesAnExceptionIfCalledWithInvalidType_String(self):
        with self.assertRaises(InvalidTTCN3TypeInAssignment):
            TemplateBoolean().assign("WAX")

class TypeSystem_TemplateBoolean_Boolean_Eq(unittest.TestCase):
    #
    # Successful matching.
    #
    def test_ComparisonReturnsTrueForTwoVariablesWithTheSameValue_Boolean(self):
        self.assertTrue(TemplateBoolean().assign(True) == TemplateBoolean().assign(True))

    def test_ComparisonReturnsTrueForTwoVariablesWithTheSameValue_AnyOrNone(self):
        self.assertTrue(TemplateBoolean().assign(True) == TemplateBoolean().assign(AnyOrNone()))

    #
    # Successful matching - special symbols.
    #
    # TODO: All types.
    #
    def test_ComparisonReturnsTrue_Boolean_AnyOrNone(self):
        self.assertTrue(TemplateBoolean().assign(True) == AnyOrNone())

    def test_ComparisonReturnsTrue_Boolean_AnySingleElement(self):
        self.assertTrue(TemplateBoolean().assign(True) == AnySingleElement())

    #
    # Unsuccessful matching.
    #
    def test_ComparisonReturnsFalseForTwoVariablesWithDifferentValues(self):
        self.assertFalse(TemplateBoolean().assign(True) == TemplateBoolean().assign(False))

    #
    # TODO: All types.
    #
    def test_ComparisonRaisesAnExceptionIfCalledWithInvalidType_Integer(self):
        with self.assertRaises(InvalidTTCN3TypeInComparison):
            TemplateBoolean().assign(True) == Integer().assign(1)

    def test_ComparisonRaisesAnExceptionIfCalledWithInvalidType_Float(self):
        with self.assertRaises(InvalidTTCN3TypeInComparison):
            TemplateBoolean().assign(True) == Float().assign(1.0)

    def test_ComparisonRaisesAnExceptionIfCalledWithInvalidType_Charstring(self):
        with self.assertRaises(InvalidTTCN3TypeInComparison):
            TemplateBoolean().assign(True) == Charstring().assign("WAX")

class TypeSystem_TemplateBoolean_AnyOrNone_Eq(unittest.TestCase):
    #
    # Successful matching.
    #
    def test_ComparisonReturnsTrueForTwoVariablesWithTheSameValue_Boolean(self):
        self.assertTrue(TemplateBoolean().assign(AnyOrNone()) == TemplateBoolean().assign(True))

    def test_ComparisonReturnsTrueForTwoVariablesWithTheSameValue_AnyOrNone(self):
        self.assertTrue(TemplateBoolean().assign(AnyOrNone()) == TemplateBoolean().assign(AnyOrNone()))

    #
    # Successful matching - special symbols.
    #
    # TODO: All types.
    #
    def test_ComparisonReturnsTrue_AnyOrNone_AnyOrNone(self):
        self.assertTrue(TemplateBoolean().assign(AnyOrNone()) == AnyOrNone())

    def test_ComparisonReturnsTrue_AnyOrNone_AnySingleElement(self):
        self.assertTrue(TemplateBoolean().assign(AnyOrNone()) == AnySingleElement())

    #
    # Unsuccessful matching.
    #
    # TODO: All types.
    #
    def test_ComparisonRaisesAnExceptionIfCalledWithInvalidType_Integer(self):
        with self.assertRaises(InvalidTTCN3TypeInComparison):
            TemplateBoolean().assign(AnyOrNone()) == Integer().assign(1)

    def test_ComparisonRaisesAnExceptionIfCalledWithInvalidType_Float(self):
        with self.assertRaises(InvalidTTCN3TypeInComparison):
            TemplateBoolean().assign(AnyOrNone()) == Float().assign(1.0)

    def test_ComparisonRaisesAnExceptionIfCalledWithInvalidType_Charstring(self):
        with self.assertRaises(InvalidTTCN3TypeInComparison):
            TemplateBoolean().assign(AnyOrNone()) == Charstring().assign("WAX")

class TypeSystem_TemplateInteger_Ctor(unittest.TestCase):
    #
    # Successful constructions.
    #
    def test_CtorConstructsAProperVariable_Integer(self):
        TemplateInteger()

class TypeSystem_TemplateInteger_Assign(unittest.TestCase):
    #
    # Successful assignments.
    #
    def test_AssignementOfProperValue_Integer(self):
        self.assertEqual(TemplateInteger().assign(1).value(), 1)

    def test_AssignementOfProperValue_AnyOrNone(self):
        self.assertEqual(TemplateInteger().assign(AnyOrNone()).value(), AnyOrNone())

    #
    # Unsuccessful assignments.
    #
    # TODO: All types.
    #
    def test_AssignRaisesAnExceptionIfCalledWithInvalidType_Boolean(self):
        with self.assertRaises(InvalidTTCN3TypeInAssignment):
            TemplateInteger().assign(True)

    def test_AssignRaisesAnExceptionIfCalledWithInvalidType_Float(self):
        with self.assertRaises(InvalidTTCN3TypeInAssignment):
            TemplateInteger().assign(1.0)

    def test_AssignRaisesAnExceptionIfCalledWithInvalidType_String(self):
        with self.assertRaises(InvalidTTCN3TypeInAssignment):
            TemplateInteger().assign("WAX")

class TypeSystem_TemplateInteger_Integer_Eq(unittest.TestCase):
    #
    # Successful matching.
    #
    def test_ComparisonReturnsTrueForTwoVariablesWithTheSameValue_Integer(self):
        self.assertTrue(TemplateInteger().assign(1) == TemplateInteger().assign(1))

    def test_ComparisonReturnsTrueForTwoVariablesWithTheSameValue_AnyOrNone(self):
        self.assertTrue(TemplateInteger().assign(1) == TemplateInteger().assign(AnyOrNone()))

    #
    # Successful matching - special symbols.
    #
    # TODO: All types.
    #
    def test_ComparisonReturnsTrue_Integer_AnyOrNone(self):
        self.assertTrue(TemplateInteger().assign(1) == AnyOrNone())

    def test_ComparisonReturnsTrue_Integer_AnySingleElement(self):
        self.assertTrue(TemplateInteger().assign(1) == AnySingleElement())

    #
    # Unsuccessful matching.
    #
    def test_ComparisonReturnsFalseForTwoVariablesWithDifferentValues(self):
        self.assertFalse(TemplateInteger().assign(1) == TemplateInteger().assign(2))

    #
    # TODO: All types.
    #
    def test_ComparisonRaisesAnExceptionIfCalledWithInvalidType_Boolean(self):
        with self.assertRaises(InvalidTTCN3TypeInComparison):
            TemplateInteger().assign(1) == Boolean().assign(True)

    def test_ComparisonRaisesAnExceptionIfCalledWithInvalidType_Float(self):
        with self.assertRaises(InvalidTTCN3TypeInComparison):
            TemplateInteger().assign(1) == Float().assign(1.0)

    def test_ComparisonRaisesAnExceptionIfCalledWithInvalidType_Charstring(self):
        with self.assertRaises(InvalidTTCN3TypeInComparison):
            TemplateInteger().assign(1) == Charstring().assign("WAX")

class TypeSystem_TemplateInteger_AnyOrNone_Eq(unittest.TestCase):
    #
    # Successful matching.
    #
    def test_ComparisonReturnsTrueForTwoVariablesWithTheSameValue_Integer(self):
        self.assertTrue(TemplateInteger().assign(AnyOrNone()) == TemplateInteger().assign(1))

    def test_ComparisonReturnsTrueForTwoVariablesWithTheSameValue_AnyOrNone(self):
        self.assertTrue(TemplateInteger().assign(AnyOrNone()) == TemplateInteger().assign(AnyOrNone()))

    #
    # Successful matching - special symbols.
    #
    # TODO: All types.
    #
    def test_ComparisonReturnsTrue_AnyOrNone_AnyOrNone(self):
        self.assertTrue(TemplateInteger().assign(AnyOrNone()) == AnyOrNone())

    def test_ComparisonReturnsTrue_AnyOrNone_AnySingleElement(self):
        self.assertTrue(TemplateInteger().assign(AnyOrNone()) == AnySingleElement())

    #
    # Unsuccessful matching.
    #
    # TODO: All types.
    #
    def test_ComparisonRaisesAnExceptionIfCalledWithInvalidType_Boolean(self):
        with self.assertRaises(InvalidTTCN3TypeInComparison):
            TemplateInteger().assign(AnyOrNone()) == Boolean().assign(True)

    def test_ComparisonRaisesAnExceptionIfCalledWithInvalidType_Float(self):
        with self.assertRaises(InvalidTTCN3TypeInComparison):
            TemplateInteger().assign(AnyOrNone()) == Float().assign(1.0)

    def test_ComparisonRaisesAnExceptionIfCalledWithInvalidType_Charstring(self):
        with self.assertRaises(InvalidTTCN3TypeInComparison):
            TemplateInteger().assign(AnyOrNone()) == Charstring().assign("WAX")

class TypeSystem_TemplateFloat_Ctor(unittest.TestCase):
    #
    # Successful constructions.
    #
    def test_CtorConstructsAProperVariable_Float(self):
        TemplateFloat()

class TypeSystem_TemplateFloat_Assign(unittest.TestCase):
    #
    # Successful assignments.
    #
    def test_AssignementOfProperValue_Float(self):
        self.assertEqual(TemplateFloat().assign(1.0).value(), 1)

    def test_AssignementOfProperValue_AnyOrNone(self):
        self.assertEqual(TemplateFloat().assign(AnyOrNone()).value(), AnyOrNone())

    #
    # Unsuccessful assignments.
    #
    # TODO: All types.
    #
    def test_AssignRaisesAnExceptionIfCalledWithInvalidType_Boolean(self):
        with self.assertRaises(InvalidTTCN3TypeInAssignment):
            TemplateFloat().assign(True)

    def test_AssignRaisesAnExceptionIfCalledWithInvalidType_Integer(self):
        with self.assertRaises(InvalidTTCN3TypeInAssignment):
            TemplateFloat().assign(1)

    def test_AssignRaisesAnExceptionIfCalledWithInvalidType_String(self):
        with self.assertRaises(InvalidTTCN3TypeInAssignment):
            TemplateFloat().assign("WAX")

class TypeSystem_TemplateFloat_Float_Eq(unittest.TestCase):
    #
    # Successful matching.
    #
    def test_ComparisonReturnsTrueForTwoVariablesWithTheSameValue_Float(self):
        self.assertTrue(TemplateFloat().assign(1.0) == TemplateFloat().assign(1.0))

    def test_ComparisonReturnsTrueForTwoVariablesWithTheSameValue_AnyOrNone(self):
        self.assertTrue(TemplateFloat().assign(1.0) == TemplateFloat().assign(AnyOrNone()))

    #
    # Successful matching - special symbols.
    #
    # TODO: All types.
    #
    def test_ComparisonReturnsTrue_Float_AnyOrNone(self):
        self.assertTrue(TemplateFloat().assign(1.0) == AnyOrNone())

    def test_ComparisonReturnsTrue_Float_AnySingleElement(self):
        self.assertTrue(TemplateFloat().assign(1.0) == AnySingleElement())

    #
    # Unsuccessful matching.
    #
    def test_ComparisonReturnsFalseForTwoVariablesWithDifferentValues(self):
        self.assertFalse(TemplateFloat().assign(1.0) == TemplateFloat().assign(2.0))

    #
    # TODO: All types.
    #
    def test_ComparisonRaisesAnExceptionIfCalledWithInvalidType_Boolean(self):
        with self.assertRaises(InvalidTTCN3TypeInComparison):
            TemplateFloat().assign(1.0) == Boolean().assign(True)

    def test_ComparisonRaisesAnExceptionIfCalledWithInvalidType_Integer(self):
        with self.assertRaises(InvalidTTCN3TypeInComparison):
            TemplateFloat().assign(1.0) == Integer().assign(1)

    def test_ComparisonRaisesAnExceptionIfCalledWithInvalidType_Charstring(self):
        with self.assertRaises(InvalidTTCN3TypeInComparison):
            TemplateFloat().assign(1.0) == Charstring().assign("WAX")

class TypeSystem_TemplateFloat_AnyOrNone_Eq(unittest.TestCase):
    #
    # Successful matching.
    #
    def test_ComparisonReturnsTrueForTwoVariablesWithTheSameValue_Float(self):
        self.assertTrue(TemplateFloat().assign(AnyOrNone()) == TemplateFloat().assign(1.0))

    def test_ComparisonReturnsTrueForTwoVariablesWithTheSameValue_AnyOrNone(self):
        self.assertTrue(TemplateFloat().assign(AnyOrNone()) == TemplateFloat().assign(AnyOrNone()))

    #
    # Successful matching - special symbols.
    #
    # TODO: All types.
    #
    def test_ComparisonReturnsTrue_AnyOrNone_AnyOrNone(self):
        self.assertTrue(TemplateFloat().assign(AnyOrNone()) == AnyOrNone())

    def test_ComparisonReturnsTrue_AnyOrNone_AnySingleElement(self):
        self.assertTrue(TemplateFloat().assign(AnyOrNone()) == AnySingleElement())

    #
    # Unsuccessful matching.
    #
    # TODO: All types.
    #
    def test_ComparisonRaisesAnExceptionIfCalledWithInvalidType_Boolean(self):
        with self.assertRaises(InvalidTTCN3TypeInComparison):
            TemplateFloat().assign(AnyOrNone()) == Boolean().assign(True)

    def test_ComparisonRaisesAnExceptionIfCalledWithInvalidType_Integer(self):
        with self.assertRaises(InvalidTTCN3TypeInComparison):
            TemplateFloat().assign(AnyOrNone()) == Integer().assign(1)

    def test_ComparisonRaisesAnExceptionIfCalledWithInvalidType_Charstring(self):
        with self.assertRaises(InvalidTTCN3TypeInComparison):
            TemplateFloat().assign(AnyOrNone()) == Charstring().assign("WAX")

class TypeSystem_TemplateCharstring_Ctor(unittest.TestCase):
    #
    # Successful constructions.
    #
    def test_CtorConstructsAProperVariable_Charstring(self):
        TemplateCharstring()

class TypeSystem_TemplateCharstring_Assign(unittest.TestCase):
    #
    # Successful assignments.
    #
    def test_AssignementOfProperValue_Charstring(self):
        self.assertEqual(TemplateCharstring().assign("WAX").value(), "WAX")

    def test_AssignementOfProperValue_AnyOrNone(self):
        self.assertEqual(TemplateCharstring().assign(AnyOrNone()).value(), AnyOrNone())

    #
    # Unsuccessful assignments.
    #
    # TODO: All types.
    #
    def test_AssignRaisesAnExceptionIfCalledWithInvalidType_Boolean(self):
        with self.assertRaises(InvalidTTCN3TypeInAssignment):
            TemplateCharstring().assign(True)

    def test_AssignRaisesAnExceptionIfCalledWithInvalidType_Integer(self):
        with self.assertRaises(InvalidTTCN3TypeInAssignment):
            TemplateCharstring().assign(1)

    def test_AssignRaisesAnExceptionIfCalledWithInvalidType_Float(self):
        with self.assertRaises(InvalidTTCN3TypeInAssignment):
            TemplateCharstring().assign(1.0)

class TypeSystem_TemplateCharstring_Charstring_Eq(unittest.TestCase):
    #
    # Successful matching.
    #
    def test_ComparisonReturnsTrueForTwoVariablesWithTheSameValue_Charstring(self):
        self.assertTrue(TemplateCharstring().assign("WAX") == TemplateCharstring().assign("WAX"))

    def test_ComparisonReturnsTrueForTwoVariablesWithTheSameValue_AnyOrNone(self):
        self.assertTrue(TemplateCharstring().assign("WAX") == TemplateCharstring().assign(AnyOrNone()))

    #
    # Successful matching - special symbols.
    #
    # TODO: All types.
    #
    def test_ComparisonReturnsTrue_Charstring_AnyOrNone(self):
        self.assertTrue(TemplateCharstring().assign("WAX") == AnyOrNone())

    def test_ComparisonReturnsTrue_Charstring_AnySingleElement(self):
        self.assertTrue(TemplateCharstring().assign("WAX") == AnySingleElement())

    #
    # Unsuccessful matching.
    #
    def test_ComparisonReturnsFalseForTwoVariablesWithDifferentValues(self):
        self.assertFalse(TemplateCharstring().assign("WAX") == TemplateCharstring().assign("XAW"))

    #
    # TODO: All types.
    #
    def test_ComparisonRaisesAnExceptionIfCalledWithInvalidType_Boolean(self):
        with self.assertRaises(InvalidTTCN3TypeInComparison):
            TemplateCharstring().assign("WAX") == Boolean().assign(True)

    def test_ComparisonRaisesAnExceptionIfCalledWithInvalidType_Integer(self):
        with self.assertRaises(InvalidTTCN3TypeInComparison):
            TemplateCharstring().assign("WAX") == Integer().assign(1)

    def test_ComparisonRaisesAnExceptionIfCalledWithInvalidType_Float(self):
        with self.assertRaises(InvalidTTCN3TypeInComparison):
            TemplateCharstring().assign("WAX") == Float().assign(1.0)

class TypeSystem_TemplateCharstring_AnyOrNone_Eq(unittest.TestCase):
    #
    # Successful matching.
    #
    def test_ComparisonReturnsTrueForTwoVariablesWithTheSameValue_Charstring(self):
        self.assertTrue(TemplateCharstring().assign(AnyOrNone()) == TemplateCharstring().assign("WAX"))

    def test_ComparisonReturnsTrueForTwoVariablesWithTheSameValue_AnyOrNone(self):
        self.assertTrue(TemplateCharstring().assign(AnyOrNone()) == TemplateCharstring().assign(AnyOrNone()))

    #
    # Successful matching - special symbols.
    #
    # TODO: All types.
    #
    def test_ComparisonReturnsTrue_AnyOrNone_AnyOrNone(self):
        self.assertTrue(TemplateCharstring().assign(AnyOrNone()) == AnyOrNone())

    def test_ComparisonReturnsTrue_AnyOrNone_AnySingleElement(self):
        self.assertTrue(TemplateCharstring().assign(AnyOrNone()) == AnySingleElement())

    #
    # Unsuccessful matching.
    #
    # TODO: All types.
    #
    def test_ComparisonRaisesAnExceptionIfCalledWithInvalidType_Boolean(self):
        with self.assertRaises(InvalidTTCN3TypeInComparison):
            TemplateCharstring().assign(AnyOrNone()) == Boolean().assign(True)

    def test_ComparisonRaisesAnExceptionIfCalledWithInvalidType_Integer(self):
        with self.assertRaises(InvalidTTCN3TypeInComparison):
            TemplateCharstring().assign(AnyOrNone()) == Integer().assign(1)

    def test_ComparisonRaisesAnExceptionIfCalledWithInvalidType_Float(self):
        with self.assertRaises(InvalidTTCN3TypeInComparison):
            TemplateCharstring().assign(AnyOrNone()) == Float().assign(1.0)

class MySubtypedInteger(Integer):
    def __init__(self, aSubtypeOfSimpleTypeConstraints):
        if type(aSubtypeOfSimpleTypeConstraints) is not list:
            raise InvalidTTCN3TypeInCtor
        self.mSubtypeOfSimpleTypeConstraints = aSubtypeOfSimpleTypeConstraints
        Integer.__init__(self)

    def assign(self, aValue):
        for constraint in self.mSubtypeOfSimpleTypeConstraints:
            if not constraint.accept(aValue):
                raise InvalidTTCN3TypeValueNotInConstraint
        return Integer.assign(self, aValue)

    def accept(self, aValue):
        for constraint in self.mSubtypeOfSimpleTypeConstraints:
            if constraint.accept(aValue):
                return True
        return False

class MySubtypedFloat(Float):
    def __init__(self, aSubtypeOfSimpleTypeConstraints):
        if type(aSubtypeOfSimpleTypeConstraints) is not list:
            raise InvalidTTCN3TypeInCtor
        self.mSubtypeOfSimpleTypeConstraints = aSubtypeOfSimpleTypeConstraints
        Float.__init__(self)

    def assign(self, aValue):
        for constraint in self.mSubtypeOfSimpleTypeConstraints:
            if not constraint.accept(aValue):
                raise InvalidTTCN3TypeValueNotInConstraint
        return Float.assign(self, aValue)

    def accept(self, aValue):
        for constraint in self.mSubtypeOfSimpleTypeConstraints:
            if constraint.accept(aValue):
                return True
        return False

class TypeSystem_Subtyping_ListOfTemplates_Integer(unittest.TestCase):
    #
    # Constructions.
    #
    def test_Ctor(self):
        subtypedInteger = MySubtypedInteger([ListOfTemplates([Integer().assign(1)])])

    #
    # Successful assignments.
    #
    def test_SuccessfulAssignment_OneItem(self):
        subtypedInteger = MySubtypedInteger([ListOfTemplates([Integer().assign(1)])])
        subtypedInteger.assign(1)

    def test_SuccessfulAssignment_ManyItems(self):
        subtypedInteger = MySubtypedInteger([ListOfTemplates([Integer().assign(1), Integer().assign(2)])])
        subtypedInteger.assign(2)

    #
    # Unsuccessful assignments.
    #
    def test_UnsuccessfulAssignment_OneItem(self):
        with self.assertRaises(InvalidTTCN3TypeValueNotInConstraint):
            subtypedInteger = MySubtypedInteger([ListOfTemplates([Integer().assign(1)])])
            subtypedInteger.assign(0)

    def test_UnsuccessfulAssignment_ManyItems(self):
        with self.assertRaises(InvalidTTCN3TypeValueNotInConstraint):
            subtypedInteger = MySubtypedInteger([ListOfTemplates([Integer().assign(1), Integer().assign(2)])])
            subtypedInteger.assign(3)

class TypeSystem_Subtyping_ListOfTemplates_Float(unittest.TestCase):
    #
    # Constructions.
    #
    def test_Ctor(self):
        subtypedFloat = MySubtypedFloat([ListOfTemplates([Float().assign(1.0)])])

    #
    # Successful assignments.
    #
    def test_SuccessfulAssignment_OneItem(self):
        subtypedFloat = MySubtypedFloat([ListOfTemplates([Float().assign(1.0)])])
        subtypedFloat.assign(1.0)

    def test_SuccessfulAssignment_ManyItems(self):
        subtypedFloat = MySubtypedFloat([ListOfTemplates([Float().assign(1.0), Float().assign(2.0)])])
        subtypedFloat.assign(2.0)

    #
    # Unsuccessful assignments.
    #
    def test_UnsuccessfulAssignment_OneItem(self):
        with self.assertRaises(InvalidTTCN3TypeValueNotInConstraint):
            subtypedFloat = MySubtypedFloat([ListOfTemplates([Float().assign(1.0)])])
            subtypedFloat.assign(0.0)

    def test_UnsuccessfulAssignment_ManyItems(self):
        with self.assertRaises(InvalidTTCN3TypeValueNotInConstraint):
            subtypedFloat = MySubtypedFloat([ListOfTemplates([Float().assign(1.0), Float().assign(2.0)])])
            subtypedFloat.assign(3.0)

class TypeSystem_Subtyping_ListOfTypes_Integer(unittest.TestCase):
    #
    # Constructions.
    #
    def test_Ctor(self):
        subtypedInteger1 = MySubtypedInteger([ListOfTemplates([Integer().assign(1)])])
        subtypedInteger2 = MySubtypedInteger([ListOfTemplates([Integer().assign(2)])])
        subtypedInteger3 = MySubtypedInteger([ListOfTypes([subtypedInteger1, subtypedInteger2])])

    #
    # Successful assignments.
    #
    def test_SuccessfulAssignment_OneItem(self):
        subtypedInteger1 = MySubtypedInteger([ListOfTemplates([Integer().assign(1)])])
        subtypedInteger2 = MySubtypedInteger([ListOfTypes([subtypedInteger1])])
        subtypedInteger2.assign(1)

    def test_SuccessfulAssignment_ManyItems(self):
        subtypedInteger1 = MySubtypedInteger([ListOfTemplates([Integer().assign(1)])])
        subtypedInteger2 = MySubtypedInteger([ListOfTemplates([Integer().assign(2)])])
        subtypedInteger3 = MySubtypedInteger([ListOfTypes([subtypedInteger1, subtypedInteger2])])
        subtypedInteger3.assign(1)
        subtypedInteger3.assign(2)

    def test_SuccessfulAssignment_ManyItems_Overlaping(self):
        subtypedInteger1 = MySubtypedInteger([ListOfTemplates([Integer().assign(1), Integer().assign(2)])])
        subtypedInteger2 = MySubtypedInteger([ListOfTemplates([Integer().assign(1), Integer().assign(3)])])
        subtypedInteger3 = MySubtypedInteger([ListOfTypes([subtypedInteger1, subtypedInteger2])])
        subtypedInteger3.assign(1)
        subtypedInteger3.assign(2)
        subtypedInteger3.assign(3)

    #
    # Unsuccessful assignments.
    #
    def test_UnsuccessfulAssignment_OneItem(self):
        with self.assertRaises(InvalidTTCN3TypeValueNotInConstraint):
            subtypedInteger1 = MySubtypedInteger([ListOfTemplates([Integer().assign(1)])])
            subtypedInteger2 = MySubtypedInteger([ListOfTypes([subtypedInteger1])])
            subtypedInteger2.assign(0)

    def test_UnsuccessfulAssignment_ManyItems(self):
        with self.assertRaises(InvalidTTCN3TypeValueNotInConstraint):
            subtypedInteger1 = MySubtypedInteger([ListOfTemplates([Integer().assign(1)])])
            subtypedInteger2 = MySubtypedInteger([ListOfTemplates([Integer().assign(2)])])
            subtypedInteger3 = MySubtypedInteger([ListOfTypes([subtypedInteger1, subtypedInteger2])])
            subtypedInteger3.assign(3)

class TypeSystem_Subtyping_ListOfTypes_Float(unittest.TestCase):
    #
    # Constructions.
    #
    def test_Ctor(self):
        subtypedFloat1 = MySubtypedFloat([ListOfTemplates([Float().assign(1.0)])])
        subtypedFloat2 = MySubtypedFloat([ListOfTemplates([Float().assign(2.0)])])
        subtypedFloat3 = MySubtypedFloat([ListOfTypes([subtypedFloat1, subtypedFloat2])])

    #
    # Successful assignments.
    #
    def test_SuccessfulAssignment_OneItem(self):
        subtypedFloat1 = MySubtypedFloat([ListOfTemplates([Float().assign(1.0)])])
        subtypedFloat2 = MySubtypedFloat([ListOfTypes([subtypedFloat1])])
        subtypedFloat2.assign(1.0)

    def test_SuccessfulAssignment_ManyItems(self):
        subtypedFloat1 = MySubtypedFloat([ListOfTemplates([Float().assign(1.0)])])
        subtypedFloat2 = MySubtypedFloat([ListOfTemplates([Float().assign(2.0)])])
        subtypedFloat3 = MySubtypedFloat([ListOfTypes([subtypedFloat1, subtypedFloat2])])
        subtypedFloat3.assign(1.0)
        subtypedFloat3.assign(2.0)

    def test_SuccessfulAssignment_ManyItems_Overlaping(self):
        subtypedFloat1 = MySubtypedFloat([ListOfTemplates([Float().assign(1.0), Float().assign(2.0)])])
        subtypedFloat2 = MySubtypedFloat([ListOfTemplates([Float().assign(1.0), Float().assign(3.0)])])
        subtypedFloat3 = MySubtypedFloat([ListOfTypes([subtypedFloat1, subtypedFloat2])])
        subtypedFloat3.assign(1.0)
        subtypedFloat3.assign(2.0)
        subtypedFloat3.assign(3.0)

    #
    # Unsuccessful assignments.
    #
    def test_UnsuccessfulAssignment_OneItem(self):
        with self.assertRaises(InvalidTTCN3TypeValueNotInConstraint):
            subtypedFloat1 = MySubtypedFloat([ListOfTemplates([Float().assign(1.0)])])
            subtypedFloat2 = MySubtypedFloat([ListOfTypes([subtypedFloat1])])
            subtypedFloat2.assign(0.0)

    def test_UnsuccessfulAssignment_ManyItems(self):
        with self.assertRaises(InvalidTTCN3TypeValueNotInConstraint):
            subtypedFloat1 = MySubtypedFloat([ListOfTemplates([Float().assign(1.0)])])
            subtypedFloat2 = MySubtypedFloat([ListOfTemplates([Float().assign(2.0)])])
            subtypedFloat3 = MySubtypedFloat([ListOfTypes([subtypedFloat1, subtypedFloat2])])
            subtypedFloat3.assign(3.0)

class TypeSystem_Subtyping_Range_ClosedBoundaries_Integer(unittest.TestCase):
    #
    # Constructions.
    #
    def test_Ctor(self):
        subtypedInteger = MySubtypedInteger([Range(BoundaryInteger(1, True), BoundaryInteger(255, True))])

    #
    # Successful assignments.
    #
    def test_SuccessfulAssignment_LowerBoundary(self):
        subtypedInteger = MySubtypedInteger([Range(BoundaryInteger(1, True), BoundaryInteger(255, True))])
        subtypedInteger.assign(1)

    def test_SuccessfulAssignment_InRange(self):
        subtypedInteger = MySubtypedInteger([Range(BoundaryInteger(1, True), BoundaryInteger(255, True))])
        subtypedInteger.assign(22)

    def test_SuccessfulAssignment_UpperBoundary(self):
        subtypedInteger = MySubtypedInteger([Range(BoundaryInteger(1, True), BoundaryInteger(255, True))])
        subtypedInteger.assign(255)

    #
    # Unsuccessful assignments.
    #
    def test_UnsuccessfulAssignment_LowerBoundaryExceeded(self):
        with self.assertRaises(InvalidTTCN3TypeValueNotInConstraint):
            subtypedInteger = MySubtypedInteger([Range(BoundaryInteger(1, True), BoundaryInteger(255, True))])
            subtypedInteger.assign(0)

    def test_UnsuccessfulAssignment_UpperBoundaryExceeded(self):
        with self.assertRaises(InvalidTTCN3TypeValueNotInConstraint):
            subtypedInteger = MySubtypedInteger([Range(BoundaryInteger(1, True), BoundaryInteger(255, True))])
            subtypedInteger.assign(256)

class TypeSystem_Subtyping_Range_ClosedBoundaries_Float(unittest.TestCase):
    #
    # Constructions.
    #
    def test_Ctor(self):
        subtypedFloat = MySubtypedFloat([Range(BoundaryFloat(1.0, True), BoundaryFloat(255.0, True))])

    #
    # Successful assignments.
    #
    def test_SuccessfulAssignment_LowerBoundary(self):
        subtypedFloat = MySubtypedFloat([Range(BoundaryFloat(1.0, True), BoundaryFloat(255.0, True))])
        subtypedFloat.assign(1.0)

    def test_SuccessfulAssignment_InRange(self):
        subtypedFloat = MySubtypedFloat([Range(BoundaryFloat(1.0, True), BoundaryFloat(255.0, True))])
        subtypedFloat.assign(22.0)

    def test_SuccessfulAssignment_UpperBoundary(self):
        subtypedFloat = MySubtypedFloat([Range(BoundaryFloat(1.0, True), BoundaryFloat(255.0, True))])
        subtypedFloat.assign(255.0)

    #
    # Unsuccessful assignments.
    #
    def test_UnsuccessfulAssignment_LowerBoundaryExceeded(self):
        with self.assertRaises(InvalidTTCN3TypeValueNotInConstraint):
            subtypedFloat = MySubtypedFloat([Range(BoundaryFloat(1.0, True), BoundaryFloat(255.0, True))])
            subtypedFloat.assign(0.0)

    def test_UnsuccessfulAssignment_UpperBoundaryExceeded(self):
        with self.assertRaises(InvalidTTCN3TypeValueNotInConstraint):
            subtypedFloat = MySubtypedFloat([Range(BoundaryFloat(1.0, True), BoundaryFloat(255.0, True))])
            subtypedFloat.assign(256.0)

class TypeSystem_Subtyping_Range_OpenBoundaries_Integer(unittest.TestCase):
    #
    # Constructions.
    #
    def test_Ctor(self):
        subtypedInteger = MySubtypedInteger([Range(BoundaryInteger(1, False), BoundaryInteger(255, False))])

    #
    # Successful assignments.
    #
    def test_SuccessfulAssignment_LowerBoundary(self):
        subtypedInteger = MySubtypedInteger([Range(BoundaryInteger(1, False), BoundaryInteger(255, False))])
        subtypedInteger.assign(2)

    def test_SuccessfulAssignment_InRange(self):
        subtypedInteger = MySubtypedInteger([Range(BoundaryInteger(1, False), BoundaryInteger(255, False))])
        subtypedInteger.assign(22)

    def test_SuccessfulAssignment_UpperBoundary(self):
        subtypedInteger = MySubtypedInteger([Range(BoundaryInteger(1, False), BoundaryInteger(255, False))])
        subtypedInteger.assign(254)

    #
    # Unsuccessful assignments.
    #
    def test_UnsuccessfulAssignment_LowerBoundary(self):
        with self.assertRaises(InvalidTTCN3TypeValueNotInConstraint):
            subtypedInteger = MySubtypedInteger([Range(BoundaryInteger(1, False), BoundaryInteger(255, False))])
            subtypedInteger.assign(1)

    def test_UnsuccessfulAssignment_UpperBoundary(self):
        with self.assertRaises(InvalidTTCN3TypeValueNotInConstraint):
            subtypedInteger = MySubtypedInteger([Range(BoundaryInteger(1, False), BoundaryInteger(255, False))])
            subtypedInteger.assign(255)

class TypeSystem_Subtyping_Range_OpenBoundaries_Float(unittest.TestCase):
    #
    # Constructions.
    #
    def test_Ctor(self):
        subtypedFloat = MySubtypedFloat([Range(BoundaryFloat(1.0, False), BoundaryFloat(255.0, False))])

    #
    # Successful assignments.
    #
    def test_SuccessfulAssignment_LowerBoundary(self):
        subtypedFloat = MySubtypedFloat([Range(BoundaryFloat(1.0, False), BoundaryFloat(255.0, False))])
        subtypedFloat.assign(1.1)

    def test_SuccessfulAssignment_InRange(self):
        subtypedFloat = MySubtypedFloat([Range(BoundaryFloat(1.0, False), BoundaryFloat(255.0, False))])
        subtypedFloat.assign(22.0)

    def test_SuccessfulAssignment_UpperBoundary(self):
        subtypedFloat = MySubtypedFloat([Range(BoundaryFloat(1.0, False), BoundaryFloat(255.0, False))])
        subtypedFloat.assign(249.9)

    #
    # Unsuccessful assignments.
    #
    def test_UnsuccessfulAssignment_LowerBoundaryExceeded(self):
        with self.assertRaises(InvalidTTCN3TypeValueNotInConstraint):
            subtypedFloat = MySubtypedFloat([Range(BoundaryFloat(1.0, False), BoundaryFloat(255.0, False))])
            subtypedFloat.assign(1.0)

    def test_UnsuccessfulAssignment_UpperBoundaryExceeded(self):
        with self.assertRaises(InvalidTTCN3TypeValueNotInConstraint):
            subtypedFloat = MySubtypedFloat([Range(BoundaryFloat(1.0, False), BoundaryFloat(255.0, False))])
            subtypedFloat.assign(255.0)
#
# TODO: All types
#

class TypeSystem_SpecialSymbols_UsedInsteadOfAValue_AnyOrNone(unittest.TestCase):
    #
    # Constructions.
    #
    def test_Ctor(self):
        try:
            AnyOrNone()
        except:
            self.fail()

    #
    # Successful matching: simple types.
    #
    def test_MatchingReturnsTrue_Self(self):
        # TODO: Define whether this should be allowed. Why to compare a template with another template?
        self.assertTrue(AnyOrNone() == AnyOrNone())

    #
    # Simple types.
    #
    # TODO: All types
    #
    def test_MatchingReturnsTrue_Boolean(self):
        self.assertTrue(AnyOrNone() == Boolean().assign(True))

    def test_MatchingReturnsTrue_Integer(self):
        self.assertTrue(AnyOrNone() == Integer().assign(1))

    def test_MatchingReturnsTrue_Float(self):
        self.assertTrue(AnyOrNone() == Float().assign(1.0))

    def test_MatchingReturnsTrue_Charstring(self):
        self.assertTrue(AnyOrNone() == Charstring().assign("WAX"))

    #
    # Successful matching: structured types.
    #
    # TODO: All types
    #
    def test_Record(self):
        class myRecord(Record):
            def __init__(self):
                Record.__init__(self, {'field1': Integer, 'field2': Charstring})
        myRecordInstance = myRecord()
        myRecordInstance.assign({'field1': Integer().assign(1),
                                 'field2': Charstring().assign("QUARK")})
        self.assertTrue(AnyOrNone() == myRecordInstance)

    #
    # Unsuccessful matching.
    #
    def test_ComparisonRaisesAnException_InvalidType(self):
        with self.assertRaises(InvalidTTCN3TypeInComparison):
            AnyOrNone() == True

class TypeSystem_SpecialSymbols_UsedInsteadOfAValue_AnySingleElement(unittest.TestCase):
    #
    # Constructions.
    #
    def test_Ctor(self):
        try:
            AnySingleElement()
        except:
            self.fail()

    #
    # Successful matching: simple types.
    #
    def test_MatchingReturnsTrue_Self(self):
        # TODO: Define whether this should be allowed. Why to compare a template with another template?
        self.assertTrue(AnySingleElement() == AnySingleElement())

    #
    # Simple types.
    #
    # TODO: All types
    #
    def test_MatchingReturnsTrue_Boolean(self):
        self.assertTrue(AnySingleElement() == Boolean().assign(True))

    def test_MatchingReturnsTrue_Integer(self):
        self.assertTrue(AnySingleElement() == Integer().assign(1))

    def test_MatchingReturnsTrue_Float(self):
        self.assertTrue(AnySingleElement() == Float().assign(1.0))

    def test_MatchingReturnsTrue_Charstring(self):
        self.assertTrue(AnySingleElement() == Charstring().assign("WAX"))

    #
    # Successful matching: structured types.
    #
    # TODO: All types
    #

    #
    # Unsuccessful matching.
    #
    def test_ComparisonRaisesAnException_InvalidType(self):
        with self.assertRaises(InvalidTTCN3TypeInComparison):
            AnySingleElement() == True

if __name__ == '__main__':
    unittest.main()
