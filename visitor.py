from decafeGenerated.grammars.DecafeParser import DecafeParser
from decafeGenerated.grammars.DecafeVisitor import DecafeVisitor

from evaluator import MyEvaluator
from SymbolTable import SymbolTable, Symbol

from errorPrinter import RecordError

class MyVistor(DecafeVisitor):
    def __init__(self):
        self.symTable = SymbolTable()
        self.errorMsg = []
    
    # Visit a parse tree produced by DecafeParser#classDeclaration.
    def visitClassDeclaration(self, ctx:DecafeParser.ClassDeclarationContext):
        name = str(ctx.ID())
        current = self.symTable.getCurrentScope()
        self.symTable.pushScope(name, current.id, "class")
        self.symTable.nextScope()
        # visit the inside of the scope with the current scope setup
        visit = self.visitChildren(ctx)
        # return to scope
        self.symTable.prevScope()
        return visit

    def visitStructDeclaration(self, ctx:DecafeParser.StructDeclarationContext):
        name = str(ctx.ID())
        current = self.symTable.getCurrentScope()
        # create scope of type
        scopeId = self.symTable.pushScope(name, current.id, "struct")
        self.symTable.nextScope()
        # visit
        visit = self.visitChildren(ctx)
        # create type
        self.symTable.prevScope()
        self.symTable.pushStructType(name, self.symTable.getScope(scopeId).symbols)

        return visit

    # Visit a parse tree produced by DecafeParser#uniqueVar.
    def visitUniqueVar(self, ctx:DecafeParser.UniqueVarContext):
        name = str(ctx.ID())
        scope = self.symTable.getCurrentScope()
        typeVar = ctx.typevar.getText()
        
        if scope.type == "struct":
            if "struct" in typeVar:
                # struct declaration
                typeVar = typeVar.replace("struct", "")
                var = self.symTable.pushStruct(name, typeVar)
                if var == None:
                    self.errorMsg.extend(RecordError("Struct not defined yet " + typeVar, ctx))
                    return self.visitChildren(ctx)
                return
            # is a declaration of a symbol inside a struct
            type = self.symTable.types.getByName(typeVar)
            var = self.symTable.pushVar(name, type.id)
            if var == None:
                self.errorMsg.extend(RecordError("Variable " + name + " is already declare", ctx))

            return self.visitChildren(ctx)
        elif "struct" in typeVar:
            # struct declaration
            typeVar = typeVar.replace("struct", "")
            var = self.symTable.pushStruct(name, typeVar)
            if var == None:
                self.errorMsg.extend(RecordError("Struct not defined yet " + typeVar, ctx))
            return self.visitChildren(ctx)

        type = self.symTable.types.getByName(typeVar)
        var = self.symTable.pushVar(name, type.id)
        if var == None:
            self.errorMsg.extend(RecordError("Variable " + name + " is already declare", ctx))
        return self.visitChildren(ctx)

    def visitListVar(self, ctx:DecafeParser.ListVarContext):
        name = str(ctx.ID())
        typeVar = ctx.typevar.getText()
        times = int(str(ctx.NUM()))

        if times <= 0:
            self.errorMsg.extend(RecordError("Variable size is negative or 0", ctx))

        type = self.symTable.types.getByName(typeVar)
        if type == None:
            type = self.symTable.types.getByName(typeVar.replace("struct", ""))

        var = self.symTable.pushVar(name, type.id, times=times)
        if var == None:
            self.errorMsg.extend(RecordError("Variable " + name + " is already declare", ctx))
        return self.visitChildren(ctx)

    def visitMethodDeclaration(self, ctx:DecafeParser.MethodDeclarationContext):
        name = str(ctx.ID())
        scope = self.symTable.getCurrentScope()
        returnType = ctx.returnType.getText()

        # make the new scope
        self.symTable.pushScope(name, scope.id, "method", returnType)
        self.symTable.nextScope()
        # visit
        if ctx.parameter() != None:
            parameters = ctx.parameter()
            for param in parameters:
                id = param.lex.text
                typ = param.typevar.getText()
                type = self.symTable.types.getByName(typ)
                self.symTable.pushVar(id, type.id)
                self.symTable.pushParam(type.id)
        

        visit = self.visitChildren(ctx.block())
        # exit scope

        # check for right return type
        evaluator = MyEvaluator(self.symTable)
        evaluator.visit(ctx)

        if evaluator.typeVal == "error":
            self.errorMsg.extend(RecordError(evaluator.errorMsg, ctx))

        self.symTable.prevScope()
        return visit
    
    def visitParameter(self, ctx:DecafeParser.ParameterContext):
        return self.visitChildren(ctx)

    def visitAsignStmt(self, ctx:DecafeParser.AsignStmtContext):
        evaluator = MyEvaluator(self.symTable)
        evaluator.visit(ctx)
        if evaluator.typeVal == 'error':
            self.errorMsg.extend(RecordError(evaluator.errorMsg, ctx))
        return

    def visitDerivedOpExpr(self, ctx:DecafeParser.DerivedOpExprContext):
        evaluator = MyEvaluator(self.symTable)
        evaluator.visit(ctx)
        if evaluator.typeVal == 'error':
            self.errorMsg.extend(RecordError(evaluator.errorMsg, ctx))
        return

    def visitOpExpr(self, ctx:DecafeParser.OpExprContext):
        evaluator = MyEvaluator(self.symTable)
        evaluator.visit(ctx)
        if evaluator.typeVal == 'error':
            self.errorMsg.extend(RecordError(evaluator.errorMsg, ctx))
        return

    def visitNegativeExpr(self, ctx:DecafeParser.NegativeExprContext):
        evaluator = MyEvaluator(self.symTable)
        evaluator.visit(ctx.expression())
        if evaluator.typeVal == 'error':
            self.errorMsg.extend(RecordError(evaluator.errorMsg, ctx))
        return

    def visitNegationExpr(self, ctx:DecafeParser.NegationExprContext):
        evaluator = MyEvaluator(self.symTable)
        evaluator.visit(ctx.expression())
        if evaluator.typeVal == 'error':
            self.errorMsg.extend(RecordError(evaluator.errorMsg, ctx))
        return

    def visitRelOpExpr(self, ctx:DecafeParser.RelOpExprContext):
        evaluator = MyEvaluator(self.symTable)
        evaluator.visit(ctx)
        if evaluator.typeVal == 'error':
            self.errorMsg.extend(RecordError(evaluator.errorMsg, ctx))
        return

    def visitEqOpExpr(self, ctx:DecafeParser.EqOpExprContext):
        evaluator = MyEvaluator(self.symTable)
        evaluator.visit(ctx)
        if evaluator.typeVal == 'error':
            self.errorMsg.extend(RecordError(evaluator.errorMsg, ctx))
        return

    def visitCondOpExpr(self, ctx:DecafeParser.CondOpExprContext):
        evaluator = MyEvaluator(self.symTable)
        evaluator.visit(ctx)
        if evaluator.typeVal == 'error':
            self.errorMsg.extend(RecordError(evaluator.errorMsg, ctx))
        return
    
    def visitIfStmt(self, ctx:DecafeParser.IfStmtContext):
        scope = self.symTable.getCurrentScope()

        evaluator = MyEvaluator(self.symTable)
        evaluator.visit(ctx.expression())
        t = evaluator.typeVal
        
        if t != 'boolean':
            self.errorMsg.extend(RecordError("Expected a boolean expression", ctx))

        # make the new scope
        print(self.symTable.getCurrentScope().id)
        self.symTable.pushScope("if", scope.id, "if")
        self.symTable.nextScope()

        if ctx.block() != None:
            try:
                for b in ctx.block():
                    self.visit(b)
            except:
                self.visit(ctx.block())
        
        if ctx.elseStmt() != None:
            self.symTable.prevScope()
            self.symTable.pushScope("else", scope.id, "else")
            self.visit(ctx.elseStmt())
            self.symTable.nextScope()

        # exit scope
        self.symTable.prevScope()
        return

    def visitWhileStmt(self, ctx:DecafeParser.WhileStmtContext):
        scope = self.symTable.getCurrentScope()

        evaluator = MyEvaluator(self.symTable)
        evaluator.visit(ctx.expression())
        t = evaluator.typeVal
        
        if t != 'boolean':
            self.errorMsg.extend(RecordError("Expected a boolean expression", ctx))

        # make the new scope
        print(self.symTable.getCurrentScope().id)
        self.symTable.pushScope("while", scope.id, "while")
        self.symTable.nextScope()

        if ctx.block() != None:
            try:
                for b in ctx.block():
                    self.visit(b)
            except:
                self.visit(ctx.block())

        # exit scope
        self.symTable.prevScope()
        return