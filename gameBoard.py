import pygame
import time
import sys
from rotation import *
from translation import *
import piece
import game
import board
import numpy as np
import copy
from enum import Enum


#Initialize pygame
pygame.init()
black = (0, 0, 0)
white = (255, 255, 255)
size = width, height = 1000, 600
screen = pygame.display.set_mode(size)
mediumFont = pygame.font.Font("OpenSans-Regular.ttf", 20)
largeFont = pygame.font.Font("OpenSans-Regular.ttf", 40)


#Important game elements
pieceList = [[],[],[],[],[],[],[],[]]
boardList = []
currentPiece = None
currentTurn = 0


#Setup the necesites for the game
def startGame(pieceCount, boardSize):

    #Setup the game object and save the piece count array to currentPieceCount
    currentGame = game.Game(pieceCount, boardSize)
    currentPieceCount = copy.deepcopy(currentGame.getPieceCount())

    #Creates all of the board and piece objects needed for the game
    turnVal = 0
    for i in range(0, currentPieceCount.size):
        for j in range(0, currentPieceCount[i]):

            pieceList[i].append(piece.Piece(i))

            #Boards start with no piece and are empty by default
            boardList.append(board.Board(boardSize[0], boardSize[1], boardSize[2], turnVal, None))
            turnVal += 1

#input keys for the buttons w,a,s,d,space
keys = [False, False, False, False, False, False]
        
#Enum for the stage that the game is in
class Stage(Enum):
    BASKING = 0
    SELECTING = 1
    ROTATING = 2
    TRANSLATING = 3

gameStage = Stage.BASKING

def undo(value):
    keys[5] = False
    if (value == 0):
        return Stage.TRANSLATING
    elif (value == 1):
        return Stage.BASKING
    elif (value == 2):
        return Stage.SELECTING
    elif (value == 3):
        return Stage.ROTATING 


#Starts the game with a test boardSize and piece array
startGame(np.array([1,0,2,5,1,2,2,3]) , np.array([4,4,4]))


#Where the Pi game takes place
while True:

    #Fills the screen with black every time
    screen.fill(black)

    #Read the events and end the game when it ends and read in the keyboards keys
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
                if event.key==pygame.K_w:
                    keys[0]=True
                    time.sleep(0.2)
                if event.key==pygame.K_a:
                    keys[1]=True
                    time.sleep(0.2)
                if event.key==pygame.K_s:
                    keys[2]=True
                    time.sleep(0.2)
                if event.key==pygame.K_d:
                    keys[3]=True
                    time.sleep(0.2)
                if event.key==pygame.K_SPACE:
                    keys[4]=True
                    time.sleep(0.2)
                if event.key==pygame.K_u:
                    keys[5]=True
                    time.sleep(0.2)

    #Basking state where you can look at the board
    if (gameStage.value == 0):
        
        #If you are out of pieces
        if any(pieceList) == False:

            # Draw title
            title = largeFont.render("Congratualtions. You won!", True, white)
            titleRect = title.get_rect()
            titleRect.center = ((width / 2), (height/2))
            screen.blit(title, titleRect)

            #If you then push space the game ends
            if keys[4] == True:
                sys.exit()

        else:
            # Draw title
            title = largeFont.render("Basking State, \"look at that board!\"", True, white)
            titleRect = title.get_rect()
            titleRect.center = ((width / 2), height - 50)
            screen.blit(title, titleRect)

            #Get the most recent board
            currentBoard = boardList[currentTurn].getBoard()

            #Render the board
            titleRects = []
            titles = []

            offset = [0, 0]
            for x in range(0, currentBoard.shape[0]):
                printY = 300 + offset[1]
                for y in range(0, currentBoard.shape[1]):
                    printX = 200 + offset[0]
                    for z in range(0, currentBoard.shape[2]):
                        if currentBoard[x][y][z] == True:
                            tempTitle = largeFont.render("1", True, white)
                        else:
                            tempTitle = largeFont.render("0", True, white)   
                        tempTitleRect = tempTitle.get_rect()
                        tempTitleRect.center = (printX, printY)
                        titles.append(tempTitle)
                        titleRects.append(tempTitleRect)
                        printX += 40
                    printY += 40
                offset[0] += 160
                offset[1] -= 60
                
            for i in range(0, len(titles)):
                screen.blit(titles[i], titleRects[i])

            #Go to the selecting stage when space is pushed
            if (keys[4] == True):
                gameStage = Stage.SELECTING

            #Undo if you can
            if (keys[5] == True and currentTurn != 0):

                currentTurn -= 1
                boardCopy = boardList[currentTurn - 1].getBoard()

                if (currentTurn == 0):
                    boardCopy = np.full((boardCopy.shape[0], boardCopy.shape[1], boardCopy.shape[2]), False, dtype=bool)

                for i in range(currentTurn, len(boardList)):
                    boardList[i].setBoard(boardCopy)

                rotatedPiece = boardList[currentTurn].getPiece().getRotatedPiece()
                boardList[currentTurn].getPiece().setTranslatedPiece(rotatedPiece)

                gameStage = undo(gameStage.value)

    #The selecting Routine(Currently only lets you select one piece)
    if (gameStage.value == 1):

        keys[4] = False

        # Draw title
        title = largeFont.render("Select a piece", True, white)
        titleRect = title.get_rect()
        titleRect.center = ((width / 2), height - 200)
        screen.blit(title, titleRect)

        buttonSizeX = 70
        buttonSizeY = 70

        buttonOriginX = 100
        buttonOriginY = 200 
        space = 100

        # Draw buttons
        oneCButton = pygame.Rect(buttonOriginX, buttonOriginY, buttonSizeX, buttonSizeY)
        oneC = mediumFont.render(("1C (" + str(len(pieceList[0])) + ")"), True, black)
        oneCButtonRec = oneC.get_rect()
        oneCButtonRec.center = oneCButton.center
        pygame.draw.rect(screen, white, oneCButton)
        screen.blit(oneC, oneCButtonRec)

        fourCButton = pygame.Rect(buttonOriginX + (space), buttonOriginY, buttonSizeX, buttonSizeY)
        fourC = mediumFont.render(("4C (" + str(len(pieceList[1]))) + ")", True, black)
        fourCButtonRec = fourC.get_rect()
        fourCButtonRec.center = fourCButton.center
        pygame.draw.rect(screen, white, fourCButton)
        screen.blit(fourC, fourCButtonRec)

        iButton = pygame.Rect(buttonOriginX + (2 * space), buttonOriginY, buttonSizeX, buttonSizeY)
        i = mediumFont.render(("I (" + str(len(pieceList[2]))) + ")", True, black)
        iButtonRec = i.get_rect()
        iButtonRec.center = iButton.center
        pygame.draw.rect(screen, white, iButton)
        screen.blit(i, iButtonRec)

        lButton = pygame.Rect(buttonOriginX + (3 * space), buttonOriginY, buttonSizeX, buttonSizeY)
        l = mediumFont.render(("L (" + str(len(pieceList[3]))) + ")", True, black)
        lButtonRec = l.get_rect()
        lButtonRec.center = lButton.center
        pygame.draw.rect(screen, white, lButton)
        screen.blit(l, lButtonRec)

        oButton = pygame.Rect(buttonOriginX + (4 * space), buttonOriginY, buttonSizeX, buttonSizeY)
        o = mediumFont.render(("O (" + str(len(pieceList[4]))) + ")", True, black)
        oButtonRec = o.get_rect()
        oButtonRec.center = oButton.center
        pygame.draw.rect(screen, white,oButton)
        screen.blit(o, oButtonRec)

        sButton = pygame.Rect(buttonOriginX + (5 * space), buttonOriginY, buttonSizeX, buttonSizeY)
        s = mediumFont.render(("S (" + str(len(pieceList[5]))) + ")", True, black)
        sButtonRec = s.get_rect()
        sButtonRec.center = sButton.center
        pygame.draw.rect(screen, white,sButton)
        screen.blit(s, sButtonRec)

        stButton = pygame.Rect(buttonOriginX + (6 * space), buttonOriginY, buttonSizeX, buttonSizeY)
        st = mediumFont.render(("ST (" + str(len(pieceList[6]))) + ")", True, black)
        stButtonRec = st.get_rect()
        stButtonRec.center = stButton.center
        pygame.draw.rect(screen, white,stButton)
        screen.blit(st, stButtonRec)

        tButton = pygame.Rect(buttonOriginX + (7 * space), buttonOriginY, buttonSizeX, buttonSizeY)
        t = mediumFont.render(("T (" + str(len(pieceList[7]))) + ")", True, black)
        tButtonRec = t.get_rect()
        tButtonRec.center = tButton.center
        pygame.draw.rect(screen, white,tButton)
        screen.blit(t, tButtonRec)

        if (keys[5] == True):
            gameStage = undo(gameStage.value)

        # Check if button is clicked and react differently for each button
        click, _, _ = pygame.mouse.get_pressed()
        if click == 1 and gameStage.value == 1:
            mouse = pygame.mouse.get_pos()
            if oneCButton.collidepoint(mouse):
                time.sleep(0.2)

                #Creates a 1C piece
                if pieceList[0]:
                    currentPiece = pieceList[0][0]
                    del pieceList[0][0]
                    gameStage = Stage.ROTATING

            if fourCButton.collidepoint(mouse):
                time.sleep(0.2)

                #Creates a 1C piece
                if pieceList[1]:
                    currentPiece = pieceList[1][0]
                    del pieceList[1][0]
                    gameStage = Stage.ROTATING
                    
            if iButton.collidepoint(mouse):
                time.sleep(0.2)

                #Creates a 1C piece
                if pieceList[2]:
                    currentPiece = pieceList[2][0]
                    del pieceList[2][0]
                    gameStage = Stage.ROTATING
                    
            if lButton.collidepoint(mouse):
                time.sleep(0.2)

                #Creates a 1C piece
                if pieceList[3]:
                    currentPiece = pieceList[3][0]
                    del pieceList[3][0]
                    gameStage = Stage.ROTATING
                    
            if oButton.collidepoint(mouse):
                time.sleep(0.2)

                #Creates a 1C piece
                if pieceList[4]:
                    currentPiece = pieceList[4][0]
                    del pieceList[4][0]
                    gameStage = Stage.ROTATING
                    
            if sButton.collidepoint(mouse):
                time.sleep(0.2)

                #Creates a 1C piece
                if pieceList[5]:
                    currentPiece = pieceList[5][0]
                    del pieceList[5][0]
                    gameStage = Stage.ROTATING
                    
            if stButton.collidepoint(mouse):
                time.sleep(0.2)

                #Creates a 1C piece
                if pieceList[6]:
                    currentPiece = pieceList[6][0]
                    del pieceList[6][0]
                    gameStage = Stage.ROTATING


            if tButton.collidepoint(mouse):
                time.sleep(0.2)

                #Creates a 1C piece
                if pieceList[7]:
                    currentPiece = pieceList[7][0]
                    del pieceList[7][0]
                    gameStage = Stage.ROTATING

    #The Rotating Routine
    if (gameStage.value == 2):

    	# Draw title
        title = largeFont.render("Rotate piece", True, white)
        titleRect = title.get_rect()
        titleRect.center = ((width / 2), 50)
        screen.blit(title, titleRect)

        subTitle = mediumFont.render("Use the 'WASD' buttons to rotate and SPACE to finish Rotation", True, white)
        titleRect = subTitle.get_rect()
        titleRect.center = ((width / 2), 90)
        screen.blit(subTitle, titleRect)

        #Get the piece and render it
        printPiece = shrinkPiece(currentPiece)

        titleRects = []
        titles = []

        offset = [0, 0]
        for x in range(0, printPiece.shape[0]):
            printY = 300 + offset[1]
            for y in range(0, printPiece.shape[1]):
                printX = 300 + offset[0]
                for z in range(0, printPiece.shape[2]):
                    if printPiece[x][y][z] == True:
                        tempTitle = mediumFont.render("1", True, white)
                    else:
                        tempTitle = mediumFont.render("0", True, white)   
                    tempTitleRect = tempTitle.get_rect()
                    tempTitleRect.center = (printX, printY)
                    titles.append(tempTitle)
                    titleRects.append(tempTitleRect)
                    printX += 20
                printY += 20
            offset[0] += 80
            offset[1] -= 30
            

        for i in range(0, len(titles)):
            screen.blit(titles[i], titleRects[i])

        currentBoard = boardList[currentTurn].getBoard()

        boardTitleRects = []
        boardTitles = []

        offset = [0, 0]
        for x in range(0, currentBoard.shape[0]):
            printY = 400 + offset[1]
            for y in range(0, currentBoard.shape[1]):
                printX = 300 + offset[0]
                for z in range(0, currentBoard.shape[2]):
                    if currentBoard[x][y][z] == True:
                        tempTitle = mediumFont.render("1", True, white)
                    else:
                        tempTitle = mediumFont.render("0", True, white)   
                    tempTitleRect = tempTitle.get_rect()
                    tempTitleRect.center = (printX, printY)
                    boardTitles.append(tempTitle)
                    boardTitleRects.append(tempTitleRect)
                    printX += 20
                printY += 20
            offset[0] += 80
            offset[1] -= 30

        for i in range(0, len(boardTitles)):
            screen.blit(boardTitles[i], boardTitleRects[i])

        #The piece is rotated in the direction of input until space is pushed
        if (keys[0] == True):
            rotationRoutine(currentPiece, 2)
            keys[0] = False
        if (keys[1] == True):
            rotationRoutine(currentPiece, 0)
            keys[1] = False
        if (keys[2] == True):
            rotationRoutine(currentPiece, 3)
            keys[2] = False
        if (keys[3] == True):
            rotationRoutine(currentPiece, 1)
            keys[3] = False
        if (keys[4] == True):
            finishRotation(currentPiece)
            keys[4] = False
            ##Remove the following and have it just move onto translating
            postRotation(currentTurn, boardList, currentPiece)
            gameStage = Stage.TRANSLATING
        if (keys[5] == True):

            originalPiece = currentPiece.getPiece()
            currentPiece.setRotatedPiece(originalPiece)

            shape = currentPiece.getShape()
            pieceList[shape].append(currentPiece)
            currentPiece = None
            gameStage = undo(gameStage.value)
            

    #If on the translating routine
    if (gameStage.value == 3):
    
        # Draw title
        title = largeFont.render("Translate piece", True, white)
        titleRect = title.get_rect()
        titleRect.center = ((width / 2), (50))
        screen.blit(title, titleRect)

        subTitle = mediumFont.render("Use the 'WASD' buttons to translate and SPACE to finish Translation", True, white)
        titleRect = subTitle.get_rect()
        titleRect.center = ((width / 2), 90)
        screen.blit(subTitle, titleRect)

        #Get and render the piece
        printPiece = boardList[currentTurn].getPiece().getTranslatedPiece()

        titleRects = []
        titles = []

        offset = [0, 0]
        for x in range(0, printPiece.shape[0]):
            printY = 300 + offset[1]
            for y in range(0, printPiece.shape[1]):
                printX = 300 + offset[0]
                for z in range(0, printPiece.shape[2]):
                    if printPiece[x][y][z] == True:
                        tempTitle = mediumFont.render("1", True, white)
                    else:
                        tempTitle = mediumFont.render("0", True, white)   
                    tempTitleRect = tempTitle.get_rect()
                    tempTitleRect.center = (printX, printY)
                    titles.append(tempTitle)
                    titleRects.append(tempTitleRect)
                    printX += 20
                printY += 20
            offset[0] += 80
            offset[1] -= 30
            

        for i in range(0, len(titles)):
            screen.blit(titles[i], titleRects[i])

        currentBoard = boardList[currentTurn].getBoard()
        boardTitleRects = []
        boardTitles = []

        offset = [0, 0]
        for x in range(0, currentBoard.shape[0]):
            printY = 400 + offset[1]
            for y in range(0, currentBoard.shape[1]):
                printX = 300 + offset[0]
                for z in range(0, currentBoard.shape[2]):
                    if currentBoard[x][y][z] == True:
                        tempTitle = mediumFont.render("1", True, white)
                    else:
                        tempTitle = mediumFont.render("0", True, white)   
                    tempTitleRect = tempTitle.get_rect()
                    tempTitleRect.center = (printX, printY)
                    boardTitles.append(tempTitle)
                    boardTitleRects.append(tempTitleRect)
                    printX += 20
                printY += 20
            offset[0] += 80
            offset[1] -= 30
            

        for i in range(0, len(boardTitles)):
            screen.blit(boardTitles[i], boardTitleRects[i])

        if (keys[0] == True):
            translationRoutine(boardList[currentTurn], 0)
            keys[0] = False
        if (keys[1] == True):
            translationRoutine(boardList[currentTurn], 1)
            keys[1] = False
        if (keys[2] == True):
            translationRoutine(boardList[currentTurn], 2)
            keys[2] = False
        if (keys[3] == True):
            translationRoutine(boardList[currentTurn], 3)
            keys[3] = False
        if (keys[4] == True):
            attempt = attemptDrop(boardList, currentTurn)

            if attempt:
                currentTurn += 1
                gameStage = Stage.BASKING

            keys[4] = False

        if (keys[5] == True):
            currentPiece = boardList[currentTurn].getPiece()
            boardList[currentTurn].setPiece(None)

            currentPiece.setTranslatedPiece(None)
            originalPiece = currentPiece.getPiece()
            currentPiece.setRotatedPiece(originalPiece)

            gameStage = undo(gameStage.value)
          
    pygame.display.flip()

