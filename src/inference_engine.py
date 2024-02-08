from parser import TokenType
from stack import Stack
from proposition import Proposition

class InferenceEngine:
    def __init__(self, rules, props):
        self.rules = rules
        self.props = props

    def find_rules_for_goal(self, goal):
        res = []
        for rule in self.rules:
            if rule.right.type == TokenType.Prop and rule.right.value == goal:
                res.append(rule)
            elif rule.right.type != TokenType.Prop and (rule.right.left.value == goal or rule.right.right.value == goal):
                res.append(rule)
            elif rule.type == TokenType.IFF and rule.left.find_node(goal) is not None:
                res.append(rule)
        return res

    def answer_queries(self, facts, queries):
        res = {query: True if query in facts else None for query in queries}
        goals = Stack([k for k, v in res.items() if v is None])

        while not goals.is_empty():
            pass

    def evaluate_goal(self, goal):
        rules = self.find_rules_for_goal(goal)
        
        pass


    def evaluate_node(self, node):
        if node.type == TokenType.Prop:
            return self.get_prop_value(node.value)
        elif node.type == TokenType.AND:
            return self.evaluate_node(node.left) and self.evaluate_node(node.right)
        elif node.type == TokenType.OR:
            return self.evaluate_node(node.left) or self.evaluate_node(node.right)
        elif node.type == TokenType.XOR:
            return self.evaluate_node(node.left) ^ self.evaluate_node(node.right)
        elif node.type == TokenType.NOT:
            return not self.evaluate_node(node.right)
        elif node.type == TokenType.IMPLIES:
            return not self.evaluate_node(node.left) or self.evaluate_node(node.right)
        elif node.type == TokenType.IFF:
            return self.evaluate_node(node.left) == self.evaluate_node(node.right)
        return False


    def get_prop_value(self, symbol):
        res = self.props[symbol].value
        if res is None and res.evaluated is False:
            res = self.evaluate_goal(symbol)
        if res is None and res.evaluated is True:
            print('Error: Proposition cannot be evaluated')