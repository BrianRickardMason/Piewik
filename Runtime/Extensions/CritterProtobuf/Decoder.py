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

from Piewik.Runtime.Decoder                                                        import Decoder
from Piewik.Runtime.Extensions.CritterProtobuf.CritterInterface.MessageCommon      import *
from Piewik.Runtime.Extensions.CritterProtobuf.CritterInterface.Messages_pb2       import *
from Piewik.Runtime.Extensions.CritterProtobuf.CritterInterface.Translation        import *
from Piewik.Runtime.Extensions.CritterProtobuf.CritterInterface.TranslationHelpers import *
from Piewik.Runtime.TypeSystem                                                     import *

class ProtobufDecoder(Decoder):
    def decode(self, aBytesRead):
        envelope = Envelope()
        envelope.ParseFromString(aBytesRead)

        message = getMessageByHeaderId(envelope.header.id)
        message.ParseFromString(envelope.payload.payload)

        # Translation of the python representation of protobuf to the Piewik representation.
        return self.encodeInternally(message)

    def encodeInternally(self, aData):
        aHook = getCorrespondingPiewikType(aData)()
        dictionary = self.encodeDictionary(aData)
        aHook.assign(dictionary)
        return aHook

    def encodeDictionary(self, aData):
        dictionary = {}

        for field in aData.ListFields():
            # TODO: Integer, float...
            # Built-in types.
            if type(field[1]) in (str, unicode):
                # TODO: Potentially dangerous casting of unicode to str.
                dictionary[field[0].name] = Charstring().assign(str(field[1]))

            # Composite fields.
            elif type(field[1]) is RepeatedCompositeFieldContainer:
                # TODO: What if there's nothing?
                piewikType = getCorrespondingPiewikType(field[1][0])
                recordOf = RecordOf(piewikType)
                list = []
                for element in field[1]:
                    list.append(piewikType().assign(self.encodeDictionary(element)))
                    self.encodeDictionary(element)
                recordOf.assign(list)
                dictionary[field[0].name] = recordOf

            # Other protobuf types (structured).
            elif isinstance(field[1], Message):
                piewikType = getCorrespondingPiewikType(field[1])
                dictionary[field[0].name] = piewikType().assign(self.encodeDictionary(field[1]))

        return dictionary
