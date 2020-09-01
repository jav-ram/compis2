from decafeGenerated.grammars.DecafeParser import DecafeParser
from decafeGenerated.grammars.DecafeVisitor import DecafeVisitor

from evaluator import MyEvaluator

from SymbolTable import SymbolTable, Symbol

class MyVistor(DecafeVisitor):
    def __init__(self):
        self.symTable = SymbolTable()
    
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
                self.symTable.pushStruct(name, typeVar)
                return self.visitChildren(ctx)
            # is a declaration of a symbol inside a struct
            type = self.symTable.types.getByName(typeVar)
            self.symTable.pushVar(name, type.id)

            return self.visitChildren(ctx)
        elif "struct" in typeVar:
            # struct declaration
            typeVar = typeVar.replace("struct", "")
            self.symTable.pushStruct(name, typeVar)
            return self.visitChildren(ctx)

        type = self.symTable.types.getByName(typeVar)
        self.symTable.pushVar(name, type.id)
        return self.visitChildren(ctx)

    def visitListVar(self, ctx:DecafeParser.ListVarContext):
        name = str(ctx.ID())
        typeVar = ctx.typevar.getText()
        times = times=int(str(ctx.NUM()))

        type = self.symTable.types.getByName(typeVar)

        self.symTable.pushVar(name, type.id, times=times)
        return self.visitChildren(ctx)

    def visitMethodDeclaration(self, ctx:DecafeParser.MethodDeclarationContext):
        name = str(ctx.ID())
        scope = self.symTable.getCurrentScope()
        returnType = ctx.returnType.getText()

        # make the new scope
        self.symTable.pushScope(name, scope.id, "method", returnType)
        self.symTable.nextScope()
        # visit
        visit = self.visitChildren(ctx)
        # exit scope

        # check for right return type
        evaluator = MyEvaluator(self.symTable)
        evaluator.visit(ctx)

        if evaluator.typeVal == "error":
            print(evaluator.errorMsg)

        self.symTable.prevScope()
        return visit
    
    def visitParameter(self, ctx:DecafeParser.ParameterContext):
        name = str(ctx.ID())
        scope = self.symTable.getCurrentScope()
        typeVar = ctx.typevar.getText()
        type = self.symTable.types.getByName(typeVar)

        self.symTable.pushVar(name, type.id)
        scope.params.append(type.id)
        
        return self.visitChildren(ctx)

    def visitAsignStmt(self, ctx:DecafeParser.AsignStmtContext):
        evaluator = MyEvaluator(self.symTable)
        evaluator.visit(ctx.left)
        leftType =  evaluator.typeVal
        leftErrMsg = evaluator.errorMsg

        evaluator = MyEvaluator(self.symTable)
        evaluator.visit(ctx.right)
        rightType = evaluator.typeVal
        rightErrMsg = evaluator.errorMsg

        if leftType == "error":
            print(leftErrMsg)
        if rightType == "error":
            print(rightErrMsg)

        if leftType != rightType:
            print("Asign Error: type " + leftType + " is not equal to " + rightType + " in line " + str(ctx.start.line))

        return self.visitChildren(ctx)

    def visitMethodCall(self, ctx:DecafeParser.MethodCallContext):
        evaluator = MyEvaluator(self.symTable)
        evaluator.visit(ctx)

        if evaluator.typeVal == "error":
            print(evaluator.errorMsg)

        return self.visitChildren(ctx)

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

        if leftType == "error":
            print(leftErrMsg)
        if rightType == "error":
            print(rightErrMsg)

        if leftType != 'int' or rightType != 'int' or leftType != rightType:
            print("Operation " + op + " can only be apply on variables of type int")

        return self.visitChildren(ctx)

    def visitOpExpr(self, ctx:DecafeParser.OpExprContext):
        op = ctx.op_derive.getText()

        evaluator = MyEvaluator(self.symTable)
        evaluator.visit(ctx.left)
        leftType =  evaluator.typeVal
        leftErrMsg = evaluator.errorMsg

        evaluator = MyEvaluator(self.symTable)
        evaluator.visit(ctx.right)
        rightType = evaluator.typeVal
        rightErrMsg = evaluator.errorMsg

        if leftType == "error":
            print(leftErrMsg)
        if rightType == "error":
            print(rightErrMsg)

        if leftType != 'int' or rightType != 'int' or leftType != rightType:
            print("Operation " + op + " can only be apply on variables of type int")

        return self.visitChildren(ctx)