from BinaryIndividual import *
from IntIndividual import *
from RealIndividual import *
from IntPermIndividual import *

POPULATION_SIZE = 10
DIMENSION = 15

def create_pop(indType, popSize, dim):
    """Cria população INT, BIN, REAL, INT-PERM"""

    population = []
    if indType == "REAL":
        for _ in range(popSize):
            population.append(RealIndividual(dim, -10, 10))
    elif indType == "INT":
        for _ in range(popSize):
            population.append(IntIndividual(dim, -5, 10))
    elif indType == "INT-PERM":
        for _ in range(popSize):
            population.append(IntPermIndividual(dim, 100, 1000))
    elif indType == "BIN":
        for _ in range(popSize):
            population.append(BinaryIndividual(dim, 100, 1000))
            
    return population


individual_type = input("FODASE:")
pop = create_pop(individual_type, POPULATION_SIZE, DIMENSION)

for idx, individual in enumerate(pop):
    print(f"Individual {idx+1}: {individual}")
