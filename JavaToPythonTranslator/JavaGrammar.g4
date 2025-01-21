grammar JavaGrammar;

compilationUnit
    : (typeDeclaration | ';')* ;

typeDeclaration
    : classOrInterfaceModifier* (
        classDeclaration
    )
    ;

classOrInterfaceModifier
    : PUBLIC
    | PROTECTED
    | PRIVATE
    | STATIC
    | ABSTRACT
    ;

classDeclaration
    : CLASS identifier classBody ;

classBody
    : '{' classBodyDeclaration* '}';

classBodyDeclaration
    : classOrInterfaceModifier* memberDeclaration;

memberDeclaration
    : fieldDeclaration
    | constructorDeclaration
    | methodDeclaration
    ; //dorzuć klasę w klasie

fieldDeclaration
    : typeType variableDeclarators ';'
    ;

typeType
    : primitiveType //dorzuć tworzenie zmiennych z klas
    ;

variableDeclarators
    : variableDeclarator (',' variableDeclarator)*
    ;

variableDeclarator
    : variableDeclaratorId ('=' variableInitializer)?
    ;

variableDeclaratorId
    : identifier ('[' ']')*
    ;

variableInitializer
    : arrayInitializer
    | expression
    ;

arrayInitializer
    : '{' (variableInitializer (',' variableInitializer)* ','?)? '}'
    ;

primitiveType
    : BOOLEAN
    | CHAR
    | BYTE
    | SHORT
    | INT
    | LONG
    | FLOAT
    | DOUBLE
    ;

identifier
    : IDENTIFIER ;

expression
    : creator
    | identifier
    ;

creator
    : NEW typeType ('[]')*;

CLASS: 'class' ;
PUBLIC: 'public' ;
PROTECTED: 'protected' ;
PRIVATE: 'private' ;
STATIC: 'static' ;
ABSTRACT: 'abstract' ;
FINAL: 'final' ;
NEW: 'new' ;

BOOLEAN: 'boolean';
CHAR: 'char';
BYTE: 'byte';
SHORT: 'short';
INT: 'int';
LONG: 'long';
FLOAT: 'float';
DOUBLE: 'double';

IDENTIFIER: Letter LetterOrDigit*;

fragment LetterOrDigit: Letter | [0-9];

fragment Letter:
    [a-zA-Z$_]                        // these are the "java letters" below 0x7F
    | ~[\u0000-\u007F\uD800-\uDBFF]   // covers all characters above 0x7F which are not a surrogate
    | [\uD800-\uDBFF] [\uDC00-\uDFFF] // covers UTF-16 surrogate pairs encodings for U+10000 to U+10FFFF
;

WS : [ \t\r\n\u000C]+ -> channel(HIDDEN);