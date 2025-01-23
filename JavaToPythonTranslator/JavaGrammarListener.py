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


    # Enter a parse tree produced by JavaGrammarParser#modifier.
    def enterModifier(self, ctx:JavaGrammarParser.ModifierContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#modifier.
    def exitModifier(self, ctx:JavaGrammarParser.ModifierContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#classOrInterfaceModifier.
    def enterClassOrInterfaceModifier(self, ctx:JavaGrammarParser.ClassOrInterfaceModifierContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#classOrInterfaceModifier.
    def exitClassOrInterfaceModifier(self, ctx:JavaGrammarParser.ClassOrInterfaceModifierContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#variableModifier.
    def enterVariableModifier(self, ctx:JavaGrammarParser.VariableModifierContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#variableModifier.
    def exitVariableModifier(self, ctx:JavaGrammarParser.VariableModifierContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#classDeclaration.
    def enterClassDeclaration(self, ctx:JavaGrammarParser.ClassDeclarationContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#classDeclaration.
    def exitClassDeclaration(self, ctx:JavaGrammarParser.ClassDeclarationContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#typeParameters.
    def enterTypeParameters(self, ctx:JavaGrammarParser.TypeParametersContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#typeParameters.
    def exitTypeParameters(self, ctx:JavaGrammarParser.TypeParametersContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#typeParameter.
    def enterTypeParameter(self, ctx:JavaGrammarParser.TypeParameterContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#typeParameter.
    def exitTypeParameter(self, ctx:JavaGrammarParser.TypeParameterContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#typeBound.
    def enterTypeBound(self, ctx:JavaGrammarParser.TypeBoundContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#typeBound.
    def exitTypeBound(self, ctx:JavaGrammarParser.TypeBoundContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#enumDeclaration.
    def enterEnumDeclaration(self, ctx:JavaGrammarParser.EnumDeclarationContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#enumDeclaration.
    def exitEnumDeclaration(self, ctx:JavaGrammarParser.EnumDeclarationContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#enumConstants.
    def enterEnumConstants(self, ctx:JavaGrammarParser.EnumConstantsContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#enumConstants.
    def exitEnumConstants(self, ctx:JavaGrammarParser.EnumConstantsContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#enumConstant.
    def enterEnumConstant(self, ctx:JavaGrammarParser.EnumConstantContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#enumConstant.
    def exitEnumConstant(self, ctx:JavaGrammarParser.EnumConstantContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#enumBodyDeclarations.
    def enterEnumBodyDeclarations(self, ctx:JavaGrammarParser.EnumBodyDeclarationsContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#enumBodyDeclarations.
    def exitEnumBodyDeclarations(self, ctx:JavaGrammarParser.EnumBodyDeclarationsContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#interfaceDeclaration.
    def enterInterfaceDeclaration(self, ctx:JavaGrammarParser.InterfaceDeclarationContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#interfaceDeclaration.
    def exitInterfaceDeclaration(self, ctx:JavaGrammarParser.InterfaceDeclarationContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#classBody.
    def enterClassBody(self, ctx:JavaGrammarParser.ClassBodyContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#classBody.
    def exitClassBody(self, ctx:JavaGrammarParser.ClassBodyContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#interfaceBody.
    def enterInterfaceBody(self, ctx:JavaGrammarParser.InterfaceBodyContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#interfaceBody.
    def exitInterfaceBody(self, ctx:JavaGrammarParser.InterfaceBodyContext):
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


    # Enter a parse tree produced by JavaGrammarParser#methodDeclaration.
    def enterMethodDeclaration(self, ctx:JavaGrammarParser.MethodDeclarationContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#methodDeclaration.
    def exitMethodDeclaration(self, ctx:JavaGrammarParser.MethodDeclarationContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#methodParameters.
    def enterMethodParameters(self, ctx:JavaGrammarParser.MethodParametersContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#methodParameters.
    def exitMethodParameters(self, ctx:JavaGrammarParser.MethodParametersContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#methodParameter.
    def enterMethodParameter(self, ctx:JavaGrammarParser.MethodParameterContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#methodParameter.
    def exitMethodParameter(self, ctx:JavaGrammarParser.MethodParameterContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#methodBody.
    def enterMethodBody(self, ctx:JavaGrammarParser.MethodBodyContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#methodBody.
    def exitMethodBody(self, ctx:JavaGrammarParser.MethodBodyContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#typeTypeOrVoid.
    def enterTypeTypeOrVoid(self, ctx:JavaGrammarParser.TypeTypeOrVoidContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#typeTypeOrVoid.
    def exitTypeTypeOrVoid(self, ctx:JavaGrammarParser.TypeTypeOrVoidContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#genericMethodDeclaration.
    def enterGenericMethodDeclaration(self, ctx:JavaGrammarParser.GenericMethodDeclarationContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#genericMethodDeclaration.
    def exitGenericMethodDeclaration(self, ctx:JavaGrammarParser.GenericMethodDeclarationContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#genericConstructorDeclaration.
    def enterGenericConstructorDeclaration(self, ctx:JavaGrammarParser.GenericConstructorDeclarationContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#genericConstructorDeclaration.
    def exitGenericConstructorDeclaration(self, ctx:JavaGrammarParser.GenericConstructorDeclarationContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#constructorDeclaration.
    def enterConstructorDeclaration(self, ctx:JavaGrammarParser.ConstructorDeclarationContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#constructorDeclaration.
    def exitConstructorDeclaration(self, ctx:JavaGrammarParser.ConstructorDeclarationContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#compactConstructorDeclaration.
    def enterCompactConstructorDeclaration(self, ctx:JavaGrammarParser.CompactConstructorDeclarationContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#compactConstructorDeclaration.
    def exitCompactConstructorDeclaration(self, ctx:JavaGrammarParser.CompactConstructorDeclarationContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#fieldDeclaration.
    def enterFieldDeclaration(self, ctx:JavaGrammarParser.FieldDeclarationContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#fieldDeclaration.
    def exitFieldDeclaration(self, ctx:JavaGrammarParser.FieldDeclarationContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#interfaceBodyDeclaration.
    def enterInterfaceBodyDeclaration(self, ctx:JavaGrammarParser.InterfaceBodyDeclarationContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#interfaceBodyDeclaration.
    def exitInterfaceBodyDeclaration(self, ctx:JavaGrammarParser.InterfaceBodyDeclarationContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#interfaceMemberDeclaration.
    def enterInterfaceMemberDeclaration(self, ctx:JavaGrammarParser.InterfaceMemberDeclarationContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#interfaceMemberDeclaration.
    def exitInterfaceMemberDeclaration(self, ctx:JavaGrammarParser.InterfaceMemberDeclarationContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#constDeclaration.
    def enterConstDeclaration(self, ctx:JavaGrammarParser.ConstDeclarationContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#constDeclaration.
    def exitConstDeclaration(self, ctx:JavaGrammarParser.ConstDeclarationContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#constantDeclarator.
    def enterConstantDeclarator(self, ctx:JavaGrammarParser.ConstantDeclaratorContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#constantDeclarator.
    def exitConstantDeclarator(self, ctx:JavaGrammarParser.ConstantDeclaratorContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#interfaceMethodDeclaration.
    def enterInterfaceMethodDeclaration(self, ctx:JavaGrammarParser.InterfaceMethodDeclarationContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#interfaceMethodDeclaration.
    def exitInterfaceMethodDeclaration(self, ctx:JavaGrammarParser.InterfaceMethodDeclarationContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#interfaceMethodModifier.
    def enterInterfaceMethodModifier(self, ctx:JavaGrammarParser.InterfaceMethodModifierContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#interfaceMethodModifier.
    def exitInterfaceMethodModifier(self, ctx:JavaGrammarParser.InterfaceMethodModifierContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#genericInterfaceMethodDeclaration.
    def enterGenericInterfaceMethodDeclaration(self, ctx:JavaGrammarParser.GenericInterfaceMethodDeclarationContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#genericInterfaceMethodDeclaration.
    def exitGenericInterfaceMethodDeclaration(self, ctx:JavaGrammarParser.GenericInterfaceMethodDeclarationContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#interfaceCommonBodyDeclaration.
    def enterInterfaceCommonBodyDeclaration(self, ctx:JavaGrammarParser.InterfaceCommonBodyDeclarationContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#interfaceCommonBodyDeclaration.
    def exitInterfaceCommonBodyDeclaration(self, ctx:JavaGrammarParser.InterfaceCommonBodyDeclarationContext):
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


    # Enter a parse tree produced by JavaGrammarParser#classOrInterfaceType.
    def enterClassOrInterfaceType(self, ctx:JavaGrammarParser.ClassOrInterfaceTypeContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#classOrInterfaceType.
    def exitClassOrInterfaceType(self, ctx:JavaGrammarParser.ClassOrInterfaceTypeContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#typeArgument.
    def enterTypeArgument(self, ctx:JavaGrammarParser.TypeArgumentContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#typeArgument.
    def exitTypeArgument(self, ctx:JavaGrammarParser.TypeArgumentContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#qualifiedNameList.
    def enterQualifiedNameList(self, ctx:JavaGrammarParser.QualifiedNameListContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#qualifiedNameList.
    def exitQualifiedNameList(self, ctx:JavaGrammarParser.QualifiedNameListContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#formalParameters.
    def enterFormalParameters(self, ctx:JavaGrammarParser.FormalParametersContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#formalParameters.
    def exitFormalParameters(self, ctx:JavaGrammarParser.FormalParametersContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#receiverParameter.
    def enterReceiverParameter(self, ctx:JavaGrammarParser.ReceiverParameterContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#receiverParameter.
    def exitReceiverParameter(self, ctx:JavaGrammarParser.ReceiverParameterContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#formalParameterList.
    def enterFormalParameterList(self, ctx:JavaGrammarParser.FormalParameterListContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#formalParameterList.
    def exitFormalParameterList(self, ctx:JavaGrammarParser.FormalParameterListContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#formalParameter.
    def enterFormalParameter(self, ctx:JavaGrammarParser.FormalParameterContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#formalParameter.
    def exitFormalParameter(self, ctx:JavaGrammarParser.FormalParameterContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#lastFormalParameter.
    def enterLastFormalParameter(self, ctx:JavaGrammarParser.LastFormalParameterContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#lastFormalParameter.
    def exitLastFormalParameter(self, ctx:JavaGrammarParser.LastFormalParameterContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#lambdaLVTIList.
    def enterLambdaLVTIList(self, ctx:JavaGrammarParser.LambdaLVTIListContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#lambdaLVTIList.
    def exitLambdaLVTIList(self, ctx:JavaGrammarParser.LambdaLVTIListContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#lambdaLVTIParameter.
    def enterLambdaLVTIParameter(self, ctx:JavaGrammarParser.LambdaLVTIParameterContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#lambdaLVTIParameter.
    def exitLambdaLVTIParameter(self, ctx:JavaGrammarParser.LambdaLVTIParameterContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#qualifiedName.
    def enterQualifiedName(self, ctx:JavaGrammarParser.QualifiedNameContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#qualifiedName.
    def exitQualifiedName(self, ctx:JavaGrammarParser.QualifiedNameContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#literal.
    def enterLiteral(self, ctx:JavaGrammarParser.LiteralContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#literal.
    def exitLiteral(self, ctx:JavaGrammarParser.LiteralContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#integerLiteral.
    def enterIntegerLiteral(self, ctx:JavaGrammarParser.IntegerLiteralContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#integerLiteral.
    def exitIntegerLiteral(self, ctx:JavaGrammarParser.IntegerLiteralContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#floatLiteral.
    def enterFloatLiteral(self, ctx:JavaGrammarParser.FloatLiteralContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#floatLiteral.
    def exitFloatLiteral(self, ctx:JavaGrammarParser.FloatLiteralContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#altAnnotationQualifiedName.
    def enterAltAnnotationQualifiedName(self, ctx:JavaGrammarParser.AltAnnotationQualifiedNameContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#altAnnotationQualifiedName.
    def exitAltAnnotationQualifiedName(self, ctx:JavaGrammarParser.AltAnnotationQualifiedNameContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#annotation.
    def enterAnnotation(self, ctx:JavaGrammarParser.AnnotationContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#annotation.
    def exitAnnotation(self, ctx:JavaGrammarParser.AnnotationContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#elementValuePairs.
    def enterElementValuePairs(self, ctx:JavaGrammarParser.ElementValuePairsContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#elementValuePairs.
    def exitElementValuePairs(self, ctx:JavaGrammarParser.ElementValuePairsContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#elementValuePair.
    def enterElementValuePair(self, ctx:JavaGrammarParser.ElementValuePairContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#elementValuePair.
    def exitElementValuePair(self, ctx:JavaGrammarParser.ElementValuePairContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#elementValue.
    def enterElementValue(self, ctx:JavaGrammarParser.ElementValueContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#elementValue.
    def exitElementValue(self, ctx:JavaGrammarParser.ElementValueContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#elementValueArrayInitializer.
    def enterElementValueArrayInitializer(self, ctx:JavaGrammarParser.ElementValueArrayInitializerContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#elementValueArrayInitializer.
    def exitElementValueArrayInitializer(self, ctx:JavaGrammarParser.ElementValueArrayInitializerContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#annotationTypeDeclaration.
    def enterAnnotationTypeDeclaration(self, ctx:JavaGrammarParser.AnnotationTypeDeclarationContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#annotationTypeDeclaration.
    def exitAnnotationTypeDeclaration(self, ctx:JavaGrammarParser.AnnotationTypeDeclarationContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#annotationTypeBody.
    def enterAnnotationTypeBody(self, ctx:JavaGrammarParser.AnnotationTypeBodyContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#annotationTypeBody.
    def exitAnnotationTypeBody(self, ctx:JavaGrammarParser.AnnotationTypeBodyContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#annotationTypeElementDeclaration.
    def enterAnnotationTypeElementDeclaration(self, ctx:JavaGrammarParser.AnnotationTypeElementDeclarationContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#annotationTypeElementDeclaration.
    def exitAnnotationTypeElementDeclaration(self, ctx:JavaGrammarParser.AnnotationTypeElementDeclarationContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#annotationTypeElementRest.
    def enterAnnotationTypeElementRest(self, ctx:JavaGrammarParser.AnnotationTypeElementRestContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#annotationTypeElementRest.
    def exitAnnotationTypeElementRest(self, ctx:JavaGrammarParser.AnnotationTypeElementRestContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#annotationMethodOrConstantRest.
    def enterAnnotationMethodOrConstantRest(self, ctx:JavaGrammarParser.AnnotationMethodOrConstantRestContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#annotationMethodOrConstantRest.
    def exitAnnotationMethodOrConstantRest(self, ctx:JavaGrammarParser.AnnotationMethodOrConstantRestContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#annotationMethodRest.
    def enterAnnotationMethodRest(self, ctx:JavaGrammarParser.AnnotationMethodRestContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#annotationMethodRest.
    def exitAnnotationMethodRest(self, ctx:JavaGrammarParser.AnnotationMethodRestContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#annotationConstantRest.
    def enterAnnotationConstantRest(self, ctx:JavaGrammarParser.AnnotationConstantRestContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#annotationConstantRest.
    def exitAnnotationConstantRest(self, ctx:JavaGrammarParser.AnnotationConstantRestContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#defaultValue.
    def enterDefaultValue(self, ctx:JavaGrammarParser.DefaultValueContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#defaultValue.
    def exitDefaultValue(self, ctx:JavaGrammarParser.DefaultValueContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#moduleDeclaration.
    def enterModuleDeclaration(self, ctx:JavaGrammarParser.ModuleDeclarationContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#moduleDeclaration.
    def exitModuleDeclaration(self, ctx:JavaGrammarParser.ModuleDeclarationContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#moduleBody.
    def enterModuleBody(self, ctx:JavaGrammarParser.ModuleBodyContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#moduleBody.
    def exitModuleBody(self, ctx:JavaGrammarParser.ModuleBodyContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#moduleDirective.
    def enterModuleDirective(self, ctx:JavaGrammarParser.ModuleDirectiveContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#moduleDirective.
    def exitModuleDirective(self, ctx:JavaGrammarParser.ModuleDirectiveContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#requiresModifier.
    def enterRequiresModifier(self, ctx:JavaGrammarParser.RequiresModifierContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#requiresModifier.
    def exitRequiresModifier(self, ctx:JavaGrammarParser.RequiresModifierContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#recordDeclaration.
    def enterRecordDeclaration(self, ctx:JavaGrammarParser.RecordDeclarationContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#recordDeclaration.
    def exitRecordDeclaration(self, ctx:JavaGrammarParser.RecordDeclarationContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#recordHeader.
    def enterRecordHeader(self, ctx:JavaGrammarParser.RecordHeaderContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#recordHeader.
    def exitRecordHeader(self, ctx:JavaGrammarParser.RecordHeaderContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#recordComponentList.
    def enterRecordComponentList(self, ctx:JavaGrammarParser.RecordComponentListContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#recordComponentList.
    def exitRecordComponentList(self, ctx:JavaGrammarParser.RecordComponentListContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#recordComponent.
    def enterRecordComponent(self, ctx:JavaGrammarParser.RecordComponentContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#recordComponent.
    def exitRecordComponent(self, ctx:JavaGrammarParser.RecordComponentContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#recordBody.
    def enterRecordBody(self, ctx:JavaGrammarParser.RecordBodyContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#recordBody.
    def exitRecordBody(self, ctx:JavaGrammarParser.RecordBodyContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#block.
    def enterBlock(self, ctx:JavaGrammarParser.BlockContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#block.
    def exitBlock(self, ctx:JavaGrammarParser.BlockContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#blockStatement.
    def enterBlockStatement(self, ctx:JavaGrammarParser.BlockStatementContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#blockStatement.
    def exitBlockStatement(self, ctx:JavaGrammarParser.BlockStatementContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#localVariableDeclaration.
    def enterLocalVariableDeclaration(self, ctx:JavaGrammarParser.LocalVariableDeclarationContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#localVariableDeclaration.
    def exitLocalVariableDeclaration(self, ctx:JavaGrammarParser.LocalVariableDeclarationContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#identifier.
    def enterIdentifier(self, ctx:JavaGrammarParser.IdentifierContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#identifier.
    def exitIdentifier(self, ctx:JavaGrammarParser.IdentifierContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#typeIdentifier.
    def enterTypeIdentifier(self, ctx:JavaGrammarParser.TypeIdentifierContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#typeIdentifier.
    def exitTypeIdentifier(self, ctx:JavaGrammarParser.TypeIdentifierContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#localTypeDeclaration.
    def enterLocalTypeDeclaration(self, ctx:JavaGrammarParser.LocalTypeDeclarationContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#localTypeDeclaration.
    def exitLocalTypeDeclaration(self, ctx:JavaGrammarParser.LocalTypeDeclarationContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#statement.
    def enterStatement(self, ctx:JavaGrammarParser.StatementContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#statement.
    def exitStatement(self, ctx:JavaGrammarParser.StatementContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#catchClause.
    def enterCatchClause(self, ctx:JavaGrammarParser.CatchClauseContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#catchClause.
    def exitCatchClause(self, ctx:JavaGrammarParser.CatchClauseContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#catchType.
    def enterCatchType(self, ctx:JavaGrammarParser.CatchTypeContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#catchType.
    def exitCatchType(self, ctx:JavaGrammarParser.CatchTypeContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#finallyBlock.
    def enterFinallyBlock(self, ctx:JavaGrammarParser.FinallyBlockContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#finallyBlock.
    def exitFinallyBlock(self, ctx:JavaGrammarParser.FinallyBlockContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#resourceSpecification.
    def enterResourceSpecification(self, ctx:JavaGrammarParser.ResourceSpecificationContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#resourceSpecification.
    def exitResourceSpecification(self, ctx:JavaGrammarParser.ResourceSpecificationContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#resources.
    def enterResources(self, ctx:JavaGrammarParser.ResourcesContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#resources.
    def exitResources(self, ctx:JavaGrammarParser.ResourcesContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#resource.
    def enterResource(self, ctx:JavaGrammarParser.ResourceContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#resource.
    def exitResource(self, ctx:JavaGrammarParser.ResourceContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#switchBlockStatementGroup.
    def enterSwitchBlockStatementGroup(self, ctx:JavaGrammarParser.SwitchBlockStatementGroupContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#switchBlockStatementGroup.
    def exitSwitchBlockStatementGroup(self, ctx:JavaGrammarParser.SwitchBlockStatementGroupContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#switchLabel.
    def enterSwitchLabel(self, ctx:JavaGrammarParser.SwitchLabelContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#switchLabel.
    def exitSwitchLabel(self, ctx:JavaGrammarParser.SwitchLabelContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#forControl.
    def enterForControl(self, ctx:JavaGrammarParser.ForControlContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#forControl.
    def exitForControl(self, ctx:JavaGrammarParser.ForControlContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#enhancedForControl.
    def enterEnhancedForControl(self, ctx:JavaGrammarParser.EnhancedForControlContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#enhancedForControl.
    def exitEnhancedForControl(self, ctx:JavaGrammarParser.EnhancedForControlContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#parExpression.
    def enterParExpression(self, ctx:JavaGrammarParser.ParExpressionContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#parExpression.
    def exitParExpression(self, ctx:JavaGrammarParser.ParExpressionContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#expressionList.
    def enterExpressionList(self, ctx:JavaGrammarParser.ExpressionListContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#expressionList.
    def exitExpressionList(self, ctx:JavaGrammarParser.ExpressionListContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#methodCall.
    def enterMethodCall(self, ctx:JavaGrammarParser.MethodCallContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#methodCall.
    def exitMethodCall(self, ctx:JavaGrammarParser.MethodCallContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#TernaryExpression.
    def enterTernaryExpression(self, ctx:JavaGrammarParser.TernaryExpressionContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#TernaryExpression.
    def exitTernaryExpression(self, ctx:JavaGrammarParser.TernaryExpressionContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#InstanceOfOperatorExpression.
    def enterInstanceOfOperatorExpression(self, ctx:JavaGrammarParser.InstanceOfOperatorExpressionContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#InstanceOfOperatorExpression.
    def exitInstanceOfOperatorExpression(self, ctx:JavaGrammarParser.InstanceOfOperatorExpressionContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#UnaryOperatorExpression.
    def enterUnaryOperatorExpression(self, ctx:JavaGrammarParser.UnaryOperatorExpressionContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#UnaryOperatorExpression.
    def exitUnaryOperatorExpression(self, ctx:JavaGrammarParser.UnaryOperatorExpressionContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#PrimaryExpression.
    def enterPrimaryExpression(self, ctx:JavaGrammarParser.PrimaryExpressionContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#PrimaryExpression.
    def exitPrimaryExpression(self, ctx:JavaGrammarParser.PrimaryExpressionContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#ObjectCreationExpression.
    def enterObjectCreationExpression(self, ctx:JavaGrammarParser.ObjectCreationExpressionContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#ObjectCreationExpression.
    def exitObjectCreationExpression(self, ctx:JavaGrammarParser.ObjectCreationExpressionContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#ExpressionLambda.
    def enterExpressionLambda(self, ctx:JavaGrammarParser.ExpressionLambdaContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#ExpressionLambda.
    def exitExpressionLambda(self, ctx:JavaGrammarParser.ExpressionLambdaContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#PostIncrementDecrementOperatorExpression.
    def enterPostIncrementDecrementOperatorExpression(self, ctx:JavaGrammarParser.PostIncrementDecrementOperatorExpressionContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#PostIncrementDecrementOperatorExpression.
    def exitPostIncrementDecrementOperatorExpression(self, ctx:JavaGrammarParser.PostIncrementDecrementOperatorExpressionContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#MemberReferenceExpression.
    def enterMemberReferenceExpression(self, ctx:JavaGrammarParser.MemberReferenceExpressionContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#MemberReferenceExpression.
    def exitMemberReferenceExpression(self, ctx:JavaGrammarParser.MemberReferenceExpressionContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#ExpressionSwitch.
    def enterExpressionSwitch(self, ctx:JavaGrammarParser.ExpressionSwitchContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#ExpressionSwitch.
    def exitExpressionSwitch(self, ctx:JavaGrammarParser.ExpressionSwitchContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#BinaryOperatorExpression.
    def enterBinaryOperatorExpression(self, ctx:JavaGrammarParser.BinaryOperatorExpressionContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#BinaryOperatorExpression.
    def exitBinaryOperatorExpression(self, ctx:JavaGrammarParser.BinaryOperatorExpressionContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#MethodCallExpression.
    def enterMethodCallExpression(self, ctx:JavaGrammarParser.MethodCallExpressionContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#MethodCallExpression.
    def exitMethodCallExpression(self, ctx:JavaGrammarParser.MethodCallExpressionContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#MethodReferenceExpression.
    def enterMethodReferenceExpression(self, ctx:JavaGrammarParser.MethodReferenceExpressionContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#MethodReferenceExpression.
    def exitMethodReferenceExpression(self, ctx:JavaGrammarParser.MethodReferenceExpressionContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#SquareBracketExpression.
    def enterSquareBracketExpression(self, ctx:JavaGrammarParser.SquareBracketExpressionContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#SquareBracketExpression.
    def exitSquareBracketExpression(self, ctx:JavaGrammarParser.SquareBracketExpressionContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#CastExpression.
    def enterCastExpression(self, ctx:JavaGrammarParser.CastExpressionContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#CastExpression.
    def exitCastExpression(self, ctx:JavaGrammarParser.CastExpressionContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#pattern.
    def enterPattern(self, ctx:JavaGrammarParser.PatternContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#pattern.
    def exitPattern(self, ctx:JavaGrammarParser.PatternContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#lambdaExpression.
    def enterLambdaExpression(self, ctx:JavaGrammarParser.LambdaExpressionContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#lambdaExpression.
    def exitLambdaExpression(self, ctx:JavaGrammarParser.LambdaExpressionContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#lambdaParameters.
    def enterLambdaParameters(self, ctx:JavaGrammarParser.LambdaParametersContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#lambdaParameters.
    def exitLambdaParameters(self, ctx:JavaGrammarParser.LambdaParametersContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#lambdaBody.
    def enterLambdaBody(self, ctx:JavaGrammarParser.LambdaBodyContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#lambdaBody.
    def exitLambdaBody(self, ctx:JavaGrammarParser.LambdaBodyContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#primary.
    def enterPrimary(self, ctx:JavaGrammarParser.PrimaryContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#primary.
    def exitPrimary(self, ctx:JavaGrammarParser.PrimaryContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#switchExpression.
    def enterSwitchExpression(self, ctx:JavaGrammarParser.SwitchExpressionContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#switchExpression.
    def exitSwitchExpression(self, ctx:JavaGrammarParser.SwitchExpressionContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#switchLabeledRule.
    def enterSwitchLabeledRule(self, ctx:JavaGrammarParser.SwitchLabeledRuleContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#switchLabeledRule.
    def exitSwitchLabeledRule(self, ctx:JavaGrammarParser.SwitchLabeledRuleContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#guardedPattern.
    def enterGuardedPattern(self, ctx:JavaGrammarParser.GuardedPatternContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#guardedPattern.
    def exitGuardedPattern(self, ctx:JavaGrammarParser.GuardedPatternContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#switchRuleOutcome.
    def enterSwitchRuleOutcome(self, ctx:JavaGrammarParser.SwitchRuleOutcomeContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#switchRuleOutcome.
    def exitSwitchRuleOutcome(self, ctx:JavaGrammarParser.SwitchRuleOutcomeContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#classType.
    def enterClassType(self, ctx:JavaGrammarParser.ClassTypeContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#classType.
    def exitClassType(self, ctx:JavaGrammarParser.ClassTypeContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#creator.
    def enterCreator(self, ctx:JavaGrammarParser.CreatorContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#creator.
    def exitCreator(self, ctx:JavaGrammarParser.CreatorContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#createdName.
    def enterCreatedName(self, ctx:JavaGrammarParser.CreatedNameContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#createdName.
    def exitCreatedName(self, ctx:JavaGrammarParser.CreatedNameContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#innerCreator.
    def enterInnerCreator(self, ctx:JavaGrammarParser.InnerCreatorContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#innerCreator.
    def exitInnerCreator(self, ctx:JavaGrammarParser.InnerCreatorContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#arrayCreatorRest.
    def enterArrayCreatorRest(self, ctx:JavaGrammarParser.ArrayCreatorRestContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#arrayCreatorRest.
    def exitArrayCreatorRest(self, ctx:JavaGrammarParser.ArrayCreatorRestContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#classCreatorRest.
    def enterClassCreatorRest(self, ctx:JavaGrammarParser.ClassCreatorRestContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#classCreatorRest.
    def exitClassCreatorRest(self, ctx:JavaGrammarParser.ClassCreatorRestContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#explicitGenericInvocation.
    def enterExplicitGenericInvocation(self, ctx:JavaGrammarParser.ExplicitGenericInvocationContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#explicitGenericInvocation.
    def exitExplicitGenericInvocation(self, ctx:JavaGrammarParser.ExplicitGenericInvocationContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#typeArgumentsOrDiamond.
    def enterTypeArgumentsOrDiamond(self, ctx:JavaGrammarParser.TypeArgumentsOrDiamondContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#typeArgumentsOrDiamond.
    def exitTypeArgumentsOrDiamond(self, ctx:JavaGrammarParser.TypeArgumentsOrDiamondContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#nonWildcardTypeArgumentsOrDiamond.
    def enterNonWildcardTypeArgumentsOrDiamond(self, ctx:JavaGrammarParser.NonWildcardTypeArgumentsOrDiamondContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#nonWildcardTypeArgumentsOrDiamond.
    def exitNonWildcardTypeArgumentsOrDiamond(self, ctx:JavaGrammarParser.NonWildcardTypeArgumentsOrDiamondContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#nonWildcardTypeArguments.
    def enterNonWildcardTypeArguments(self, ctx:JavaGrammarParser.NonWildcardTypeArgumentsContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#nonWildcardTypeArguments.
    def exitNonWildcardTypeArguments(self, ctx:JavaGrammarParser.NonWildcardTypeArgumentsContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#typeList.
    def enterTypeList(self, ctx:JavaGrammarParser.TypeListContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#typeList.
    def exitTypeList(self, ctx:JavaGrammarParser.TypeListContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#typeType.
    def enterTypeType(self, ctx:JavaGrammarParser.TypeTypeContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#typeType.
    def exitTypeType(self, ctx:JavaGrammarParser.TypeTypeContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#primitiveType.
    def enterPrimitiveType(self, ctx:JavaGrammarParser.PrimitiveTypeContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#primitiveType.
    def exitPrimitiveType(self, ctx:JavaGrammarParser.PrimitiveTypeContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#typeArguments.
    def enterTypeArguments(self, ctx:JavaGrammarParser.TypeArgumentsContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#typeArguments.
    def exitTypeArguments(self, ctx:JavaGrammarParser.TypeArgumentsContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#superSuffix.
    def enterSuperSuffix(self, ctx:JavaGrammarParser.SuperSuffixContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#superSuffix.
    def exitSuperSuffix(self, ctx:JavaGrammarParser.SuperSuffixContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#explicitGenericInvocationSuffix.
    def enterExplicitGenericInvocationSuffix(self, ctx:JavaGrammarParser.ExplicitGenericInvocationSuffixContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#explicitGenericInvocationSuffix.
    def exitExplicitGenericInvocationSuffix(self, ctx:JavaGrammarParser.ExplicitGenericInvocationSuffixContext):
        pass


    # Enter a parse tree produced by JavaGrammarParser#arguments.
    def enterArguments(self, ctx:JavaGrammarParser.ArgumentsContext):
        pass

    # Exit a parse tree produced by JavaGrammarParser#arguments.
    def exitArguments(self, ctx:JavaGrammarParser.ArgumentsContext):
        pass



del JavaGrammarParser