from JavaGrammarVisitor import JavaGrammarVisitor

class Translator(JavaGrammarVisitor):
    def visitClassDeclaration(self, ctx):
        className = ctx.Identifier().getText()
        result = f"class {className}:\n"
        for method in ctx.methodDeclaration():
            result += self.visit(method)
        return result

    def visitMethodDeclaration(self, ctx):
        methodName = ctx.Identifier().getText()
        result = f"    def {methodName}(self):\n"
        for statement in ctx.statement():
            result += "        " + self.visit(statement)
        return result + "\n"

    def visitStatement(self, ctx):
        if ctx.getText().startswith("System.out.println"):
            expr = self.visit(ctx.expression())
            return f"print({expr})\n"
        elif ctx.expression():
            return self.visit(ctx.expression()) + "\n"
        return ""

    def visitExpression(self, ctx):
        if ctx.Identifier():
            return ctx.Identifier().getText()
        elif ctx.Literal():
            return ctx.Literal().getText()
        elif "=" in ctx.getText():
            left = ctx.Identifier(0).getText()
            right = self.visit(ctx.expression(0))
            return f"{left} = {right}"
        return ""