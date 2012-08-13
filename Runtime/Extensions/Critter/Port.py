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

import zmq

from Piewik.Runtime.Extensions.Critter import Decoder
from Piewik.Runtime.Extensions.Critter import Encoder
from Piewik.Runtime.Port               import MessagePort

class PiewikPort(MessagePort):
    def __init__(self, aAddress=None, aMapParam=None, aUnmapParam=None, aIn=[], aOut=[], aInOut=[]):
        MessagePort.__init__(self, aAddress, aMapParam, aUnmapParam, aIn, aOut, aInOut)

        self.mCtx = zmq.Context()

        self.mSendSocket = self.mCtx.socket(zmq.PUB)
        self.mSendSocket.setsockopt(zmq.LINGER, 0)
        # TODO: Remove the hardcoded value.
        self.mSendSocket.connect('tcp://127.0.0.1:2222')

        self.mReceiveSocket = self.mCtx.socket(zmq.SUB)
        # TODO: Remove the hardcoded value.
        self.mReceiveSocket.connect('tcp://127.0.0.1:4444')
        self.mReceiveSocket.setsockopt(zmq.SUBSCRIBE, '')

        self.mDecoder = Decoder()
        self.mEncoder = Encoder()

    def send(self, aPiewikMessage):
        """Sends a message (a valid Piewik type).

        Arguments:
            aPiewikMessage: A message to be sent.

        """
        protobufEnvelope = self.mEncoder.encode(aPiewikMessage)

        wireMessage = protobufEnvelope.SerializeToString()

        try:
            self.mSendSocket.send(wireMessage)
        except:
            # TODO: Raise a meaningful exception.
            raise

    def receive(self):
        """Receives bytes and translates them on the fly into a valie Piewik type.

        Returns:
            A valid Piewik type representing the received bytes.

        """
        bytesRead = self.mReceiveSocket.recv()

        piewikMessage = self.mDecoder.decode(bytesRead)

        if piewikMessage:
            return piewikMessage
        else:
            # TODO: Raise a meaningful exception.
            raise
