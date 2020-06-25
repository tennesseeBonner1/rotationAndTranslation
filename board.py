import numpy as np

#Board holds the current board as well as the current piece and turn number
class Board:

	def getBoard(self):
		return self.currentBoard

	def setBoard(self, updatedBoard):
		self.currentBoard = updatedBoard

	def getPiece(self):
		return self.currentPiece

	def setPiece(self, updatedPiece):
		self.currentPiece = updatedPiece

	def __init__(self, x, y, z, turn, currentPiece):

		self.currentBoard = np.full((x, y, z), False, dtype=bool)
		self.turn = turn
		self.currentPiece = currentPiece