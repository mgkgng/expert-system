from .token import TokenString

class Node:
    def __init__(self, type, value=None, left=None, right=None):
        self.type = type
        self.value = value
        self.left = left
        self.right = right
        
    def __str__(self):
        return self.print_tree()

    def print_tree(self, depth=0):
        indent = '  ' * depth  # Two spaces per depth level
        node_rep = f"{TokenString[self.type]}" + (f"({self.value})" if self.value is not None else "")
        tree_str = f"{indent}{node_rep}\n"
        
        if self.left is not None:
            tree_str += self.left.print_tree(depth + 1)
        if self.right is not None:
            tree_str += self.right.print_tree(depth + 1)
        return tree_str