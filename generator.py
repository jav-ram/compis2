from decafeGenerated.grammars.DecafeParser import DecafeParser
from decafeGenerated.grammars.DecafeVisitor import DecafeVisitor

from evaluator import MyEvaluator
from SymbolTable import SymbolTable, Symbol, Scope

from errorPrinter import RecordError

REGISTERS = [
    'R0',
    'R1',
    'R2',
    'R3',
    'R4',
    'R5',
    'R6',
    'R7',
    'R8',
]

REGISTER_FLAG = 'FL'

def GetSymbolOnStruct(s:dict, name:str):
    for key in s:
        sym = s[key]
        if name == sym.name:
            return sym

def GetMemoryAddress(name:str, offset:int):
    return '{}[{}]'.format(name.capitalize(), str(offset))

def GetTemporal(used:list):
    usable = list(set(REGISTERS) - set(used))
    usable = sorted(usable)
    return usable[0]

def Simplify(line:list, used:list=[], isStart=True):
    result = []
    t = []
    for i in range(len(line)):
        node = line[i]
        if type(node) is list:
            tmp = Simplify(node, used, False)
            tmpName = tmp[-1].dest
            result.extend(tmp)
            t.append(tmpName)
        else:
            t.append(node)

    if not isStart:
        dest = GetTemporal(used)
        used.append(dest)
        if len(t) == 3:
            if t[0] in used:
                i = used.index(t[0])
                del used[i]
            if t[2] in used:
                i = used.index(t[2])
                del used[i]
            t = Line(op=t[1], arg1=t[0], arg2=t[2], dest=dest)
        elif len(t) == 2:
            if t[1] in used:
                i = used.index(t[1])
                del used[i]
            t = Line(op=t[0], arg1=t[1], dest=dest)
        else:
            print("error")
    else:
        if len(t) == 3:
            if t[0] in used:
                i = used.index(t[0])
                del used[i]
            if t[2] in used:
                i = used.index(t[2])
                del used[i]
            t = Line(op=t[1], arg1=t[0], arg2=t[2])
        elif len(t) == 2:
            if t[1] in used:
                i = used.index(t[1])
                del used[i]
            t = Line(op=t[0], arg1=t[1])
        else:
            print("error")
        
    result.append(t)
    return result

def StartScope(scope:Scope):
    label = '{}{}'.format(scope.name[0].capitalize(), scope.id)
    return Line(op="START_" + label, type="label")

def EndScope(scope:Scope):
    label = '{}{}'.format(scope.name[0].capitalize(), scope.id)
    return Line(op="END_" + label, type="label")
    
class Line():
    def __init__(self, op:str, arg1:str=None, arg2:str=None, dest:str=None, type="expr"):
        self.op = op
        self.arg1 = arg1
        self.arg2 = arg2
        self.dest = dest
        self.type = type

    def __repr__(self):
        tmp = ""
        if self.type == "label":
            return self.op
        if self.dest != None:
            tmp += self.dest + " := "
        tmp += self.op + " " + self.arg1
        if self.arg2 != None:
            tmp += " " + self.arg2
        return tmp

    def __str__(self):
        tmp = ""
        if self.type == "label":
            return self.op
        if self.dest != None:
            tmp += self.dest + " := "
        tmp += self.op + " " + self.arg1
        if self.arg2 != None:
            tmp += " " + self.arg2
        return tmp
    

class ScopeStack():
    def __init__(self, symTable: SymbolTable):
        self.symTable = symTable
        self.count = 0
        self.current = 0
    
    def push(self):
        self.count += 1
        self.current = self.count
        return self.current
    
    def pop(self):
        prevScopeId = self.symTable.getScope(self.current).father
        self.current = prevScopeId
        return self.current

    def getCurrent(self):
        return self.symTable.getScope(self.current)

class Code():
    def __init__(self):
        self.lines = []

    def append(self, item: list):
        self.lines.append(item)

    def insert(self, item: list, index: int):
        self.lines.insert(index, item)

    def replace(self, item: list, index: int):
        self.lines[index] = item

class IntermediateCodeGenerator(DecafeVisitor):
    def __init__(self, symTable: SymbolTable):
        self.symTable = symTable
        self.scopeStack = ScopeStack(symTable)
        
        self.lines = []

    def visitClassDeclaration(self, ctx:DecafeParser.ClassDeclarationContext):
        self.scopeStack.push()              # get inside scope
        scope = self.scopeStack.getCurrent()
        self.lines.append(StartScope(scope))  # add label of scope
        self.visitChildren(ctx)             # visit
        self.lines.append(EndScope(scope))  # add label of scope
        self.scopeStack.pop()               # exit scope
        return


    def visitMethodDeclaration(self, ctx:DecafeParser.MethodDeclarationContext):
        self.scopeStack.push()              # get inside scope
        scope = self.symTable.getCurrentScope()
        self.lines.append(StartScope(scope))  # add label of scope
        self.visitChildren(ctx)             # visit
        self.lines.append(EndScope(scope))  # add label of scope
        self.scopeStack.pop()               # exit scope
        return

    def visitWhileStmt(self, ctx:DecafeParser.WhileStmtContext):
        self.scopeStack.push()              # get inside scope
        scope = self.scopeStack.getCurrent()
        expr = Simplify(self.visit(ctx.expression()))
        expr[-1].dest = REGISTER_FLAG
        self.lines.append(Line("GOTO", EndScope(scope).op))     # send to end to check if condition is met
        self.lines.append(StartScope(scope))                    # add label of scope

        self.visitChildren(ctx)                                 # visit
        self.lines.append(EndScope(scope))                      # add label of end scope
        self.scopeStack.pop()                                   # exit scope

        self.lines.extend(expr)                                 # calculate expr
        self.lines.append(Line("IF", REGISTER_FLAG))            # evaluate 
        self.lines.append(Line("GOTO", StartScope(scope).op))   # if true return to the loop else continue
        return

    def visitIfStmt(self, ctx:DecafeParser.IfStmtContext):
        self.scopeStack.push()
        scope = self.scopeStack.getCurrent()

        expr = Simplify(self.visit(ctx.expression()))
        expr[-1].dest = REGISTER_FLAG

        self.lines.extend(expr)                                 # calculate expr
        self.lines.append(Line("IF NOT", REGISTER_FLAG))        # evaluate the negation
        self.lines.append(Line("GOTO", EndScope(scope).op))     # if false go to the end of the if

        self.lines.append(StartScope(scope))                    # add label of IF_START scope

        self.visit(ctx.block())
        
        if ctx.elseStmt() != None:
            self.lines.append(EndScope(scope))                  # add label of IF_END of scope
            self.scopeStack.pop()
            self.scopeStack.push()
            scope = self.scopeStack.getCurrent()
            self.lines.append(StartScope(scope))                # add label of ELSE_START scope
            self.visit(ctx.elseStmt())

        # exit scope
        self.scopeStack.pop()
        self.lines.append(EndScope(scope))                      # add label of IF_END or ELSE_END scope
        return

    def visitStructDeclaration(self, ctx:DecafeParser.StructDeclarationContext):
        self.scopeStack.push()              # get inside scope
        self.visitChildren(ctx)
        self.scopeStack.pop()               # exit scope
        return 
    
    # Expressions

    def visitLocation(self, ctx:DecafeParser.LocationContext, struct:Symbol=None, offset:int=0, sp:Scope=None):
        name = str(ctx.ID())
        tokenIdx = ctx.expr
        tokenLoc = ctx.loc

        scope = self.scopeStack.getCurrent()
        # we have 3 options but we only need the offset and in what scope it is the variable
        if tokenIdx == None and tokenLoc == None:       # option 1 is a single variable
            if struct == None:
                symbol, scopeSym = self.symTable.GetSymbolScope(name, scope.id)
            else:
                symbol = GetSymbolOnStruct(struct.symbols, name)
                scopeSym = sp
            ma = scopeSym.name[0] + str(scopeSym.id)
            return GetMemoryAddress(ma, symbol.offset + offset)
        elif tokenIdx != None and tokenLoc == None:     # option 2 is a list variables
            index = int(tokenIdx.getText())
            if struct == None:
                symbol, scopeSym = self.symTable.GetSymbolScope(name, scope.id)
            else:
                symbol = GetSymbolOnStruct(struct.symbols.table, name)
                scopeSym = sp
            size = self.symTable.getType(symbol.type).size
            ma = scopeSym.name[0] + str(scopeSym.id)
            return GetMemoryAddress(ma, (symbol.offset + size * index) + offset)
        elif tokenLoc != None:                          # option 3 is a struct property
            if struct == None:
                symbol, scopeSym = self.symTable.GetSymbolScope(name, scope.id)
                tmp = symbol
            else:
                tmp = GetSymbolOnStruct(struct.symbols.table, name)
                scopeSym = sp
            return self.visitLocation(ctx.location(), struct=tmp, offset=tmp.offset, sp=scopeSym)
    
    def visitLiteralExpr(self, ctx:DecafeParser.LiteralExprContext):
        return ctx.literal().getText()
    
    def visitParentExpr(self, ctx:DecafeParser.ParentExprContext):
        return self.visit(ctx.expression())

    def visitDerivedOpExpr(self, ctx:DecafeParser.DerivedOpExprContext):
        left = self.visit(ctx.left)
        op = ctx.op_derive.getText()
        right = self.visit(ctx.right)
        return [left, op, right]

    def visitOpExpr(self, ctx:DecafeParser.OpExprContext):
        left = self.visit(ctx.left)
        op = ctx.op_basic.getText()
        right = self.visit(ctx.right)
        return [left, op, right]

    def visitRelOpExpr(self, ctx:DecafeParser.RelOpExprContext):
        left = self.visit(ctx.left)
        op = ctx.operator.getText()
        right = self.visit(ctx.right)
        return [left, op, right]

    def visitEqOpExpr(self, ctx:DecafeParser.EqOpExprContext):
        left = self.visit(ctx.left)
        op = ctx.operator.getText()
        right = self.visit(ctx.right)
        return [left, op, right]

    def visitCondOpExpr(self, ctx:DecafeParser.CondOpExprContext):
        left = self.visit(ctx.left)
        op = ctx.operator.getText()
        right = self.visit(ctx.right)
        return [left, op, right]
    
    def visitNegativeExpr(self, ctx:DecafeParser.NegativeExprContext):
        op = '-'
        expr = self.visit(ctx.expression())
        return [op, expr]
    
    def visitNegationExpr(self, ctx:DecafeParser.NegativeExprContext):
        op = '!'
        expr = self.visit(ctx.expression())
        return [op, expr]

    def visitAsignStmt(self, ctx:DecafeParser.AsignStmtContext):
        name = ctx.location().getText()
        scope = self.scopeStack.getCurrent()
        symbol, scopeSym = self.symTable.GetSymbolScope(name, scope.id)
        ma = scopeSym.name[0] + str(scopeSym.id)
        dest = GetMemoryAddress(ma, symbol.offset)

        expr = Simplify(self.visit(ctx.expression()))
        expr[-1].dest = dest
        self.lines.extend(expr)
        return self.visitChildren(ctx)