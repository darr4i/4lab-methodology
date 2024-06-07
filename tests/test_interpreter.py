import unittest
from io import StringIO
import sys
from interpreter import Interpreter
from parser import PrintNode, SpecialCharNode

class TestInterpreter(unittest.TestCase):
    def test_interpret_print(self):
        ast = [PrintNode("Hello, World!")]
        interpreter = Interpreter(ast)
        
        captured_output = StringIO()
        sys.stdout = captured_output
        
        interpreter.interpret()
        
        sys.stdout = sys.__stdout__
        
        self.assertIn('Hello, World!', captured_output.getvalue())
        
    def test_interpret_special_chars(self):
        ast = [SpecialCharNode('NEWLINE'), SpecialCharNode('TAB'), SpecialCharNode('BELL')]
        interpreter = Interpreter(ast)
        
        captured_output = StringIO()
        sys.stdout = captured_output
        
        interpreter.interpret()
        
        sys.stdout = sys.__stdout__
        
        self.assertIn('\n', captured_output.getvalue())
        self.assertIn('\t', captured_output.getvalue())
        self.assertIn('\a', captured_output.getvalue())

if __name__ == '__main__':
    unittest.main()
