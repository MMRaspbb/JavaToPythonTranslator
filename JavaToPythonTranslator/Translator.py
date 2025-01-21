from JavaGrammarParser import JavaGrammarParser
from JavaGrammarVisitor import JavaGrammarVisitor

class Translator(JavaGrammarVisitor):
    def visitTypeDeclaration(self, ctx):
        modifier = self.visitClassOrInterfaceModifier(ctx.classOrInterfaceModifier())
        class_declaration = self.visitClassDeclaration(ctx.classDeclaration())
        result = modifier + " " + class_declaration
        return result
    def visitClassOrInterfaceModifier(self, ctx):
        modifiers = []
        for modifier in ctx:
            modifiers.append(modifier.getText())
        return " ".join(modifiers)
    def visitClassDeclaration(self, ctx):
        class_name = self.visitIdentifier(ctx.identifier())
        class_body = self.visitClassBody(ctx.classBody())
        result = f"class {class_name}:\n {class_body}"
        return result
    def visitIdentifier(self, ctx):
        return ctx.getText()
    def visitClassBody(self, ctx):
        return self.visitClassBodyDeclaration(ctx.classBodyDeclaration())
    def visitClassBodyDeclaration(self, ctx):
        if ctx.fieldDeclaration():
            # If the matched alternative is fieldDeclaration
            return self.visitFieldDeclaration(ctx.fieldDeclaration())
        # elif ctx.constructorDeclaration():
        #     # If the matched alternative is constructorDeclaration
        #     return self.visitConstructorDeclaration(ctx.constructorDeclaration())
        # elif ctx.methodDeclaration():
        #     # If the matched alternative is methodDeclaration
        #     return self.visitMethodDeclaration(ctx.methodDeclaration())
    def visitFieldDeclaration(self, ctx): #ignoring the type of variable as python is skibidi
        return self.visitVariableDeclarators(ctx.variableDeclarators())
    def visitVariableDeclarators(self, ctx):


    # def visitClassDeclaration(self, ctx):
    #     className = ctx.Identifier().getText()
    #     result = f"class {className}:\n"
    #     for method in ctx.methodDeclaration():
    #         result += self.visit(method)
    #     return result
    #
    # def visitMethodDeclaration(self, ctx):
    #     methodName = ctx.Identifier().getText()
    #     result = f"    def {methodName}(self):\n"
    #     for statement in ctx.statement():
    #         result += "        " + self.visit(statement)
    #     return result + "\n"
    #
    # def visitStatement(self, ctx):
    #     if ctx.getText().startswith("System.out.println"):
    #         expr = self.visit(ctx.expression())
    #         return f"print({expr})\n"
    #     elif ctx.expression():
    #         return self.visit(ctx.expression()) + "\n"
    #     return ""
    #
    # def visitExpression(self, ctx):
    #     if ctx.Identifier():
    #         return ctx.Identifier().getText()
    #     elif ctx.Literal():
    #         return ctx.Literal().getText()
    #     elif "=" in ctx.getText():
    #         left = ctx.Identifier(0).getText()
    #         right = self.visit(ctx.expression(0))
    #         return f"{left} = {right}"
    #     return ""