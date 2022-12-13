import unittest
from src.integration import \
    Integration, Simpsons, CompositeSimpsons, CompositeTrapezoidal

__all__ = ["Simpsons", "CompositeSimpsons", "CompositeTrapezoidal"]


class TestIntegration(unittest.TestCase):

    def setUp(self) -> None:
        self.integration = Integration(0, 1, 'x')

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

        func = eval(method)(lower_limit, upper_limit, f)

        self.assertAlmostEqual(intf(lower_limit, upper_limit),
                               func.integrate(n), 13,
                               msg=f"Test failed in {method}")
    
    def test_init_ok(self):
        self.integration.set_f('x**2')
        self.integration.set_lower_limit(1)
        self.integration.set_upper_limit(2)
        assert self.integration.get_f() == 'x**2'
        assert self.integration.get_lower_limit() == 1
        assert self.integration.get_upper_limit() == 2

    def test_get_exact_value(self):
        """
            Test that it returns the exact
            value of the integral for f(x)=x
            integral(x) = x^2/2
        """
        self.assertEqual(Integration(0, 1, "x").get_exact_value(), 1/2)

    def test_get_error(self):
        """
            Test that it returns the absolute difference
            between exact value and approximation
        """
        self.assertEqual(Integration(0, 1, "x").get_error(1/4), 1/4)

    def test_raise_not_implemented(self):
        self.assertRaises(NotImplementedError, self.integration.integrate, 'x')


if __name__ == '__main__':
    unittest.main()
