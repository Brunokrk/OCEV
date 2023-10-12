import math
def queensProblem (cromossome):
    """ Função Fitness para problema das rainhas"""
    tabLenght = len(cromossome) #Numero de rainhas e tamanho do tabuleiro
    clashes = 0
    for i in range(tabLenght-1):
        for j in range(i+1, tabLenght):
            if abs(i-j) == abs(cromossome[i]-cromossome[j]):
                clashes += 1
    
    maxClashes = ((tabLenght -1)* tabLenght)/2
    return (maxClashes - clashes)/maxClashes , clashes

def queensProblemPenalties(cromossome):
    tam = len(cromossome)
    global lucros, maxLuc
    #print("oi")
    if not "lucros" in globals():
        lucros = []
        c = 1
        for i in range(tam):
            l = []
            for j in range(tam):
                if i % 2  == 0: #impar
                    l.append(math.sqrt(c))
                else:
                    l.append(math.log(c, 10.9))
                c+=1
            lucros.append(l)
        maxLuc = 0
        for i in range(tam):
            maxLuc += lucros[i][tam-1] #soma da diagonal principal

        #calculo da primeira parte do fitness
    clashes = 0
    for i in range(tam-1):
        for j in range(i+1, tam):
            if abs(i-j) == abs(cromossome[i]-cromossome[j]):
                clashes += 1
    m = ((tam-1)*tam)/2

    somaLucro = 0
    for i in range(tam):
        somaLucro += lucros[i][cromossome[i]]

    fit = somaLucro / maxLuc #fitness Base

    h = clashes/m

    fo = max(0, fit-h)

    return fo, somaLucro