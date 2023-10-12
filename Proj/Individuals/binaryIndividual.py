from Individuals.individual import *
import numpy as np

from Fncs.radioFitness import radioProblem

class BinaryIndividual(Individual):
    def __init__(self, size, minB, maxB):
        self.min_bound = minB
        self.max_bound = maxB
        self.score = 0
        self.cod = "BIN"
        self.standard = 0
        self.luxo = 0
        #self.fo = 0
        self.cromossome = self.init_cromossome(size)

    def init_cromossome(self, size):
        return np.random.RandomState().randint(2, size=size)
    
    def radioFitness(self):   
        self.score, self.standard, self.luxo = radioProblem(self.cromossome)

    def crossover(self, secondParent, type):
        if type == "1 Ponto":
            return self.crossover1pto(secondParent)
        elif type == "2 Pontos":
            return self.crossover2pto(secondParent)
        elif type == "Unif":
            return self.crossoverUnif(secondParent)
        
    def crossover1pto(self, secondParent):
        cut    = np.random.randint(0, len(self.cromossome))
        first  = np.concatenate((secondParent.cromossome[:cut], self.cromossome[cut:]))
        second = np.concatenate((self.cromossome[:cut], secondParent.cromossome[cut:]))
        return [first, second]

    def crossover2pto(self, secondParent):
        firstCut  = np.random.randint(0, len(self.cromossome)-1)
        secondCut = np.random.randint(firstCut+1, len(self.cromossome))

        first = np.concatenate((self.cromossome[:firstCut],
                                secondParent.cromossome[firstCut:secondCut],
                                self.cromossome[secondCut:]))
        second = np.concatenate((secondParent.cromossome[:firstCut],
                                self.cromossome[firstCut:secondCut],
                                secondParent.cromossome[secondCut:]))
        return[first, second]

    def crossoverUnif(self, secondParent):
        if np.random.random() < 0.5: #50% de chance
            first = np.array((self.cromossome[0]))
            second = np.array((secondParent.cromossome[0]))
        else:
            first = np.array((secondParent.cromossome[0]))
            second = np.array((self.cromossome[0]))

        for gene in range(1, len(self.cromossome)):
            if np.random.random() < 0.5: #50% de chance
                first = np.append(self.cromossome[0])
                second = np.append(secondParent.cromossome[0])
            else:
                first = np.append(secondParent.cromossome[0])
                second = np.append(self.cromossome[0])
        
        return [first, second]
    
    def mutation(self, type, chance):
        if type == "BIT-FLIP":
            self.bitFlipMutation(chance)
        else:
            raise Exception("Mutação selecionada não existente")
    
    def bitFlipMutation(self, chance):
        for i in range(len(self.cromossome)):
            if np.random.random() < chance:
                if self.cromossome[i] == 0:
                    #print(bit)
                    self.cromossome[i] = 1
                else:
                    self.cromossome[i] = 0