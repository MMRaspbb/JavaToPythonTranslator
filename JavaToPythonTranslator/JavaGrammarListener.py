# Generated from JavaGrammar.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .JavaGrammarParser import JavaGrammarParser
else:
    from JavaGrammarParser import JavaGrammarParser

# This class defines a complete listener for a parse tree produced by JavaGrammarParser.
class JavaGrammarListener(ParseTreeListener):

    # Enter a parse tree produced by JavaGrammarParser#compilationUnit.
    def enterCompilationUnit(self, ctx:JavaGrammarParser.CompilationUnitContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#compilationUnit.
    def exitCompilationUnit(self, ctx:JavaGrammarParser.CompilationUnitContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#typeDeclaration.
    def enterTypeDeclaration(self, ctx:JavaGrammarParser.TypeDeclarationContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#typeDeclaration.
    def exitTypeDeclaration(self, ctx:JavaGrammarParser.TypeDeclarationContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#classOrInterfaceModifier.
    def enterClassOrInterfaceModifier(self, ctx:JavaGrammarParser.ClassOrInterfaceModifierContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#classOrInterfaceModifier.
    def exitClassOrInterfaceModifier(self, ctx:JavaGrammarParser.ClassOrInterfaceModifierContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#classDeclaration.
    def enterClassDeclaration(self, ctx:JavaGrammarParser.ClassDeclarationContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#classDeclaration.
    def exitClassDeclaration(self, ctx:JavaGrammarParser.ClassDeclarationContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#classBody.
    def enterClassBody(self, ctx:JavaGrammarParser.ClassBodyContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#classBody.
    def exitClassBody(self, ctx:JavaGrammarParser.ClassBodyContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#classBodyDeclaration.
    def enterClassBodyDeclaration(self, ctx:JavaGrammarParser.ClassBodyDeclarationContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#classBodyDeclaration.
    def exitClassBodyDeclaration(self, ctx:JavaGrammarParser.ClassBodyDeclarationContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#memberDeclaration.
    def enterMemberDeclaration(self, ctx:JavaGrammarParser.MemberDeclarationContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#memberDeclaration.
    def exitMemberDeclaration(self, ctx:JavaGrammarParser.MemberDeclarationContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#fieldDeclaration.
    def enterFieldDeclaration(self, ctx:JavaGrammarParser.FieldDeclarationContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#fieldDeclaration.
    def exitFieldDeclaration(self, ctx:JavaGrammarParser.FieldDeclarationContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#typeType.
    def enterTypeType(self, ctx:JavaGrammarParser.TypeTypeContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#typeType.
    def exitTypeType(self, ctx:JavaGrammarParser.TypeTypeContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#variableDeclarators.
    def enterVariableDeclarators(self, ctx:JavaGrammarParser.VariableDeclaratorsContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#variableDeclarators.
    def exitVariableDeclarators(self, ctx:JavaGrammarParser.VariableDeclaratorsContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#variableDeclarator.
    def enterVariableDeclarator(self, ctx:JavaGrammarParser.VariableDeclaratorContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#variableDeclarator.
    def exitVariableDeclarator(self, ctx:JavaGrammarParser.VariableDeclaratorContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#variableDeclaratorId.
    def enterVariableDeclaratorId(self, ctx:JavaGrammarParser.VariableDeclaratorIdContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#variableDeclaratorId.
    def exitVariableDeclaratorId(self, ctx:JavaGrammarParser.VariableDeclaratorIdContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#variableInitializer.
    def enterVariableInitializer(self, ctx:JavaGrammarParser.VariableInitializerContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#variableInitializer.
    def exitVariableInitializer(self, ctx:JavaGrammarParser.VariableInitializerContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#arrayInitializer.
    def enterArrayInitializer(self, ctx:JavaGrammarParser.ArrayInitializerContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#arrayInitializer.
    def exitArrayInitializer(self, ctx:JavaGrammarParser.ArrayInitializerContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#primitiveType.
    def enterPrimitiveType(self, ctx:JavaGrammarParser.PrimitiveTypeContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#primitiveType.
    def exitPrimitiveType(self, ctx:JavaGrammarParser.PrimitiveTypeContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#identifier.
    def enterIdentifier(self, ctx:JavaGrammarParser.IdentifierContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#identifier.
    def exitIdentifier(self, ctx:JavaGrammarParser.IdentifierContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#expression.
    def enterExpression(self, ctx:JavaGrammarParser.ExpressionContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#expression.
    def exitExpression(self, ctx:JavaGrammarParser.ExpressionContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#creator.
    def enterCreator(self, ctx:JavaGrammarParser.CreatorContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#creator.
    def exitCreator(self, ctx:JavaGrammarParser.CreatorContext):
        pass



del JavaGrammarParser