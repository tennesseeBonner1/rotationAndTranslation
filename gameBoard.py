import pygame
import time
import sys
import rotation
import translation
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
size = width, height = 600, 400
screen = pygame.display.set_mode(size)
mediumFont = pygame.font.Font("OpenSans-Regular.ttf", 20)
largeFont = pygame.font.Font("OpenSans-Regular.ttf", 40)


#Keeps track of this game's pieces
pieceList = [[],[],[],[],[],[],[],[]]

#Keeps track of this game's boards
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

#Starts the game with a test boardSize and piece array
startGame(np.array([2,2,2,2,2,2,2,2]) , np.array([6,4,4]))

#Enum for the stage that the game is in
class Stage(Enum):
    BASKING = 0
    SELECTING = 1
    ROTATING = 2
    TRANSLATING = 3

gameStage = Stage.SELECTING

#input keys for the buttons w,a,s,d,space
keys = [False, False, False, False, False]

#Where the Pi game takes place
while True:

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

    #Fills the screen with black every time
    screen.fill(black)

    #The selecting Routine(Currently only lets you select one piece)
    if (gameStage.value == 1):

        # Draw title
        title = largeFont.render("Select piece", True, white)
        titleRect = title.get_rect()
        titleRect.center = ((width / 2), height - 50)
        screen.blit(title, titleRect)

        # Draw buttons
        oneCButton = pygame.Rect((width / 2) , ((height / 2) - (3 *(height / 7))), 50, 50)
        oneC = mediumFont.render("1C", True, black)
        oneCButtonRec = oneC.get_rect()
        oneCButtonRec.center = oneCButton.center
        pygame.draw.rect(screen, white, oneCButton)
        screen.blit(oneC, oneCButtonRec)

        # Check if button is clicked and react differently for each button
        click, _, _ = pygame.mouse.get_pressed()
        if click == 1 and gameStage.value == 1:
            mouse = pygame.mouse.get_pos()
            if oneCButton.collidepoint(mouse):
                time.sleep(0.2)
                print("1C")

                #Creates a 1C piece
                if pieceList[0]:
                    currentPiece = pieceList[0][0]
                    del pieceList[0][0]
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

        #The piece is rotated in the direction of input until space is pushed
        if (keys[0] == True):
            rotation.rotationRoutine(currentPiece, 2)
            keys[0] = False
        if (keys[1] == True):
            rotation.rotationRoutine(currentPiece, 0)
            keys[1] = False
        if (keys[2] == True):
            rotation.rotationRoutine(currentPiece, 3)
            keys[2] = False
        if (keys[3] == True):
            rotation.rotationRoutine(currentPiece, 1)
            keys[3] = False
        if (keys[4] == True):
            print("Rotated piece \n" + str(currentPiece.getPiece()))
            rotation.finishRotation(currentPiece)
            print("Condensed piece \n" + str(currentPiece.getPiece()))
            keys[4] = False
            rotation.postRotation(currentTurn, boardList, currentPiece)
            print("Board sized piece ready to translate \n" + str(boardList[currentTurn].getPiece().getPiece()))
            gameStage = Stage.TRANSLATING
            

    #If on the translating routine
    if (gameStage.value == 3):
    
        # Draw title
        title = largeFont.render("Translate piece", True, white)
        titleRect = title.get_rect()
        titleRect.center = ((width / 2), 50)
        screen.blit(title, titleRect)

        subTitle = mediumFont.render("Use the 'WASD' buttons to translate and SPACE to finish Translation", True, white)
        titleRect = subTitle.get_rect()
        titleRect.center = ((width / 2), 90)
        screen.blit(subTitle, titleRect)

        if (keys[0] == True):
            print("UP")
            translation.translationRoutine(boardList[currentTurn])
            keys[0] = False
        if (keys[1] == True):
            print("LEFT")
            translation.translationRoutine(boardList[currentTurn])
            keys[1] = False
        if (keys[2] == True):
            print("DOWN")
            translation.translationRoutine(boardList[currentTurn])
            keys[2] = False
        if (keys[3] == True):
            print("RIGHT")
            translation.translationRoutine(boardList[currentTurn])
            keys[3] = False
        if (keys[4] == True):
            print("SPACE PUSHED")
            keys[4] = False
            gameStage = Stage.BASKING
           
    pygame.display.flip()

