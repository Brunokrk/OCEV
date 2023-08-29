from Individuals.binaryIndividual import BinaryIndividual
from Individuals.intIndividual import *
from Individuals.realIndividual import *
from Individuals.intPermIndividual import *
from Fncs.queensFitness import *
from Fncs.radioFitness import *

def create_pop(indType, popSize, dim):
    """Cria população INT, BIN, REAL, INT-PERM de acordo com o problema"""
    population = []
    #print(indType)
    if indType == "Real":
        for _ in range(popSize):
            population.append(RealIndividual(dim, -10, 10))
    elif indType == "Inteiro":
        for _ in range(popSize):
            population.append(IntIndividual(dim, -5, 10))
    elif indType == "Inteiro Permutado":
        for _ in range(popSize):
            population.append(IntPermIndividual(dim))
    elif indType == "Binário":
        for _ in range(popSize):
            population.append(BinaryIndividual(dim, 100, 1000))
            
    return population

def apply_problem(population, problem):
    '''Aplicação da Função Fitness de acordo com o problema'''
    if problem == "N-Queens":
        for ind in(population):
            ind.score = queensProblem(ind.cromossome)
    elif problem == "Fábrica de Rádios":
        for ind in (population):
            ind.score = radioProblem(ind.cromossome)
    return population

def attackButton(individuals_type, population_size, dimension, problem):
    '''Ao clicar no botão "ATTACK!" um problema é executado'''
    createdPopulation = create_pop(individuals_type, population_size, dimension)
    createdPopulation = apply_problem(createdPopulation, problem)
    return createdPopulation


