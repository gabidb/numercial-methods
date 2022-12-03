from abc import ABC, abstractmethod

class NumericalMethod(ABC):
    def __init__(self) -> None:
        super().__init__()
    
    # @abstractmethod
    # def error(self):
    #     raise NotImplementedError("Not implemented")