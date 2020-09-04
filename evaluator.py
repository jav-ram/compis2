from decafeGenerated.grammars.DecafeParser import DecafeParser
from decafeGenerated.grammars.DecafeVisitor import DecafeVisitor

INT = "int"
CHAR = "char"
BOOL = "boolean"
STRUCT = "struct"
VOID = "void"
ERROR = "error"

class MyEvaluator(DecafeVisitor):
    def __init__(self, SymbolTable, struct={}):
        self.symTable = SymbolTable
        self.struct = struct
        self.typeVal = VOID
        self.errorMsg = []

    # Literals
    def visitInt_literal(self, ctx:DecafeParser.Int_literalContext):
        self.typeVal = INT
        return self.visitChildren(ctx)
    def visitChar_literal(self, ctx:DecafeParser.Char_literalContext):
        self.typeVal = CHAR
        return self.visitChildren(ctx)
    def visitBool_literal(self, ctx:DecafeParser.Bool_literalContext):
        self.typeVal = BOOL
        return self.visitChildren(ctx)

    # Expressions
    def visitLiteralExpr(self, ctx:DecafeParser.LiteralExprContext):
        return self.visitChildren(ctx)
    def visitLocation(self, ctx:DecafeParser.LocationContext):
        id = ctx.lex.text
        if self.typeVal == STRUCT and self.struct != {}:
            symbols = self.struct.symbols
            isDefined = False

            for sid in symbols:
                sym = symbols[sid]
                if sym.name == id:
                    isDefined = True
                    break
            
            if not isDefined:
                self.typeVal = ERROR
                self.errorMsg.append("Property " + id + " is not define on the struct " + self.struct.name)
                return
            
            typ = self.symTable.types.get(sym.type)
            if typ.type == STRUCT:
                self.struct = sym
                evaluator = MyEvaluator(self.symTable, self.struct)
                evaluator.visitChildren(ctx)
                if evaluator.typeVal == ERROR:
                    self.errorMsg.append(evaluator.errorMsg)
                    return
            self.typeVal = typ.type
            # check inside struct

            if ctx.expr != None:
                num_expr = ctx.expr.getText()
                if sym.times == 1:
                    # is not an array
                    self.typeVal = ERROR
                    self.errorMsg.append("Variable " + id + " is not an array")
                try:
                    num = int(num_expr)
                    if not(num >= 0 and num < sym.times):
                        self.typeVal = ERROR
                        self.errorMsg.append("Index exceeds the length of variable " + id)
                except ValueError:
                    pass
                ev = MyEvaluator(self.symTable)
                ev.visit(ctx.expr)
                if not ev.typeVal == INT:
                    self.typeVal = ERROR
                    self.errorMsg.append("Index of varaible " + id + " should be an integer but we get " + ev.typeVal)
                return

            pass
        else:
            sym = self.symTable.isSymbolDeclared(id, self.symTable.getCurrentScope().id)
            if sym == None:
                self.errorMsg.append("Error variable " + id + " is not declared ")
                return
            
            typ = self.symTable.types.get(sym.type)
            if typ.type == STRUCT:
                self.struct = sym
                evaluator = MyEvaluator(self.symTable, self.struct)
                evaluator.visitChildren(ctx)
                if evaluator.typeVal == ERROR:
                    self.errorMsg.append(evaluator.errorMsg)
                    return

            self.typeVal = typ.type

            if ctx.expr != None:
                num_expr = ctx.expr.getText()
                if sym.times == 1:
                    # is not an array
                    self.typeVal = ERROR
                    self.errorMsg.append("Variable " + id + " is not an array")
                try:
                    num = int(num_expr)
                    if not(num >= 0 and num < sym.times):
                        self.typeVal = ERROR
                        self.errorMsg.append("Index exceeds the length of variable " + id)
                except ValueError:
                    pass
                ev = MyEvaluator(self.symTable)
                ev.visit(ctx.expr)
                if not ev.typeVal == INT:
                    self.typeVal = ERROR
                    self.errorMsg.append("Index of varaible " + id + " should be an integer but we get " + ev.typeVal)
                return

            # is list?
            # is NUM a literal if so is < times else check if at least is int

        return self.visitChildren(ctx)

    def visitMethodCall(self, ctx:DecafeParser.MethodCallContext):
        id = str(ctx.ID())
        method = self.symTable.isMethodDeclared(id, self.symTable.getCurrentScope().id)
        params = list(map(lambda tid: self.symTable.types.get(tid).name, method.params))

        visit = self.visitChildren(ctx)
        incoming=[]
        [incoming.extend([v]) for k,v in self.struct.items()]

        if not params == incoming:
            self.typeVal = ERROR
            self.errorMsg.append("Arguments for method " +  id + " are not of the same type. We expected " + str(params) + " but we got " + str(incoming))
            return

        self.typeVal = method.returnType

        return visit

    def visitArg(self, ctx:DecafeParser.ArgContext):
        visit = self.visitChildren(ctx)
        self.struct[ctx.getText()] = self.typeVal
        return visit

    def visitReturnStmt(self, ctx:DecafeParser.ReturnStmtContext):
        method = self.symTable.getCurrentScope()
        t = ERROR

        if ctx.expression() == None:
            t = VOID
        else:
            ev = MyEvaluator(self.symTable)
            ev.visit(ctx.expression())
            t = ev.typeVal


        if method.returnType != t:
            self.typeVal = ERROR
            self.errorMsg.append("Method " + method.name + " is trying to return type " + t + " but is expected to be of type " + method.returnType)
            return

    def visitAsignStmt(self, ctx:DecafeParser.AsignStmtContext):
        evaluator = MyEvaluator(self.symTable)
        evaluator.visit(ctx.left)
        leftType =  evaluator.typeVal
        leftErrMsg = evaluator.errorMsg

        evaluator = MyEvaluator(self.symTable)
        evaluator.visit(ctx.right)
        rightType = evaluator.typeVal
        rightErrMsg = evaluator.errorMsg

        if leftType == ERROR:
            self.errorMsg.append(leftErrMsg)
        if rightType == ERROR:
            self.errorMsg.append(rightErrMsg)


        if leftType != rightType:
            self.errorMsg.append("Asign Error: type " + leftType + " is not equal to " + rightType + " in line " + str(ctx.start.line))
            self.typeVal = ERROR
            return

        return

    def visitDerivedOpExpr(self, ctx:DecafeParser.DerivedOpExprContext):
        op = ctx.op_derive.getText()

        evaluator = MyEvaluator(self.symTable)
        evaluator.visit(ctx.left)
        leftType =  evaluator.typeVal
        leftErrMsg = evaluator.errorMsg

        evaluator = MyEvaluator(self.symTable)
        evaluator.visit(ctx.right)
        rightType = evaluator.typeVal
        rightErrMsg = evaluator.errorMsg


        if leftType == ERROR:
            self.errorMsg.append(leftErrMsg)
        if rightType == ERROR:
            self.errorMsg.append(rightErrMsg)

        if leftType != INT or rightType != INT or leftType != rightType:
            self.errorMsg.append("Operation " + op + " can only be apply on variables of type int")
            self.typeVal = ERROR
            return
        
        self.typeVal = INT

        return

    def visitOpExpr(self, ctx:DecafeParser.OpExprContext):
        op = ctx.op_basic.getText()

        evaluator = MyEvaluator(self.symTable)
        evaluator.visit(ctx.left)
        leftType =  evaluator.typeVal
        leftErrMsg = evaluator.errorMsg

        evaluator = MyEvaluator(self.symTable)
        evaluator.visit(ctx.right)
        rightType = evaluator.typeVal
        rightErrMsg = evaluator.errorMsg

        if leftType == ERROR:
            self.errorMsg.append(leftErrMsg)
        if rightType == ERROR:
            self.errorMsg.append(rightErrMsg)

        if leftType != INT or rightType != INT or leftType != rightType:
            self.errorMsg.append("Operation " + op + " can only be apply on variables of type int")
            self.typeVal = ERROR
            return

        self.typeVal = INT

        return

    def visitNegativeExpr(self, ctx:DecafeParser.NegativeExprContext):
        evaluator = MyEvaluator(self.symTable)
        evaluator.visit(ctx.expression())
        
        if evaluator.typeVal != INT:
            self.errorMsg.append("The negative operation can only be applied on variables of type int")
            self.typeVal = ERROR
            return

        self.typeVal = INT

        return

    def visitNegationExpr(self, ctx:DecafeParser.NegationExprContext):
        evaluator = MyEvaluator(self.symTable)
        evaluator.visit(ctx.expression())
        
        if evaluator.typeVal != 'boolean':
            self.errorMsg.append("The negation (!) operation can only be applied on variables of type boolean")
            self.typeVal = ERROR
            return

        self.typeVal = BOOL

        return

    def visitRelOpExpr(self, ctx:DecafeParser.RelOpExprContext):
        op = ctx.operator.getText()

        evaluator = MyEvaluator(self.symTable)
        evaluator.visit(ctx.left)
        leftType =  evaluator.typeVal
        leftErrMsg = evaluator.errorMsg

        evaluator = MyEvaluator(self.symTable)
        evaluator.visit(ctx.right)
        rightType = evaluator.typeVal
        rightErrMsg = evaluator.errorMsg

        if leftType == ERROR:
            self.errorMsg.append(leftErrMsg)
        if rightType == ERROR:
            self.errorMsg.append(rightErrMsg)

        if leftType != INT or rightType != INT or leftType != rightType:
            self.errorMsg.append("Comparative operations like " + op + " can only be apply on variables of type int")
            self.typeVal = ERROR
            return
        
        self.typeVal = BOOL

        return

    def visitEqOpExpr(self, ctx:DecafeParser.EqOpExprContext):
        op = ctx.operator.getText()

        evaluator = MyEvaluator(self.symTable)
        evaluator.visit(ctx.left)
        leftType =  evaluator.typeVal
        leftErrMsg = evaluator.errorMsg

        evaluator = MyEvaluator(self.symTable)
        evaluator.visit(ctx.right)
        rightType = evaluator.typeVal
        rightErrMsg = evaluator.errorMsg

        if leftType == ERROR:
            self.errorMsg.append(leftErrMsg)
        if rightType == ERROR:
            self.errorMsg.append(rightErrMsg)

        if leftType != rightType:
            self.errorMsg.append("Comparative operations like " + op + " can only be apply on variables of type int")
            self.typeVal = ERROR
            return

        
        self.typeVal = BOOL

        return

    def visitCondOpExpr(self, ctx:DecafeParser.CondOpExprContext):
        op = ctx.operator.getText()

        evaluator = MyEvaluator(self.symTable)
        evaluator.visit(ctx.left)
        leftType =  evaluator.typeVal
        leftErrMsg = evaluator.errorMsg

        evaluator = MyEvaluator(self.symTable)
        evaluator.visit(ctx.right)
        rightType = evaluator.typeVal
        rightErrMsg = evaluator.errorMsg

        if leftType == ERROR:
            self.errorMsg.append(leftErrMsg)
        if rightType == ERROR:
            self.errorMsg.append(rightErrMsg)

        if leftType != BOOL or rightType != BOOL or leftType != rightType:
            self.errorMsg.append("Comparative operations like " + op + " can only be apply on variables of type int")
            self.typeVal = ERROR
            return
        
        self.typeVal = BOOL

        return