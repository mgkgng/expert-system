from parser import TokenType

class Proposition:
    def __init__(self, symbol, value=False, to_query=False, evaluated=False):
        self.symbol = symbol
        self.value = value
        self.to_query = to_query
        self.evaluated = evaluated

def create_propositions(rules, facts, queries):
    propositions = {}
    
    for query in queries:
        propositions[query] = Proposition(query, to_query=True)
    
    for fact in facts:
        propositions[fact] = Proposition(fact, value=True, evaluated=True)

    rules_proposition_set = propositions_from_rules(rules)

    for prop in rules_proposition_set:
        if prop not in propositions:
            propositions[prop] = Proposition(prop)
    
    return propositions

def propositions_from_rules(node, propositions=set()):
    if node.type == TokenType.Prop:
        propositions.add(node.value)
    elif node.type != TokenType.NOT:
        propositions_from_rules(node.left, propositions)
        propositions_from_rules(node.right, propositions)
    return propositions