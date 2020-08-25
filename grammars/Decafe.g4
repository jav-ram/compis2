grammar Decafe;

ID : LETTER (LETTER | DIGIT)*;
NUM : DIGIT (DIGIT)*;
CHAR: LETTER | '\'' DIGIT '\'';

LETTER : ('a' .. 'z' | 'A' .. 'Z');
DIGIT : [0-9]+;

SPACE : (' ' | '\n' | '\r' | '\t') -> skip;

program: declaration+;
declaration: structDeclaration
    | varDeclaration
    | methodDeclaration
    | classDeclaration;
classDeclaration: 'class' lex=ID block;
varDeclaration: typevar=varType lex=ID ';'          #uniqueVar
    | typevar=varType lex=ID '[' size=NUM ']' ';'   #listVar;
structDeclaration: 'struct' lex=ID '{' (varDeclaration)* '}';
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
block: '{' (varDeclaration)* (statement)* '}';
statement: ifStmt
    | whileStmt
    | returnStmt
    | methodCall ';'
    | block
    | asignStmt
    | (expression)? ';';
asignStmt: left=location '=' right=expression ';';
ifStmt: 'if' '(' expression ')' block ('else' block)?;
whileStmt: 'while' '('expression')' block;
returnStmt: 'return' (expression)? ';';
location: (lex=ID | lex=ID '[' expr=expression ']') ('.' loc=location)?;
expression: location #locExpr
    | methodCall #methodCallExpr
    | literal #literalExpr
    | left=expression op_derive=arith_op_derived right=expression #derivedOpExpr
    | left=expression op_basic=arith_op right=expression #opExpr
    | '-' expression #negativeExpr
    | '!' expression #negationExpr
    | '(' expression ')' #parentExpr;
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
