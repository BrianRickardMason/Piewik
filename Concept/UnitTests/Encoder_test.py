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

from Concept.Encoder    import ProtobufEncoder
from Concept.TypeSystem import *
from Messages_pb2       import *

class PiewiekCritterData(Record):
    def __init__(self):
        Record.__init__(self, {'type': Charstring,
                               'nick': Charstring})

class PiewikHeartbeatAnnouncement(Record):
    def __init__(self):
        Record.__init__(self, {'messageName': Charstring,
                               'sender':      PiewiekCritterData,
                               'timestamp':   Float})

class PiewikPresentYourselfRequest(Record):
    def __init__(self):
        Record.__init__(self, {'messageName': Charstring,
                               'sender':      PiewiekCritterData,
                               'receiver':    PiewiekCritterData})

class PiewikPresentYourselfResponse(Record):
    def __init__(self):
        Record.__init__(self, {'messageName': Charstring,
                               'sender':      PiewiekCritterData,
                               'receiver':    PiewiekCritterData})

class Encoder_EncodePayload(unittest.TestCase):
    def test_HeartbeatAnnouncement(self):
        sender = PiewiekCritterData()
        sender.assign({'type': Charstring().assign("TYPE"),
                       'nick': Charstring().assign("NICK")})

        heartbeatAnnouncement = PiewikHeartbeatAnnouncement()
        heartbeatAnnouncement.assign({'messageName': Charstring().assign("HeartbeatAnnouncement"),
                                      'sender':      sender,
                                      'timestamp':   Float().assign(1234.5678)})

        encoder = ProtobufEncoder()

        payload = HeartbeatAnnouncement()

        encoder.encodePayload(aPayload=payload,
                              aPayloadData=heartbeatAnnouncement)

        self.assertEqual(payload.messageName, "HeartbeatAnnouncement")
        self.assertEqual(payload.sender.type, "TYPE")
        self.assertEqual(payload.sender.nick, "NICK")
        self.assertEqual(payload.timestamp,   1234.5678)

    def test_PresentYourselfRequest(self):
        sender = PiewiekCritterData()
        sender.assign({'type': Charstring().assign("HelloCritty"),
                       'nick': Charstring().assign("Sender")})

        receiver = PiewiekCritterData()
        receiver.assign({'type': Charstring().assign("HelloCritty"),
                         'nick': Charstring().assign("Receiver")})

        presentYourselfRequest = PiewikPresentYourselfRequest()
        presentYourselfRequest.assign({'messageName': Charstring().assign("PresentYourselfRequest"),
                                       'sender':      sender,
                                       'receiver':    receiver})

        encoder = ProtobufEncoder()

        payload = PresentYourselfRequest()

        encoder.encodePayload(aPayload=payload,
                              aPayloadData=presentYourselfRequest)

        self.assertEqual(payload.messageName,   "PresentYourselfRequest")
        self.assertEqual(payload.sender.type,   "HelloCritty")
        self.assertEqual(payload.sender.nick,   "Sender")
        self.assertEqual(payload.receiver.type, "HelloCritty")
        self.assertEqual(payload.receiver.nick, "Receiver")

    def test_PresentYourselfResponse(self):
        sender = PiewiekCritterData()
        sender.assign({'type': Charstring().assign("HelloCritty"),
                       'nick': Charstring().assign("Sender")})

        receiver = PiewiekCritterData()
        receiver.assign({'type': Charstring().assign("HelloCritty"),
                         'nick': Charstring().assign("Receiver")})

        presentYourselfResponse = PiewikPresentYourselfResponse()
        presentYourselfResponse.assign({'messageName': Charstring().assign("PresentYourselfResponse"),
                                        'sender':      sender,
                                        'receiver':    receiver})

        encoder = ProtobufEncoder()

        payload = PresentYourselfResponse()

        encoder.encodePayload(aPayload=payload,
                              aPayloadData=presentYourselfResponse)

        self.assertEqual(payload.messageName,   "PresentYourselfResponse")
        self.assertEqual(payload.sender.type,   "HelloCritty")
        self.assertEqual(payload.sender.nick,   "Sender")
        self.assertEqual(payload.receiver.type, "HelloCritty")
        self.assertEqual(payload.receiver.nick, "Receiver")

if __name__ == '__main__':
    unittest.main()
