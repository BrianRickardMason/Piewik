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

from google.protobuf.internal.containers import RepeatedCompositeFieldContainer
from google.protobuf.message             import Message

from Runtime.Decoder                                         import Decoder
from Runtime.Extensions.Critter.Interface.MessageCommon      import *
from Runtime.Extensions.Critter.Interface.Messages_pb2       import *
from Runtime.Extensions.Critter.Interface.Translation        import *
from Runtime.Extensions.Critter.Interface.TranslationHelpers import *
from Runtime.NewTypeSystem                                   import *

class ProtobufDecoder(Decoder):
    def decode(self, aBytesRead):
        envelope = Envelope()
        envelope.ParseFromString(aBytesRead)

        message = getMessageByHeaderId(envelope.header.id)
        message.ParseFromString(envelope.payload.payload)

        # Translation of the python representation of protobuf to the Piewik representation.
        return self.decodeInternally(message)

    def decodeInternally(self, aData):
        aHook = getCorrespondingPiewikType(aData)()
        dictionary = self.decodeDictionary(aData)
        aHook.assignValueType(dictionary)
        return aHook

    def decodeDictionary(self, aData):
        dictionary = {}

        for field in aData.ListFields():
            # Built-in types.
            if type(field[1]) is bool:
                dictionary[field[0].name] = Boolean().assignValueType(BooleanValue(field[1]))
            elif type(field[1]) is int:
                dictionary[field[0].name] = Integer().assignValueType(IntegerValue(field[1]))
            elif type(field[1]) is float:
                dictionary[field[0].name] = Float().assignValueType(FloatValue(field[1]))
            elif type(field[1]) in (str, unicode):
                # TODO: Potentially dangerous casting of unicode to str.
                dictionary[field[0].name] = Charstring().assignValueType(CharstringValue(str(field[1])))
            # Composite fields.
            elif type(field[1]) is RepeatedCompositeFieldContainer:
                # TODO: What if there's nothing?
                list = []
                for element in field[1]:
                    list.append(self.decodeDictionary(element))
                    self.decodeDictionary(element)
                dictionary[field[0].name] = list
            # Other protobuf types (structured).
            elif isinstance(field[1], Message):
                dictionary[field[0].name] = self.decodeDictionary(field[1])

        return dictionary
