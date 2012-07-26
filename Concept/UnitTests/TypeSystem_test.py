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
    # Successful constructions.
    #
    def test_CtorConstructsAProperVariable_WithoutParameter(self):
        try:
            Boolean()
        except:
            self.fail()

    def test_CtorConstructsAProperVariable_WithParameter(self):
        try:
            Boolean(True)
        except:
            self.fail()

    def test_CtorSetsAProperValueIfCalledWithoutParameter(self):
        self.assertEqual(Boolean(), Boolean(False))

    #
    # Unsuccessful constructions.
    #
    # TODO: All types.
    #
    def test_CtorRaisesAnExceptionIfCalledWithInvalidType_Integer(self):
        with self.assertRaises(InvalidTTCN3TypeInCtor):
            Boolean(1)

    def test_CtorRaisesAnExceptionIfCalledWithInvalidType_Float(self):
        with self.assertRaises(InvalidTTCN3TypeInCtor):
            Boolean(1.0)

    def test_CtorRaisesAnExceptionIfCalledWithInvalidType_String(self):
        with self.assertRaises(InvalidTTCN3TypeInCtor):
            Boolean("WAX")

    #
    # Successful matching.
    #
    def test_ComparisonReturnsTrueForTwoVariablesWithTheSameValue(self):
        self.assertTrue(Boolean(True) == Boolean(True))

    #
    # Unsuccessful matching.
    #
    def test_ComparisonReturnsFalseForTwoVariablesWithDifferentValues(self):
        self.assertFalse(Boolean(True) == Boolean(False))

    #
    # TODO: All types.
    #
    def test_ComparisonRaisesAnExceptionIfCalledWithInvalidType_Boolean(self):
        with self.assertRaises(InvalidTTCN3TypeInComparison):
            Boolean(True) == Integer(1)

    def test_ComparisonRaisesAnExceptionIfCalledWithInvalidType_Float(self):
        with self.assertRaises(InvalidTTCN3TypeInComparison):
            Boolean(True) == Float(1.0)

    def test_ComparisonRaisesAnExceptionIfCalledWithInvalidType_Charstring(self):
        with self.assertRaises(InvalidTTCN3TypeInComparison):
            Boolean(True) == Charstring("WAX")

class TypeSystem_Integer(unittest.TestCase):

    #
    # Successful constructions.
    #
    def test_CtorConstructsAProperVariable_WithoutParameter(self):
        try:
            Integer()
        except:
            self.fail()

    def test_CtorConstructsAProperVariable_WithParameter(self):
        try:
            Integer(1)
        except:
            self.fail()

    def test_CtorSetsAProperValueIfCalledWithoutParameter(self):
        self.assertEqual(Integer(), Integer(0))

    #
    # Unsuccessful constructions.
    #
    # TODO: All types.
    #
    def test_CtorRaisesAnExceptionIfCalledWithInvalidType_Boolean(self):
        with self.assertRaises(InvalidTTCN3TypeInCtor):
            Integer(True)

    def test_CtorRaisesAnExceptionIfCalledWithInvalidType_Float(self):
        with self.assertRaises(InvalidTTCN3TypeInCtor):
            Integer(1.0)

    def test_CtorRaisesAnExceptionIfCalledWithInvalidType_String(self):
        with self.assertRaises(InvalidTTCN3TypeInCtor):
            Integer("WAX")

    #
    # Successful matching.
    #
    def test_ComparisonReturnsTrueForTwoVariablesWithTheSameValue(self):
        self.assertTrue(Integer(1) == Integer(1))

    #
    # Unsuccessful matching.
    #
    def test_ComparisonReturnsFalseForTwoVariablesWithDifferentValues(self):
        self.assertFalse(Integer(1) == Integer(2))

    #
    # TODO: All types.
    #
    def test_ComparisonRaisesAnExceptionIfCalledWithInvalidType_Boolean(self):
        with self.assertRaises(InvalidTTCN3TypeInComparison):
            Integer(1) == Boolean(False)

    def test_ComparisonRaisesAnExceptionIfCalledWithInvalidType_Float(self):
        with self.assertRaises(InvalidTTCN3TypeInComparison):
            Integer(1) == Float(1.0)

    def test_ComparisonRaisesAnExceptionIfCalledWithInvalidType_Charstring(self):
        with self.assertRaises(InvalidTTCN3TypeInComparison):
            Integer(1) == Charstring("WAX")

class TypeSystem_Float(unittest.TestCase):

    #
    # Successful constructions.
    #
    def test_CtorConstructsAProperVariable_WithoutParameter(self):
        try:
            Float()
        except:
            self.fail()

    def test_CtorConstructsAProperVariable_WithParameter(self):
        try:
            Float(1.0)
        except:
            self.fail()

    def test_CtorSetsAProperValueIfCalledWithoutParameter(self):
        self.assertEqual(Float(), Float(0.0))

    #
    # Unsuccessful constructions.
    #
    # TODO: All types.
    #
    def test_CtorRaisesAnExceptionIfCalledWithInvalidType_Boolean(self):
        with self.assertRaises(InvalidTTCN3TypeInCtor):
            Float(True)

    def test_CtorRaisesAnExceptionIfCalledWithInvalidType_Integer(self):
        with self.assertRaises(InvalidTTCN3TypeInCtor):
            Float(1)

    def test_CtorRaisesAnExceptionIfCalledWithInvalidType_String(self):
        with self.assertRaises(InvalidTTCN3TypeInCtor):
            Float("WAX")

    #
    # Successful matching.
    #
    def test_ComparisonReturnsTrueForTwoVariablesWithTheSameValue(self):
        self.assertTrue(Float(1.0) == Float(1.0))

    #
    # Unsuccessful matching.
    #
    def test_ComparisonReturnsFalseForTwoVariablesWithDifferentValues(self):
        self.assertFalse(Float(1.0) == Float(2.0))

    #
    # TODO: All types.
    #
    def test_ComparisonRaisesAnExceptionIfCalledWithInvalidType_Boolean(self):
        with self.assertRaises(InvalidTTCN3TypeInComparison):
            Float(1.0) == Boolean(False)

    def test_ComparisonRaisesAnExceptionIfCalledWithInvalidType_Integer(self):
        with self.assertRaises(InvalidTTCN3TypeInComparison):
            Float(1.0) == Integer(1)

    def test_ComparisonRaisesAnExceptionIfCalledWithInvalidType_Charstring(self):
        with self.assertRaises(InvalidTTCN3TypeInComparison):
            Float(1.0) == Charstring("WAX")

if __name__ == '__main__':
    unittest.main()
