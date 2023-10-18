from Individuals.individual import *
import numpy as np
from Fncs.mazeFitness import mazeProblem

class IntIndividual(Individual):
    def __init__(self, size, minB, maxB):
            self.min_bound = minB
            self.max_bound = maxB
            self.cod = "INT"
            self.cromossome = self.init_cromossome(size)
            self.positions =[]

    def init_cromossome(self, size):
        return np.random.RandomState().randint(self.min_bound, self.max_bound, size=size)
    
    def labirintoFitness(self):
        self.score, self.positions = mazeProblem(self.cromossome)

    def crossover(self, secondParent, type):
        if type == "1 Ponto":
            return self.crossover1pto(secondParent)
        elif type == "2 Pontos":
            return self.crossover2pto(secondParent)
        elif type == "Unif":
            return self.crossoverUnif(secondParent)
        

    def crossover1pto(self, i2):
        #Define o ponto de corte
        ptoC = np.random.randint(0, len(self.cromossome))
        crom1 = np.concatenate((self.cromossome[:ptoC], i2.cromossome[ptoC:]))
        crom2 = np.concatenate((i2.cromossome[:ptoC], self.cromossome[ptoC:]))

        return [crom1, crom2]

    def crossover2pto(self, i2):
        #Define os pontos de corte
        ptoC1 = np.random.randint(0, len(self.cromossome)-1)
        ptoC2 = np.random.randint(ptoC1+1, len(self.cromossome))
        #print("cromossome 1: ", self.cromossome)
        #print("cromossome 2: ", i2.cromossome)
        #print("Ponto de corte 1: ", ptoC1)
        #print("Ponto de corte 2: ", ptoC2)
 
        #gera os 2 individuos resultantes do crossover
        crom1 = np.concatenate((self.cromossome[:ptoC1], i2.cromossome[ptoC1:ptoC2], self.cromossome[ptoC2:]))
        crom2 = np.concatenate((i2.cromossome[:ptoC1], self.cromossome[ptoC1:ptoC2], i2.cromossome[ptoC2:]))
 
        #retorna uma lista com os 2 individuos gerados
        return [crom1, crom2]


    def crossoverUnif(self, i2):
        #Define os pontos de corte
        #print("cromossome 1: ", self.cromossome)
        #print("cromossome 2: ", i2.cromossome)
 
        #gera os 2 individuos resultantes do crossover
        #inicializa o array com o primeiro elemento
        if np.random.random() < 0.5:
            crom1 = np.array((self.cromossome[0]))
            crom2 = np.array((i2.cromossome[0]))
        else:
            #print("Flip em 0")
            crom1 = np.array((i2.cromossome[0]))
            crom2 = np.array((self.cromossome[0]))
 
        #percorre o resto do array verificando se ocorre o flip ou nao
        for i in range(1, len(self.cromossome)):
            if np.random.random() < 0.5:
                crom1 = np.append(crom1, self.cromossome[i]);
                crom2 = np.append(crom2, i2.cromossome[i]);
            else:
                #print("Flip em ", i)
                crom1 = np.append(crom1, i2.cromossome[i]);
                crom2 = np.append(crom2, self.cromossome[i]);
        #retorna uma lista com os 2 individuos gerados
        return [crom1, crom2]
    
    def mutation(self, tipo, tx):
        if tipo == "Valor Aleatório no domínio":
            self.mutacaoRndVal(tx)
        else:
            raise Exception("Mutacao[", tipo, "] indefinida") 

    def mutacaoRndVal(self, tx):
        #para cada elemento do cromossome da bitflip com um chance de txMut
        for i in range(len(self.cromossome)):
            if np.random.random() < tx:
                #print("Flip em ", i)
                self.cromossome[i] = np.random.randint(self.min_bound, self.max_bound)
       