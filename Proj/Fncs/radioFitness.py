import math
from Fncs.manipulationFunctions import *

def radioProblem(cromossome):
    '''Função Fitness para problema dos radios
        Função Objetivo: 30ST + 40LX
        Restrições(h): 1ST + 2LX <= 40
        ST -> 5 Bits
        LX -> 5 Bits
        
        Função Objetivo Normalizada: (30ST + 40 LS)/1360 → 1360 MELHOR CASO
        Restrição Normalizada: max{0, (ST +2LX -40)/16}
        Fitness Normalizada: FOnormalizada - R
    '''

    standard = math.floor(scaleAdjustment(decodifyBinCromossome(cromossome, 0, 5), 5, 0.0, 24.0))
    luxo =     math.floor(scaleAdjustment(decodifyBinCromossome(cromossome, 5, 9), 4, 0.0, 16.0))

    h = max(0,(standard +2*luxo -40)/16)
    fo = (30*standard + 40*luxo)/1360 - h
    
    return fo, standard, luxo