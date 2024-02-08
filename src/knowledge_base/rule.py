from parser import TokenType
from proposition import Proposition

class Rule:
    def __init__(self, premise, conclusion, connection_type):
        self.premise = premise
        self.conclusion = conclusion
        self.connection_type = connection_type
        

    ## TODO : during the parsing, if the concluson part is too complex (more than a simple prop, or OR, AND, XOR, NOT), then error 
    def is_applicable(self, goal):
        if self.conclusion.type == TokenType.Prop and self.conclusion.value == goal:
            return True
        elif self.conclusion.type != TokenType.Prop and (self.conclusion.left.value == goal or self.conclusion.right.value == goal):
            return True
        elif self.connection_type == TokenType.IFF and self.premises.find_node(goal) is not None:
            return True
        return False

    def evaluate(self, facts):
        # Evaluate the rule's premises based on known facts
        # Return True if the premises are satisfied, False otherwise
        pass

    def get_props(self):
        prop_set = set()
        self.collect_props_recursive(self.conclusion, prop_set)
        self.collect_props_recursive(self.premise, prop_set)
        return prop_set

    def collect_props_recursive(self, node, prop_set):
        if node.type == TokenType.Prop:
            prop_set.add(node.value)
        elif node.type != TokenType.NOT:
            self.collect_props_recursive(node.left, prop_set)
            self.collect_props_recursive(node.right, prop_set)
        else:
            self.collect_props_recursive(node.left, prop_set)