"""
    File contains abstract class for numerical methods
"""
from abc import ABC, abstractmethod


class NumericalMethod(ABC):
    def __init__(self, f) -> None:
        self._f = f
    
    def get_f(self):
        """
            Get the function
        """
        return self._f
    
    def set_f(self, f):
        """
            Set the function
        """
        self._f = f
    
    @abstractmethod
    def get_exact_value(self):
        """
            Returns exact value for f
        """
        raise NotImplementedError('No default behviour')
    
    def get_error(self, approximation):
        """
            Returns the difference between the exact value
            and the approximation of the method
        """
        return abs(self.get_exact_value() - approximation)
