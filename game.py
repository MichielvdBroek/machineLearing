import pygame
import sys
import time
import random

from pygame.locals import *
from Values import *
from character import spriteSheet
from thorns import *

class Game:

#	WindowSurface = 0
#	BackGround = 0
#	Ground = 0
#	BackGroundCorX = 0
#	GroundCorX = 0
#	GROUNDHEIGHT = 0

	def getGroundHeight(self):
		return self.GROUNDHEIGHT

	def getWindowSurface(self):
		return self.WindowSurface

	def __init__(self, PG):

		pygame = PG
		self.WindowSurface = pygame.display.set_mode((ScreenWidth, ScreenHeight))
		self.BackGround = pygame.image.load("sources/mountain.bmp").convert()
		self.Ground = pygame.image.load("sources/ground.bmp").convert()
		self.BackGroundCorX = 0
		self.GroundCorX = 0
		self.GROUNDHEIGHT = self.Ground.get_rect().height
		self.Thorns  = []
		pygame.display.set_caption('Runner')

	def moveBackGround(self):
		#movebackground 

		self.BackGroundCorX -= 5
		BackGroundRelativeX = self.BackGroundCorX % self.BackGround.get_rect().width

		#draw infinite backGround
		self.WindowSurface.blit(self.BackGround, (BackGroundRelativeX - self.BackGround.get_rect().width, 0))
		if BackGroundRelativeX < ScreenWidth:
			self.WindowSurface.blit(self.BackGround, (BackGroundRelativeX, 0))

	def moveGround(self):
		#move backGround and ground
		self.GroundCorX -= 25
		GroundRelativeX = self.GroundCorX % self.Ground.get_rect().width

		#draw infinite Ground
		self.WindowSurface.blit(self.Ground, (GroundRelativeX - self.Ground.get_rect().width, ScreenHeight - self.GROUNDHEIGHT))
		if GroundRelativeX < ScreenWidth:
			self.WindowSurface.blit(self.Ground, (GroundRelativeX, ScreenHeight - self.GROUNDHEIGHT))	

#these should be in the thorn class.
#draw should become animate.
	def spawnThorn(self):

		length = random.randint(self.GROUNDHEIGHT * 2, ScreenHeight - self.GROUNDHEIGHT * 4)
		side = length % 2
		imageLocation = "sources/Thorns.png"
		thorn = Thorn(length, side, THORNSPEED, imageLocation)
		self.Thorns.append(thorn)


	def drawThorns(self):
		for thorn in self.Thorns:
			thorn.draw(self.WindowSurface, self.GROUNDHEIGHT)
	#pygame.image.load("sources/ground.bmp").convert()

	def moveThorns(self):
		ID = 0
		for thorn in self.Thorns:
			if thorn.getPosition() > 0:
				thorn.move()
			else:
				del self.Thorns[ID]
			ID += 1

	def checkCollision(self, character):
		if character.getSize():
			a = 0

	#	def moveThorn():
		#move thorn