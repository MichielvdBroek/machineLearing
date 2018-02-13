from pygame.locals import *
from Values import ScreenWidth

class Thorn:
	def __init__(self, length, side, speed, imageLocation):
		self.Position = ScreenWidth
		self.Length = length
		self.Speed = speed
		self.Side = side

	def getLength(self):
		return self.Length

	def getSide(self):
		return self.Side

	def getPosition(self):
		return self.Position

	def moveThorn(self):
		self.Position -= self.Speed 

	#def drawThorn(self, windowSerface):
