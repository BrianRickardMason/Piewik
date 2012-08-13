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

from Piewik.Runtime.TypeSystem import *

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

    #
    # Successful matching - special symbols.
    #
    # TODO: All types.
    #
    def test_ComparisonReturnsTrue_AnyOrNone(self):
        self.assertTrue(Boolean().assign(True), AnyOrNone())


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

    #
    # Successful matching - special symbols.
    #
    # TODO: All types.
    #
    def test_ComparisonReturnsTrue_AnyOrNone(self):
        self.assertTrue(Integer().assign(1), AnyOrNone())

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

    #
    # Successful matching - special symbols.
    #
    # TODO: All types.
    #
    def test_ComparisonReturnsTrue_AnyOrNone(self):
        self.assertTrue(Float().assign(1.0), AnyOrNone())

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

    #
    # Successful matching - special symbols.
    #
    # TODO: All types.
    #
    def test_ComparisonReturnsTrue_AnyOrNone(self):
        self.assertTrue(Charstring().assign("WAX"), AnyOrNone())

class TypeSystem_RecordOf(unittest.TestCase):
    #
    # Successful constructions.
    #
    def test_CtorConstructsAProperVariableAndSetsProperDefaultValue(self):
        try:
            self.assertEqual(RecordOf(Integer).value(), [])
        except:
            self.fail()

    #
    # Unsuccessful constructions.
    #
    def test_CtorRaisesAnExceptionForInvalidValue(self):
        with self.assertRaises(InvalidTTCN3TypeInCtor):
            RecordOf(int)

    #
    # Successful assignments.
    #
    def test_AssignementOfProperValue_EmptyList(self):
        self.assertEqual(RecordOf(Integer).assign([]).value(), [])

    def test_AssignementOfProperValue_NonEmptyList(self):
        self.assertEqual(RecordOf(Integer).assign([Integer().assign(1), Integer().assign(2)]).value(),
                         [Integer().assign(1), Integer().assign(2)])

    #
    # Unsuccessful assignments.
    #
    # TODO: All types.
    #
    def test_AssignRaisesAnExceptionIfCalledWithInvalidType_Boolean(self):
        with self.assertRaises(InvalidTTCN3TypeInAssignment):
            RecordOf(Boolean).assign(True)

    def test_AssignRaisesAnExceptionIfCalledWithInvalidType_Integer(self):
        with self.assertRaises(InvalidTTCN3TypeInAssignment):
            RecordOf(Boolean).assign(1)

    def test_AssignRaisesAnExceptionIfCalledWithInvalidType_Float(self):
        with self.assertRaises(InvalidTTCN3TypeInAssignment):
            RecordOf(Boolean).assign(1.0)

    def test_AssignRaisesAnExceptionIfCalledWithInvalidType_ValidType_InvalidContent_OneElement(self):
        with self.assertRaises(InvalidTTCN3TypeInAssignment):
            RecordOf(Integer).assign([Float().assign(1.0)])

    def test_AssignRaisesAnExceptionIfCalledWithInvalidType_ValidType_InvalidContent_OneOfElements(self):
        with self.assertRaises(InvalidTTCN3TypeInAssignment):
            RecordOf(Integer).assign([Integer().assign(1), Float().assign(1.0), Integer().assign(2)])

    #
    # Getting a field.
    #
    def test_GetFieldReturnsTheValueOfTheField(self):
        myRecord = RecordOf(Integer).assign([Integer().assign(1), Integer().assign(2), Integer().assign(3)])
        self.assertEqual(myRecord.getField(1), Integer().assign(2))


    def test_GetFieldRaisesAnExceptionForMissingField(self):
        with self.assertRaises(LookupErrorMissingField):
            myRecord = RecordOf(Integer).assign([Integer().assign(1), Integer().assign(2), Integer().assign(3)])
            myRecord.getField(4)

    #
    # Successful matching.
    #
    def test_ComparisonReturnsTrueForTwoVariablesWithTheSameValue_EmptyRecordsOf(self):
        myRecord1 = RecordOf(Integer)
        myRecord2 = RecordOf(Integer)
        self.assertTrue(myRecord1 == myRecord2)

    def test_ComparisonReturnsTrueForTwoVariablesWithTheSameValue_OneElement(self):
        myRecord1 = RecordOf(Integer).assign([Integer().assign(1)])
        myRecord2 = RecordOf(Integer).assign([Integer().assign(1)])
        self.assertTrue(myRecord1 == myRecord2)

    def test_ComparisonReturnsTrueForTwoVariablesWithTheSameValue_ManyElements(self):
        myRecord1 = RecordOf(Integer).assign([Integer().assign(1), Integer().assign(2), Integer().assign(3)])
        myRecord2 = RecordOf(Integer).assign([Integer().assign(1), Integer().assign(2), Integer().assign(3)])
        self.assertTrue(myRecord1 == myRecord2)

    #
    # Unsuccessful matching.
    #
    def test_ComparisonReturnsFalseForTwoVariablesWithDifferentValues_OneElement(self):
        myRecord1 = RecordOf(Integer).assign([Integer().assign(1)])
        myRecord2 = RecordOf(Integer).assign([Integer().assign(2)])
        self.assertFalse(myRecord1 == myRecord2)

    def test_ComparisonReturnsFalseForTwoVariablesWithDifferentValues_OneElement_DifferentLength(self):
        myRecord1 = RecordOf(Integer).assign([Integer().assign(1)])
        myRecord2 = RecordOf(Integer).assign([Integer().assign(1), Integer().assign(2)])
        self.assertFalse(myRecord1 == myRecord2)

    def test_ComparisonReturnsFalseForTwoVariablesWithDifferentValues_ManyElements(self):
        myRecord1 = RecordOf(Integer).assign([Integer().assign(1), Integer().assign(2), Integer().assign(3)])
        myRecord2 = RecordOf(Integer).assign([Integer().assign(1), Integer().assign(2), Integer().assign(4)])
        self.assertFalse(myRecord1 == myRecord2)

    def test_ComparisonReturnsFalseForTwoVariablesWithDifferentValues_ManyElements_SequenceMatters(self):
        myRecord1 = RecordOf(Integer).assign([Integer().assign(1), Integer().assign(2), Integer().assign(3)])
        myRecord2 = RecordOf(Integer).assign([Integer().assign(1), Integer().assign(3), Integer().assign(2)])
        self.assertFalse(myRecord1 == myRecord2)

    #
    # TODO: All types.
    #
    def test_ComparisonRaisesAnExceptionIfCalledWithInvalidType_Boolean(self):
        with self.assertRaises(InvalidTTCN3TypeInComparison):
            RecordOf(Integer).assign([Integer().assign(1)]) == Boolean().assign(True)

    def test_ComparisonRaisesAnExceptionIfCalledWithInvalidType_Integer(self):
        with self.assertRaises(InvalidTTCN3TypeInComparison):
            RecordOf(Integer).assign([Integer().assign(1)]) == Integer().assign(1)

    def test_ComparisonRaisesAnExceptionIfCalledWithInvalidType_Float(self):
        with self.assertRaises(InvalidTTCN3TypeInComparison):
            RecordOf(Integer).assign([Integer().assign(1)]) == Float().assign(1.0)

    #
    # Successful matching - special symbols.
    #
    # TODO: All types.
    #
    def test_ComparisonReturnsTrue_AnyOrNone(self):
        self.assertTrue(RecordOf(Integer).assign([Integer().assign(1)]), AnyOrNone())

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
        self.assertTrue(AnyOrNone(), Boolean().assign(True))

    def test_MatchingReturnsTrue_Integer(self):
        self.assertTrue(AnyOrNone(), Integer().assign(1))

    def test_MatchingReturnsTrue_Float(self):
        self.assertTrue(AnyOrNone(), Float().assign(1.0))

    def test_MatchingReturnsTrue_Charstring(self):
        self.assertTrue(AnyOrNone(), Charstring().assign("WAX"))

    #
    # Successful matching: structured types.
    #
    # TODO: All types
    # FIXME: This assignment should not be possible! Only special symbols used inside values are allowed.
    #
    def test_Record(self):
        class myRecord(Record):
            def __init__(self):
                Record.__init__(self, {'field1': Integer, 'field2': Charstring})
        myRecordInstance = myRecord()
        myRecordInstance.assign({})
        self.assertTrue(AnyOrNone(), myRecordInstance)

    #
    # Unsuccessful matching.
    #
    def test_ComparisonRaisesAnException_InvalidType(self):
        with self.assertRaises(InvalidTTCN3TypeInComparison):
            AnyOrNone() == True

if __name__ == '__main__':
    unittest.main()
