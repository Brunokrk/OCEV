from Individuals.binaryIndividual import BinaryIndividual
from Individuals.intIndividual import *
from Individuals.realIndividual import *
from Individuals.intPermIndividual import *
from Fncs.queensFitness import *
from Fncs.radioFitness import *
import numpy as np
import copy

class EvolutiveAlgorithm():
    """Guarda informações sobre uma execução do algoritmo"""
    def __init__(self, problem, population_size, dimension, ind, generations, selectionType, crossoverType, mutationType, crossoverChance, mutationChance, elitismo):
        self.problem = problem
        self.populationSize = population_size
        self.dimension = dimension
        self.individualType = ind
        self.population = self.create_pop()
        self.selectionType = selectionType
        self.crossoverType = crossoverType
        self.mutationType = mutationType
        self.crossoverChance = crossoverChance
        self.mutationChance = mutationChance
        self.qtdGenerations = generations
        self.isElitist = elitismo

        #Atributos de cunho estatístico
        self.generalBest = None #Guardará sempre o melhor indivíduo a cada Loop Evolutivo

    def evolutive_loop(self):
        bestIndividuals = [] #Por Geração
        averageFitness = [] #Por Geração
        bestIndividualsFitness = []
        generation = 0

        worstIndAux, bestIndAux = self.calculaFitness()

        #best Indivíduo até então
        self.generalBest = copy.deepcopy(self.population[bestIndAux])

        bestIndividuals = [self.population[bestIndAux].cromossome]
        bestIndividualsFitness += [self.population[bestIndAux].score]
        averageFitness = [self.averagePopulationFitness()]

        while generation < self.qtdGenerations:
            generation += 1
            #print(self.population)
            selection = self.selectionChoice()
            
            #cross
            intermediatePop = self.recombination(selection)
            
            #Substitui
            for i in range(len(intermediatePop)):
                self.population[i].cromossome = intermediatePop[i]

            #mutation
            for i in self.population:
                i.mutation(self.mutationType, self.mutationChance)

            #fitness da geração
            worstIndAux, bestIndAux = self.calculaFitness()

            #elitismo
            if self.isElitist == True:
                self.population[worstIndAux] = copy.deepcopy(self.generalBest)
            
            #Verifica se tem novo melhor geral
            if self.population[bestIndAux].score > self.generalBest.score:
                self.generalBest = copy.deepcopy(self.population[bestIndAux])
            else:
                if self.isElitist == True:
                    bestIndAux = worstIndAux
            
            bestIndividuals += [self.population[bestIndAux].cromossome]
            bestIndividualsFitness += [self.population[bestIndAux].score]
            averageFitness  += [self.averagePopulationFitness()]
        
        return averageFitness, bestIndividuals, bestIndividualsFitness
        #print("\n\nMelhor Solução Encontrada: " + generalBest.cromossome+ " -> "+ generalBest.score)



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
                ind.queensFitness()
        elif self.problem == "Fábrica de Rádios":
            for ind in (self.population):
                ind.radioFitness()
    
    def somaFitnessValues(self):
        total = 0
        for ind in self.population:
            total += ind.score
        return total

    def calculaFitness(self):
        #calculando a fitness
        self.apply_problem()
        
        worstInd = bestInd = 0
        bestF = self.population[bestInd].score
        worstF = self.population[worstInd].score
        
        for i in range(1, len(self.population)):
            if self.population[i].score > bestF:
                bestInd = i
                bestF = self.population[i].score
            if self.population[i].score < worstF:
                worstInd = i
                worstF = self.population[i].score
        return  worstInd, bestInd

    def averagePopulationFitness(self):
        soma = 0.0
        for ind in self.population:
            soma += ind.score
        return soma/len(self.population)

    def recombination(self, individuos):
        popInt = []
        for i in range(int(len(self.population)/2)):
            if np.random.random() < self.crossoverChance:
                inds = individuos[i*2].crossover(individuos[i*2+1], self.crossoverType)
                popInt += [inds[0]]
                popInt += [inds[1]]
            else:
                popInt += [individuos[i*2].cromossome]
                popInt += [individuos[i*2+1].cromossome]
        return popInt
    
    #Rotinas de seleção
    def selectionChoice(self):
        if self.selectionType == "Roleta":
            return self.roleta()
        elif self.selectionType == "Torneio":
            return self.torneio(2)
        else:
            raise Exception("Tipo de Seleção não existente!!"+self.selectionType+" Escolha Uma")

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
        
        #for idx, individual in enumerate(selected):
        #    print(f"Individual {idx+1}: {individual}")
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
        

        #for idx, individual in enumerate(selected):
        #    print(f"Individual {idx+1}: {individual}")
        return selected