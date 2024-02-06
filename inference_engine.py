class InferenceEngine:
    def __init__(self, rules, facts, queries):
        self.rules = rules
        self.facts = facts
        self.queries = {query: None for query in queries}
        self.facts_set = set(facts)
