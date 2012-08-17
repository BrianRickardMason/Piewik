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

from Runtime.Template   import *
from Runtime.TypeSystem import *

class Template_Ctor(unittest.TestCase):
    #
    # Successful constructions.
    #
    # TODO: All types.
    #
    def test_CtorConstructsAProperVariable_Boolean(self):
        template = Template(Boolean)

    def test_CtorConstructsAProperVariable_Integer(self):
        template = Template(Integer)

    def test_CtorConstructsAProperVariable_Float(self):
        template = Template(Float)

    def test_CtorConstructsAProperVariable_Charstring(self):
        template = Template(Charstring)

    def test_CtorConstructsAProperVariable_Record(self):
        class MyRecord(Record):
            def __init__(self):
                Record.__init__(self, {})
        template = Template(MyRecord)

    def test_CtorConstructsAProperVariable_RecordOf(self):
        class MyRecordOf(Record):
            def __init__(self):
                Record.__init__(self, Integer)
        template = Template(MyRecordOf)

    #
    # Unsuccessful constructions.
    #
    def test_CtorRaisesAnExceptionForInvalidType(self):
        with self.assertRaises(InvalidTTCN3TypeInCtor):
            template = Template(int)

if __name__ == '__main__':
    unittest.main()
