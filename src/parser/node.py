from .token import TokenString, TokenType, TokenNotation

class Node:
    def __init__(self, type, value=None, left=None, right=None):
        self.type = type
        self.value = value
        self.left = left
        self.right = right
        
    def __str__(self):
        return self.print_tree()

    def find_node(self, value):
        if self.value == value:
            return self
        if self.left is not None:
            return self.left.find_node(value)
        if self.right is not None:
            return self.right.find_node(value)
        return None
    
    def to_rpn(self):
        if self.type == TokenType.Prop:
            return self.value
        
        left_str = self.left.to_rpn() if self.left is not None else ""
        right_str = self.right.to_rpn() if self.right is not None else ""
        
        if self.type == TokenType.NOT:
            return left_str + TokenNotation[self.type]
        
        return left_str + right_str + TokenNotation[self.type]
    
    def print_tree(self, depth=0):
        indent = '  ' * depth  # Two spaces per depth level
        node_rep = f"{TokenString[self.type]}" + (f"({self.value})" if self.value is not None else "")
        tree_str = f"{indent}{node_rep}\n"
        
        if self.left is not None:
            tree_str += self.left.print_tree(depth + 1)
        if self.right is not None:
            tree_str += self.right.print_tree(depth + 1)
        return tree_str