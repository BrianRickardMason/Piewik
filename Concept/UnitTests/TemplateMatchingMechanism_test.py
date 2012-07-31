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

from Concept.Message                   import Message
from Concept.Template                  import Template
from Concept.TemplateMatchingMechanism import TemplateMatchingMechanism
from Concept.TypeSystem                import *

#
# TODO: All types.
#
class TemplateMatchingMechanism_SimpleTypes_Boolean_Boolean(unittest.TestCase):
    pass

class TemplateMatchingMechanism_SimpleTypes_Integer_Integer(unittest.TestCase):
    #
    # Successful matching.
    #
    def test_ReturnsTrueOnTheSameValues_Positive(self):
        message  = Message (Integer().assign(1))
        template = Template(Integer().assign(1))
        self.assertTrue(TemplateMatchingMechanism(message, template)())

    def test_ReturnsTrueOnTheSameValues_Negative(self):
        message  = Message (Integer().assign(-1))
        template = Template(Integer().assign(-1))
        self.assertTrue(TemplateMatchingMechanism(message, template)())

    def test_ReturnsTrueOnTheSameValues_Zero(self):
        message  = Message (Integer().assign(0))
        template = Template(Integer().assign(0))
        self.assertTrue(TemplateMatchingMechanism(message, template)())

    #
    # Unsuccessful matching.
    #
    def test_ReturnsFalseOnDifferentValues_Positive(self):
        message  = Message (Integer().assign(1))
        template = Template(Integer().assign(2))
        self.assertFalse(TemplateMatchingMechanism(message, template)())

    def test_ReturnsFalseOnDifferentValues_Negative(self):
        message  = Message (Integer().assign(-1))
        template = Template(Integer().assign(-2))
        self.assertFalse(TemplateMatchingMechanism(message, template)())

class TemplateMatchingMechanism_SimpleTypes_Float_Float(unittest.TestCase):
    pass

class TemplateMatchingMechanism_SimpleTypes_Charstring_Charstring(unittest.TestCase):
    pass

class TemplateMatchingMechanism_StructuredTypes_Record_Record(unittest.TestCase):
    #
    # Successful matching.
    #
    def test_ReturnsTrueOnTheSameValues_EmptyRecord(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self)
        myRecordInstance1 = MyRecord()
        myRecordInstance2 = MyRecord()
        message  = Message (myRecordInstance1)
        template = Template(myRecordInstance2)
        self.assertTrue(TemplateMatchingMechanism(message, template)())

    def test_ReturnsTrueOnTheSameValues_NonEmptyRecord(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, {'foo': Boolean})
        myRecordInstance1 = MyRecord()
        myRecordInstance1.assign({'foo': Boolean().assign(True)})
        myRecordInstance2 = MyRecord()
        myRecordInstance2.assign({'foo': Boolean().assign(True)})
        message  = Message (myRecordInstance1)
        template = Template(myRecordInstance2)
        self.assertTrue(TemplateMatchingMechanism(message, template)())

    def test_ReturnsTrueOnTheSameValues_NestedRecord(self):
        class MyInnerRecord(Record):
            def __init__(self):
                Record.__init__(self, {'foo': Charstring})
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, {'foo': Integer,
                                       'bar': Float,
                                       'baz': MyInnerRecord})
        myInnerRecordInstance1 = MyInnerRecord()
        myInnerRecordInstance1.assign({'foo': Charstring().assign("WAX")})
        myRecordInstance1 = MyRecord()
        myRecordInstance1.assign({'foo': Integer().assign(1),
                                  'bar': Float().assign(123.4),
                                  'baz': myInnerRecordInstance1})
        myInnerRecordInstance2 = MyInnerRecord()
        myInnerRecordInstance2.assign({'foo': Charstring().assign("WAX")})
        myRecordInstance2 = MyRecord()
        myRecordInstance2.assign({'foo': Integer().assign(1),
                                  'bar': Float().assign(123.4),
                                  'baz': myInnerRecordInstance2})
        message  = Message (myRecordInstance1)
        template = Template(myRecordInstance2)
        self.assertTrue(TemplateMatchingMechanism(message, template)())

    #
    # Unsuccessful matching.
    #
    def test_ReturnsFalseOnDifferentValues_EmptyRecord_NonEmptyRecord(self):
        class MyRecordEmpty(Record):
            def __init__(self):
                Record.__init__(self)
        class MyRecordNonEmpty(Record):
            def __init__(self):
                Record.__init__(self, {'foo': Boolean})
        myRecordInstance1 = MyRecordEmpty()
        myRecordInstance2 = MyRecordNonEmpty()
        myRecordInstance2.assign({'foo': Boolean().assign(True)})
        message  = Message (myRecordInstance1)
        template = Template(myRecordInstance2)
        self.assertFalse(TemplateMatchingMechanism(message, template)())

    def test_ReturnsFalseOnDifferentValues_NonEmptyRecord_EmptyRecord(self):
        class MyRecordEmpty(Record):
            def __init__(self):
                Record.__init__(self)
        class MyRecordNonEmpty(Record):
            def __init__(self):
                Record.__init__(self, {'foo': Boolean})
        myRecordInstance1 = MyRecordNonEmpty()
        myRecordInstance1.assign({'foo': Boolean().assign(True)})
        myRecordInstance2 = MyRecordEmpty()
        message  = Message (myRecordInstance1)
        template = Template(myRecordInstance2)
        self.assertFalse(TemplateMatchingMechanism(message, template)())

    def test_ReturnsFalseOnDifferentValues_NonEmptyRecord_DifferentValue(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, {'foo': Boolean})
        myRecordInstance1 = MyRecord()
        myRecordInstance1.assign({'foo': Boolean().assign(True)})
        myRecordInstance2 = MyRecord()
        myRecordInstance2.assign({'foo': Boolean().assign(False)})
        message  = Message (myRecordInstance1)
        template = Template(myRecordInstance2)
        self.assertFalse(TemplateMatchingMechanism(message, template)())

    def test_ReturnsFalseOnDifferentValues_NonEmptyRecord_DifferentKey(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, {'foo': Boolean})
        myRecordInstance1 = MyRecord()
        myRecordInstance1.assign({'foo': Boolean().assign(True)})
        myRecordInstance2 = MyRecord()
        myRecordInstance2.assign({'foO': Boolean().assign(True)})
        message  = Message (myRecordInstance1)
        template = Template(myRecordInstance2)
        self.assertFalse(TemplateMatchingMechanism(message, template)())

    def test_ReturnsFalseOnDifferentValues_NestedRecord_DifferentValue(self):
        class MyInnerRecord(Record):
            def __init__(self):
                Record.__init__(self, {'foo': Charstring})
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, {'foo': Integer,
                                       'bar': Float,
                                       'baz': MyInnerRecord})
        myInnerRecordInstance1 = MyInnerRecord()
        myInnerRecordInstance1.assign({'foo': Charstring().assign("WAX")})
        myRecordInstance1 = MyRecord()
        myRecordInstance1.assign({'foo': Integer().assign(1),
                                  'bar': Float().assign(123.4),
                                  'baz': myInnerRecordInstance1})
        myInnerRecordInstance2 = MyInnerRecord()
        myInnerRecordInstance2.assign({'foo': Charstring().assign("WAX")})
        myRecordInstance2 = MyRecord()
        myRecordInstance2.assign({'foo': Integer().assign(1),
                                  'bar': Float().assign(123.3),
                                  'baz': myInnerRecordInstance2})
        message  = Message (myRecordInstance1)
        template = Template(myRecordInstance2)
        self.assertFalse(TemplateMatchingMechanism(message, template)())

    def test_ReturnsFalseOnDifferentValues_NestedRecord_DifferentKey(self):
        class MyInnerRecord(Record):
            def __init__(self):
                Record.__init__(self, {'foo': Charstring})
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, {'foo': Integer,
                                       'bar': Float,
                                       'baz': MyInnerRecord})
        myInnerRecordInstance1 = MyInnerRecord()
        myInnerRecordInstance1.assign({'foo': Charstring().assign("WAX")})
        myRecordInstance1 = MyRecord()
        myRecordInstance1.assign({'foo': Integer().assign(1),
                                  'bar': Float().assign(123.4),
                                  'baz': myInnerRecordInstance1})
        myInnerRecordInstance2 = MyInnerRecord()
        myInnerRecordInstance2.assign({'fos': Charstring().assign("WAX")})
        myRecordInstance2 = MyRecord()
        myRecordInstance2.assign({'foo': Integer().assign(1),
                                  'bar': Float().assign(123.3),
                                  'baz': myInnerRecordInstance2})
        message  = Message (myRecordInstance1)
        template = Template(myRecordInstance2)
        self.assertFalse(TemplateMatchingMechanism(message, template)())

if __name__ == '__main__':
    unittest.main()
