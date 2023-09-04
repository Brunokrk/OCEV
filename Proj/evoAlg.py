from Individuals.binaryIndividual import BinaryIndividual
from Individuals.intIndividual import *
from Individuals.realIndividual import *
from Individuals.intPermIndividual import *
from Fncs.queensFitness import *
from Fncs.radioFitness import *
import numpy as np
import random 
import copy

class EvolutiveAlgorithm():
    def __init__(self, problem, population_size, dimension, ind):
        self.problem = problem
        self.populationSize = population_size
        self.dimension = dimension
        self.individualType = ind
        self.population = self.create_pop()
        self.mutationType = None
        self.selectionType = None

    def create_pop(self):
        """Cria população INT, BIN, REAL, INT-PERM de acordo com o problema"""
        population = []
        if self.individualType == "Real":
            for _ in range(self.populationSize):
                population.append(RealIndividual(self.dimension, -10, 10))
        elif self.individualType == "Inteiro":
            for _ in range(self.populationSize):
                population.append(IntIndividual(self.dimension, -5, 10))
        elif self.individualType == "Inteiro Permutado":
            for _ in range(self.populationSize):
                population.append(IntPermIndividual(self.dimension))
        elif self.individualType == "Binário":
            for _ in range(self.populationSize):
                population.append(BinaryIndividual(self.dimension, 100, 1000))
            
        return population
    
    def apply_problem(self):
        '''Aplicação da Função Fitness de acordo com o problema'''
        if self.problem == "N-Queens":
            for ind in(self.population):
                ind.score = queensProblem(ind.cromossome)
        elif self.problem == "Fábrica de Rádios":
            for ind in (self.population):
                ind.score = radioProblem(ind.cromossome)
    
    def somaFitnessValues(self):
        total = 0
        for ind in self.population:
            total += ind.score
        return total

    #Rotinas de seleção
    def roleta(self):
        """Rotina de seleção baseada em roleta"""
        #Calculando chances
        somaFitness = self.somaFitnessValues()
        chances = []
        for ind in self.population:
            chances += [ind.score/somaFitness]

        #Selecionando indivíduos par-a-par
        selected = []
        for ind in range(int(len(self.population)/2)):
            randInd = np.random.choice(list(range(len(self.population))), p=chances)
            selected += [self.population[randInd]]

            #Segunda Roleta
            secondChances = []
            for i in self.population:
                secondChances += [i.score/(somaFitness - self.population[randInd].score)]
            secondChances[randInd] = 0.0 #Não pode ser escolhido novamente

            secondRandInd = np.random.choice(list(range(len(self.population))), p=secondChances)
            selected += [self.population[secondRandInd]]
        
        for idx, individual in enumerate(selected):
            print(f"Individual {idx+1}: {individual}")
        return selected
    
    def torneio(self, tamTorneio):
        """Rotina de seleção baseada em torneio estocástico"""
        selected = []
        bestIndividualIndex = -1

        for i in range(int(len(self.population))):
            partTorn=[]
            for j in range(tamTorneio):
                partTorn += [np.random.randint(len(self.population))]
            bestIndividualIndex = partTorn[0]
            for j in partTorn:
                if self.population[j].score > self.population[bestIndividualIndex].score:
                    bestIndividualIndex = j
            selected += [self.population[bestIndividualIndex]]
        

        for idx, individual in enumerate(selected):
            print(f"Individual {idx+1}: {individual}")
        return selected