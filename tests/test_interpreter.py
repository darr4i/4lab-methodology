import unittest
from io import StringIO
import sys
from interpreter import Interpreter
from parser import PrintNode

class TestInterpreter(unittest.TestCase):
    def test_interpret_print(self):
        ast = PrintNode("Hello, World!")
        interpreter = Interpreter(ast)
        
        captured_output = StringIO()
        sys.stdout = captured_output
        
        interpreter.interpret()
        
        sys.stdout = sys.__stdout__
        
        self.assertIn('Hello, World!', captured_output.getvalue())

if __name__ == '__main__':
    unittest.main()
