from Individuals.individual import *
import numpy as np

from Fncs.queensFitness import queensProblem

class IntPermIndividual(Individual):
    def __init__(self, size):
            self.cod = "INT-PERM"
            self.score = 0
            self.cromossome = self.init_cromossome(size)

    def init_cromossome(self, size):
        return np.random.RandomState().permutation(size)
    
    def queensFitness(self):
        self.score = queensProblem(self.cromossome)
    
    def crossover(self, secondParent, type):
        #tipo de crossover
        if type == "PMX":
            return self.crossoverPMX(secondParent)
        else:
            raise Exception("Crossover [", type, "] indefinido")
        
    def crossoverPMX(self, secondParent):
        p1, p2 = [0]*len(self.cromossome), [0]*len(self.cromossome)
        crom1, crom2 = [], []

        #inicializa a posicao dos indices
        for i in range(len(self.cromossome)):
            p1[self.cromossome[i]] = i
            p2[secondParent.cromossome[i]] = i
            crom1 += [self.cromossome[i]]
            crom2 += [secondParent.cromossome[i]]
            
        #Define os pontos de corte
        ptoC1 = np.random.randint(0, len(self.cromossome)-1)
        ptoC2 = np.random.randint(ptoC1+1, len(self.cromossome))
        
        for i in range(ptoC1, ptoC2):
            temp1 = crom1[i]
            temp2 = crom2[i]
            
            crom1[i], crom1[p1[temp2]] = temp2, temp1
            crom2[i], crom2[p2[temp1]] = temp1, temp2
            
            p1[temp1], p1[temp2] = p1[temp2], p1[temp1]
            p2[temp1], p2[temp2] = p2[temp2], p2[temp1]
        
        return [crom1, crom2]
    
    def mutation(self, type, chance):
        if type == "SWAP":
            self.swapMutation(chance)
        else:
            raise Exception("Mutação selecionada não existente")
    
    def swapMutation(self, chance):
        for i in range(len(self.cromossome)):
            if np.random.random() < chance:
                p2 = np.random.randint(0, len(self.cromossome))
                atual = self.cromossome[i]
                self.cromossome[i] = self.cromossome[p2]
                self.cromossome[p2] = atual