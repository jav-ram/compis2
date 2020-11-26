grammar Decafe;

ID : LETTER (LETTER | DIGIT)*;
NUM : DIGIT (DIGIT)*;
CHAR: '\''LETTER '\'';

LETTER : ('a' .. 'z' | 'A' .. 'Z');
DIGIT : [0-9]+;

SPACE : (' ' | '\n' | '\r' | '\t') -> skip;

program: declaration+;
declaration: structDeclaration
    | structInstantiation
    | varDeclaration
    | methodDeclaration
    | classDeclaration;
classDeclaration: 'class' lex=ID block;
varDeclaration: typevar=varType lex=ID ';'          #uniqueVar
    | typevar=varType lex=ID '[' size=NUM ']' ';'   #listVar;
structDeclaration: 'struct' lex=ID '{' (varDeclaration)* '}';
structInstantiation: 'struct' struct=ID lex=ID;
varType: 'int'
    | 'char'
    | 'boolean'
    | 'struct' ID
    | structDeclaration
    | 'void';
methodDeclaration: returnType=methodType lex=ID '(' (parameter (',' parameter)*)? ')' block;
methodType: 'int'
    | 'char'
    | 'boolean'
    | 'void';
parameter: typevar=parameterType lex=ID;
parameterType: 'int'
    | 'char'
    | 'boolean';
block: '{' (declaration)* (statement)* '}';
statement: ifStmt
    | whileStmt
    | returnStmt
    | methodCall ';'
    | block
    | asignStmt
    | (expression)? ';';
asignStmt: left=location '=' right=expression ';';
ifStmt: 'if' '(' expression ')' block elseStmt?;
elseStmt: ('else' block);
whileStmt: 'while' '('expression')' block;
returnStmt: 'return' (expression)? ';';
location: (lex=ID | lex=ID '[' expr=expression ']') ('.' loc=location)?;
expression: location #locExpr
    | methodCall #methodCallExpr
    | literal #literalExpr
    | '(' expression ')' #parentExpr
    | left=expression op_derive=arith_op_derived right=expression #derivedOpExpr
    | left=expression op_basic=arith_op right=expression #opExpr
    | left=expression operator=rel_op right=expression #relOpExpr
    | left=expression operator=eq_op right=expression #eqOpExpr
    | left=expression operator=cond_op right=expression #condOpExpr
    | '-' expression #negativeExpr
    | '!' expression #negationExpr;
arith_op: '+' | '-' | '%';
arith_op_derived:  '*' | '/';
methodCall: ID '(' (arg(','arg)*)? ')';
arg: expression;
op: arith_op | arith_op_derived | rel_op | eq_op | cond_op;
rel_op: '<' | '>' | '<=' | '>=';
eq_op: '==' | '!=';
cond_op: '&&' | '||';
literal: int_literal | char_literal | bool_literal;
int_literal: NUM;
char_literal: CHAR;
bool_literal: 'true' | 'false';
