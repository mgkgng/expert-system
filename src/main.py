import sys
from parser import Parser, Lexer, ParserType, ASTWrapper

from utils import *

if __name__ == '__main__':
    if (len(sys.argv) != 2):
        print('Usage: python3 main.py <path to .txt file>')
        sys.exit(1)
    
    contents = retrieve_contents(sys.argv[1])
    lexer = Lexer()
    asts = []
    facts = None
    queries = None
    for line in contents:
        tokens = lexer.tokenize(line)
        parser = Parser(tokens)
        parser_type, parser_res = parser.parse()
        if parser_type == ParserType.Fact:
            if facts is not None:
                raise Exception("Multiple facts")
            facts = parser_res
        elif parser_type == ParserType.Query:
            if queries is not None:
                raise Exception("Multiple queries")
            queries = parser_res
        else:
            print(ASTWrapper(parser_res))
            asts.append(ASTWrapper(parser_res))

        # ast.append(parser.expression())