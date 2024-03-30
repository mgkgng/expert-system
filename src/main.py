import sys
from parser import Parser, Lexer, ParserType
from inference import InferenceEngine, create_propositions
from knowledge_base import Rule, DepedencyGraph
from utils import *

def main():
    if (len(sys.argv) != 2):
        print('Usage: python3 main.py <path to .txt file>')
        sys.exit(1)

    try:
        contents = retrieve_contents(sys.argv[1])
        lexer = Lexer()
        rules = []
        facts = None
        queries = None
        for line in contents:
            tokens = lexer.tokenize(line)
            parser = Parser(tokens)
            parser_type, parser_res = parser.parse()
            # print(parser_res)
            if parser_type == ParserType.Fact:
                if facts is not None:
                    raise Exception("Multiple facts")
                facts = parser_res
            elif parser_type == ParserType.Query:
                if queries is not None:
                    raise Exception("Multiple queries")
                queries = parser_res
            else:
                rules.append(Rule(parser_res.left, parser_res.right, parser_res.type))
        
        if facts is None:
            raise Exception('No rules')
        
        if queries is None:
            raise Exception('No queries')

        dependency_graph = DepedencyGraph(rules)
        props = create_propositions(rules, facts, queries)
        inference_engine = InferenceEngine(rules, props, dependency_graph)
        answers = inference_engine.answer_queries(facts, queries)
        for k, v in answers.items():
            print(f'{k}: {v if v != None else "Undetermined"}')
            # print(f'{k}: {v if v != None else "False"}') # Setting Undetermined to False because of the 42 correction
    except Exception as e:
        print(f'Error: {e}')

if __name__ == '__main__':
    main()