#Rotation and Translation

This program uses matrices to rotate 3D tetronimo-like pieces and translate them to be dropped into a board larger or equal to 4x4x4. This acts as the backend for a 3D tetris like puzzle game. 

##Getting Started

To begin the program type the following into the commandline

'''
python3 gameBoard.py
'''

##How to play

The game is broken up into a cycle of states. These states are BASKING, SELECTING, ROTATING, and TRANSLATING. The game will begin in the Basking state and work as follows:

###Basking 

This state lets you look at the existing board. Currently the board is represented by a 3D matrix of 0's and 1's. If you want to move onto the next state, press SPACE

###Selecting

This state lets you select which piece to are going to drop into the board. These pieces are a 3D reimagining of the original tetronimos, plus a couple of special ones I designed myself. The pieces are:

* One Corner Piece (1C)
* Four Corner Piece (4C)
* I Piece (I)
* L Piece (L)
* O Piece (O)
* S Piece (S)
* Stair Piece (St)
* T Piece (T)

When you click on one of the pieces(and there are enough pieces left) the game moves onto the next state. 

###Rotating

Now the piece matrix(representing the piece) and the board matrix are displayed with the piece over the board. You can rotate the piece by using the w, a, s, d buttons. When you are done rotating the piece, move on to the next state by pressing SPACE.

###Translating

Again, the piece matrix will be displayed over the board matrix. Now you can move the translated piece by using the w, a, s, d buttons. When you are done translating the piece, move on to the next state by pressing SPACE.


##Ending the game

The game will end if all the pieces are put in the box correctly. Currently if you make any mistakes and are unable to put any more pieces in, you will have to completely restart the game. When you reach the win state press SPACE to close the window. 