import math
#-------Lista de funções fitness para solução dos problemas-------

def queensProblem (cromossome):
    """ Função Fitness para problema das rainhas"""
    tabLenght = len(cromossome) #Numero de rainhas e tamanho do tabuleiro
    clashes = 0
    print(tabLenght)
    for i in range(tabLenght-1):
        for j in range(i+1, tabLenght):
            if abs(i-j) == abs(cromossome[i]-cromossome[j]):
                clashes += 1
    
    maxClashes = ((tabLenght -1)* tabLenght)/2
    return (maxClashes - clashes)
    


