from lark import Lark

def load_grammar():
    with open('src/grammar/dsl.lark', 'r') as f:
        return f.read()

def create_parser():
    grammar = load_grammar()
    return Lark(grammar, parser='lalr')