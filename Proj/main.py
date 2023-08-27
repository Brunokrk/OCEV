from Individuals.binaryIndividual import BinaryIndividual
from Fncs.fitness import *
from Individuals.intIndividual import *
from Individuals.realIndividual import *
from Individuals.intPermIndividual import *
import json
import streamlit as st
from streamlit_elements import elements, mui


def ler_arquivo_json():
    with open("input.json", 'r') as inputJson:
        dados = json.load(inputJson)
        individual_type = dados.get('individualType')
        dimension = dados.get('dimension')
        population_size = dados.get('population_size')
        problem = dados.get('problem')

        print(individual_type)
        return individual_type, dimension, population_size, problem

def create_pop(indType, popSize, dim):
    """Cria população INT, BIN, REAL, INT-PERM"""
    population = []
    #print(indType)
    if indType == "REAL":
        for _ in range(popSize):
            population.append(RealIndividual(dim, -10, 10))
    elif indType == "INT":
        for _ in range(popSize):
            population.append(IntIndividual(dim, -5, 10))
    elif indType == "INT-PERM":
        for _ in range(popSize):
            population.append(IntPermIndividual(dim))
    elif indType == "BIN":
        for _ in range(popSize):
            population.append(BinaryIndividual(dim, 100, 1000))
            
    return population

def apply_problem(population, problem):
    if problem == "n-queens":
        for ind in(population):
            ind.score = queensProblem(ind.cromossome)
    return population

def printPopulation (pop):
    for idx, individual in enumerate(pop):
        print(f"Individual {idx+1}: {individual}")

    print("\n\n$$$ SCORE $$$ \n")
    for idx, individual in enumerate(pop):
        print(f"Individual {idx+1}: {individual.score}")


if __name__ == "__main__":

    individual_type, dimension, population_size, problem = ler_arquivo_json()
    createdPopulation = create_pop(individual_type, population_size, dimension)
    #createdPopulation[0].cromossome = [0,2,4,6,1,3,5,7]
    createdPopulation = apply_problem(createdPopulation, problem)
    printPopulation(createdPopulation)



