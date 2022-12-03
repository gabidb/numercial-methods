from src.numerical_method import NumericalMethod


class Derivative(NumericalMethod):

    def __init__(self, f, h=1E-5) -> None:
        self._f = f
        print(h)
        if h != 0:
            self._h = float(h)
        else:
            self._h = float(1E-5)

    def get_f(self):
        return self._f

    def get_h(self):
        return self._h


class Forward(Derivative):
    def __call__(self, x):
        f, h = self.get_f(), self.get_h()
        return (f(x+h) - f(x)) / h


class Forward2(Derivative):
    def __call__(self, x):
        f, h = self.get_f(), self.get_h()
        return (4*f(x+h) - f(x+2*h) - 3*f(x)) / (2*h)


class Centered(Derivative):
    def __call__(self, x):
        f, h = self.get_f(), self.get_h()
        return (f(x+h) - f(x-h)) / (2*h)


class Centered4(Derivative):
    def __call__(self, x):
        f, h = self.get_f(), self.get_h()
        return (f(x-2*h) - 8*f(x-h) + 8*f(x+h) - f(x+2*h)) / (12*h)


class Backward(Derivative):
    def __call__(self, x):
        f, h = self.get_f(), self.get_h()
        return (f(x) - f(x-h)) / h


class Backward2(Derivative):
    def __call__(self, x):
        f, h = self.get_f(), self.get_h()
        return (3*f(x) - 4*f(x-h) + f(x-2*h)) / (2*h)
