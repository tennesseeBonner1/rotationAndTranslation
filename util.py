
#Used to check if a dimension is occupied (I.E. all positions where x = 1, y = 3, etc.)
def dimensionOccupied(dimension, value, checkBoard):

    numElements = checkBoard.size
    dimensionSize = int(round(numElements ** (1./3))) 

    #Check X dimension
    if (dimension == 0):
        for y in range(0,dimensionSize):
            for z in range (0,dimensionSize):
                if (checkBoard[value][y][z] == True):
                    return True

    #Check Y dimension
    elif (dimension == 1):
        for x in range(0,dimensionSize):
            for z in range (0,dimensionSize):
                if (checkBoard[x][value][z] == True):
                    return True

    #Check Z dimension
    elif (dimension == 2):
        for x in range(0,dimensionSize):
            for y in range (0,dimensionSize):
                if (checkBoard[x][y][value] == True):
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
