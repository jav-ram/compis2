from graphviz import Digraph
from antlr4.tree.Trees import Trees
from decafeGenerated.grammars.DecafeParser import DecafeParser

TERMINAL_NODE_TYPE = "<class 'antlr4.tree.Tree.TerminalNodeImpl'>"
ERROR_NODE_TYPE = "<class 'antlr4.tree.Tree.ErrorNodeImpl'>"

def getNameRule(node):
    stringified = node.toString(DecafeParser.ruleNames, node.stop)
    return stringified.replace('[', ']').replace(']', '').split(' ')[0]

def convertInit(tree):
    D = Digraph("Gramatica", "gramatic")
    count = 0
    D.node(str(count), getNameRule(tree))
    def convert(node, parentId):
        count = parentId
        children = node.getChildCount()
        if children <= 0:
            return D, count

        for i in range(0, children):
            child = node.getChild(i)
            color = "black"
            if str(type(child)) == TERMINAL_NODE_TYPE:
                label = child.getText()
                shape = "rectangle"
                color = "green"
            elif str(type(child)) == ERROR_NODE_TYPE:
                label = child.getText()
                shape = "ellipse"
                color = "red"
            else:
                label = getNameRule(child)
                shape = "ellipse"
                color = "blue"
                if child.getChildCount() <= 0:
                    color = "red"

            count += 1                          # move to next id
            D.node(str(count), label, shape=shape, color=color)           # make node
            D.edge(str(parentId), str(count))   # connect node to parent
            _, count = convert(child, count)               # convert all childs of current node
        
        return D, count
    return convert



        