import json
from parser import TokenType

class DepedencyGraph:
    def __init__(self, rules):
        self.dependencies = {}
        for index, rule in enumerate(rules):
            self.add_rule(rule, index)
    
    def add_rule(self, rule, index):
        premise_props = rule.get_premise_props(True)
        conclusion_props = rule.get_conclusion_props()

        self.update_dependencies(conclusion_props, premise_props, index)
        if rule.connection_type == TokenType.IFF:
            self.update_dependencies(premise_props, conclusion_props, index)

    def update_dependencies(self, target_props, source_props, index):
        for target_prop in target_props:
            if target_prop not in self.dependencies:
                self.dependencies[target_prop] = {}
            for source_prop in source_props:
                if source_prop not in self.dependencies[target_prop]:
                    self.dependencies[target_prop][source_prop] = []
                self.dependencies[target_prop][source_prop].append(index)

    def get_rule_indices_for_goal(self, goal):
        if goal not in self.dependencies:
            return set()
        return set(index for indices in self.dependencies[goal].values() for index in indices)
    
    def get_related_props(self, goal):
        return self.dependencies[goal].keys()

    def __str__(self):
        return json.dumps(self.dependencies, indent=2, sort_keys=True, default=str)
