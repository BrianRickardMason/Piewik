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

from Concept.Encoder    import Encoder
from Concept.TypeSystem import *

class ProtobufEncoder(Encoder):
    # TODO: Remove the aHeaderId.
    def encode(self, aEnvelope, aHeaderId, aMessageName, aPayloadData):
        envelope = aEnvelope()
        envelope.header.id = aHeaderId
        payload = aMessageName()
        self.encodePayload(aPayloadContent=payload,
                           aPayloadData=aPayloadData)
        envelope.payload.payload = payload.SerializeToString()
        return envelope

    def encodePayload(self, aPayloadContent, aPayloadData):
        # TODO: What type?
        # TODO: What exception?
        if not isinstance(aPayloadData, TTCN3Type):
            raise

        for key in aPayloadData.mDictionary.keys():
            if isinstance(aPayloadData.mValue[key], Record):
                payload     = getattr(aPayloadContent, key)
                payloadData = aPayloadData.mValue[key]
                self.encodePayload(payload, payloadData)
            elif isinstance(aPayloadData.mValue[key], RecordOf):
                payload     = getattr(aPayloadContent, key)
                payloadData = aPayloadData.mValue[key]
                for element in payloadData.mValue:
                    tmpPayload = payload.add()
                    self.encodePayload(tmpPayload, element)
            else:
                setattr(aPayloadContent, key, aPayloadData.mValue[key].value())