from parser import TokenType
from stack import Stack
from proposition import Proposition

class InferenceEngine:
    def __init__(self, rules):
        self.rules = rules
        self.facts_set = set(facts)

    def match_rule(self, goal):
        res = []
        for rule in self.rules:
            if rule.right.type == TokenType.Prop and rule.right.value == goal:
                res.append(rule)
            elif rule.right.type != TokenType.Prop and (rule.right.left.value == goal or rule.right.right.value == goal):
                res.append(rule)
        return res
    

    def answer_queries(self, facts, queries):
        res = {query: True if query in facts else None for query in queries}
        goals = Stack([k for k, v in res.items() if v is None])


    def evaluate_condition(self):
        pass

    