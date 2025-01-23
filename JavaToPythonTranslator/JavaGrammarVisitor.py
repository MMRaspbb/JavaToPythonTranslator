# Generated from JavaGrammar.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .JavaGrammarParser import JavaGrammarParser
else:
    from JavaGrammarParser import JavaGrammarParser

# This class defines a complete generic visitor for a parse tree produced by JavaGrammarParser.

class JavaGrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by JavaGrammarParser#compilationUnit.
    def visitCompilationUnit(self, ctx:JavaGrammarParser.CompilationUnitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#typeDeclaration.
    def visitTypeDeclaration(self, ctx:JavaGrammarParser.TypeDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#modifier.
    def visitModifier(self, ctx:JavaGrammarParser.ModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#classOrInterfaceModifier.
    def visitClassOrInterfaceModifier(self, ctx:JavaGrammarParser.ClassOrInterfaceModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#variableModifier.
    def visitVariableModifier(self, ctx:JavaGrammarParser.VariableModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#classDeclaration.
    def visitClassDeclaration(self, ctx:JavaGrammarParser.ClassDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#typeParameters.
    def visitTypeParameters(self, ctx:JavaGrammarParser.TypeParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#typeParameter.
    def visitTypeParameter(self, ctx:JavaGrammarParser.TypeParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#typeBound.
    def visitTypeBound(self, ctx:JavaGrammarParser.TypeBoundContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#enumDeclaration.
    def visitEnumDeclaration(self, ctx:JavaGrammarParser.EnumDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#enumConstants.
    def visitEnumConstants(self, ctx:JavaGrammarParser.EnumConstantsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#enumConstant.
    def visitEnumConstant(self, ctx:JavaGrammarParser.EnumConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#enumBodyDeclarations.
    def visitEnumBodyDeclarations(self, ctx:JavaGrammarParser.EnumBodyDeclarationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#interfaceDeclaration.
    def visitInterfaceDeclaration(self, ctx:JavaGrammarParser.InterfaceDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#classBody.
    def visitClassBody(self, ctx:JavaGrammarParser.ClassBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#interfaceBody.
    def visitInterfaceBody(self, ctx:JavaGrammarParser.InterfaceBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#classBodyDeclaration.
    def visitClassBodyDeclaration(self, ctx:JavaGrammarParser.ClassBodyDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#memberDeclaration.
    def visitMemberDeclaration(self, ctx:JavaGrammarParser.MemberDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#methodDeclaration.
    def visitMethodDeclaration(self, ctx:JavaGrammarParser.MethodDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#methodParameters.
    def visitMethodParameters(self, ctx:JavaGrammarParser.MethodParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#methodParameter.
    def visitMethodParameter(self, ctx:JavaGrammarParser.MethodParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#methodBody.
    def visitMethodBody(self, ctx:JavaGrammarParser.MethodBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#typeTypeOrVoid.
    def visitTypeTypeOrVoid(self, ctx:JavaGrammarParser.TypeTypeOrVoidContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#genericMethodDeclaration.
    def visitGenericMethodDeclaration(self, ctx:JavaGrammarParser.GenericMethodDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#genericConstructorDeclaration.
    def visitGenericConstructorDeclaration(self, ctx:JavaGrammarParser.GenericConstructorDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#constructorDeclaration.
    def visitConstructorDeclaration(self, ctx:JavaGrammarParser.ConstructorDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#compactConstructorDeclaration.
    def visitCompactConstructorDeclaration(self, ctx:JavaGrammarParser.CompactConstructorDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#fieldDeclaration.
    def visitFieldDeclaration(self, ctx:JavaGrammarParser.FieldDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#interfaceBodyDeclaration.
    def visitInterfaceBodyDeclaration(self, ctx:JavaGrammarParser.InterfaceBodyDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#interfaceMemberDeclaration.
    def visitInterfaceMemberDeclaration(self, ctx:JavaGrammarParser.InterfaceMemberDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#constDeclaration.
    def visitConstDeclaration(self, ctx:JavaGrammarParser.ConstDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#constantDeclarator.
    def visitConstantDeclarator(self, ctx:JavaGrammarParser.ConstantDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#interfaceMethodDeclaration.
    def visitInterfaceMethodDeclaration(self, ctx:JavaGrammarParser.InterfaceMethodDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#interfaceMethodModifier.
    def visitInterfaceMethodModifier(self, ctx:JavaGrammarParser.InterfaceMethodModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#genericInterfaceMethodDeclaration.
    def visitGenericInterfaceMethodDeclaration(self, ctx:JavaGrammarParser.GenericInterfaceMethodDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#interfaceCommonBodyDeclaration.
    def visitInterfaceCommonBodyDeclaration(self, ctx:JavaGrammarParser.InterfaceCommonBodyDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#variableDeclarators.
    def visitVariableDeclarators(self, ctx:JavaGrammarParser.VariableDeclaratorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#variableDeclarator.
    def visitVariableDeclarator(self, ctx:JavaGrammarParser.VariableDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#variableDeclaratorId.
    def visitVariableDeclaratorId(self, ctx:JavaGrammarParser.VariableDeclaratorIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#variableInitializer.
    def visitVariableInitializer(self, ctx:JavaGrammarParser.VariableInitializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#arrayInitializer.
    def visitArrayInitializer(self, ctx:JavaGrammarParser.ArrayInitializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#classOrInterfaceType.
    def visitClassOrInterfaceType(self, ctx:JavaGrammarParser.ClassOrInterfaceTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#typeArgument.
    def visitTypeArgument(self, ctx:JavaGrammarParser.TypeArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#qualifiedNameList.
    def visitQualifiedNameList(self, ctx:JavaGrammarParser.QualifiedNameListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#formalParameters.
    def visitFormalParameters(self, ctx:JavaGrammarParser.FormalParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#receiverParameter.
    def visitReceiverParameter(self, ctx:JavaGrammarParser.ReceiverParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#formalParameterList.
    def visitFormalParameterList(self, ctx:JavaGrammarParser.FormalParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#formalParameter.
    def visitFormalParameter(self, ctx:JavaGrammarParser.FormalParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#lastFormalParameter.
    def visitLastFormalParameter(self, ctx:JavaGrammarParser.LastFormalParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#lambdaLVTIList.
    def visitLambdaLVTIList(self, ctx:JavaGrammarParser.LambdaLVTIListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#lambdaLVTIParameter.
    def visitLambdaLVTIParameter(self, ctx:JavaGrammarParser.LambdaLVTIParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#qualifiedName.
    def visitQualifiedName(self, ctx:JavaGrammarParser.QualifiedNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#literal.
    def visitLiteral(self, ctx:JavaGrammarParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#integerLiteral.
    def visitIntegerLiteral(self, ctx:JavaGrammarParser.IntegerLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#floatLiteral.
    def visitFloatLiteral(self, ctx:JavaGrammarParser.FloatLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#altAnnotationQualifiedName.
    def visitAltAnnotationQualifiedName(self, ctx:JavaGrammarParser.AltAnnotationQualifiedNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#annotation.
    def visitAnnotation(self, ctx:JavaGrammarParser.AnnotationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#elementValuePairs.
    def visitElementValuePairs(self, ctx:JavaGrammarParser.ElementValuePairsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#elementValuePair.
    def visitElementValuePair(self, ctx:JavaGrammarParser.ElementValuePairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#elementValue.
    def visitElementValue(self, ctx:JavaGrammarParser.ElementValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#elementValueArrayInitializer.
    def visitElementValueArrayInitializer(self, ctx:JavaGrammarParser.ElementValueArrayInitializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#annotationTypeDeclaration.
    def visitAnnotationTypeDeclaration(self, ctx:JavaGrammarParser.AnnotationTypeDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#annotationTypeBody.
    def visitAnnotationTypeBody(self, ctx:JavaGrammarParser.AnnotationTypeBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#annotationTypeElementDeclaration.
    def visitAnnotationTypeElementDeclaration(self, ctx:JavaGrammarParser.AnnotationTypeElementDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#annotationTypeElementRest.
    def visitAnnotationTypeElementRest(self, ctx:JavaGrammarParser.AnnotationTypeElementRestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#annotationMethodOrConstantRest.
    def visitAnnotationMethodOrConstantRest(self, ctx:JavaGrammarParser.AnnotationMethodOrConstantRestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#annotationMethodRest.
    def visitAnnotationMethodRest(self, ctx:JavaGrammarParser.AnnotationMethodRestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#annotationConstantRest.
    def visitAnnotationConstantRest(self, ctx:JavaGrammarParser.AnnotationConstantRestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#defaultValue.
    def visitDefaultValue(self, ctx:JavaGrammarParser.DefaultValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#moduleDeclaration.
    def visitModuleDeclaration(self, ctx:JavaGrammarParser.ModuleDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#moduleBody.
    def visitModuleBody(self, ctx:JavaGrammarParser.ModuleBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#moduleDirective.
    def visitModuleDirective(self, ctx:JavaGrammarParser.ModuleDirectiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#requiresModifier.
    def visitRequiresModifier(self, ctx:JavaGrammarParser.RequiresModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#recordDeclaration.
    def visitRecordDeclaration(self, ctx:JavaGrammarParser.RecordDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#recordHeader.
    def visitRecordHeader(self, ctx:JavaGrammarParser.RecordHeaderContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#recordComponentList.
    def visitRecordComponentList(self, ctx:JavaGrammarParser.RecordComponentListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#recordComponent.
    def visitRecordComponent(self, ctx:JavaGrammarParser.RecordComponentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#recordBody.
    def visitRecordBody(self, ctx:JavaGrammarParser.RecordBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#block.
    def visitBlock(self, ctx:JavaGrammarParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#blockStatement.
    def visitBlockStatement(self, ctx:JavaGrammarParser.BlockStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#localVariableDeclaration.
    def visitLocalVariableDeclaration(self, ctx:JavaGrammarParser.LocalVariableDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#identifier.
    def visitIdentifier(self, ctx:JavaGrammarParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#typeIdentifier.
    def visitTypeIdentifier(self, ctx:JavaGrammarParser.TypeIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#localTypeDeclaration.
    def visitLocalTypeDeclaration(self, ctx:JavaGrammarParser.LocalTypeDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#statement.
    def visitStatement(self, ctx:JavaGrammarParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#catchClause.
    def visitCatchClause(self, ctx:JavaGrammarParser.CatchClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#catchType.
    def visitCatchType(self, ctx:JavaGrammarParser.CatchTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#finallyBlock.
    def visitFinallyBlock(self, ctx:JavaGrammarParser.FinallyBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#resourceSpecification.
    def visitResourceSpecification(self, ctx:JavaGrammarParser.ResourceSpecificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#resources.
    def visitResources(self, ctx:JavaGrammarParser.ResourcesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#resource.
    def visitResource(self, ctx:JavaGrammarParser.ResourceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#switchBlockStatementGroup.
    def visitSwitchBlockStatementGroup(self, ctx:JavaGrammarParser.SwitchBlockStatementGroupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#switchLabel.
    def visitSwitchLabel(self, ctx:JavaGrammarParser.SwitchLabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#forControl.
    def visitForControl(self, ctx:JavaGrammarParser.ForControlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#enhancedForControl.
    def visitEnhancedForControl(self, ctx:JavaGrammarParser.EnhancedForControlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#parExpression.
    def visitParExpression(self, ctx:JavaGrammarParser.ParExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#expressionList.
    def visitExpressionList(self, ctx:JavaGrammarParser.ExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#methodCall.
    def visitMethodCall(self, ctx:JavaGrammarParser.MethodCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#TernaryExpression.
    def visitTernaryExpression(self, ctx:JavaGrammarParser.TernaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#InstanceOfOperatorExpression.
    def visitInstanceOfOperatorExpression(self, ctx:JavaGrammarParser.InstanceOfOperatorExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#UnaryOperatorExpression.
    def visitUnaryOperatorExpression(self, ctx:JavaGrammarParser.UnaryOperatorExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#PrimaryExpression.
    def visitPrimaryExpression(self, ctx:JavaGrammarParser.PrimaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#ObjectCreationExpression.
    def visitObjectCreationExpression(self, ctx:JavaGrammarParser.ObjectCreationExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#ExpressionLambda.
    def visitExpressionLambda(self, ctx:JavaGrammarParser.ExpressionLambdaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#PostIncrementDecrementOperatorExpression.
    def visitPostIncrementDecrementOperatorExpression(self, ctx:JavaGrammarParser.PostIncrementDecrementOperatorExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#MemberReferenceExpression.
    def visitMemberReferenceExpression(self, ctx:JavaGrammarParser.MemberReferenceExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#ExpressionSwitch.
    def visitExpressionSwitch(self, ctx:JavaGrammarParser.ExpressionSwitchContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#BinaryOperatorExpression.
    def visitBinaryOperatorExpression(self, ctx:JavaGrammarParser.BinaryOperatorExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#MethodCallExpression.
    def visitMethodCallExpression(self, ctx:JavaGrammarParser.MethodCallExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#MethodReferenceExpression.
    def visitMethodReferenceExpression(self, ctx:JavaGrammarParser.MethodReferenceExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#SquareBracketExpression.
    def visitSquareBracketExpression(self, ctx:JavaGrammarParser.SquareBracketExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#CastExpression.
    def visitCastExpression(self, ctx:JavaGrammarParser.CastExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#pattern.
    def visitPattern(self, ctx:JavaGrammarParser.PatternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#lambdaExpression.
    def visitLambdaExpression(self, ctx:JavaGrammarParser.LambdaExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#lambdaParameters.
    def visitLambdaParameters(self, ctx:JavaGrammarParser.LambdaParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#lambdaBody.
    def visitLambdaBody(self, ctx:JavaGrammarParser.LambdaBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#primary.
    def visitPrimary(self, ctx:JavaGrammarParser.PrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#switchExpression.
    def visitSwitchExpression(self, ctx:JavaGrammarParser.SwitchExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#switchLabeledRule.
    def visitSwitchLabeledRule(self, ctx:JavaGrammarParser.SwitchLabeledRuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#guardedPattern.
    def visitGuardedPattern(self, ctx:JavaGrammarParser.GuardedPatternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#switchRuleOutcome.
    def visitSwitchRuleOutcome(self, ctx:JavaGrammarParser.SwitchRuleOutcomeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#classType.
    def visitClassType(self, ctx:JavaGrammarParser.ClassTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#creator.
    def visitCreator(self, ctx:JavaGrammarParser.CreatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#createdName.
    def visitCreatedName(self, ctx:JavaGrammarParser.CreatedNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#innerCreator.
    def visitInnerCreator(self, ctx:JavaGrammarParser.InnerCreatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#arrayCreatorRest.
    def visitArrayCreatorRest(self, ctx:JavaGrammarParser.ArrayCreatorRestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#classCreatorRest.
    def visitClassCreatorRest(self, ctx:JavaGrammarParser.ClassCreatorRestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#explicitGenericInvocation.
    def visitExplicitGenericInvocation(self, ctx:JavaGrammarParser.ExplicitGenericInvocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#typeArgumentsOrDiamond.
    def visitTypeArgumentsOrDiamond(self, ctx:JavaGrammarParser.TypeArgumentsOrDiamondContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#nonWildcardTypeArgumentsOrDiamond.
    def visitNonWildcardTypeArgumentsOrDiamond(self, ctx:JavaGrammarParser.NonWildcardTypeArgumentsOrDiamondContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#nonWildcardTypeArguments.
    def visitNonWildcardTypeArguments(self, ctx:JavaGrammarParser.NonWildcardTypeArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#typeList.
    def visitTypeList(self, ctx:JavaGrammarParser.TypeListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#typeType.
    def visitTypeType(self, ctx:JavaGrammarParser.TypeTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#primitiveType.
    def visitPrimitiveType(self, ctx:JavaGrammarParser.PrimitiveTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#typeArguments.
    def visitTypeArguments(self, ctx:JavaGrammarParser.TypeArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#superSuffix.
    def visitSuperSuffix(self, ctx:JavaGrammarParser.SuperSuffixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#explicitGenericInvocationSuffix.
    def visitExplicitGenericInvocationSuffix(self, ctx:JavaGrammarParser.ExplicitGenericInvocationSuffixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JavaGrammarParser#arguments.
    def visitArguments(self, ctx:JavaGrammarParser.ArgumentsContext):
        return self.visitChildren(ctx)



del JavaGrammarParser