import pygame

from pygame.locals import *
from Settings import ScreenWidth, ScreenHeight

class Thorn:
	def __init__(self, length, side, speed, imageLocation, groundHeight):
		self.Position = ScreenWidth
		self.Length = length
		self.Speed = speed
		self.Side = side
		self.Thorn = pygame.image.load(imageLocation).convert_alpha()
		self.Thorn = pygame.transform.scale(self.Thorn, (length, length))
		self.y = 0

		if self.Side:
			self.Thorn = pygame.transform.flip(self.Thorn, 0, 1)
		else :
			self.y = ScreenHeight - groundHeight  - self.Thorn.get_rect().height

	def getLength(self):
		return self.Length

	def getSide(self):
		return self.Side

	def getPosition(self):
		return self.Position

	def move(self):
		self.Position -= self.Speed 

	def draw(self, WindowSurface):
		if self.Side:
			WindowSurface.blit(self.Thorn, (self.Position, self.y))
		else:
			WindowSurface.blit(self.Thorn, (self.Position, self.y))

	def animate(self, WindowSurface):
		self.draw(WindowSurface)

	def getCollission(self):
		collission = []
		collission.append(self.Position)
		collission.append(self.y )
		collission.append(self.Position + self.Thorn.get_rect().width)
		collission.append(self.y + self.Thorn.get_rect().height)
		return collission
	#def drawThorn(self, windowSurface):
