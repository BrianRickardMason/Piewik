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
            Boolean("String")

    # Positive matching.
    def testBooleanMatchReturnsTrueOnTheSameType(self):
        self.assertTrue(Boolean(True).match(Boolean(True)))

    # Negative matching.
    def testBooleanMatchReturnsFalseOnTheSameTypeAndDifferentValue(self):
        self.assertFalse(Boolean(True).match(Boolean(False)))

    def testBooleanMatchReturnsFalseOnDifferentType_Integer(self):
        self.skipTest("Implement me!")

    def testBooleanMatchReturnsFalseOnDifferentType_Float(self):
        self.skipTest("Implement me!")

    def testBooleanMatchReturnsFalseOnDifferentType_Charstring(self):
        self.skipTest("Implement me!")

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

if __name__ == '__main__':
    unittest.main()
