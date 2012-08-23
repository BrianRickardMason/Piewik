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

from Runtime.Extensions.Critter.Decoder                import ProtobufDecoder
from Runtime.Extensions.Critter.Encoder                import ProtobufEncoder
from Runtime.Extensions.Critter.Interface.Messages_pb2 import *
from Runtime.Extensions.Critter.Interface.Translation  import *
from Runtime.NewTypeSystem                             import *

class Decoder_Decode(unittest.TestCase):
    def test_LoadGraphAndWorkResponse(self):
        senderData = {'type': Charstring().assignValueType(CharstringValue("HelloCritty")),
                      'nick': Charstring().assignValueType(CharstringValue("Sender"))}

        receiverData = {'type': Charstring().assignValueType(CharstringValue("HelloCritty")),
                        'nick': Charstring().assignValueType(CharstringValue("Receiver"))}

        graphsData = [
            {'graphName': Charstring().assignValueType(CharstringValue("Graph1"))},
            {'graphName': Charstring().assignValueType(CharstringValue("Graph2"))}
        ]

        worksData = [
            {'graphName': Charstring().assignValueType(CharstringValue("Graph1")),
             'workName':  Charstring().assignValueType(CharstringValue("Work1"))},
            {'graphName': Charstring().assignValueType(CharstringValue("Graph1")),
             'workName':  Charstring().assignValueType(CharstringValue("Work2"))}
        ]

        workPredecessorsData = [
            {'workName':            Charstring().assignValueType(CharstringValue("Work2")),
             'predecessorWorkName': Charstring().assignValueType(CharstringValue("Work1"))}
        ]

        loadGraphAndWorkResponse = PiewikLoadGraphAndWorkResponse()
        loadGraphAndWorkResponse.assignValueType({
            'messageName':      Charstring().assignValueType(CharstringValue("LoadGraphAndWorkResponse")),
            'sender':           senderData,
            'receiver':         receiverData,
            'graphs':           graphsData,
            'works':            worksData,
            'workPredecessors': workPredecessorsData
        })

        encoder = ProtobufEncoder()

        envelope = encoder.encode(aPayloadData=loadGraphAndWorkResponse)

        decoder = ProtobufDecoder()

        message = decoder.decode(envelope.SerializeToString())

        self.assertEqual(message.getField('messageName').valueType().value(), 'LoadGraphAndWorkResponse')
        self.assertEqual(message.getField('sender').getField('type').valueType().value(), 'HelloCritty')
        self.assertEqual(message.getField('sender').getField('nick').valueType().value(), 'Sender')
        self.assertEqual(message.getField('receiver').getField('type').valueType().value(), 'HelloCritty')
        self.assertEqual(message.getField('receiver').getField('nick').valueType().value(), 'Receiver')
        self.assertEqual(message.getField('graphs').getField(0).getField('graphName').valueType().value(), 'Graph1')
        self.assertEqual(message.getField('graphs').getField(1).getField('graphName').valueType().value(), 'Graph2')
        self.assertEqual(message.getField('works').getField(0).getField('graphName').valueType().value(), 'Graph1')
        self.assertEqual(message.getField('works').getField(0).getField('workName').valueType().value(), 'Work1')
        self.assertEqual(message.getField('works').getField(1).getField('graphName').valueType().value(), 'Graph1')
        self.assertEqual(message.getField('works').getField(1).getField('workName').valueType().value(), 'Work2')
        self.assertEqual(message.getField('workPredecessors').getField(0).getField('workName').valueType().value(), 'Work2')
        self.assertEqual(message.getField('workPredecessors').getField(0).getField('predecessorWorkName').valueType().value(), 'Work1')

if __name__ == '__main__':
    unittest.main()
