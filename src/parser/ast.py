class ASTWrapper:
    def __init__(self, root):
        self.root = root
    
    def __str__(self):
        return self.root.__str__()
