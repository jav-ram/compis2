from decafeGenerated.grammars.DecafeParser import DecafeParser
from decafeGenerated.grammars.DecafeVisitor import DecafeVisitor

from SymbolTable import SymbolTable

class MyVistor(DecafeVisitor):
    def __init__(self):
        self.symTable = SymbolTable()
    
    # Visit a parse tree produced by DecafeParser#classDeclaration.
    def visitClassDeclaration(self, ctx:DecafeParser.ClassDeclarationContext):
        # first make the new scope
        self.symTable.PushScope(str(ctx.ID()), "class", None, self.symTable.scopes.Current(), [])
        self.symTable.scopes.Next()
        # visit the inside of the scope with the current scope setup
        visit = self.visitChildren(ctx)
        # exit the scope
        self.symTable.scopes.Prev()
        return visit

    # Visit a parse tree produced by DecafeParser#uniqueVar.
    def visitUniqueVar(self, ctx:DecafeParser.UniqueVarContext):
        self.symTable.PushSymbol(str(ctx.ID()), ctx.typevar.getText(), self.symTable.currentScope(), False)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DecafeParser#listVar.
    def visitListVar(self, ctx:DecafeParser.ListVarContext):
        self.symTable.PushSymbol(str(ctx.ID()), ctx.typevar.getText(), self.symTable.currentScope(), False)
        return self.visitChildren(ctx)
    
    # Visit a parse tree produced by DecafeParser#structDeclaration.
    def visitStructDeclaration(self, ctx:DecafeParser.StructDeclarationContext):
        # first declare new type
        self.symTable.PushType(str(ctx.ID()), "struct", 0, self.symTable.currentScope())
        # make the new scope
        self.symTable.PushScope(str(ctx.ID()), "struct", None, self.symTable.currentScope(), [])
        self.symTable.scopes.Next()
        # visit
        visit = self.visitChildren(ctx)
        # exit scope
        self.symTable.scopes.Prev()

        return visit

    