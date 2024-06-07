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
        for token, expected in zip(tokens, expected_tokens):
            self.assertEqual(token.type, expected.type)
            self.assertEqual(token.value, expected.value)

    def test_tokenize_unexpected_character(self):
        code = 'VISIBLE @'
        lexer = Lexer(code)
        with self.assertRaises(RuntimeError):
            lexer.tokenize()

if __name__ == '__main__':
    unittest.main()
