from antlr4 import FileStream, CommonTokenStream
from JavaGrammarLexer import JavaGrammarLexer
from JavaGrammarParser import JavaGrammarParser
from JavaGrammarVisitor import JavaGrammarVisitor
from Translator import Translator


def main():
    # Load the Java file to be parsed
    input_stream = FileStream("Example.java")

    # Create lexer, token stream, and parser
    lexer = JavaGrammarLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = JavaGrammarParser(tokens)

    # Parse the input to generate the parse tree
    tree = parser.compilationUnit()

    # Use the Translator to visit the parse tree and convert to Python
    translator = Translator()
    python_code = translator.visit(tree)  # This triggers the visitor

    # Print the generated Python code
    print(python_code)


if __name__ == "__main__":
    main()