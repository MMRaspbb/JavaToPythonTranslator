grammar JavaGrammar;

compilationUnit : classDeclaration ;

classDeclaration : CLASS Identifier '{' (methodDeclaration)* '}' ;

methodDeclaration : VOID Identifier '(' ')' '{' (statement)* '}' ;

statement
    : expression ';'
    | 'System.out.println' '(' expression ')' ';'
    ;
expression : Identifier '=' expression
           | Identifier
           | Literal
           ;
Literal : INTEGER | STRING | '';

CLASS : 'class';
VOID : 'void';

Identifier : [a-zA-Z_][a-zA-Z_0-9]*;
INT : [0-9]+ ;
STRING : '"' .*? '"' ;
WS : [ \t\r\n]+ -> skip;