from antlr4 import FileStream, CommonTokenStream
from JavaGrammarLexer import JavaGrammarLexer
from JavaGrammarParser import JavaGrammarParser
from JavaGrammarVisitor import JavaGrammarVisitor
from Translator import Translator

def main():
    # Wczytaj plik z kodem Javy
    input_stream = FileStream("Example.java")

    # Stwórz lexer, parser i drzewo
    lexer = JavaGrammarLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = JavaGrammarParser(tokens)
    tree = parser.compilationUnit()
    # Użyj wizytora do tłumaczenia
    translator = Translator()
    python_code = translator.visit(tree)

    # Wypisz wynikowy kod w Pythonie
    print(python_code)

if __name__ == "__main__":
    main()