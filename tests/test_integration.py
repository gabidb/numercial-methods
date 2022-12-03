import unittest
import inspect
from src.integration import Simpsons, CompositeSimpsons, Trapezoidal

__all__ = ["Simpsons", "CompositeSimpsons", "Trapezoidal"]


class TestIntegration(unittest.TestCase):

    def test_all_integration_methods(self):
        """
        Test that linear func are integrated accuratley with all methods
        """
        for method in __all__:
            self._test_integration_method(method)

    def _test_integration_method(self, method):
        """
        Test that the difference between the estimates
        and the true value is less than 1E-13
        """
        def f(x): return 1.2*x + 0.65

        def intf(lower_limit, upper_limit):
            return (1.2*(upper_limit**2) / 2 + 0.65*upper_limit) - \
                (1.2*(lower_limit**2) / 2 + 0.65*lower_limit)

        lower_limit, upper_limit, n = 1.5, 10.25, 100

        if len(inspect.getfullargspec(eval(method)).args) == 3:
            func = eval(method)(lower_limit, upper_limit)
        else:
            func = eval(method)(lower_limit, upper_limit, n)

        self.assertAlmostEqual(intf(lower_limit, upper_limit),
                               func.integrate(f), 13,
                               msg=f"Test failed in {method}")


if __name__ == '__main__':
    unittest.main()
