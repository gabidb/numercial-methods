import unittest
from src.differentiation \
    import Forward, Forward2, Centered, Centered4, Backward, Backward2

__all__ = ["Forward", "Forward2", "Centered",
           "Centered4", "Backward", "Backward2"]


class TestDifferentiation(unittest.TestCase):

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


if __name__ == '__main__':
    unittest.main()
