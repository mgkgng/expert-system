import json

class DepedencyGraph:
    def __init__(self, rules):
        self.dependencies = {}
        for index, rule in enumerate(rules):
            self.add_rule(rule, index)
    
    def add_rule(self, rule, index):
        premise_props = rule.get_premise_props(True)
        conclusion_props = rule.get_conclusion_props()

        for conclusion_prop in conclusion_props:
            if conclusion_prop not in self.dependencies:
                self.dependencies[conclusion_prop] = {}
            for premise_prop in premise_props:
                if premise_prop not in self.dependencies[conclusion_prop]:
                    self.dependencies[conclusion_prop][premise_prop] = []
                self.dependencies[conclusion_prop][premise_prop].append(index)

    def get_rule_indices_for_goal(self, goal):
        if goal not in self.dependencies:
            return set()
        return set(index for indices in self.dependencies[goal].values() for index in indices)
    
    def get_related_props(self, goal):
        return self.dependencies[goal].keys()

    def __str__(self):
        return json.dumps(self.dependencies, indent=2, sort_keys=True, default=str)
