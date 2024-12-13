import sys
import os
from pathlib import Path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.parser.parser import DSLParser

def test_basic_command():
    parser = DSLParser()
    test_input = """command say_hello:
  print "hello world"
"""
    result = parser.parse(test_input)
    assert result["command"] == "say_hello"
    assert len(result["actions"]) == 1
    assert result["actions"][0]["type"] == "print"
    assert result["actions"][0]["argument"] == "hello world"

def test_from_file():
    parser = DSLParser()
    example_path = Path(__file__).parent / "examples" / "hello.dsl"
    with open(example_path, 'r') as f:
        content = f.read()
        print("\nFile content:")
        print(repr(content))
    result = parser.parse_file(example_path)
    assert result["command"] == "say_hello"
    assert len(result["actions"]) == 1
    assert result["actions"][0]["type"] == "print"
    assert result["actions"][0]["argument"] == "hello world"