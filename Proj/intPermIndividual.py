from individual import *
import numpy as np

class IntPermIndividual(Individual):
    def __init__(self, size):
            self.cod = "INT-PERM"
            self.score = 0
            self.cromossome = self.init_cromossome(size)
            #self.cromossome = [0,2,4,6,1,3,5,7]

    def init_cromossome(self, size):
        return np.random.RandomState().permutation(size)
    
    #Demais features por individuo