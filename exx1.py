import random

POPULATION = 10
DIMENSION = 15
INT_BOUNDS = [-5, 10]
REAL_BOUNDS = [-10, 10]

#DIMENSION -> NÚMERO DE COMPONENETES (VARIÁVEIS) EM CADA INDIVÍDUO

def generate_indv_BIN(dimension):
    #Função para gerar indivíduos BIN
    return [random.choice([0,1]) for a in range(dimension)]

def generate_indv_REAL(dimension):
    return

def generate_indv_INT(dimension):
    return

def generate_indv_INT_PERM(dimension):
    return