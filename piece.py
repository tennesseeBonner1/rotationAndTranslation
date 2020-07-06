import numpy as np

#Piece that holds the 3D matrix of the current piece
class Piece:

	def getShape(self):
		return self.shape
		
	def getPiece(self):
		return self.originalMatrix

	def getRotatedPiece(self):
		return self.rotatedPiece

	def getTranslatedPiece(self):
		return self.translatedPiece

	def setPiece(self, originalMatrix):
		self.originalMatrix = originalMatrix
		
	def setRotatedPiece(self, rotatedPiece):
		self.rotatedPiece = rotatedPiece

	def setTranslatedPiece(self, translatedPiece):
		self.translatedPiece = translatedPiece

	def __init__(self, shape):

		oneC = np.array([[[False,False,False,False,False],[False,False,False,False,False],[False,False,False,False,False],[False,False,False,False,False],[False,False,False,False,False]],[[False,False,False,False,False],[False,False,False,False,False],[False,False,False,False,False],[False,True ,False,True ,False],[False,False,False,False,False]],[[False,False,False,False,False],[False,False,False,False,False],[False,False,False,False,False],[False,False,False,False,False],[False,False,False,False,False]],[[False,False,False,False,False],[False,False,False,True ,False],[False,False,False,False,False],[False,True ,False,False,False],[False,False,False,False,False]],[[False,False,False,False,False],[False,False,False,False,False],[False,False,False,False,False],[False,False,False,False,False],[False,False,False,False,False]] ])
		fourC = np.array([[[False,False,False,False,False],[False,False,False,False,False],[False,False,False,False,False],[False,False,False,False,False],[False,False,False,False,False]],[[False,False,False,False,False],[False,False,False,True ,False],[False,False,False,False,False],[False,True ,False,False,False],[False,False,False,False,False]],[[False,False,False,False,False],[False,False,False,False,False],[False,False,False,False,False],[False,False,False,False,False],[False,False,False,False,False]],[[False,False,False,False,False],[False,False,False,False,False],[False,False,False,False,False],[False,False,False,True ,False],[False,False,False,False,False]],[[False,False,False,False,False],[False,True ,False,False,False],[False,False,False,False,False],[False,False,False,False,False],[False,False,False,False,False]] ])
		i = np.array([[[False,False,False,False,False],[False,False,False,False,False],[False,False,True ,False,False],[False,False,False,False,False],[False,False,False,False,False]],[[False,False,False,False,False],[False,False,False,False,False],[False,False,True ,False,False],[False,False,False,False,False],[False,False,False,False,False]],[[False,False,False,False,False],[False,False,False,False,False],[False,False,False,False,False],[False,False,False,False,False],[False,False,False,False,False]],[[False,False,False,False,False],[False,False,False,False,False],[False,False,True ,False,False],[False,False,False,False,False],[False,False,False,False,False]],[[False,False,False,False,False],[False,False,False,False,False],[False,False,True ,False,False],[False,False,False,False,False],[False,False,False,False,False]] ])
		l = np.array([[[False,False,False,False,False],[False,False,False,False,False],[False,False,False,False,False],[False,False,False,False,False],[False,False,False,False,False]],[[False,False,False,False,False],[False,False,False,False,False],[False,False,True ,False,False],[False,False,False,False,False],[False,False,False,False,False]],[[False,False,False,False,False],[False,False,False,False,False],[False,False,True ,False,False],[False,False,False,False,False],[False,False,False,False,False]],[[False,False,False,False,False],[False,False,False,False,False],[False,True ,True ,False,False],[False,False,False,False,False],[False,False,False,False,False]],[[False,False,False,False,False],[False,False,False,False,False],[False,False,False,False,False],[False,False,False,False,False],[False,False,False,False,False]] ])
		o = np.array([[[False,False,False,False,False],[False,False,False,False,False],[False,False,False,False,False],[False,False,False,False,False],[False,False,False,False,False]],[[False,False,False,False,False],[False,False,False,False,False],[False,False,False,False,False],[False,True ,False,True ,False],[False,False,False,False,False]],[[False,False,False,False,False],[False,False,False,False,False],[False,False,False,False,False],[False,False,False,False,False],[False,False,False,False,False]],[[False,False,False,False,False],[False,False,False,False,False],[False,False,False,False,False],[False,True ,False,True ,False],[False,False,False,False,False]],[[False,False,False,False,False],[False,False,False,False,False],[False,False,False,False,False],[False,False,False,False,False],[False,False,False,False,False]] ])
		s = np.array([[[False,False,False,False,False],[False,False,False,False,False],[False,False,False,False,False],[False,False,False,False,False],[False,False,False,False,False]],[[False,False,False,False,False],[False,False,False,False,False],[False,False,False,True ,False],[False,False,False,False,False],[False,False,False,False,False]],[[False,False,False,False,False],[False,False,False,False,False],[False,True ,False,True ,False],[False,False,False,False,False],[False,False,False,False,False]],[[False,False,False,False,False],[False,False,False,False,False],[False,True ,False,False,False],[False,False,False,False,False],[False,False,False,False,False]],[[False,False,False,False,False],[False,False,False,False,False],[False,False,False,False,False],[False,False,False,False,False],[False,False,False,False,False]] ])
		st = np.array([[[False,False,False,False,False],[False,False,False,False,False],[False,False,False,False,False],[False,False,False,False,False],[False,False,False,False,False]],[[False,False,False,False,False],[False,True ,False,False,False],[False,False,False,False,False],[False,False,False,True ,False],[False,False,False,False,False]],[[False,False,False,False,False],[False,False,False,False,False],[False,False,False,False,False],[False,False,False,False,False],[False,False,False,False,False]],[[False,False,False,False,False],[False,True ,False,False,False],[False,False,False,False,False],[False,False,False,True ,False],[False,False,False,False,False]],[[False,False,False,False,False],[False,False,False,False,False],[False,False,False,False,False],[False,False,False,False,False],[False,False,False,False,False]] ])
		t = np.array([[[False,False,False,False,False],[False,False,False,False,False],[False,False,False,False,False],[False,False,False,False,False],[False,False,False,False,False]],[[False,False,False,False,False],[False,False,False,False,False],[False,False,True ,False,False],[False,False,False,False,False],[False,False,False,False,False]],[[False,False,False,False,False],[False,False,False,False,False],[False,True ,True ,False,False],[False,False,False,False,False],[False,False,False,False,False]],[[False,False,False,False,False],[False,False,False,False,False],[False,False,True ,False,False],[False,False,False,False,False],[False,False,False,False,False]],[[False,False,False,False,False],[False,False,False,False,False],[False,False,False,False,False],[False,False,False,False,False],[False,False,False,False,False]] ])

		switch = {
			0:oneC,
			1:fourC,
			2:i,
			3:l,
			4:o,
			5:s,
			6:st,
			7:t
		}

		theOriginalMatrix = switch.get(shape, "Invalid Piece")
		self.shape = shape
		self.originalMatrix = theOriginalMatrix
		self.rotatedPiece = theOriginalMatrix
		self.translatedPiece = None

