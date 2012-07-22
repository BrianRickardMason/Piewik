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

from Template import isTemplate

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