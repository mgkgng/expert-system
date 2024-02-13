from parser import TokenType
from utils import Stack
from .logical_value import LogicalValue

class InferenceEngine:
    def __init__(self, rules, props, dependency_graph):
        self.rules = rules
        self.props = props
        self.dependency_graph = dependency_graph

    def answer_queries(self, facts, queries):
        res = {query: LogicalValue(True) if query in facts else LogicalValue(None) for query in queries}
        goals = Stack([k for k, v in res.items() if v == None])

        while not goals.is_empty():
            goal = goals.pop()
            res[goal] = self.evaluate_goal(goal)
        return res

    def evaluate_goal(self, goal):
        if self.props[goal].evaluated is True:
            return self.props[goal].value
        
        self.props[goal].evaluated = True
        rule_indices = self.dependency_graph.get_rule_indices_for_goal(goal)
        deduced_value = LogicalValue(None) if self.props[goal].to_query else LogicalValue(False)

        for index in rule_indices:
            rule = self.rules[index]
            premise_value = self.evaluate_node(rule.premise)
            if premise_value == True:
                deduced_value = LogicalValue(self.deduce_proposition(rule.conclusion, goal))
                if deduced_value != None:
                    self.props[goal].value = deduced_value
                    break
                
        return deduced_value
    
    def deduce_proposition(self, conclusion, goal):
        #TODO when negation is involved
        if conclusion.type == TokenType.Prop:
            return True
        elif conclusion.type == TokenType.AND:
            return True # TODO check contradiction
        elif conclusion.type == TokenType.OR:
            if conclusion.left.value == goal and conclusion.right.value == False:
                return True
            elif conclusion.right.value == goal and conclusion.left.value == False:
                return True
            return None
        # TODO elif conclusion.type == TokenType.XOR:
        return None

    def evaluate_node(self, node):
        if node.type == TokenType.Prop:
            return self.get_prop_value(node.value)
        elif node.type == TokenType.AND:
            return self.evaluate_node(node.left)._and(self.evaluate_node(node.right))
        elif node.type == TokenType.OR:
            return self.evaluate_node(node.left)._or(self.evaluate_node(node.right))
        elif node.type == TokenType.XOR:
            return self.evaluate_node(node.left)._xor(self.evaluate_node(node.right))
        elif node.type == TokenType.NOT:
            return self.evaluate_node(node.left)._not()
        print('-------error---------')
        return LogicalValue(None)

    def get_prop_value(self, symbol):
        prop = self.props[symbol]
        if prop.evaluated is True:
            return prop.value
        return self.evaluate_goal(symbol)
