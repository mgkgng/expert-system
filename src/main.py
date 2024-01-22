import sys
from parser import Parser
from utils import *

if __name__ == '__main__':
    if (len(sys.argv) != 2):
        print('Usage: python3 main.py <path to .txt file>')
        sys.exit(1)
    
    contents = retrieve_contents(sys.argv[1])
    parser = Parser()
    asts = parser.parse(contents)