"""
    File contains classes for differentiation techniques
"""
from src.numerical_method import NumericalMethod
from sympy import Symbol, diff

 
class Derivative(NumericalMethod):

    def __init__(self, f, h=1E-5) -> None:
        super().__init__(f)
        if h != 0:
            self._h = float(h)
        else:
            self._h = float(1E-5)

    def get_exact_value(self):
        """
            Returns exact value of the derivative of f
        """
        return diff(self._f, Symbol('x'))


class Forward(Derivative):
    def __call__(self, x):
        """
            Computes the derivative of f using Forward difference

            returns float
        """
        f, h = self._f, self._h
        return (f(x+h) - f(x)) / h


class Forward2(Derivative):
    def __call__(self, x):
        """
            Computes the derivative of f using Forward
            second order difference

            returns float
        """
        f, h = self._f, self._h
        return (4*f(x+h) - f(x+2*h) - 3*f(x)) / (2*h)


class Centered(Derivative):
    def __call__(self, x):
        """
            Computes the derivative of f using
            Central difference

            returns float
        """
        f, h = self._f, self._h
        return (f(x+h) - f(x-h)) / (2*h)


class Centered4(Derivative):
    def __call__(self, x):
        """
            Computes the derivative of f using
            Central 4th order difference

            returns float
        """
        f, h = self._f, self._h
        return (f(x-2*h) - 8*f(x-h) + 8*f(x+h) - f(x+2*h)) / (12*h)


class Backward(Derivative):
    def __call__(self, x):
        """
            Computes the derivative of f using
            Backward difference

            returns float
        """
        f, h = self._f, self._h
        return (f(x) - f(x-h)) / h


class Backward2(Derivative):
    def __call__(self, x):
        """
            Computes the derivative of f using
            Backward second order difference

            returns float
        """
        f, h = self._f, self._h
        return (3*f(x) - 4*f(x-h) + f(x-2*h)) / (2*h)
