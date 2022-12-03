import unittest
from src.differentiation import *

class TestDifferentiation(unittest.TestCase):

    def test_all_derivatives(self):
        all_methods = ["Forward", "Forward2", "Centered", "Centered4", "Backward", "Backward2"]
        for method in all_methods:
            print(method)
            TestDifferentiation._test_any_derivative(self,method)

    def _test_any_derivative(self, method):
        def f(x): return a*x - b
        def df(x): return a

        a,b,x,error = 2, 5.5, 9.01, 1E-14
        func = eval(method)(f, h = 0.25)
        self.assertTrue(abs(df(x) - func(x)) < error, msg = f"Test failed in class {method}")

if __name__ == '__main__':
    unittest.main()