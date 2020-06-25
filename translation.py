import numpy as np
import copy

#This translation routine needs to be written
def translationRoutine(board, direction):

    currentPiece = board.getPiece().getPiece()

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
        #(Forward) check cpX dimension for true values 
        for y in range(0, cpY):
            for z in range(0, cpZ):
                if (currentPiece[0][y][z] == True):
                    return

        for x in range(0, cpX - 1):
            for y in range(0, cpY):
                for z in range(0, cpZ):
                    cleanPiece[x][y][z] = copy.deepcopy(currentPiece[x + 1][y][z])

    if (direction == 3):
        #(Forward) check cpX dimension for true values 
        for x in range(0, cpX):
            for y in range(0, cpY):
                if (currentPiece[x][y][cpZ - 1] == True):
                    return

        for x in range(0, cpX):
            for y in range(0, cpY):
                for z in range(1, cpZ):
                    cleanPiece[x][y][z] = copy.deepcopy(currentPiece[x][y][z - 1])
                    
    board.getPiece().setPiece(cleanPiece)

#The drop is attempted if it is possible
def attemptDrop(board):
	print("Drop Attempted")