import numpy as np

#Piece that holds the 3D matrix of the current piece
class Piece:

	def getPiece(self):
		return self.type

	def setPiece(self, type):
		self.type = type
		
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

		theType = switch.get(shape, "Invalid Piece")
		self.type = theType

