import sys
import argparse
from antlr4 import *
from antlr4.tree.Trees import Trees

from decafeGenerated.grammars.DecafeLexer import DecafeLexer
from decafeGenerated.grammars.DecafeParser import DecafeParser
from decafeGenerated.grammars.DecafeListener import DecafeListener

from visitor import MyVistor

from Tree import convertor

def setUpArgParser():
    argparser = argparse.ArgumentParser(description="Proyecto # 0")
    argparser.add_argument("-i", dest="input", help="input file", type=str)
    argparser.add_argument("-t", dest="showTree", help="If tag is on the tree will show", action='store_true')

    return argparser.parse_args()

def main(argv):
    args = setUpArgParser()

    text = FileStream(args.input)
    lexer = DecafeLexer(text)
    stream = CommonTokenStream(lexer)
    parser = DecafeParser(stream)
    tree = parser.program()
    # print(Trees.toStringTree(tree, None, parser))
    tsymbol = MyVistor()
    tsymbol.visit(tree)
    print(tsymbol.symTable.ToString())
    if args.showTree:
        treeView, _ = convertor.convertInit(tree)(tree, 0)
        treeView.view()
        

if __name__ == '__main__':
    main(sys.argv)