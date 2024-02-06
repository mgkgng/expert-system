from parser import TokenType

def evaluate_node(node, facts):
    if node.type == TokenType.Prop:
        return node.value in facts
    elif node.type == TokenType.AND:
        return evaluate_node(node.left, facts) and evaluate_node(node.right, facts)
    elif node.type == TokenType.OR:
        return evaluate_node(node.left, facts) or evaluate_node(node.right, facts)
    elif node.type == TokenType.XOR:
        return evaluate_node(node.left, facts) ^ evaluate_node(node.right, facts)
    elif node.type == TokenType.NOT:
        return not evaluate_node(node.right, facts)
    elif node.type == TokenType.IMPLIES:
        return not evaluate_node(node.left, facts) or evaluate_node(node.right, facts)
    elif node.type == TokenType.IFF:
        return evaluate_node(node.left, facts) == evaluate_node(node.right, facts)

    return False

def evaluate_rules(asts, facts):
    new_facts = set(facts)
    for ast in asts:
        if evaluate_node(ast, facts) is True:
            new_facts.add(ast.right.value)
    return new_facts

def answer_queries(queries, facts):
    answers = {}
    for query in queries:
        answers[query] = query in facts
    return answers