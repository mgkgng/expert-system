from .token import Token, TokenType

class Lexer:
    def __init__(self):
        pass

    def tokenize(self, input_str):
        tokens = []
        pos = 0
        while pos < len(input_str):
            curr_char = input_str[pos]            
            if curr_char.isalpha() and curr_char.isupper():
                tokens.append(Token(TokenType.Prop, curr_char))
            elif curr_char == '+':
                tokens.append(Token(TokenType.AND))
            elif curr_char == '|':
                tokens.append(Token(TokenType.OR))
            elif curr_char == '=':
                if pos + 1 < len(input_str) and input_str[pos + 1] == '>':
                    tokens.append(Token(TokenType.IMPLIES))
                    pos += 1
                else:
                    tokens.append(Token(TokenType.FACTS))
            elif curr_char == '!':
                tokens.append(Token(TokenType.NOT))
            elif curr_char == '^':
                tokens.append(Token(TokenType.XOR))
            elif curr_char == '<':
                if pos + 2 < len(input_str) and input_str[pos + 1] == '=' and input_str[pos + 2] == '>':
                    tokens.append(Token(TokenType.IFF))
                    pos += 2
                else:
                    raise Exception(f"Unexpected character: {curr_char}")
            elif curr_char == '?':
                tokens.append(Token(TokenType.QUERY))
            elif curr_char == '(':
                tokens.append(Token(TokenType.LPAREN))
            elif curr_char == ')':
                tokens.append(Token(TokenType.RPAREN))
            else:
                raise Exception(f"Unexpected character: {curr_char}")
            pos += 1            
        return tokens
