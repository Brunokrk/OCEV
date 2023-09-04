def decodifyBinCromossome (cromossome, initial, final):
    '''A ideia aqui é receber um cromossomo binário e retornar o inteiro, dentro de um intervalo'''
    numTotal = cromossome[initial:final]
    numStr = ""
    for n in numTotal:
        numStr += str(n)
    return int(numStr, 2) #2 para base binária

def scaleAdjustment(int_n, qtd_bits, min_bound, max_bound):
    '''A ideia aqui é receber um numero inteiro, e ajustar sua escala'''
    return min_bound + ((max_bound - min_bound)/(2**qtd_bits-1))* int_n

