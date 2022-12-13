"""
    File contains classes for integration techniques
"""
from src.numerical_method import NumericalMethod
from sympy import Symbol, integrate


class Integration(NumericalMethod):
    """
        Integration class is the parent class
        of all integration methods classes
    """

    def __init__(self, lower_limit, upper_limit, f) -> None:
        super().__init__(f)
        self._lower_limit = lower_limit
        self._upper_limit = upper_limit

    def get_lower_limit(self):
        """
            Get the lower bound of integration
        """
        return self._lower_limit

    def set_lower_limit(self, lower_limit):
        """
            Set the lower bound of integration
        """
        self._lower_limit = lower_limit

    def get_upper_limit(self):
        """
            Get the upper bound of integration
        """
        return self._upper_limit

    def set_upper_limit(self, upper_limit):
        """
            Set the upper bound of integration
        """
        self._upper_limit = upper_limit

    def get_exact_value(self):
        """
            Returns exact value of the integral of f
        """
        x = Symbol('x')
        return integrate(self._f, (x, self._lower_limit, self._upper_limit))

    def integrate(self, f):
        raise NotImplementedError(
            'No integration method implemented in ' + self.__class__.__name__)

    def __str__(self) -> str:
        return f"""Integral has lower limit
                    {self._lower_limit} and upper limit {self._upper_limit}"""


class Simpsons(Integration):

    def __init__(self, lower_limit, upper_limit, f) -> None:
        super().__init__(lower_limit, upper_limit, f)
        self._h = (self._upper_limit - self._lower_limit) / 2
        self._midpoint = (self._upper_limit + self._lower_limit) / 2

    def integrate(self, n):
        """
            Computes the integral of f using the Simpsons rule

            returns float
        """
        return (self._h / 3) * \
            (self._f(self._lower_limit) + 4*self._f(self._midpoint)
             + self._f(self._upper_limit))


class CompositeSimpsons(Integration):

    def __init__(self, lower_limit, upper_limit, f) -> None:
        super().__init__(lower_limit, upper_limit, f)

    def integrate(self, n):
        """
            Computes the integral of f using the Composite Simpsons rule

            returns float
        """
        h = (self._upper_limit - self._lower_limit) / n
        x = [self._lower_limit + j*h for j in range(n + 1)]

        return sum(map(lambda i: self._f(x[2*i-2]) + 4*self._f(x[2*i-1])
                   + self._f(x[2*i]), range(1, int(n / 2) + 1))) * (h / 3)


class CompositeTrapezoidal(Integration):
    def __init__(self, lower_limit, upper_limit, f) -> None:
        super().__init__(lower_limit, upper_limit, f)

    def integrate(self, n):
        """
            Computes the integral of f using the Composite Trapezoidal rule

            returns float
        """
        h = (self._upper_limit - self._lower_limit) / n
        x = [self._lower_limit + j*h for j in range(n + 1)]

        return (self._f(x[0]) + self._f(x[-1]) +
                sum(map(lambda i: 2*self._f(x[i]),
                    range(1, int(n)))))*(h / 2)
