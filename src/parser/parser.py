from pathlib import Path
from lark import Lark
from .transformer import DSLTransformer
from .indenter import DSLIndenter

class DSLParser:
    def __init__(self):
        grammar_path = Path(__file__).parent.parent / "grammar" / "dsl.lark"
        with open(grammar_path, 'r') as f:
            self.grammar = f.read()
        
        self.parser = Lark(
            self.grammar,
            parser='lalr',
            postlex=DSLIndenter(),
            debug=True,
            propagate_positions=True
        )
        self.transformer = DSLTransformer()

    def parse(self, text):
        # Normalize line endings
        text = text.replace('\r\n', '\n')
        tree = self.parser.parse(text)
        return self.transformer.transform(tree)

    def parse_file(self, file_path):
        with open(file_path, 'r', newline='') as f:
            return self.parse(f.read())