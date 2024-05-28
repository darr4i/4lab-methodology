class ASTNode:
    pass

class PrintNode(ASTNode):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f'PrintNode({self.value})'

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token_index = 0

    def parse(self):
        if self.tokens[self.current_token_index].type == 'PRINT':
            self.current_token_index += 1
            value = self.tokens[self.current_token_index]
            if value.type == 'STRING':
                self.current_token_index += 1
                return PrintNode(value.value)
            else:
                raise SyntaxError("Expected a string after VISIBLE")
        else:
            raise SyntaxError("Unknown statement")

if __name__ == '__main__':
    from lexer import Lexer

    code = 'VISIBLE "Hello, World!" :)'
    lexer = Lexer(code)
    tokens = lexer.tokenize()
    
    parser = Parser(tokens)
    ast = parser.parse()
    print(ast)
