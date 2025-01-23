from JavaGrammarParser import JavaGrammarParser
from JavaGrammarVisitor import JavaGrammarVisitor

class Translator(JavaGrammarVisitor):
    def __init__(self):
        self.tab_spaces = 0
        self.variables = []
        self.methods = []
        self.abandon_self = False
        self.enable_self_variables = True
        self.enable_self_methods = True

    def visitTypeDeclaration(self, ctx): #TODO implement abstract and interface!!
        modifiers = []
        for modifier_ctx in ctx.classOrInterfaceModifier():
            modifiers.append(self.visitClassOrInterfaceModifier(modifier_ctx))
        result = ""
        if ctx.classDeclaration():
            result = self.visitClassDeclaration(ctx.classDeclaration())
        return result
    def visitClassOrInterfaceModifier(self, ctx):
        return ctx.getText()
    def visitClassDeclaration(self, ctx):
        class_name = self.visitIdentifier(ctx.identifier())
        extender = ""
        # if ctx.EXTENDS():
        #     parent_class = self.visitTypeType(ctx.typeType())
        # else:
        #     parent_class = None
        self.tab_spaces += 1
        class_body = self.visitClassBody(ctx.classBody())
        self.tab_spaces -= 1
        result = f"{self.make_tab_string()}class {class_name}:\n{class_body}"
        return result

    def visitClassBody(self, ctx):
        bodyDeclarations = []
        for declaration in ctx.classBodyDeclaration():
            bodyDeclarations.append(self.visitClassBodyDeclaration(declaration))
        result = "\n".join(bodyDeclarations)
        return result
    def visitClassBodyDeclaration(self, ctx):
        member = self.visitMemberDeclaration(ctx.memberDeclaration())
        return f"{member}"
    def visitMemberDeclaration(self, ctx):
        if ctx.methodDeclaration():
            return self.visitMethodDeclaration(ctx.methodDeclaration())
        if ctx.fieldDeclaration():
            return self.visitFieldDeclaration(ctx.fieldDeclaration())
        if ctx.constructorDeclaration():
            return self.visitConstructorDeclaration(ctx.constructorDeclaration())
        if ctx.classDeclaration():
            return self.visitClassDeclaration(ctx.classDeclaration())
    def visitMethodDeclaration(self, ctx):
        modifiers = []
        for modifier in ctx.classOrInterfaceModifier():
            modifiers.append(self.visitClassOrInterfaceModifier(modifier))
        method_name = self.visitIdentifier(ctx.identifier())
        clear_name = method_name
        static_decorator = False
        if "static" in modifiers:
            self.abandon_self = True
            static_decorator = True
        parameters = self.visitMethodParameters(ctx.methodParameters())
        body = ""
        if ctx.methodBody():
            body = self.visitMethodBody(ctx.methodBody())
        if "private" in modifiers:
            method_name = "_" + method_name
        self.methods.append((method_name, clear_name))
        if static_decorator:
            return f"{self.make_tab_string()}@staticmethod\n{self.make_tab_string()}def {method_name}({parameters}):\n{body}"
        return f"{self.make_tab_string()}def {method_name}({parameters}):\n{body}"
    def visitMethodParameters(self, ctx):
        parameters = ["self"]
        if self.abandon_self:
            self.abandon_self = False
            parameters = []
        for parameter in ctx.methodParameter():
            parameters.append(self.visitMethodParameter(parameter))
        return ", ".join(parameters)
    def visitMethodParameter(self, ctx):
        # type doesn't matter here as python doesn't care about types
        return self.visitIdentifier(ctx.identifier())
    def visitMethodBody(self, ctx):
        if ctx.block():
            return self.visitBlock(ctx.block())
        return None
    def visitBlock(self, ctx): #Adding two tabs not sure if it is the correct it's 2 am and i am dying <- spoiler: not correct
        block_statements = []
        self.tab_spaces += 1
        for statement in ctx.blockStatement():
            block_statements.append(f"{self.make_tab_string()}{self.visitBlockStatement(statement)}")
        self.tab_spaces -= 1
        result = "\n".join(block_statements)
        return result
    def visitBlockStatement(self, ctx):
        if ctx.localVariableDeclaration():
            return self.visitLocalTypeDeclaration(ctx.localVariableDeclaration())
        if ctx.statement():
            return self.visitStatement(ctx.statement())
    def visitLocalVariableDeclaration(self, ctx):
        return self.visitVariableDeclarators(ctx.variableDeclarators())
    def visitVariableDeclarators(self, ctx):
        variable_declarator_array = []
        for declarator in ctx.variableDeclarator():
            variable_declarator_array.append(self.visitVariableDeclarator(declarator))
        identifiers, values = [], []
        for declarator in [t for t in variable_declarator_array if t[1] is not None]:
            identifiers.append(declarator[0])
            values.append(declarator[1])
        for declarator in [t for t in variable_declarator_array if t[1] is None]:
            identifiers.append(declarator[0])
        identifiers_str = ", ".join(identifiers)
        values_str = ", ".join(values)
        if values:
            return f"{identifiers_str} = {values_str}"
        return f"{identifiers_str}"
    def visitVariableDeclarator(self, ctx):
        variable_name = self.visitVariableDeclaratorId(ctx.variableDeclaratorId())
        variable_value = None
        if ctx.variableInitializer():
            variable_value = self.visitVariableInitializer(ctx.variableInitializer())
        return variable_name, variable_value
    def visitVariableDeclaratorId(self, ctx):
        return self.visitIdentifier(ctx.identifier())
    def visitVariableInitializer(self, ctx):
        if ctx.arrayInitializer():
            return self.visitArrayInitializer(ctx.arrayInitializer())
        elif ctx.expression():
            # if isinstance(ctx.expression(), JavaGrammarParser.PrimaryExpressionContext):
            #     return self.visitPrimaryExpression(ctx.expression())
            # elif isinstance(ctx.expression(), JavaGrammarParser.BinaryOperatorExpressionContext):
            #     return self.visitBinaryOperatorExpression(ctx.expression())
            return self.visitAndReturnCorrectExpression(ctx.expression())
    def visitPrimaryExpression(self, ctx):
        return self.visitPrimary(ctx.primary())
    def visitPrimary(self, ctx):
        if ctx.identifier():
            return self.visitIdentifier(ctx.identifier())
        if ctx.THIS():
            return "self"
        return ctx.getText()
    def visitBinaryOperatorExpression(self, ctx):#TODO can add more operations like ! or ~ as well as method calls, for now it is fine
        expression1 = self.visitAndReturnCorrectExpression(ctx.expression(0))
        expression_operator = self.translate_operator(ctx.bop.text)
        expression2 = self.visitAndReturnCorrectExpression(ctx.expression(1))
        return f"{expression1} {expression_operator} {expression2}"
    def visitPostIncrementDecrementOperatorExpression(self, ctx):
        postfix = ctx.getChild(1).getText()
        expression = self.visitAndReturnCorrectExpression(ctx.expression())
        if postfix == "++":
            return f"{expression} += 1"
        if postfix == "--":
            return f"{expression} -= 1"
        if postfix == "!":
            return f"not {expression}"
        return f"{postfix} {expression}"
    def visitStatement(self, ctx): #TODO delete unused statement productions
        if ctx.RETURN():
            result = f"return"
            if ctx.expression():
                expression = self.visitAndReturnCorrectExpression(ctx.expression(0))
                result = f"return {expression}"
            return result
        if ctx.IF():
            statement = self.visitStatement(ctx.statement(0))
            par_expression = self.visitParExpression(ctx.parExpression())
            if ctx.ELSE():
                else_statement = self.visitStatement(ctx.statement(1))
                if else_statement[0:2] == "if":
                    return f"if {par_expression}:\n{statement}\n{self.make_tab_string()}elif{else_statement[2:len(else_statement)]}"
                else:
                    return f"if {par_expression}:\n{statement}\n{self.make_tab_string()}else:\n{else_statement}"
            return f"if {par_expression}:\n{statement}"
        if ctx.FOR():
            for_control = self.visitForControl(ctx.forControl())
            statement = self.visitStatement(ctx.statement(0))
            return f"{for_control} {statement}"
        if ctx.WHILE():
            par_expression = self.visitParExpression(ctx.parExpression())
            statement = self.visitStatement(ctx.statement(0))
            return f"while {par_expression}:\n{statement}"
        if ctx.PRINT():
            expression = self.visitAndReturnCorrectExpression(ctx.expression(0))
            return f"print({expression})"
        if ctx.expression(): #default expression block should be at the end
            return self.visitAndReturnCorrectExpression(ctx.expression(0))
        if ctx.block(): #default block statement should be at the end as some productions contain block and can be recognized by other factors
            return self.visitBlock(ctx.block())
    def visitForControl(self, ctx):
        variable_declarator = self.visitVariableDeclarator(ctx.variableDeclarator())
        for_start = variable_declarator[1]
        middle_expression = self.visitBinaryOperatorExpression(ctx.expression(0))
        symbols_to_remove = " <>="
        translation_table = str.maketrans('', '', symbols_to_remove)
        for_end = middle_expression.translate(translation_table).replace(variable_declarator[0], "")
        if isinstance(ctx.expression(1), JavaGrammarParser.BinaryOperatorExpressionContext):
            end_expression = self.visitBinaryOperatorExpression(ctx.expression(1))
            if end_expression.find("+=") != -1:
                symbols_to_remove = " +="
                translation_table = str.maketrans('', '', symbols_to_remove)
                jump = end_expression.translate(translation_table).replace(variable_declarator[0], "")
            elif end_expression.find("-=") != -1:
                symbols_to_remove = " -="
                translation_table = str.maketrans('', '', symbols_to_remove)
                jump = end_expression.translate(translation_table).replace(variable_declarator[0], "")
        elif isinstance(ctx.expression(1), JavaGrammarParser.PostIncrementDecrementOperatorExpressionContext):
            end_expression = self.visitPostIncrementDecrementOperatorExpression(ctx.expression(1))
            if "+=" in end_expression:
                jump = 1
            elif "-=" in end_expression:
                jump = -1
        return f"for {variable_declarator[0]} in range({for_start}, {for_end}, {jump}):\n"
    def visitMethodCall(self, ctx):
        identifier = self.visitIdentifier(ctx.identifier())
        arguments = self.visitArguments(ctx.arguments())
        return f"{identifier}({arguments})"
    def visitParExpression(self, ctx):
        return self.visitAndReturnCorrectExpression(ctx.expression())
    def visitMemberReferenceExpression(self, ctx):
        self.enable_self_methods = False
        expression1 = self.visitAndReturnCorrectExpression(ctx.expression())
        bop = None
        if ctx.identifier():
            bop = self.visitIdentifier(ctx.identifier())
        if ctx.methodCall():
            bop = self.visitMethodCall(ctx.methodCall())
        self.enable_self_methods = True
        return f"{expression1}.{bop}"
    def visitObjectCreationExpression(self, ctx):
        creator = self.visitCreator(ctx.creator())
        return creator

    def visitCreator(self, ctx):
        self.enable_self_variables = False
        identifier = self.visitIdentifier(ctx.identifier())
        arguments = self.visitArguments(ctx.arguments())
        self.enable_self_variables = True
        return f"{identifier}({arguments})"
    def visitArguments(self, ctx):
        if ctx.expressionList():
            expression_list = self.visitExpressionList(ctx.expressionList())
            return expression_list
        return ""
    def visitExpressionList(self, ctx):
        expressions = []
        for e in ctx.expression():
            expressions.append(self.visitAndReturnCorrectExpression(e))
        return ", ".join(expressions)
    def visitMethodCallExpression(self, ctx):
        return self.visitMethodCall(ctx.methodCall())
    def visitFieldDeclaration(self, ctx):
        self.enable_self_variables = False
        variables = self.visitVariableDeclarators(ctx.variableDeclarators())
        clean_variables = variables.split(" ")[0]
        modifiers = []
        for m in ctx.classOrInterfaceModifier():
            modifiers.append(self.visitClassOrInterfaceModifier(m))
        #if "private" in modifiers:
        #    variables = "__" + variables
        if "static" in modifiers:
            stripped_variable = "self." + variables.split(" ")[0]
            self.variables.append((stripped_variable, clean_variables))
            if "=" not in variables:
                variables = variables + " = 0"
            return f"{self.make_tab_string()}{variables}"
        stripped_variable = "self." + variables.split(" ")[0]
        self.variables.append((stripped_variable, clean_variables))
        return ""
        #if "=" in variables:
        #    return f"{self.make_tab_string()}self.{variables}"
        #return f"{self.make_tab_string()}self.{variables} = 0"
    def visitConstructorDeclaration(self, ctx):
        self.enable_self_variables = False
        constructor_parameters = self.visitMethodParameters(ctx.methodParameters())
        init = f"{self.make_tab_string()}def __init__({constructor_parameters}):\n"
        body = self.visitBlock(ctx.block())
        self.enable_self_variables = True
        return f"{init}{body}"
    def visitTypeType(self, ctx):
        if ctx.primitiveType():
            type = self.visitPrimitiveType(ctx.primitiveType())
        elif ctx.classOrInterfaceType():
            type = self.visitClassOrInterfaceType(ctx.classOrInterfaceType())
        else:
            type = ""
        return type
    def visitIdentifier(self, ctx):
        if ctx.IDENTIFIER():
            if self.enable_self_variables:
                variable_name = ctx.getText()
                for variable in self.variables:
                    if variable_name == variable[1]:
                        return variable[0]
            if self.enable_self_methods:
                method_name = ctx.getText()
                for method in self.methods:
                    if method_name == method[1]:
                        return "self." + method[0]

        return ctx.getText()
    def translate_operator(self, o):
        if o == "&&":
            return "and"
        if o == "||":
            return "or"
        return o
    def visitAndReturnCorrectExpression(self, expression):
        result = None
        if isinstance(expression, JavaGrammarParser.PrimaryExpressionContext):
            result = self.visitPrimaryExpression(expression)
        elif isinstance(expression, JavaGrammarParser.BinaryOperatorExpressionContext):
            result = self.visitBinaryOperatorExpression(expression)
        elif isinstance(expression, JavaGrammarParser.PostIncrementDecrementOperatorExpressionContext):
            result = self.visitPostIncrementDecrementOperatorExpression(expression)
        elif isinstance(expression, JavaGrammarParser.MemberReferenceExpressionContext):
            result = self.visitMemberReferenceExpression(expression)
        elif isinstance(expression, JavaGrammarParser.ObjectCreationExpressionContext):
            result = self.visitObjectCreationExpression(expression)
        elif isinstance(expression, JavaGrammarParser.MethodCallExpressionContext):
            result = self.visitMethodCallExpression(expression)
        return result
    def make_tab_string(self):
        return "    " * self.tab_spaces