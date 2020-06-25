import numpy as np
import copy

#Used everytime the piece is rotated in the direction that is passed
def rotationRoutine(piece, direction):

    tempBool = None
    tempMatrix = piece.getPiece()

    #Left
    if(direction == 0):

        for x in range(0,5):
            for y in range(0,int(5/2)):
                for z in range(y, (4 - y)):
                    tempBool = tempMatrix[x][y][z]
                    tempMatrix[x][y][z] = tempMatrix[x][z][4 - y]
                    tempMatrix[x][z][4 - y] = tempMatrix[x][4 - y][4 - z]
                    tempMatrix[x][4 - y][4 - z] = tempMatrix[x][4 - z][y]
                    tempMatrix[x][4 - z][y] = tempBool
        piece.setPiece(tempMatrix)

    #Right 
    if(direction == 1):

        for i in range(0,3):

            for x in range(0,5):
                for y in range(0,int(5/2)):
                    for z in range(y, (4 - y)):
                        tempBool = tempMatrix[x][y][z]
                        tempMatrix[x][y][z] = tempMatrix[x][z][4 - y]
                        tempMatrix[x][z][4 - y] = tempMatrix[x][4 - y][4 - z]
                        tempMatrix[x][4 - y][4 - z] = tempMatrix[x][4 - z][y]
                        tempMatrix[x][4 - z][y] = tempBool

        piece.setPiece(tempMatrix)
    
    #Forward
    if(direction == 2):

        for z in range(0,5):
            for x in range(0,int(5/2)):
                for y in range(x, 4 - x):
                    tempBool = tempMatrix[x][y][z]
                    tempMatrix[x][y][z] = tempMatrix[y][4 - x][z]
                    tempMatrix[y][4 - x][z] = tempMatrix[4 - x][4 - y][z]
                    tempMatrix[4 - x][4 - y][z] = tempMatrix[4 - y][x][z]
                    tempMatrix[4 - y][x][z] = tempBool

        piece.setPiece(tempMatrix)

    #BackWards
    if(direction == 3):

        for i in range(0,3):

            for z in range(0,5):
                for x in range(0,int(5/2)):
                    for y in range(x, 4 - x):
                        tempBool = tempMatrix[x][y][z]
                        tempMatrix[x][y][z] = tempMatrix[y][4 - x][z]
                        tempMatrix[y][4 - x][z] = tempMatrix[4 - x][4 - y][z]
                        tempMatrix[4 - x][4 - y][z] = tempMatrix[4 - y][x][z]
                        tempMatrix[4 - y][x][z] = tempBool

        piece.setPiece(tempMatrix)


#Used when the piece rotation is complete
def finishRotation(piece):

    tempMatrix = piece.getPiece()
    smallMatrix = np.full((4, 4, 4), False, dtype=bool)

    #This is the order in which 2D slices of the 3D matrix are checked and removed
    checkOrder = [2,3,1,4,0]
    elimVals = [2,2,2]
    
    #In order to condense this 5x5x5 array to a 4x4x4 array we need to first check which 2D array slices to remove
    for i in range(0,3):
        for j in range(0,5):
            if dimensionOccupied(i, checkOrder[j], tempMatrix):
                elimVals[i] = checkOrder[j+1]
            else:
                break

    #The piece in the original matrix is writen to the smallMatrix(but only part that has the piece)
    scanX = 0
    for x in range(0,4):
        scanY = 0
        if scanX == elimVals[0]:
            scanX += 1
        for y in range(0,4):
            scanZ = 0
            if scanY == elimVals[1]:
                scanY += 1
            for z in range(0,4):
                if scanZ == elimVals[2]:
                    scanZ += 1
                smallMatrix[x][y][z] = copy.deepcopy(tempMatrix[scanX][scanY][scanZ])
                scanZ += 1
            scanY += 1
        scanX += 1

    #The lowest occupied spot is found
    testPosition = 3
    for y in range(3,-1,-1):
        if (dimensionOccupied(1,y,smallMatrix)):
            testPosition = copy.deepcopy(y)
            break

    finalMatrix = np.full((4, 4, 4), False, dtype=bool)

    #The piece is essentially dropped to the bottom of the matrix
    for y in range(3,-1,-1):
        for x in range(0,4):
            for z in range(0,4):
                if(testPosition <= -1):
                    finalMatrix[x][y][z] = copy.deepcopy(smallMatrix[x][3][z])
                else:
                    finalMatrix[x][y][z] = copy.deepcopy(smallMatrix[x][testPosition][z])
        testPosition -= 1     

    #Change the piece
    piece.setPiece(finalMatrix)



#Used to check if a dimension is occupied (I.E. all positions where x = 1, y = 3, etc.)
def dimensionOccupied(dimension, value, checkBoard):

    numElements = checkBoard.size
    dimensionSize = int(round(numElements ** (1./3))) 

    #Check X dimension
    if (dimension == 0):
        for y in range(0,dimensionSize):
            for z in range (0,dimensionSize):
                if (checkBoard[value, y, z] == True):
                    return True

    #Check Y dimension
    elif (dimension == 1):
        for x in range(0,dimensionSize):
            for z in range (0,dimensionSize):
                if (checkBoard[x, value, z] == True):
                    return True

    #Check Z dimension
    elif (dimension == 2):
        for x in range(0,dimensionSize):
            for y in range (0,dimensionSize):
                if (checkBoard[x, y, value] == True):
                    return True

    else:
        raise Exception("Invalid Dimension")


#Calculate where the piece should go in the board based on the dimension length
def calculatePiecePosition(number):

    x = round(number - 4)

    if (x == 0):
        return int(x)

    else: 
        x = round((x / 2.), 1)

        return int(x)


#Take the curent piece, change it to be as wide and deep as board with piece in center, then attatch it to the board
def postRotation(currentTurn, boardList, currentPiece):
    
    #Select board as currentBoard if its not the first turn
    if(currentTurn != 0):
        boardList[currentTurn].setBoard(boardList[currentTurn - 1].getBoard())

    checkBoard = boardList[currentTurn].getBoard()

    #Calculate where to place the pieces in board(center)
    shape = checkBoard.shape
    xDim = shape[0]
    zDim = shape[2]

    #Board must be as wide and deep as the piece's 4x4x4 rotated matrix we translated
    if (xDim < 4 or zDim < 4):
        raise Exception("Board too small")

    xStart = calculatePiecePosition(shape[0])
    zStart = calculatePiecePosition(shape[2])

    #take piece from rotation 
    #change the piece to fit in a piece thats 4 tall but as wide as the board
    newPiece = np.full((xDim, 4, zDim), False, dtype=bool)

    #The old piece is mapped to a new piece that is wide and as deep as the board
    oldPiece = currentPiece.getPiece()

    offsetX = 0
    for x in range (xStart, (xStart+4)):
        offsetY = 0
        for y in range (0, 4):
            offsetZ = 0
            for z in range(zStart, (zStart+4)):
                newPiece[x][y][z] = copy.deepcopy(oldPiece[offsetX][offsetY][offsetZ])
                offsetZ += 1
            offsetY += 1
        offsetX += 1

    #The currentPiece is set to this new board sized piece
    currentPiece.setPiece(newPiece)

    #This piece is attatched to the board
    boardList[currentTurn].setPiece(currentPiece)

    #The current piece is cleared
    currentPiece = None