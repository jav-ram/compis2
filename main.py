import sys
from antlr4 import *
from antlr4.tree.Trees import Trees

from decafeGenerated.DecafeLexer import DecafeLexer
from decafeGenerated.DecafeParser import DecafeParser
from decafeGenerated.DecafeListener import DecafeListener

from Tree import convertor

class DecafePrintListener(DecafeListener):
    def enterProgram(self, ctx):
        print(ctx.values)


def main(argv):
    while True:
        text = InputStream("class Program { int var; }")
        lexer = DecafeLexer(text)
        stream = CommonTokenStream(lexer)
        parser = DecafeParser(stream)
        tree = parser.program()
        print(Trees.toStringTree(tree, None, parser))
        treeView, _ = convertor.convertInit(tree)(tree, 0)
        treeView.view()
        input()

if __name__ == '__main__':
    main(sys.argv)