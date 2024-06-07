import re

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __repr__(self):
        return f"Token({self.type}, {self.value})"

class Lexer:
    def __init__(self, source_code):
        self.source_code = source_code
        self.tokens = []
        self.current_position = 0

    def tokenize(self):
        token_specification = [
            ('PRINT', r'VISIBLE'),
            ('STRING', r'"([^"\\]*(?:\\.[^"\\]*)*)"'),
            ('NEWLINE', r':\)'),
            ('TAB', r':>'),
            ('BELL', r':o'),
            ('LITERAL_DOUBLE_QUOTE', r':"'),
            ('LITERAL_COLON', r'::'),
            ('SKIP', r'[ \t]+'),
            ('MISMATCH', r'.'),
        ]

        tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
        get_token = re.compile(tok_regex).match
        mo = get_token(self.source_code)
        while mo is not None:
            kind = mo.lastgroup
            value = mo.group(kind)
            if kind == 'SKIP':
                pass
            elif kind == 'MISMATCH':
                raise RuntimeError(f'{value!r} unexpected')
            else:
                token = Token(kind, value)
                self.tokens.append(token)
            self.current_position = mo.end()
            mo = get_token(self.source_code, self.current_position)
        return self.tokens

if __name__ == '__main__':
    code = 'VISIBLE "Hello, World!" :) VISIBLE "Hi" :)'
    lexer = Lexer(code)
    tokens = lexer.tokenize()
    print(tokens)

