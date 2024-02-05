from enum import Enum, auto

class TokenType(Enum):
    Prop = auto()
    AND = auto()
    OR = auto()
    NOT = auto()
    XOR = auto()
    IMPLIES = auto()
    IFF = auto()
    LPAREN = auto()
    RPAREN = auto()
    FACTS = auto()
    QUERY = auto()
    EOF = auto()
    
TokenString = {
    TokenType.Prop: "Prop",
    TokenType.AND: "AND",
    TokenType.OR: "OR",
    TokenType.NOT: "NOT",
    TokenType.XOR: "XOR",
    TokenType.IMPLIES: "IMPLIES",
    TokenType.IFF: "IFF"
}

class Token:
    def __init__(self, type, value=None):
        self.type = type
        self.value = value

    def __str__(self):
        return f"Token({self.type}, {self.value})"