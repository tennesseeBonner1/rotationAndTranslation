import numpy as np
import copy

#This translation routine needs to be written
def translationRoutine(board, direction):

    currentPiece = board.getPiece().getTranslatedPiece()

    cpX = currentPiece.shape[0]
    cpY = currentPiece.shape[1]
    cpZ = currentPiece.shape[2]

    cleanPiece = np.full((cpX, cpY, cpZ), False, dtype=bool)

    if (direction == 0):
        #(Forward) check cpX dimension for true values 
        for y in range(0, cpY):
            for z in range(0, cpZ):
                if (currentPiece[cpX - 1][y][z] == True):
                    return

        for x in range(1, cpX):
            for y in range(0, cpY):
                for z in range(0, cpZ):
                    cleanPiece[x][y][z] = copy.deepcopy(currentPiece[x - 1][y][z])

    if (direction == 1):
        #(Left) check 0 z dimension for true values 
        for x in range(0, cpX):    
            for y in range(0, cpY):
                if (currentPiece[x][y][0] == True):
                    return

        for x in range(0, cpX):
            for y in range(0, cpY):
                for z in range(0, cpZ - 1):
                    cleanPiece[x][y][z] = copy.deepcopy(currentPiece[x][y][z + 1])

    if (direction == 2):
        #(Back) check cpX dimension for true values 
        for y in range(0, cpY):
            for z in range(0, cpZ):
                if (currentPiece[0][y][z] == True):
                    return

        for x in range(0, cpX - 1):
            for y in range(0, cpY):
                for z in range(0, cpZ):
                    cleanPiece[x][y][z] = copy.deepcopy(currentPiece[x + 1][y][z])

    if (direction == 3):
        #(Right)check cpX dimension for true values 
        for x in range(0, cpX):
            for y in range(0, cpY):
                if (currentPiece[x][y][cpZ - 1] == True):
                    return

        for x in range(0, cpX):
            for y in range(0, cpY):
                for z in range(1, cpZ):
                    cleanPiece[x][y][z] = copy.deepcopy(currentPiece[x][y][z - 1])       
    board.getPiece().setTranslatedPiece(cleanPiece)

#The drop is attempted if it is possible
def attemptDrop(boardList, currentTurn):
    currentPiece = boardList[currentTurn].getPiece().getTranslatedPiece()

    cpX = currentPiece.shape[0]
    cpY = currentPiece.shape[1]
    cpZ = currentPiece.shape[2]

    pieceList = []

    #Save pieces in list of there locations with the lowest piece located near x = 0, z = 0 and y = 3
    for y in range(cpY - 1, -1, -1):
        for x in range(0, cpX):
            for z in range(0, cpZ):
                if (currentPiece[x][y][z] == True):
                    pieceList.append([x,y,z])

    currentBoard = boardList[currentTurn].getBoard()
    #go through board array starting at y = max in the first piece's x and z, y-- until that position is unoccupied, 
    #then go to the next piece and if it's valid, move onto the next piece, otherwise break, do this until every one of the 
    #spots have been checked
    cbX = currentBoard.shape[0]
    cbY = currentBoard.shape[1]
    cbZ = currentBoard.shape[2]

    difference = cbY - 4
    tempPieceList = copy.deepcopy(pieceList)

    for i in range(0, 4):
        temp = tempPieceList[i][1]
        tempPieceList[i][1] = temp + difference

    for y in range(cbY - 1, -1, -1):
        
        for i in range(0, 4):
            temp = tempPieceList[i][1]
            if (y < (cbY - 1)):
                tempPieceList[i][1] = temp - 1
            if (tempPieceList[i][1] < 0):
                return False
        
        pieceList = tempPieceList

        works = True
        for piece in tempPieceList:
            if (currentBoard[piece[0]][piece[1]][piece[2]] == True):
                works = False
                break

        if works:
            boardCopy = copy.deepcopy(currentBoard)

            for piece in tempPieceList:
                boardCopy[piece[0]][piece[1]][piece[2]] = True
            print("Board's current Turn is " + str(boardList[currentTurn].getTurn()))

            for i in range(currentTurn, len(boardList)):
                boardList[i].setBoard(boardCopy)

            return True
    return False
