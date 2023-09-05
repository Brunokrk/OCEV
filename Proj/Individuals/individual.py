from abc import ABC, abstractmethod
import numpy as np

class Individual(ABC):
    @abstractmethod
    def __init__ (self, size, minB, maxB):
        pass

    @abstractmethod
    def init_cromossome(self, size):
        pass

    def __str__(self):
        return str(self.cromossome)