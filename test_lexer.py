import unittest
from lexer import Lexer, Token

class TestLexer(unittest.TestCase):
    def test_tokenize_print_statement(self):
        code = 'VISIBLE "Hello, World!" :)'
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        
        expected_tokens = [
            Token('PRINT', 'VISIBLE'),
            Token('STRING', '"Hello, World!"'),
            Token('NEWLINE', ':)')
        ]
        
        self.assertEqual(tokens, expected_tokens)
    
    def test_tokenize_special_chars(self):
        code = 'VISIBLE "Test" :) :> :o :" ::'
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        
        expected_tokens = [
            Token('PRINT', 'VISIBLE'),
            Token('STRING', '"Test"'),
            Token('NEWLINE', ':)'),
            Token('TAB', ':>'),
            Token('BELL', ':o'),
            Token('LITERAL_DOUBLE_QUOTE', ':"'),
            Token('LITERAL_COLON', '::')
        ]
        
        self.assertEqual(tokens, expected_tokens)

if __name__ == '__main__':
    unittest.main()

