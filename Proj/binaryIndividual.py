from individual import *
import numpy as np

class BinaryIndividual(Individual):
    def __init__(self, size, minB, maxB):
            self.min_bound = minB
            self.max_bound = maxB
            self.cod = "BIN"
            self.cromossome = self.init_cromossome(size)

    def init_cromossome(self, size):
        return np.random.RandomState().randint(2, size=size)
    
    #Demais features por individuo