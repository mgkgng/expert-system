from .token import Token, TokenType
from .node import Node

from enum import Enum, auto

class ParserType(Enum):
    Rule = auto()
    Fact = auto()
    Query = auto()

# Recursive descent parser
class Parser:
    def __init__(self, tokens):
        if (len(tokens) == 0):
            raise Exception("No tokens provided")

        self.current_token = None
        self.next_token = None
        self.pos = -1

        match tokens[0].type:
            case TokenType.FACTS:
                self.type = ParserType.Fact
                self.tokens = tokens[1:]
            case TokenType.QUERY:
                self.type = ParserType.Query
                self.tokens = tokens[1:]
            case _:
                self.type = ParserType.Rule
                self.tokens = tokens

        self.next() and self.next()
                
    def parse(self):
        match self.type:
            case ParserType.Fact:
                res = self.fact_or_query()
            case ParserType.Query:
                res = self.fact_or_query()
            case ParserType.Rule:
                res = self.rule()
        return self.type, res

    def fact_or_query(self):
        res = []
        while self.current_token.type != TokenType.EOF:
            if self.current_token.type == TokenType.Prop:
                res.append(self.current_token.value)
            else:
                raise Exception(f"Unexpected token: {self.current_token}")
            self.next()
        return res
    
    def next(self):
        self.pos += 1
        self.current_token = self.next_token
        if self.pos < len(self.tokens):
            self.next_token = self.tokens[self.pos]
            return True
        else:
            self.next_token = Token(TokenType.EOF)
            return False
        
    def factor(self):
        token = self.current_token

        if token.type == TokenType.NOT:
            self.next()
            return Node(token.type, left=self.factor())
        elif token.type == TokenType.Prop:
            self.next()
            return Node(token.type, value=token.value)
        elif token.type == TokenType.LPAREN:
            self.next()
            node = self.expression()
            if self.current_token.type != TokenType.RPAREN:
                raise Exception("Unmatched parentheses")
            self.next()
            return node

        raise Exception(f"Unexpected token: {token}")

    def term(self):
        node = self.factor()

        while self.current_token.type == TokenType.AND:
            token = self.current_token
            self.next()
            node = Node(token.type, left=node, right=self.factor())

        return node
    
    def expression(self):
        node = self.term()

        while self.current_token.type in (TokenType.OR, TokenType.XOR):
            token = self.current_token
            self.next()
            node = Node(token.type, left=node, right=self.term())

        return node

    def rule(self):
        count = 0
        node = self.expression()

        while self.current_token.type in (TokenType.IMPLIES, TokenType.IFF):
            count += 1
            if count > 1:
                raise Exception("Error: Statement contains more than one IMPLIES or IFF.")

            token = self.current_token
            self.next()
            node = Node(token.type, left=node, right=self.expression())

        if count == 0:
            raise Exception("Error: Statement does not contain any IMPLIES or IFF.")

        return node