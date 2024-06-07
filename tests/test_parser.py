import unittest
from lexer import Lexer, Token
from parser import Parser, PrintNode, SpecialCharNode

class TestParser(unittest.TestCase):
    def test_parse_print_statement(self):
        tokens = [
            Token('PRINT', 'VISIBLE'),
            Token('STRING', '"Hello, World!"'),
            Token('NEWLINE', ':)')
        ]
        parser = Parser(tokens)
        ast = parser.parse()
        
        expected_ast = [
            PrintNode('"Hello, World!"'),
            SpecialCharNode('NEWLINE')
        ]
        
        self.assertEqual(ast, expected_ast)
    
    def test_parse_special_chars(self):
        tokens = [
            Token('PRINT', 'VISIBLE'),
            Token('STRING', '"Test"'),
            Token('NEWLINE', ':)'),
            Token('TAB', ':>'),
            Token('BELL', ':o'),
            Token('LITERAL_DOUBLE_QUOTE', ':"'),
            Token('LITERAL_COLON', '::')
        ]
