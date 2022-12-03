from .numerical_method import NumericalMethod
import sympy

class Integration(NumericalMethod):

    def __init__(self, lower_limit, upper_limit) -> None: 
        self._lower_limit = lower_limit
        self._upper_limit = upper_limit
    
    def get_lower_limit(self):
        return self._lower_limit

    def set_lower_limit(self, lower_limit):
        self._lower_limit = lower_limit

    def get_upper_limit(self):
        return self._upper_limit

    def set_lower_limit(self, upper_limit):
        self._upper_limit = upper_limit

    def integrate(self, f):
        raise NotImplementedError('No integration method implemented in ' + self.__class__.__name__)

    def __str__(self) -> str:
        return f"Integral has lower limit {self._lower_limit} and upper limit {self._upper_limit}"






class Simpsons(Integration):

    def __init__(self, lower_limit, upper_limit) -> None:
        super().__init__(lower_limit, upper_limit)
        self._h = (self._upper_limit - self._lower_limit) / 2
        self._midpoint = (self._upper_limit + self._lower_limit) / 2

    def integrate(self, f):
        return (self._h / 3) * (f(self._lower_limit) + 4 * f(self._midpoint) + f(self._upper_limit)) 

    def error(self):
        return max(sympy.diff(self._f, x, 4))
    

class CompositeSimpsons(Integration):

    def __init__(self, lower_limit, upper_limit, n) -> None:
        super().__init__(lower_limit, upper_limit)
        self.set_n(n)
        self._h = (self._upper_limit - self._lower_limit) / self._n

    def set_n(self,n):
        if n % 2 == 0:
            self._n = n
        else:
            print("N must be an even number... Adding 1 to n")
            self._n = n + 1            

    def integrate(self, f):
        x = [self._lower_limit + j*self._h for j in range(self._n + 1)]
        
        return sum(map(lambda i: f(x[2*i-2]) + 4*f(x[2*i-1]) + f(x[2*i]), range(1, int(self._n / 2) + 1))) * (self._h / 3)

class Trapezoidal(Integration):
    def __init__(self, lower_limit, upper_limit, n) -> None:
        super().__init__(lower_limit, upper_limit)
        self._n = n
        self._h = (self._upper_limit - self._lower_limit) / self._n
    
    def integrate(self, f):
        x = [self._lower_limit + j*self._h for j in range(self._n + 1)]

        return (f(x[0]) + f(x[-1]) + sum(map(lambda i: 2*f(x[i]), range(1, int(self._n))))) * (self._h / 2)
