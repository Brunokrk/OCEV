from Individual import *
import numpy as np

class RealIndividual (Individual):
    def __init__(self, size, minB, maxB):
        self.min_bound = minB
        self.max_bound = maxB
        self.cod = "REAL"
        self.cromossome = self.init_cromossome(size)

    def init_cromossome(self, size):
        return np.random.RandomState().uniform(self.min_bound, self.max_bound, size=size)
    
    #Demais features por individuo