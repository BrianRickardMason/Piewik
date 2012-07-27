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

class TypeSystem_ConstructionAndAssignmentViaCtor(unittest.TestCase):

    #
    # TODO: All types.
    #

    #
    # var boolean myVariable;
    #
    def test_ConstructingVariableWithoutValueAssigned_Boolean(self):
        try:
            myVariable = Boolean()
            self.assertTrue(isinstance(myVariable, Boolean))
        except:
            self.fail()

    #
    # var integer myVariable;
    #
    def test_ConstructingVariableWithoutValueAssigned_Integer(self):
        try:
            myVariable = Integer()
            self.assertTrue(isinstance(myVariable, Integer))
        except:
            self.fail()

    #
    # var float myVariable;
    #
    def test_ConstructingVariableWithoutValueAssigned_Float(self):
        try:
            myVariable = Float()
            self.assertTrue(isinstance(myVariable, Float))
        except:
            self.fail()

    #
    # var charstring myVariable;
    #
    def test_ConstructingVariableWithoutValueAssigned_Charstring(self):
        try:
            myVariable = Charstring()
            self.assertTrue(isinstance(myVariable, Charstring))
        except:
            self.fail()

    #
    # TODO: All types.
    #

    #
    # var boolean myVariable := True;
    #
    def test_ConstructingVariableWithValueAssigned_Boolean(self):
        try:
            myVariable = Boolean(True)
            self.assertTrue(isinstance(myVariable, Boolean))
        except:
            self.fail()

    #
    # var integer myVariable := 1;
    #
    def test_ConstructingVariableWithValueAssigned_Integer(self):
        try:
            myVariable = Integer(1)
            self.assertTrue(isinstance(myVariable, Integer))
        except:
            self.fail()

    #
    # var float myVariable := 1.0;
    #
    def test_ConstructingVariableWithValueAssigned_Float(self):
        try:
            myVariable = Float(1.0)
            self.assertTrue(isinstance(myVariable, Float))
        except:
            self.fail()

    #
    # var charstring myVariable := "Jochen von Ulm";
    #
    def test_ConstructingVariableWithValueAssigned_Charstring(self):
        try:
            myVariable = Charstring("Jochen von Ulm")
            self.assertTrue(isinstance(myVariable, Charstring))
        except:
            self.fail()

class Typesystem_RecordTypeDefinition(unittest.TestCase):

    #
    # type record myRecord {}
    #
    def test_DefiningAnEmptyRecord(self):
        try:
            class myRecord(Record):
                def __init__(self):
                    Record.__init__(self)
            self.assertTrue(issubclass(myRecord, Record))
        except:
            self.fail()

    #
    # type record myRecord
    # {
    #     Integer    field1,
    #     Charstring field2
    # }
    #
    def test_DefiningARecordWithTwoFieds(self):
        try:
            class myRecord(Record):
                def __init__(self):
                    Record.__init__(self, {'field1': Integer, 'field2': Charstring})
            self.assertTrue(issubclass(myRecord, Record))
        except:
            self.fail()
