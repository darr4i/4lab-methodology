from parser import PrintNode, SpecialCharNode

class Interpreter:
    def __init__(self, ast):
        self.ast = ast

    def interpret(self):
        special_chars = {
            'NEWLINE': '\n',
            'TAB': '\t',
            'BELL': '\a',
            'LITERAL_DOUBLE_QUOTE': '"',
            'LITERAL_COLON': ':',
        }
        
        for node in self.ast:
            if isinstance(node, PrintNode):
                print(node.value)
            elif isinstance(node, SpecialCharNode):
                print(special_chars[node.value], end='')

if __name__ == '__main__':
    from lexer import Lexer
    from parser import Parser

    code = 'VISIBLE "Hello, World!" :) VISIBLE "Hi" :)'
    lexer = Lexer(code)
    tokens = lexer.tokenize()
    print(f"Tokens: {tokens}")

    parser = Parser(tokens)
    ast = parser.parse()
    print(f"AST: {ast}")

    # Інтерпретація AST
    interpreter = Interpreter(ast)
    interpreter.interpret()



