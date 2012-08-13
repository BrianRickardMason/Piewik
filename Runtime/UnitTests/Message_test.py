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

from Piewik.Runtime.Message    import Message
from Piewik.Runtime.TypeSystem import *

class Message_Ctor(unittest.TestCase):
    #
    # Successful construction.
    #
    # TODO: All types.
    #
    def test_Success_SimpleType_Boolean(self):
        Message(Boolean())

    def test_Success_StrucuredType_Record(self):
        class myRecord(Record):
            def __init__(self):
                Record.__init__(self, {'field1': Integer, 'field2': Charstring})
        myRecordInstance = myRecord()
        myRecordInstance.assign({'field1': Integer().assign(1), 'field2': Charstring().assign("Varsovie")})
        Message(myRecordInstance)

    #
    # Unsuccessful construction.
    #
    def test_CtorRaisesAnException_InvalidType(self):
        with self.assertRaises(InvalidTTCN3TypeInCtor):
            Message(True)

    def test_CtorRaisesAnException_NotAMessageType(self):
        with self.assertRaises(NotAMessageType):
            Message(Any())

    def test_CtorRaisesAnException_NotAMessageTypeInAStructuredType(self):
        with self.assertRaises(NotAMessageType):
            class myRecord(Record):
                def __init__(self):
                    Record.__init__(self, {'field1': Integer, 'field2': Charstring})
            myRecordInstance = myRecord()
            myRecordInstance.assign({'field1': Integer().assign(1), 'field2': AnyOrNone()})
            Message(myRecordInstance)

if __name__ == '__main__':
    unittest.main()
