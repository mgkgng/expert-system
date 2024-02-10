from .logical_value import LogicalValue

class Proposition:
    def __init__(self, symbol, value=False, to_query=False, evaluated=False):
        self.symbol = symbol
        self.value = LogicalValue(value)
        self.to_query = to_query
        self.evaluated = evaluated

    def __str__(self):
        return f'Proposition {self.symbol} Value: {self.value}'

    def __repr__(self): 
        return self.__str__()

def create_propositions(rules, facts, queries):
    propositions = {}
    
    for query in queries:
        propositions[query] = Proposition(query, to_query=True)
    
    for fact in facts:
        propositions[fact] = Proposition(fact, value=True, evaluated=True)

    rules_proposition_set = set()
    for rule in rules:
        rules_proposition_set = rule.get_all_props(rules_proposition_set)

    for prop in rules_proposition_set:
        if prop not in propositions.keys():
            propositions[prop] = Proposition(prop)
    
    return propositions

