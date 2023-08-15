from Individual import *
import numpy as np

class IntPermIndividual(Individual):
    def __init__(self, size, minB, maxB):
            self.min_bound = minB
            self.max_bound = maxB
            self.cod = "INT-PERM"
            self.cromossome = self.init_cromossome(size)

    def init_cromossome(self, size):
        return np.random.RandomState().permutation(size)
    
    #Demais features por individuo