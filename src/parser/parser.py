from .lexer import Lexer
from .ast import ASTNode

class Parser:
    def __init__(self):
        self.lexer = Lexer()

    def parse(self, contents):
        for line in contents:
            tokens = self.lexer.tokenize(line)
            for token in tokens:
                print(token)
            print()
            # ast = self.parse_tokens(tokens)
            # print(ast)
        
        # Logic to parse tokens into ASTs
        # return asts
    

