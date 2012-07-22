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

import sys
import unittest

from Template import TemplateMatcher
from Template import isTemplate

class TemplateMatcher_Match(unittest.TestCase):

    def testMatchReturnsTrueOnNoneType(self):
        self.assertTrue(TemplateMatcher(None, None).match())
        self.assertTrue(TemplateMatcher('', None).match())
        self.assertTrue(TemplateMatcher("", None).match())
        self.assertTrue(TemplateMatcher(1, None).match())
        self.assertTrue(TemplateMatcher(1.0, None).match())
        self.assertTrue(TemplateMatcher((), None).match())
        self.assertTrue(TemplateMatcher([], None).match())
        self.assertTrue(TemplateMatcher({}, None).match())
        self.assertTrue(TemplateMatcher((1, 4), None).match())
        self.assertTrue(TemplateMatcher([1, 4, 56], None).match())

    def testMatchReturnsTrueOnTheSameSimpleTypes(self):
        self.assertTrue(TemplateMatcher(True, True).match())
        self.assertTrue(TemplateMatcher(False, False).match())
        self.assertTrue(TemplateMatcher(1, 1).match())
        self.assertTrue(TemplateMatcher(1.0, 1.0).match())
        self.assertTrue(TemplateMatcher('a', 'a').match())
        self.assertTrue(TemplateMatcher(u'Zażółć gęślą jaźń!', u'Zażółć gęślą jaźń!').match())

    def testMatchReturnsFalseOnDifferentSimpleTypes(self):
        self.assertFalse(TemplateMatcher(True, False).match())
        self.assertFalse(TemplateMatcher(1, 2).match())
        self.assertFalse(TemplateMatcher(1.0, 2.0).match())
        self.assertFalse(TemplateMatcher('a', 'b').match())
        self.assertFalse(TemplateMatcher(u'Zażółć gęślą jaźń!', u'Zażółć gęślą jaźń').match())

    def testMatchReturnsTrueOnTheSameIntegersAndFloatsTypes(self):
        self.assertTrue(TemplateMatcher(1, 1.0).match())
        self.assertTrue(TemplateMatcher(1.0, 1).match())

    def testMatchReturnsFalseOnDifferentIntegersAndFloatsTypes(self):
        self.assertFalse(TemplateMatcher(2, 1.0).match())
        self.assertFalse(TemplateMatcher(2.0, 1).match())

    def testMatchReturnsTrueOnTheSameStringAndUnicodeTypes(self):
        self.assertTrue(TemplateMatcher('b', u'b').match())
        self.assertTrue(TemplateMatcher(u'b', 'b').match())

    def testMatchReturnsFalseOnDifferentStringAndUnicodeTypes(self):
        self.assertFalse(TemplateMatcher('a', u'b').match())
        self.assertFalse(TemplateMatcher(u'a', 'b').match())

    #
    # Tuple.
    #
    def testMatchTupleComparisonReturnsFalseOnIncoherentTypes_NoneWithTuple(self):
        self.assertFalse(TemplateMatcher(None, ()).match())

    def testMatchTupleComparisonReturnsFalseOnIncoherentTypes_BooleanWithTuple(self):
        self.assertFalse(TemplateMatcher(True, ()).match())

    def testMatchTupleComparisonReturnsFalseOnIncoherentTypes_IntegerWithTuple(self):
        self.assertFalse(TemplateMatcher(1, ()).match())

    def testMatchTupleComparisonReturnsFalseOnIncoherentTypes_FloatWithTuple(self):
        self.assertFalse(TemplateMatcher(1.0, ()).match())

    def testMatchTupleComparisonReturnsFalseOnIncoherentTypes_LongWithTuple(self):
        self.assertFalse(TemplateMatcher(long(1.0), ()).match())

    def testMatchTupleComparisonReturnsFalseOnIncoherentTypes_StringWithTuple(self):
        self.assertFalse(TemplateMatcher('bad romance', ()).match())

    def testMatchTupleComparisonReturnsFalseOnIncoherentTypes_UnicodeWithTuple(self):
        self.assertFalse(TemplateMatcher(u'gżegżółka', ()).match())

    def testMatchTupleComparisonReturnsFalseOnIncoherentTypes_ListWithTuple(self):
        self.assertFalse(TemplateMatcher([], ()).match())

    def testMatchTupleComparisonReturnsFalseOnIncoherentTypes_DictionaryWithTuple(self):
        self.assertFalse(TemplateMatcher({}, ()).match())

    def testMatchTupleComparisonReturnsTrueOnTheSameTuples_Empty(self):
        self.assertTrue(TemplateMatcher((), ()).match())

    def testMatchTupleComparisonReturnsTrueOnTheSameTuples_OneElement(self):
        self.assertTrue(TemplateMatcher((1), (1)).match())

    def testMatchTupleComparisonReturnsTrueOnTheSameTuples_ManyElements(self):
        self.assertTrue(TemplateMatcher((u'a', u'b', u'ć'), (u'a', u'b', u'ć')).match())

    def testMatchTupleComparisonReturnsTrueOnTheSameTuples_Nested_Once_Tuple(self):
        self.assertTrue(TemplateMatcher((1, (1, 2, 3)), (1, (1, 2, 3))).match())

    def testMatchTupleComparisonReturnsTrueOnTheSameTuples_Nested_Once_Mixed(self):
        self.skipTest("Implement me.")

    def testMatchTupleComparisonReturnsTrueOnTheSameTuples_Nested_Twice_Tuple(self):
        tuple1 = (1, ('a', u'ręką', 1.0, (3.4, -1, -2)))
        tuple2 = (1, ('a', u'ręką', 1.0, (3.4, -1, -2)))
        self.assertTrue(TemplateMatcher(tuple1, tuple2).match())

    def testMatchTupleComparisonReturnsTrueOnTheSameTuples_Nested_Twice_Mixed(self):
        self.skipTest("Implement me.")

    def testMatchTupleComparisonReturnsFalseOnDifferentTuples_DifferentLenght(self):
        self.assertFalse(TemplateMatcher((1), (1, 2)).match())
        self.assertFalse(TemplateMatcher((1, 2), (1)).match())

    def testMatchTupleComparisonReturnsFalseOnDifferentTuples_OneEmpty(self):
        self.assertFalse(TemplateMatcher((), (1)).match())
        self.assertFalse(TemplateMatcher((1), ()).match())

    def testMatchTupleComparisonReturnsFalseOnDifferentTuples_OneElement(self):
        self.assertFalse(TemplateMatcher((1), (2)).match())

    def testMatchTupleComparisonReturnsFalseOnDifferentTuples_ManyElements(self):
        self.assertFalse(TemplateMatcher((u'a', u'b', u'ć'), (u'a', u'ą', u'ć')).match())

    def testMatchTupleComparisonReturnsFalseOnDifferentTuples_Nested_Once_Tuple(self):
        self.assertFalse(TemplateMatcher((1, (1, 2, 3)), (1, (1, 3, 3))).match())

    def testMatchTupleComparisonReturnsFalseOnDifferentTuples_Nested_Once_Mixed(self):
        self.skipTest("Implement me.")

    def testMatchTupleComparisonReturnsFalseOnDifferentTuples_Nested_Twice_Tuple(self):
        tuple1 = (1, ('a', u'ręką', 1.0, (3.4, -1, -2)))
        tuple2 = (1, ('a', u'ręką', 1.0, (3.6, -1, -2)))
        self.assertFalse(TemplateMatcher(tuple1, tuple2).match())

    def testMatchTupleComparisonReturnsFalseOnDifferentTuples_Nested_Twice_Mixed(self):
        self.skipTest("Implement me.")

    #
    # List.
    #
    def testMatchListComparisonReturnsFalseOnIncoherentTypes_NoneWithList(self):
        self.assertFalse(TemplateMatcher(None, []).match())

    def testMatchListComparisonReturnsFalseOnIncoherentTypes_BooleanWithList(self):
        self.assertFalse(TemplateMatcher(True, []).match())

    def testMatchListComparisonReturnsFalseOnIncoherentTypes_IntegerWithList(self):
        self.assertFalse(TemplateMatcher(1, []).match())

    def testMatchListComparisonReturnsFalseOnIncoherentTypes_FloatWithList(self):
        self.assertFalse(TemplateMatcher(1.0, []).match())

    def testMatchListComparisonReturnsFalseOnIncoherentTypes_LongWithList(self):
        self.assertFalse(TemplateMatcher(long(1.0), []).match())

    def testMatchListComparisonReturnsFalseOnIncoherentTypes_StringWithList(self):
        self.assertFalse(TemplateMatcher('bad romance', []).match())

    def testMatchListComparisonReturnsFalseOnIncoherentTypes_UnicodeWithList(self):
        self.assertFalse(TemplateMatcher(u'gżegżółka', []).match())

    def testMatchListComparisonReturnsFalseOnIncoherentTypes_TupleWithList(self):
        self.assertFalse(TemplateMatcher((), []).match())

    def testMatchListComparisonReturnsFalseOnIncoherentTypes_DictionaryWithList(self):
        self.assertFalse(TemplateMatcher({}, []).match())

    def testMatchListComparisonReturnsTrueOnTheSameLists_Empty(self):
        self.assertTrue(TemplateMatcher([], []).match())

    def testMatchListComparisonReturnsTrueOnTheSameLists_OneElement(self):
        self.assertTrue(TemplateMatcher([1], [1]).match())

    def testMatchListComparisonReturnsTrueOnTheSameLists_ManyElements(self):
        self.assertTrue(TemplateMatcher([u'a', u'b', u'ć'], [u'a', u'b', u'ć']).match())

    def testMatchListComparisonReturnsFalseOnTheSameLists_ManyElements_DifferentOrder(self):
        self.assertFalse(TemplateMatcher([u'a', u'b', u'ć'], [u'ć', u'b', u'a']).match())

    def testMatchListComparisonReturnsFalseOnTheSameLists_ManyElements_DifferentOrder2(self):
        self.assertFalse(TemplateMatcher([1, 2, 3], [3,1,2]).match())

    def testMatchListComparisonReturnsTrueOnTheSameLists_Nested_Once_List(self):
        self.assertTrue(TemplateMatcher([1, [1, 2, 3]], [1, [1, 2, 3]]).match())

    def testMatchListComparisonReturnsTrueOnTheSameLists_Nested_Once_Mixed(self):
        self.skipTest("Implement me.")

    def testMatchListComparisonReturnsTrueOnTheSameLists_Nested_Twice_List(self):
        list1 = [1, ['a', u'ręką', 1.0, [3.4, -1, -2]]]
        list2 = [1, ['a', u'ręką', 1.0, [3.4, -1, -2]]]
        self.assertTrue(TemplateMatcher(list1, list2).match())

    def testMatchListComparisonReturnsTrueOnTheSameLists_Nested_Twice_Mixed(self):
        self.skipTest("Implement me.")

    def testMatchListComparisonReturnsFalseOnDifferentLists_DifferentLenght(self):
        self.assertFalse(TemplateMatcher([1], [1, 2]).match())
        self.assertFalse(TemplateMatcher([1, 2], [1]).match())

    def testMatchListComparisonReturnsFalseOnDifferentLists_OneEmpty(self):
        self.assertFalse(TemplateMatcher([], [1]).match())
        self.assertFalse(TemplateMatcher([1], []).match())

    def testMatchListComparisonReturnsFalseOnDifferentLists_OneElement(self):
        self.assertFalse(TemplateMatcher([1], [2]).match())

    def testMatchListComparisonReturnsFalseOnDifferentLists_ManyElements(self):
        self.assertFalse(TemplateMatcher([u'a', u'b', u'ć'], [u'a', u'ą', u'ć']).match())

    def testMatchListComparisonReturnsFalseOnDifferentLists_Nested_Once_List(self):
        self.assertFalse(TemplateMatcher([1, [1, 2, 3]], [1, [1, 3, 3]]).match())

    def testMatchListComparisonReturnsFalseOnDifferentLists_Nested_Once_Mixed(self):
        self.skipTest("Implement me.")

    def testMatchListComparisonReturnsFalseOnDifferentLists_Nested_Twice_List(self):
        list1 = [1, ['a', u'ręką', 1.0, [3.4, -1, -2]]]
        list2 = [1, ['a', u'ręką', 1.0, [3.6, -1, -2]]]
        self.assertFalse(TemplateMatcher(list1, list2).match())

    def testMatchListComparisonReturnsFalseOnDifferentLists_Nested_Twice_Mixed(self):
        self.skipTest("Implement me.")

class IsTemplate(unittest.TestCase):

    def testIsTemplateReturnsTrueOnBooleanTypes(self):
        self.assertTrue(isTemplate(False))
        self.assertTrue(isTemplate(True))

    def testIsTemplateReturnsTrueOnIntegerTypes(self):
        self.assertTrue(isTemplate(1))
        self.assertTrue(isTemplate(0))
        self.assertTrue(isTemplate(-1))
        self.assertTrue(isTemplate( sys.maxint))
        self.assertTrue(isTemplate(-sys.maxint - 1))

    def testIsTemplateReturnsTrueOnFloatTypes(self):
        self.assertTrue(isTemplate(1.0))
        self.assertTrue(isTemplate(0.0))
        self.assertTrue(isTemplate(-1.0))
        self.assertTrue(isTemplate(sys.float_info.max))
        self.assertTrue(isTemplate(sys.float_info.min))

    def testIsTemplateReturnsTrueOnLongTypes(self):
        self.assertTrue(isTemplate(long( sys.float_info.max + 1)))
        self.assertTrue(isTemplate(long(-sys.float_info.min - 1)))

    def testIsTemplateReturnsTrueOnStringTypes(self):
        self.assertTrue(isTemplate(''))
        self.assertTrue(isTemplate(""))
        self.assertTrue(isTemplate(""""""))
        self.assertTrue(isTemplate('FooBar'))

    def testIsTemplateReturnsTrueOnUnicodeTypes(self):
        self.assertTrue(isTemplate(u"Pchnąć w tę łódź jeża lub óśm skrzyń fig."))

    def testIsTemplateReturnsTrueOnTupleTypes(self):
        self.assertTrue(isTemplate(()))
        self.assertTrue(isTemplate((1,)))
        self.assertTrue(isTemplate((1, 3)))
        self.assertTrue(isTemplate((1, 'FooFuker', ("Kręg"))))

    def testIsTemplateReturnsTrueOnListTypes(self):
        self.assertTrue(isTemplate([]))
        self.assertTrue(isTemplate([1, 4, 5]))
        self.assertTrue(isTemplate([1, 4, 5, "ASD"]))

    def testIsTemplateReturnsTrueOnDictionaryTypes(self):
        self.assertTrue(isTemplate({}))
        self.assertTrue(isTemplate({'this': "THAT"}))
        self.assertTrue(isTemplate({"tweet": "tw*t"}))

    def testIsTemplateReturnsFalseOnObjectTypes(self):
        self.assertFalse(isTemplate(object))

if __name__ == '__main__':
    unittest.main()
