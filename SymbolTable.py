from prettytable import PrettyTable
import json
import pprint

GLOBAL = 0

class Type():
    def __init__(self, id, name, type, size, scope, dependency=None, symbols={}):
        self.id = id
        self.name = name
        self.type = type
        self.size = size
        self.scope = scope

        self.symbols = symbols
        self.dependency = dependency

class Types():
    def __init__(self):
        self.table = {}

        self.count = 0

    def get(self, id):
        return self.table[id]

    def getByName(self, name):
        for id in self.table:
            type = self.get(id)
            if type.name == name:
                return type

    def getByNameScope(self, name, scope):
        for id in self.table:
            type = self.get(id)
            if type.name == name and type.scope == scope:
                return type

    def getAllInScope(self, scope):
        types = []
        for id in self.table:
            type = self.get(id)
            if type.scope == scope:
                types.append(type)
        
        return types

    def push(self, name, type, size, scope, dependency=None, symbols={}):
        self.table[self.count] = Type(self.count, name, type, size, scope, dependency, symbols)
        self.count += 1
        return self.count - 1

class Symbol():
    def __init__(self, id, name, type, size, offset, times=1, symbols={}):
        self.id = id
        self.name = name
        self.type = type
        self.size = size
        self.offset = offset

        self.times = times
        self.symbols = symbols


class Symbols():
    def __init__(self):
        self.table = {}

        self.count = 0

    def get(self, id):
        return self.table[id]

    def getParams(self):
        res = []
        for key in self.table:
            sym = self.get(key)
            res.append(sym)
        return res

    def pushVar(self, name, type, size, offset, times=1):
        self.table[self.count] = Symbol(self.count, name, type, size, offset, times=times)
        self.count += 1
        return self.count - 1

    def pushStruct(self, name, type, size, offset, symbols):
        self.table[self.count] = Symbol(self.count, name, type, size, offset, symbols=symbols)
        self.count += 1
        return self.count - 1


class Scope():
    def __init__(self, id, name, father, type, params, returnType=None):
        self.id = id
        self.name = name
        self.father = father
        self.type = type

        self.symbols = Symbols()

        self.returnType = returnType
        self.params = params

        self.count = 0

    def pushVar(self, name, type, size, offset, times=1):
        return self.symbols.pushVar(name, type, size, offset, times=times)

    def pushStruct(self, name, type, size, offset, symbols):
        return self.symbols.pushStruct(name, type, size, offset, symbols=symbols)

    def pushParam(self, type):
        self.params.append(type)


class SymbolTable():
    def __init__(self):
        self.scopes = {}
        self.types = Types()

        self.scopes[0] = Scope(0, "global", None, [], None)

        self.types.push("int", "int", 8, GLOBAL)
        self.types.push("char", "char", 8, GLOBAL)
        self.types.push("boolean", "boolean", 8, GLOBAL)
        self.types.push("void", "void", 0, GLOBAL)

        self.count = 1
        self.current = 0

    def prevScope(self):
        curr = self.getCurrentScope()
        self.current = curr.father if curr.father != None else GLOBAL
        return self.current

    def nextScope(self):
        self.current = self.getScope(self.count - 1).id
        return self.current
    
    def getCurrentScope(self):
        return self.scopes[self.current]

    def getScope(self, id):
        if not id in self.scopes:
            return None
        return self.scopes[id]
    
    def pushParam(self, type):
        scope = self.getCurrentScope()
        scope.pushParam(type)

    def getType(self, id):
        return self.types.get(id)

    def isMethodDeclared(self, name, scope):
        s = self.getScope(scope)

        possibles = self.scopes
        for sid in possibles:
            p = self.getScope(sid)
            if p.name == name:
                return p

        while s.father != None:
            s = self.getScope(s.father)
            possibles = self.types.getAllInScope(s.id)
            for sid in possibles:
                p = self.getScope(sid)
                if p != None and p.name == name:
                    return p
        return None

    def isTypeDeclared(self, name, scope):
        s = self.getScope(scope)

        possibles = self.types.getAllInScope(s.id)
        for p in possibles:
            if p.name == name:
                return p

        while s.father != None:
            s = self.getScope(s.father)
            possibles = self.types.getAllInScope(s.id)
            for p in possibles:
                if p.name == name:
                    return p
        return None

    def isSymbolDeclared(self, name, scope):
        s = self.getScope(scope)

        possibles = s.symbols.table
        for pid in possibles:
            p = s.symbols.table[pid]
            if p.name == name:
                return p

        while s.father != None:
            s = self.getScope(s.father)
            possibles = s.symbols.table
            for pid in possibles:
                p = s.symbols.table[pid]
                if p.name == name:
                    return p
        return None

    def GetSymbolScope(self, name, scope):
        s = self.getScope(scope)

        possibles = s.symbols.table
        for pid in possibles:
            p = s.symbols.table[pid]
            if p.name == name:
                return p, s

        while s.father != None:
            s = self.getScope(s.father)
            possibles = s.symbols.table
            for pid in possibles:
                p = s.symbols.table[pid]
                if p.name == name:
                    return p, s
        return None

    def pushScope(self, name, father, type, returnType=None):
        self.scopes[self.count] = Scope(self.count, name, father, type, [], returnType)
        self.count += 1
        return self.count - 1

    def pushVar(self, name, type, times=1):
        offset = 0
        size = self.getType(type).size * times
        scope = self.getCurrentScope()

        # check if is declared in same scope
        possibles = scope.symbols.table
        for pid in possibles:
            p = scope.symbols.table[pid]
            if p.name == name:
                return None

        for s in scope.symbols.table:
            sym = scope.symbols.get(s)
            offset += sym.size
        
        return scope.pushVar(name, type, size, offset, times)

    def pushStruct(self, name, structName):
        offset = 0
        scope = self.getCurrentScope()
        type = self.isTypeDeclared(structName, scope.id)

        if type == None:
            return None

        size = type.size

        for s in scope.symbols.table:
            sym = scope.symbols.get(s)
            offset += sym.size
        

        return scope.pushStruct(name, type.id, size, offset, type.dependency.table)

    def pushType(self, name, type, size, symbols={}):
        return self.types.push(name, type, size, self.getCurrentScope().id, symbols)

    def pushStructType(self, name, symbols):
        size = self.getSize(symbols)
        return self.pushType(name, "struct", size, symbols=symbols)

    def getSize(self, symbols):
        size = 0
        d = symbols if type(symbols) == type({}) else symbols.table
        for id in d:
            s = d[id]
            t = self.getType(s.type)
            if t.type == "struct":
                size += self.getSize(s.symbols)
            else:
                size += t.size

        return size

    def Print(self):
        print(json.dumps(self.scopes, default=lambda x: x.__dict__), json.dumps(self.types, default=lambda x: x.__dict__))

    def ToString(self):
        sym = json.dumps(self.scopes, default=lambda x: x.__dict__, indent=4, sort_keys=True)
        typ = json.dumps(self.types, default=lambda x: x.__dict__, indent=4, sort_keys=True)
        return (sym, typ)