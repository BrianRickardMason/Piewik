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

#
# These should be treated as a part of TTCN-3 compatibility tests.
#

import unittest

from Message                   import Message
from Template                  import Template
from TemplateMatchingMechanism import TemplateMatchingMechanism
from Type                      import *

#
# Simple types without special types in template.
#
class TemplateMatchingMechanism_Boolean_Boolean(unittest.TestCase):
    pass

class TemplateMatchingMechanism_Integer_Integer(unittest.TestCase):

    # Successful matching.
    def testReturnsTrueOnTheSameValues_Positive(self):
        message  = Message (Integer(1))
        template = Template(Integer(1))
        self.assertTrue(TemplateMatchingMechanism(message, template)())

    def testReturnsTrueOnTheSameValues_Negative(self):
        message  = Message (Integer(-1))
        template = Template(Integer(-1))
        self.assertTrue(TemplateMatchingMechanism(message, template)())

    def testReturnsTrueOnTheSameValues_Zero(self):
        message  = Message (Integer(0))
        template = Template(Integer(0))
        self.assertTrue(TemplateMatchingMechanism(message, template)())

    # Unsuccessful matching.
    def testReturnsFalseOnDifferentValues_Positive(self):
        message  = Message (Integer(1))
        template = Template(Integer(2))
        self.assertFalse(TemplateMatchingMechanism(message, template)())

    def testReturnsFalseOnDifferentValues_Negative(self):
        message  = Message (Integer(-1))
        template = Template(Integer(-2))
        self.assertFalse(TemplateMatchingMechanism(message, template)())

class TemplateMatchingMechanism_Float_Float(unittest.TestCase):
    pass

class TemplateMatchingMechanism_Charstring_Charstring(unittest.TestCase):
    pass

#
# Structured types without special types in template.
#
class TemplateMatchingMechanism_Enumeration_Enumeration(unittest.TestCase):
    pass

class TemplateMatchingMechanism_Record_Record(unittest.TestCase):

    # Successful matching.
    def testReturnsTrueOnTheSameValues_EmptyRecord(self):
        self.assertTrue(TemplateMatchingMechanism(Message(Record({})), Template(Record({})))())

    def testReturnsTrueOnTheSameValues_NonEmptyRecord(self):
        message  = Message (Record({'foo': Boolean(True)}))
        template = Template(Record({'foo': Boolean(True)}))
        self.assertTrue(TemplateMatchingMechanism(message, template)())

    def testReturnsTrueOnTheSameValues_NestedRecord(self):
        message  = Message (Record({'foo': Integer(1), 'bar': Float(123.4), 'baz': Record({'foo': Charstring("SD")})}))
        template = Template(Record({'foo': Integer(1), 'bar': Float(123.4), 'baz': Record({'foo': Charstring("SD")})}))
        self.assertTrue(TemplateMatchingMechanism(message, template)())

    # Unsuccessful matching.
    def testReturnsFalseOnDifferentValues_EmptyRecord_NonEmptyRecord(self):
        message  = Message (Record({}))
        template = Template(Record({'foo': Integer(1)}))
        self.assertFalse(TemplateMatchingMechanism(message, template)())

    def testReturnsFalseOnDifferentValues_NonEmptyRecord_EmptyRecord(self):
        message  = Message (Record({'foo': Integer(1)}))
        template = Template(Record({}))
        self.assertFalse(TemplateMatchingMechanism(message, template)())

    def testReturnsFalseOnDifferentValues_NonEmptyRecord_DifferentValue(self):
        message  = Message (Record({'foo': Boolean(False)}))
        template = Template(Record({'foo': Boolean(True )}))
        self.assertFalse(TemplateMatchingMechanism(message, template)())

    def testReturnsFalseOnDifferentValues_NonEmptyRecord_DifferentKey(self):
        message  = Message (Record({'fob': Boolean(True)}))
        template = Template(Record({'foo': Boolean(True)}))
        self.assertFalse(TemplateMatchingMechanism(message, template)())

    def testReturnsFalseOnDifferentValues_NestedRecord_DifferentValue(self):
        message  = Message (Record({'foo': Integer(1), 'bar': Float(123.3), 'baz': Record({'foo': Charstring("SD")})}))
        template = Template(Record({'foo': Integer(1), 'bar': Float(123.4), 'baz': Record({'foo': Charstring("SD")})}))
        self.assertFalse(TemplateMatchingMechanism(message, template)())

    def testReturnsFalseOnDifferentValues_NestedRecord_DifferentKey(self):
        message  = Message (Record({'foo': Integer(1), 'bar': Float(123.3), 'baz': Record({'foo': Charstring("SD")})}))
        template = Template(Record({'foo': Integer(1), 'bar': Float(123.3), 'baz': Record({'fos': Charstring("SD")})}))
        self.assertFalse(TemplateMatchingMechanism(message, template)())

class TemplateMatchingMechanism_Set_Set(unittest.TestCase):
    pass

class TemplateMatchingMechanism_Union_Union(unittest.TestCase):
    pass

class TemplateMatchingMechanism_RecordOf_RecordOf(unittest.TestCase):
    pass

class TemplateMatchingMechanism_Array_Array(unittest.TestCase):
    pass

class TemplateMatchingMechanism_MultiDimensionalArray_MultiDimensionalArray(unittest.TestCase):
    pass

class TemplateMatchingMechanism_SetOf_SetOf(unittest.TestCase):
    pass

#
# Simple types with special types in template.
#
class TemplateMatchingMechanism_Boolean_SpecialType(unittest.TestCase):
    pass

class TemplateMatchingMechanism_Integer_SpecialType(unittest.TestCase):

    # Successful matching.
    def testReturnsTrueOnTheSameValues_Any(self):
        message  = Message (Integer(1))
        template = Template(Any())
        self.assertTrue(TemplateMatchingMechanism(message, template)())

    def testReturnsTrueOnTheSameValues_AnyOrNone(self):
        message  = Message (Integer(1))
        template = Template(AnyOrNone())
        self.assertTrue(TemplateMatchingMechanism(message, template)())

    def testReturnsTrueOnTheSameValues_Omit(self):
        self.skipTest("Implement me.")

    def testReturnsTrueOnTheSameValues_List(self):
        self.skipTest("Implement me.")

    def testReturnsTrueOnTheSameValues_Complement(self):
        self.skipTest("Implement me.")

    def testReturnsTrueOnTheSameValues_Range(self):
        self.skipTest("Implement me.")

    def testReturnsTrueOnTheSameValues_Superset(self):
        self.skipTest("Implement me.")

    def testReturnsTrueOnTheSameValues_Subset(self):
        self.skipTest("Implement me.")

    def testReturnsTrueOnTheSameValues_Pattern(self):
        self.skipTest("Implement me.")

class TemplateMatchingMechanism_Float_SpecialType(unittest.TestCase):
    pass

class TemplateMatchingMechanism_Charstring_SpecialType(unittest.TestCase):
    pass

#
# Structured types with special types in template.
#

if __name__ == '__main__':
    unittest.main()
