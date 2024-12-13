import pytest
from src.parser.parser import create_parser

def test_basic_statement():
    parser = create_parser()
    tree = parser.parse("test: hello")
    assert tree is not None