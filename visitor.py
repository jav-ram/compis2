from decafeGenerated.grammars.DecafeParser import DecafeParser
from decafeGenerated.grammars.DecafeVisitor import DecafeVisitor

from SymbolTable import SymbolTable

class MyVistor(DecafeVisitor):
    def __init__(self):
        self.symTable = SymbolTable()
    
    # Visit a parse tree produced by DecafeParser#classDeclaration.
    def visitClassDeclaration(self, ctx:DecafeParser.ClassDeclarationContext):
        name = str(ctx.ID())
        currentScope = self.symTable.currentScope()
        # first make the new scope
        self.symTable.PushScope(name, "class", None, currentScope, [])
        self.symTable.scopes.Next()
        # visit the inside of the scope with the current scope setup
        visit = self.visitChildren(ctx)
        # exit the scope
        self.symTable.scopes.Prev()
        return visit

    # Visit a parse tree produced by DecafeParser#uniqueVar.
    def visitUniqueVar(self, ctx:DecafeParser.UniqueVarContext):
        name = str(ctx.ID())
        scope = self.symTable.currentScope()
        typeVar = ctx.typevar.getText()
        
        if self.symTable.currentScopeType() == "struct":
            # is a declaration of a symbol inside a struct
            type = self.symTable.getType(typeVar, self.symTable.isTypeDeclared(typeVar, scope))
            # if type null error de type declare inside
            self.symTable.PushType(name, "property", type.size, scope)
            return self.visitChildren(ctx)
        elif "struct" in typeVar:
            # is a struct declaration
            structName = typeVar.replace("struct", "")
            s = self.symTable.isTypeDeclared(structName, scope) # in what scope is declared
            structScope = self.symTable.scopes.GetByStructScope(structName, s)
            structType = self.symTable.types.GetByNameScope(structName, s)

            self.symTable.PushSymbol(name, structType.name, scope, False) # create symbols for struct
            ss = self.symTable.PushScope(name, "istruct", None, scope, [])

            types = self.symTable.types.GetAllTypesOnScope(structScope.id)
            for t in types:
                print(t.name, t.id, scope, False)
                self.symTable.PushSymbol(t.name, t.name, ss, False)

            return self.visitChildren(ctx)

        self.symTable.PushSymbol(name, typeVar, scope, False)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DecafeParser#listVar.
    def visitListVar(self, ctx:DecafeParser.ListVarContext):
        name = str(ctx.ID())
        scope = self.symTable.currentScope()
        typeVar = ctx.typevar.getText()
        times = times=int(str(ctx.NUM()))

        self.symTable.PushSymbol(name, typeVar, scope, False, times)
        return self.visitChildren(ctx)
    
    # Visit a parse tree produced by DecafeParser#structDeclaration.
    def visitStructDeclaration(self, ctx:DecafeParser.StructDeclarationContext):
        name = str(ctx.ID())
        scope = self.symTable.currentScope()
        # make the new scope
        self.symTable.PushScope(name, "struct", None, scope, [])
        self.symTable.scopes.Next()
        # visit
        visit = self.visitChildren(ctx)
        # exit scope
        self.symTable.scopes.Prev()
        # first declare new type
        # size = self.symTable.getStructSize(name, scope)
        self.symTable.PushType(name, "struct", 0, scope)

        return visit

    # Visit a parse tree produced by DecafeParser#methodDeclaration.
    def visitMethodDeclaration(self, ctx:DecafeParser.MethodDeclarationContext):
        name = str(ctx.ID())
        scope = self.symTable.currentScope()
        returnType = ctx.returnType.getText()
        # make the new scope
        methodId = self.symTable.PushScope(name, "method", returnType, scope, [])
        self.symTable.scopes.Next()
        # visit
        visit = self.visitChildren(ctx)
        # exit scope
        self.symTable.scopes.Prev()
        # set params of method
        method = self.symTable.scopes.Get(methodId)
        symbolsInScope = self.symTable.symbols.GetAllSymbolsInSameScope(methodId)
        firm = []
        for sym in symbolsInScope:
            firm.append(sym.type)
        
        method.paramsTypes = firm

        return visit

    # Visit a parse tree produced by DecafeParser#parameter.
    def visitParameter(self, ctx:DecafeParser.ParameterContext):
        name = str(ctx.ID())
        scope = self.symTable.currentScope()
        typeVar = ctx.typevar.getText()

        self.symTable.PushSymbol(name, typeVar, scope, True)
        return self.visitChildren(ctx)

    