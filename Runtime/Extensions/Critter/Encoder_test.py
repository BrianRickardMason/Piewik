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

from Runtime.Extensions.Critter.Encoder                 import ProtobufEncoder
from Runtime.Extensions.Critter.Interface.MessageCommon import *
from Runtime.Extensions.Critter.Interface.Messages_pb2  import *
from Runtime.Extensions.Critter.Interface.Translation   import *
from Runtime.TypeSystem                                 import *

class Encoder_Encode(unittest.TestCase):
    def test_LoadGraphAndWorkResponse(self):
        senderData = {'type': Charstring(SimpleType()).assign(CharstringValue("HelloCritty")),
                      'nick': Charstring(SimpleType()).assign(CharstringValue("Sender"))}

        receiverData = {'type': Charstring(SimpleType()).assign(CharstringValue("HelloCritty")),
                        'nick': Charstring(SimpleType()).assign(CharstringValue("Receiver"))}

        graphsData = [
            {'graphName': Charstring(SimpleType()).assign(CharstringValue("Graph1"))},
            {'graphName': Charstring(SimpleType()).assign(CharstringValue("Graph2"))}
        ]

        worksData =[
            {'graphName': Charstring(SimpleType()).assign(CharstringValue("Graph1")),
             'workName':  Charstring(SimpleType()).assign(CharstringValue("Work1"))},
            {'graphName': Charstring(SimpleType()).assign(CharstringValue("Graph1")),
             'workName':  Charstring(SimpleType()).assign(CharstringValue("Work2"))}
        ]

        workPredecessorsData = [
            {'workName':            Charstring(SimpleType()).assign(CharstringValue("Work2")),
             'predecessorWorkName': Charstring(SimpleType()).assign(CharstringValue("Work1"))}
        ]

        loadGraphAndWorkResponse = PiewikLoadGraphAndWorkResponse()
        loadGraphAndWorkResponse.assign({
            'messageName':      Charstring(SimpleType()).assign(CharstringValue("LoadGraphAndWorkResponse")),
            'sender':           senderData,
            'receiver':         receiverData,
            'graphs':           graphsData,
            'works':            worksData,
            'workPredecessors': workPredecessorsData
        })

        encoder = ProtobufEncoder()

        envelope = encoder.encode(aPayloadData=loadGraphAndWorkResponse)

        self.assertEqual(envelope.header.id, LOAD_GRAPH_AND_WORK_RESPONSE)

        payload = LoadGraphAndWorkResponse()
        payload.ParseFromString(envelope.payload.payload)

        self.assertEqual(payload.messageName,   "LoadGraphAndWorkResponse")
        self.assertEqual(payload.sender.type,   "HelloCritty")
        self.assertEqual(payload.sender.nick,   "Sender")
        self.assertEqual(payload.receiver.type, "HelloCritty")
        self.assertEqual(payload.receiver.nick, "Receiver")

        self.assertEqual(payload.graphs[0].graphName, "Graph1")
        self.assertEqual(payload.graphs[1].graphName, "Graph2")

        self.assertEqual(payload.works[0].graphName, "Graph1")
        self.assertEqual(payload.works[0].workName,  "Work1")
        self.assertEqual(payload.works[1].graphName, "Graph1")
        self.assertEqual(payload.works[1].workName,  "Work2")

        self.assertEqual(payload.workPredecessors[0].workName,            "Work2")
        self.assertEqual(payload.workPredecessors[0].predecessorWorkName, "Work1")

class Encoder_EncodePayload(unittest.TestCase):
    def test_HeartbeatAnnouncement(self):
        critterData = {'type': Charstring(SimpleType()).assign(CharstringValue("TYPE")),
                       'nick': Charstring(SimpleType()).assign(CharstringValue("NICK"))}

        heartbeatAnnouncement = PiewikHeartbeatAnnouncement()
        heartbeatAnnouncement.assign({
            'messageName': Charstring(SimpleType()).assign(CharstringValue("HeartbeatAnnouncement")),
            'sender':      critterData,
            'timestamp':   Float(SimpleType()).assign(FloatValue(1234.5678))
        })

        encoder = ProtobufEncoder()

        payload = HeartbeatAnnouncement()

        encoder.encodePayload(aPayloadContent=payload,
                              aPayloadData=heartbeatAnnouncement)

        self.assertEqual(payload.messageName, "HeartbeatAnnouncement")
        self.assertEqual(payload.sender.type, "TYPE")
        self.assertEqual(payload.sender.nick, "NICK")
        self.assertEqual(payload.timestamp,   1234.5678)

    def test_PresentYourselfRequest(self):
        senderData = {'type': Charstring(SimpleType()).assign(CharstringValue("HelloCritty")),
                      'nick': Charstring(SimpleType()).assign(CharstringValue("Sender"))}

        receiverData = {'type': Charstring(SimpleType()).assign(CharstringValue("HelloCritty")),
                        'nick': Charstring(SimpleType()).assign(CharstringValue("Receiver"))}

        presentYourselfRequest = PiewikPresentYourselfRequest()
        presentYourselfRequest.assign({
            'messageName': Charstring(SimpleType()).assign(CharstringValue("PresentYourselfRequest")),
            'sender':      senderData,
            'receiver':    receiverData
        })

        encoder = ProtobufEncoder()

        payload = PresentYourselfRequest()

        encoder.encodePayload(aPayloadContent=payload,
                              aPayloadData=presentYourselfRequest)

        self.assertEqual(payload.messageName,   "PresentYourselfRequest")
        self.assertEqual(payload.sender.type,   "HelloCritty")
        self.assertEqual(payload.sender.nick,   "Sender")
        self.assertEqual(payload.receiver.type, "HelloCritty")
        self.assertEqual(payload.receiver.nick, "Receiver")

    def test_PresentYourselfResponse(self):
        senderData = {'type': Charstring(SimpleType()).assign(CharstringValue("HelloCritty")),
                      'nick': Charstring(SimpleType()).assign(CharstringValue("Sender"))}

        receiverData = {'type': Charstring(SimpleType()).assign(CharstringValue("HelloCritty")),
                        'nick': Charstring(SimpleType()).assign(CharstringValue("Receiver"))}

        presentYourselfResponse = PiewikPresentYourselfResponse()
        presentYourselfResponse.assign({
            'messageName': Charstring(SimpleType()).assign(CharstringValue("PresentYourselfResponse")),
            'sender':      senderData,
            'receiver':    receiverData
        })

        encoder = ProtobufEncoder()

        payload = PresentYourselfResponse()

        encoder.encodePayload(aPayloadContent=payload,
                              aPayloadData=presentYourselfResponse)

        self.assertEqual(payload.messageName,   "PresentYourselfResponse")
        self.assertEqual(payload.sender.type,   "HelloCritty")
        self.assertEqual(payload.sender.nick,   "Sender")
        self.assertEqual(payload.receiver.type, "HelloCritty")
        self.assertEqual(payload.receiver.nick, "Receiver")

    def test_LoadGraphAndWorkReqeust(self):
        senderData = {'type': Charstring(SimpleType()).assign(CharstringValue("HelloCritty")),
                      'nick': Charstring(SimpleType()).assign(CharstringValue("Sender"))}

        loadGraphAndWorkRequest = PiewikLoadGraphAndWorkRequest()
        loadGraphAndWorkRequest.assign({
            'messageName': Charstring(SimpleType()).assign(CharstringValue("LoadGraphAndWorkRequest")),
            'sender':      senderData
        })

        encoder = ProtobufEncoder()

        payload = LoadGraphAndWorkRequest()

        encoder.encodePayload(aPayloadContent=payload,
                              aPayloadData=loadGraphAndWorkRequest)

        self.assertEqual(payload.messageName, "LoadGraphAndWorkRequest")
        self.assertEqual(payload.sender.type, "HelloCritty")
        self.assertEqual(payload.sender.nick, "Sender")

    def test_LoadGraphAndWorkResponse(self):
        senderData = {'type': Charstring(SimpleType()).assign(CharstringValue("HelloCritty")),
                      'nick': Charstring(SimpleType()).assign(CharstringValue("Sender"))}

        receiverData = {'type': Charstring(SimpleType()).assign(CharstringValue("HelloCritty")),
                        'nick': Charstring(SimpleType()).assign(CharstringValue("Receiver"))}

        graphsData = [
            {'graphName': Charstring(SimpleType()).assign(CharstringValue("Graph1"))},
            {'graphName': Charstring(SimpleType()).assign(CharstringValue("Graph2"))}
        ]

        worksData =[
            {'graphName': Charstring(SimpleType()).assign(CharstringValue("Graph1")),
             'workName':  Charstring(SimpleType()).assign(CharstringValue("Work1"))},
            {'graphName': Charstring(SimpleType()).assign(CharstringValue("Graph1")),
             'workName':  Charstring(SimpleType()).assign(CharstringValue("Work2"))}
        ]

        workPredecessorsData = [
            {'workName':            Charstring(SimpleType()).assign(CharstringValue("Work2")),
             'predecessorWorkName': Charstring(SimpleType()).assign(CharstringValue("Work1"))}
        ]

        loadGraphAndWorkResponse = PiewikLoadGraphAndWorkResponse()
        loadGraphAndWorkResponse.assign({
            'messageName':      Charstring(SimpleType()).assign(CharstringValue("LoadGraphAndWorkResponse")),
            'sender':           senderData,
            'receiver':         receiverData,
            'graphs':           graphsData,
            'works':            worksData,
            'workPredecessors': workPredecessorsData
        })

        encoder = ProtobufEncoder()

        payload = LoadGraphAndWorkResponse()

        encoder.encodePayload(aPayloadContent=payload,
                              aPayloadData=loadGraphAndWorkResponse)

        self.assertEqual(payload.messageName,   "LoadGraphAndWorkResponse")
        self.assertEqual(payload.sender.type,   "HelloCritty")
        self.assertEqual(payload.sender.nick,   "Sender")
        self.assertEqual(payload.receiver.type, "HelloCritty")
        self.assertEqual(payload.receiver.nick, "Receiver")

        self.assertEqual(payload.graphs[0].graphName, "Graph1")
        self.assertEqual(payload.graphs[1].graphName, "Graph2")

        self.assertEqual(payload.works[0].graphName, "Graph1")
        self.assertEqual(payload.works[0].workName,  "Work1")
        self.assertEqual(payload.works[1].graphName, "Graph1")
        self.assertEqual(payload.works[1].workName,  "Work2")

        self.assertEqual(payload.workPredecessors[0].workName,            "Work2")
        self.assertEqual(payload.workPredecessors[0].predecessorWorkName, "Work1")

if __name__ == '__main__':
    unittest.main()
