class Interpreter:
    def __init__(self, ast):
        self.ast = ast

    def interpret(self):
        print(f"Interpreting AST: {self.ast}")
        if isinstance(self.ast, PrintNode):
            print(self.ast.value)

if __name__ == '__main__':
    from lexer import Lexer
    from parser import Parser, PrintNode

    code = 'VISIBLE "Hello, World!"'
    lexer = Lexer(code)
    tokens = lexer.tokenize()
    print(f"Tokens: {tokens}")
    
    parser = Parser(tokens)
    ast = parser.parse()
    print(f"AST: {ast}")
    
    interpreter = Interpreter(ast)
    interpreter.interpret()
