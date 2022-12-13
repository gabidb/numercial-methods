import unittest
from src.differentiation \
    import Derivative, Forward, Forward2, Centered, Centered4, Backward, Backward2

__all__ = ["Forward", "Forward2", "Centered",
           "Centered4", "Backward", "Backward2"]


class TestDifferentiation(unittest.TestCase):

    def setUp(self) -> None:
        self.derivative = Derivative("x", 0.1)

    def test_all_derivatives(self):
        """
        Tests that linear func are differentiated accuratley with all methods
        """
        for method in __all__:
            TestDifferentiation._test_any_derivative(self, method)

    def _test_any_derivative(self, method):
        """
        Test that the difference between the estimates
        and the true value is less than 1E-14
        """
        def f(x): return a*x - b
        def df(x): return a

        a, b, x, error = 2, 5.5, 9.01, 1E-14
        func = eval(method)(f, h=0.49)
        self.assertTrue(abs(df(x) - func(x)) < error,
                        msg=f"Test failed in class {method}")

    def test_init_ok(self):
        self.assertEqual(self.derivative.get_f(),'x')
        self.assertEqual(self.derivative._h, 0.1)
    
    def test_h_zero(self):
        inst = Derivative('x', 0)
        self.assertEqual(inst._h,1E-5)
    
    def test_get_exact_value(self):
        """
            Test that it returns the exact
            value of the derivative for f(x)=x
            derivative(x) = 1
        """
        self.assertEqual(Derivative("x", 0.1).get_exact_value(), 1)

    def test_get_error(self):
        """
            Test that it returns the absolute difference
            between exact value and approximation
        """
        self.assertEqual(Derivative("x", 0.1).get_error(1/4), 3/4)


if __name__ == '__main__':
    unittest.main()
