def mazeProblem(cromossomo):
    global labirintoBoard
    if not "labirintoBoard" in globals():
        labirintoBoard = [     
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,3,1,1,0,0],
                    [0,1,1,1,1,1,1,1,1,0,1,0,1,0,1,0,0,0,0,0,0,0,1,1,0],
                    [0,1,0,0,0,0,0,0,1,0,1,0,1,0,1,0,0,0,0,0,0,0,1,0,0],
                    [0,1,1,1,1,1,1,0,1,0,1,0,1,0,1,0,1,1,1,0,1,1,1,1,0],
                    [0,1,0,0,0,0,1,0,1,0,1,0,1,0,1,0,1,0,0,0,0,0,0,1,0],
                    [0,1,0,0,0,0,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1,1,0],
                    [0,1,0,0,0,0,1,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0,0,1,0],
                    [0,1,1,1,1,1,1,1,0,1,1,0,1,1,1,0,1,0,1,0,1,0,1,1,0],
                    [0,0,0,0,0,0,1,1,0,1,1,0,1,1,1,0,1,0,1,0,1,0,0,1,0],
                    [0,2,1,1,1,0,1,0,0,1,1,0,1,0,0,0,1,0,1,0,1,0,1,1,0],
                    [0,1,0,0,1,0,1,0,0,1,1,0,1,0,0,0,1,0,1,0,1,1,1,1,0],
                    [0,1,0,0,1,0,1,0,0,1,0,0,1,0,0,0,1,0,1,0,0,0,0,1,0],
                    [0,1,0,0,1,0,1,1,0,1,0,1,1,1,1,1,1,0,1,0,1,1,1,1,0],
                    [0,1,0,0,1,0,1,1,0,1,0,0,0,0,0,0,0,0,1,0,1,0,0,1,0],
                    [0,1,1,0,1,0,0,1,1,1,0,0,0,0,0,1,1,1,1,0,1,0,0,1,0],
                    [0,1,1,0,1,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,1,0,1,1,0],
                    [0,0,1,0,1,0,1,1,0,0,0,0,0,0,0,1,1,1,1,0,1,0,1,0,0],
                    [0,1,1,0,0,0,1,1,0,1,1,1,1,0,0,0,0,0,1,0,1,1,1,1,0],
                    [0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,0,1,0,0,1,0],
                    [0,0,0,0,1,0,0,0,0,1,1,0,1,1,1,0,1,0,1,0,1,1,0,1,0],
                    [0,1,1,1,1,0,1,1,1,1,1,0,1,0,1,0,1,0,1,0,0,1,0,1,0],
                    [0,1,1,0,1,0,1,0,0,0,1,0,1,0,1,0,1,0,1,0,1,1,0,1,0],
                    [0,1,1,0,1,0,1,0,0,0,1,0,1,0,1,0,1,0,1,0,1,0,0,1,0],
                    [0,1,1,0,1,0,1,0,0,0,1,0,1,0,1,0,1,0,1,0,1,1,0,1,0],
                    [0,1,1,0,1,0,1,0,0,0,1,0,1,0,1,0,1,0,0,0,0,1,0,1,0],
                    [0,0,0,0,1,0,1,1,1,1,1,1,1,1,1,0,1,0,0,1,1,1,1,1,0],
                    [0,1,1,1,1,0,1,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,1,0,0],
                    [0,1,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                ]
    #dir:
    #0 -> cima
    #1 -> direita
    #2 -> baixo
    #3 -> esquerda
    
    distMax = abs(0 - 24) + abs(0 - 29)
    atualX = 1
    atualY = 10
    melhorX = 1
    melhorY = 1
    melhorDist = distMax
    fimX = 20
    fimY = 1
    visitados = [[10, 1]]
    positions = []

    for gene in cromossomo:
        movimentos = movimentosPossiveis(atualX, atualY, visitados)
        if len(movimentos) > 0:
            dir = movimentos[gene % len(movimentos)]
            if dir == 0:
                if labirintoBoard[atualY-1][atualX] != 0:
                    atualY -= 1
                    visitados.append([atualY, atualX])
            elif dir == 1:
                if labirintoBoard[atualY][atualX+1] != 0:
                    atualX += 1
                    visitados.append([atualY, atualX])
            elif dir == 2:
                if labirintoBoard[atualY+1][atualX] != 0:
                    atualY += 1
                    visitados.append([atualY, atualX])
            else:
                if labirintoBoard[atualY][atualX-1] != 0:
                    atualX -= 1
                    visitados.append([atualY, atualX])
            
            positions.append((atualX, atualY))
            distDest = abs(atualX - fimX) + abs(atualY - fimY)
            
            if distDest < melhorDist:
                melhorDist = distDest
                melhorX = atualX
                melhorY = atualY
            if labirintoBoard[atualY][atualX] == 3:#saida
                #print(str(atualX)+":"+str(atualY))
                print("Chegou")
                break

    distDest = abs(melhorX - fimX) + abs(melhorY - fimY)
    fit = 1.0 - distDest/distMax
    
    return fit, positions
 
def movimentosPossiveis(x, y, visitados):
    movs = []
    #cima
    if labirintoBoard[y-1][x] != 0 :
        if [y-1, x] not in visitados:
            movs.append(0)
    #direita
    if labirintoBoard[y][x+1] != 0 :
        if [y, x+1] not in visitados:
            movs.append(1)
    #baixo
    if labirintoBoard[y+1][x] != 0 :
        if [y+1, x] not in visitados:
            movs.append(2)
    #esquerda
    if labirintoBoard[y][x-1] != 0 :
        if [y, x-1] not in visitados:
            movs.append(3)
    return movs