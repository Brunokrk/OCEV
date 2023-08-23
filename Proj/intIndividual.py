from individual import *
import numpy as np

class IntIndividual(Individual):
    def __init__(self, size, minB, maxB):
            self.min_bound = minB
            self.max_bound = maxB
            self.cod = "INT"
            self.cromossome = self.init_cromossome(size)

    def init_cromossome(self, size):
        return np.random.RandomState().randint(self.min_bound, self.max_bound, size=size)