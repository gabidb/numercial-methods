import unittest
from unittest.mock import patch
from src.numerical_method import NumericalMethod


class TestAbstractClassNumericalMethods(unittest.TestCase):

    @patch.multiple(NumericalMethod, __abstractmethods__=set())
    def test_get_f(self):
        nm = NumericalMethod('x')
        self.assertEqual(nm.get_f(),'x')
    
    @patch.multiple(NumericalMethod, __abstractmethods__=set())
    def test_get_value_error(self):
         subclass = NumericalMethod('x')
         self.assertRaises(NotImplementedError, subclass.get_exact_value)
        
    @patch.multiple(NumericalMethod, __abstractmethods__=set())
    def test_get_error_error(self):
         subclass = NumericalMethod('x')
         self.assertRaises(NotImplementedError, subclass.get_error, 1/2)


if __name__ == '__main__':
    unittest.main()