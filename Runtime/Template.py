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

class TemplateMatcher(object):
    """Compares a given message with a given template."""

    def __init__(self, aMessage, aTemplate):
        """Initializes the matcher."""

        self.mMessage  = aMessage
        self.mTemplate = aTemplate

    def match(self):
        """The main function that is in charge of comparison.

        Returns:
            True if the message matches the template, False otherwise.

        """
        assert isTemplate(self.mTemplate), "The template is not a valid Piewik template."

        if self.mTemplate is None:
            return True

        if type(self.mTemplate) is tuple:
            return self.__matchTuple()

        if type(self.mTemplate) is list:
            return self.__matchList()

        if type(self.mTemplate) is dict:
            return self.__matchDictionary()

        # Simple types.
        return self.mMessage == self.mTemplate

    def __matchTuple(self):
        """A routine comparing a message with template that is a tuple.

        Returns:
            True if the message matches the template, False otherwise.

        """
        # TODO: Implement me.
        return True

    def __matchList(self):
        """A routine comparing a message with template that is a list.

        Returns:
            True if the message matches the template, False otherwise.

        """
        # TODO: Implement me.
        return True

    def __matchDictionary(self):
        """A routine comparing a message with template that is a dictionary.

        Returns:
            True if the message matches the template, False otherwise.

        """
        # TODO: Implement me.
        return True

def isTemplate(aTemplate):
    """Determines the template's correctness.

    Arguments:
        aTemplate: The template to be verified.

    Returns:
        True if the template is a correct Piewik template, False otherwise.

    """
    if aTemplate       is None    or \
       type(aTemplate) is bool    or \
       type(aTemplate) is int     or \
       type(aTemplate) is float   or \
       type(aTemplate) is long    or \
       type(aTemplate) is str     or \
       type(aTemplate) is unicode or \
       type(aTemplate) is tuple   or \
       type(aTemplate) is list    or \
       type(aTemplate) is dict:
        return True

    return False
