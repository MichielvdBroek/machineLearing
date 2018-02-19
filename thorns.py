import pygame

from pygame.locals import *
from Values import ScreenWidth, ScreenHeight

class Thorn:
	def __init__(self, length, side, speed, imageLocation):
		self.Position = ScreenWidth
		self.Length = length
		self.Speed = speed
		self.Side = side
		self.Thorn = pygame.image.load(imageLocation).convert_alpha()
		self.Thorn = pygame.transform.scale(self.Thorn, (length, length))

		if self.Side:
			self.Thorn = pygame.transform.flip(self.Thorn, 0, 1)

	def getLength(self):
		return self.Length

	def getSide(self):
		return self.Side

	def getPosition(self):
		return self.Position

	def move(self):
		self.Position -= self.Speed 

	def draw(self, WindowSurface, groundHeight):
		if self.Side:
			WindowSurface.blit(self.Thorn, (self.Position, 0))
		else:
			WindowSurface.blit(self.Thorn, (self.Position, ScreenHeight - groundHeight - self.Thorn.get_rect().height))


	#def drawThorn(self, windowSurface):
