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

class TypeSystem_Construction(unittest.TestCase):
    #
    # TODO: All types.
    #

    #
    # var boolean myVariable;
    #
    def test_Boolean(self):
        self.skipTest("Not implemented yet.")
        #
        # TTCN-3.
        #
        myVariable = Boolean()

        #
        # Compatibility.
        #
        self.assertTrue(isinstance(myVariable, Boolean))

    #
    # var integer myVariable;
    #
    def test_Integer(self):
        #
        # TTCN-3.
        #
        myVariable = Integer()

        #
        # Compatibility.
        #
        self.assertTrue(isinstance(myVariable, Integer))

    #
    # var float myVariable;
    #
    def test_Float(self):
        self.skipTest("Not implemented yet.")
        #
        # TTCN-3.
        #
        myVariable = Float()

        #
        # Compatibility.
        #
        self.assertTrue(isinstance(myVariable, Float))

    #
    # var charstring myVariable;
    #
    def test_Charstring(self):
        self.skipTest("Not implemented yet.")
        #
        # TTCN-3.
        #
        myVariable = Charstring()

        #
        # Compatibility.
        #
        self.assertTrue(isinstance(myVariable, Charstring))

class TypeSystem_AssignmentOfAValueType(unittest.TestCase):
    #
    # TODO: All types.
    #

    #
    # var boolean myVariable := True;
    #
    def test_Boolean(self):
        self.skipTest("Not implemented yet.")
        #
        # TTCN-3.
        #
        myVariable = Boolean()
        myVariable.assignValueType(BooleanValue(True))

        #
        # Compatibility.
        #
        self.assertEqual(myVariable.valueType(), BooleanValue(True))

    #
    # var integer myVariable := 1;
    #
    def test_Integer(self):
        #
        # TTCN-3.
        #
        myVariable = Integer()
        myVariable.assignValueType(IntegerValue(1))

        #
        # Compatibility.
        #
        self.assertEqual(myVariable.valueType(), IntegerValue(1))

    #
    # var float myVariable := 1.0;
    #
    def test_Float(self):
        self.skipTest("Not implemented yet.")
        #
        # TTCN-3.
        #
        myVariable = Float()
        myVariable.assignValueType(FloatValue(1.0))

        #
        # Compatibility.
        #
        self.assertEqual(myVariable.valueType(), FloatValue(1.0))

    #
    # var charstring myVariable := "Jochen von Ulm";
    #
    def test_ConstructingVariableWithValueAssigned_Charstring(self):
        self.skipTest("Not implemented yet.")
        #
        # TTCN-3.
        #
        myVariable = Charstring()
        myVariable.assign(CharstringValue("Jochen von Ulm"))

        #
        # Compatibility.
        #
        self.assertEqual(myVariable.valueType(), CharstringValue("Jochen von Ulm"))

class Typesystem_StructuredTypeDefinition_Record(unittest.TestCase):
    #
    # type record MyRecord {};
    #
    def test_Empty(self):
        #
        # TTCN-3.
        #
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, {})

        #
        # Compatibility.
        #
        self.assertTrue(issubclass(MyRecord, Record))

    #
    # type record MyRecord
    # {
    #     Integer    field1,
    #     Charstring field2
    # };
    #
    def test_NonEmpty(self):
        self.skipTest("Not implemented yet.")
        #
        # TTCN-3.
        #
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, {'foo': Integer(), 'bar': Charstring()})

        #
        # Compatibility.
        #
        self.assertTrue(issubclass(MyRecord, Record))

class TypeSystem_StructuredTypeDefinitionAndAssignmentOfAValueType_Record(unittest.TestCase):
    #
    # type record MyRecord {};
    # var MyRecord myRecordInstance := {};
    #
    def test_Empty(self):
        #
        # TTCN-3.
        #
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, {})
        myRecordInstance = MyRecord()
        myRecordInstance.assignValueType({})

        #
        # Compatibility.
        #
        self.assertTrue(isinstance(myRecordInstance, MyRecord))

    #
    # type record MyRecord
    # {
    #     Integer    field1,
    #     Charstring field2
    # };
    # var MyRecord myRecordInstance :=
    # {
    #     field1 := 1,
    #     field2 := "Varsovie"
    # };
    #
    def test_NonEmpty(self):
        self.skipTest("Not implemented yet.")
        #
        # TTCN-3.
        #
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, {'field1': Integer(),
                                       'field2': Charstring()})
        myRecordInstance = MyRecord()
        myRecordInstance.assignValueType({'field1': Integer().assign(IntegerValue(1)),
                                          'field2': Charstring().assign(CharstringValue("Varsovie"))})

        #
        # Compatibility.
        #
        self.assertTrue(isinstance(myRecordInstance, MyRecord))
        self.assertEqual(myRecordInstance.getField('field1'), Integer().assign(IntegerValue(1)))
        self.assertEqual(myRecordInstance.getField('field2'), Charstring().assign(CharstringValue("Varsovie")))

class TypeSystem_Subtyping_TypeAliasing_SimpleType(unittest.TestCase):
    #
    # type boolean MyNewBoolean;
    #
    def test_Boolean(self):
        self.skipTest("Not implemented yet.")
        #
        # TTCN-3.
        #
        class MyNewBoolean(Boolean):
            def __init__(self):
                Boolean.__init__(self)

        #
        # Compatibility.
        #
        self.assertTrue(issubclass(MyNewBoolean, Boolean))

    #
    # type integer MyNewInteger;
    #
    def test_Integer(self):
        #
        # TTCN-3.
        #
        class MyNewInteger(Integer):
            def __init__(self):
                Integer.__init__(self)

        #
        # Compatibility.
        #
        self.assertTrue(issubclass(MyNewInteger, Integer))

    #
    # type float MyNewFloat;
    #
    def test_Float(self):
        self.skipTest("Not implemented yet.")
        #
        # TTCN-3.
        #
        class MyNewFloat(Float):
            def __init__(self):
                Float.__init__(self)

        #
        # Compatibility.
        #
        self.assertTrue(issubclass(MyNewFloat, Float))

    #
    # type charstring MyNewCharstring;
    #
    def test_Charstring(self):
        self.skipTest("Not implemented yet.")
        #
        # TTCN-3.
        #
        class MyNewCharstring(Charstring):
            def __init__(self):
                Charstring.__init__(self)

        #
        # Compatibility.
        #
        self.assertTrue(issubclass(MyNewCharstring, Charstring))

class TypeSystem_Subtyping_TypeAliasing_StructuredType(unittest.TestCase):
    #
    # type record MyRecord {};
    # type MyRecord MyNewRecord;
    #
    def test_Record_Empty(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, {})
        class MyNewRecord(MyRecord):
            def __init__(self):
                MyRecord.__init__(self)

        #
        # Compatibility.
        #
        self.assertTrue(issubclass(MyNewRecord, MyRecord))

    #
    # type record MyRecord
    # {
    #     Integer    field1,
    #     Charstring field2
    # };
    # type MyRecord MyNewRecord;
    #
    def test_Record_NonEmpty(self):
        self.skipTest("Not implemented yet.")
        #
        # TTCN-3.
        #
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, {'field1': Integer(),
                                       'field2': Charstring()})
        class MyNewRecord(MyRecord):
            def __init__(self):
                MyRecord.__init__(self)

        #
        # Compatibility.
        #
        self.assertTrue(issubclass(MyNewRecord, MyRecord))
