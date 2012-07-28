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

from Concept.TypeSystem import *

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

if __name__ == '__main__':
    unittest.main()
