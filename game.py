
#Holds the setup for a game including the pieces and the size of the board
class Game:

	def getPieceCount(self):
		return self.pieceCount

	def getBoardSize(self):
		return self.boardSize

	def __init__(self, pieceCount, boardSize):
		self.pieceCount = pieceCount
		self.boardSize = boardSize
