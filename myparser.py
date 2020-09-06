from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

from decafeGenerated.grammars.DecafeParser import DecafeParser

class MyParser(DecafeParser):

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None

        self.errMsg = []

    def notifyErrorListeners(self, msg:str, offendingToken=None, e= None):
        if offendingToken is None:
            offendingToken = self.getCurrentToken()
        self._syntaxErrors += 1
        line = offendingToken.line
        #column = offendingToken.column
        #listener = self.getErrorListenerDispatch()
        #listener.syntaxError(self, offendingToken, line, column, msg, e)
        self.errMsg.append((msg, line))