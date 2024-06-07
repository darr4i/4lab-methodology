class ASTNode:
    pass

class PrintNode(ASTNode):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f'PrintNode({self.value})'

    def __eq__(self, other):
        if isinstance(other, PrintNode):
            return self.value == other.value
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

class SpecialCharNode(ASTNode):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f'SpecialCharNode({self.value})'

    def __eq__(self, other):
        if isinstance(other, SpecialCharNode):
            return self.value == other.value
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token_index = 0

    def parse(self):
        nodes = []
        while self.current_token_index < len(self.tokens):
            token = self.tokens[self.current_token_index]
            if token.type == 'PRINT':
                self.current_token_index += 1
                value = self.tokens[self.current_token_index]
                if value.type == 'STRING':
                    self.current_token_index += 1
                    nodes.append(PrintNode(value.value))
                else:
                    raise SyntaxError("Expected a string after VISIBLE")
            elif token.type in ('NEWLINE', 'TAB', 'BELL', 'LITERAL_DOUBLE_QUOTE', 'LITERAL_COLON'):
                self.current_token_index += 1
                nodes.append(SpecialCharNode(token.type))
            elif token.type == 'SKIP':
                self.current_token_index += 1
                continue
            else:
                raise SyntaxError("Unknown statement")
        return nodes

if __name__ == '__main__':
    from lexer import Lexer

    code = 'VISIBLE "Hello, World!" :) VISIBLE "Hi" :)'
    lexer = Lexer(code)
    tokens = lexer.tokenize()
    
    parser = Parser(tokens)
    ast = parser.parse()
    print(ast)
