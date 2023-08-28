from Individuals.binaryIndividual import BinaryIndividual
from Fncs.fitness import *
from Individuals.intIndividual import *
from Individuals.realIndividual import *
from Individuals.intPermIndividual import *

def create_pop(indType, popSize, dim):
    """Cria população INT, BIN, REAL, INT-PERM"""
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
    if problem == "N-Queens":
        for ind in(population):
            ind.score = queensProblem(ind.cromossome)
    return population

def attackButton(individuals_type, population_size, dimension, problem):
    createdPopulation = create_pop(individuals_type, population_size, dimension)
    createdPopulation = apply_problem(createdPopulation, problem)
    return createdPopulation

