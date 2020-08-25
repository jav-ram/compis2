from prettytable import PrettyTable

GLOBAL = "global"


class SymbolTable():
    def __init__(self):
        self.symbols = Symbols()    # list of Symbol()
        self.types = Types()        # list of Type()
        self.scopes = Scopes()      # list of Scope()
    
    # returns true if the varName is declare in the same scope or on prior scope
    def isSymbolDeclared(self, name, scope):
        possibleScopes = self.scopes.GetAllFathers(scope)

        for s in possibleScopes:
            if not self.symbols.IsDeclarable(name, s):
                return True

        return False

    def PushSymbol(self, name, t, scope, isParam, times=1):
        last = self.symbols.Last()
        offset = 0

        if last != None:
            offset = last.offset + self.types.Get(last.type).size * last.times

        ty = self.types.GetByName(t)

        self.symbols.Push(name, ty.id, offset, scope, times, isParam)

    def PushType(self, name, t, size, scope):
        self.types.Push(name, t, size, scope)

    def PushScope(self, name, type, returnType, father, paramsTypes):
        self.scopes.Push(name, type, returnType, father, paramsTypes)

    def getScopeFirm(self, scope):
        s = self.scopes.Get(scope)
        return s.paramsTypes, s.returnType

    def currentScope(self):
        return self.scopes.Current()

    def ToString(self):
        symbolString = PrettyTable(["id", "name", "type", "offset", "scope", "times", "isParam"])
        typeString = PrettyTable(['id', 'name', 'type', 'size', 'scope'])
        scopeString = PrettyTable(['id', 'name', 'type', 'returnType', 'father', 'paramsTypes'])
        
        # add symbols
        for symId in self.symbols.table:
            sym = self.symbols.Get(symId)
            symbolString.add_row([sym.id, sym.name, sym.type, sym.offset, sym.scope, sym.times, sym.isParam])

        # add types
        for typeId in self.types.table:
            typ = self.types.Get(typeId)
            typeString.add_row([typ.id, typ.name, typ.type, typ.size, typ.scope])

        # add scopes
        for scopeId in self.scopes.table:
            s = self.scopes.Get(scopeId)
            scopeString.add_row([s.id, s.name, s.type, s.returnType, s.father, s.paramsTypes])


        return "\n".join([symbolString.get_string(), typeString.get_string(), scopeString.get_string()])



class Symbol():
    def __init__(self, id, name, t, offset, scope, times, isParam):
        self.id = id
        self.name = name
        self.type = t
        self.offset = offset
        self.scope = scope
        self.times = times
        self.isParam = isParam

class Symbols():
    def __init__(self):
        self.count = 0
        self.table = {}

    def Push(self, name, t, offset, scope, times, isParam):
        self.table[self.count] = Symbol(self.count, name, t, offset, scope, times, isParam)
        self.count += 1

    def Get(self, id):
        return self.table[id]

    def GetByNameScope(self, name, scope):
        for id in self.table:
            sym = self.Get(id)
            if name == sym.name and scope == sym.scope:
                return sym
        return None

    def GetAllSymbols(self, name):
        symbols = []
        for id in self.table:
            sym = self.Get(id)
            if name == sym.name:
                symbols.append(sym)
        return symbols

    def Last(self):
        if self.count == 0:
            return None
        return self.table[self.count-1]
    
    def GetAllSymbolsInSameScope(self, scope):
        symbols = []
        for id in self.table:
            sym = self.Get(id)
            if scope == sym.scope:
                symbols.append(sym)
        return symbols
    
    def IsDeclarable(self, name, scope):
        if self.GetByNameScope(name, scope) != None:
            return False
        return True

class Type():
    def __init__(self, id, name, t, size, scope):
        self.id = id
        self.name = name
        self.type = t
        self.size = size
        self.scope = scope

BASIC_TYPES = {
    0: Type(0, "int", "basic", 8, GLOBAL),
    1: Type(1, "char", "basic", 8, GLOBAL),
    2: Type(2, "boolean", "basic", 8, GLOBAL),
    3: Type(3, "void", "basic", 0, GLOBAL),
}

class Types():
    def __init__(self):
        self.count = 4
        self.table = BASIC_TYPES

    def Push(self, name, t, size, scope):
        self.table[self.count] = Type(self.count, name, t, size, scope)
        self.count += 1

    def Get(self, id):
        return self.table[id]
    
    def GetByName(self, name):
        for id in self.table:
            sym = self.Get(id)
            if name == sym.name:
                return sym
        return None
    
    def GetByNameScope(self, name, scope):
        for id in self.table:
            sym = self.Get(id)
            if name == sym.name and scope == sym.scope:
                return sym
        return None
    
    def IsDeclarable(self, name, scope):
        if self.GetByNameScope(name, scope) != None:
            return True
        return False

class Scope():
    def __init__(self, id, name, type, returnType, father, paramsTypes):
        self.id = id
        self.name = name
        self.type = type
        self.returnType = returnType
        self.father = father
        self.paramsTypes = paramsTypes

BASIC_SCOPES = {
    0: Scope(0, GLOBAL, None, None, None, [])
}

class Scopes():
    def __init__(self):
        self.count = 1
        self.current = 0
        self.table = BASIC_SCOPES
    
    def Next(self):
        self.current += 1
        return self.current
    
    def Prev(self):
        self.current -= 1
        return self.current
    
    def Current(self):
        return self.table[self.current].id

    def Push(self, name, type, returnType, father, paramsTypes):
        self.table[self.count] = Scope(self.count, name, type, returnType, father, paramsTypes)
        self.count += 1

    def Get(self, id):
        return self.table[id]

    def GetAllFathers(self, id):
        scopes = []
        father = self.Get(id).father

        scopes.append(id)

        while self.Get(father).name != GLOBAL:
            scopes.append(father)
            father = self.Get(father).father
        
        scopes.append(father) # deberia de ser 0
        return scopes