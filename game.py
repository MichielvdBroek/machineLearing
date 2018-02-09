import pygame
import sys
import time

from pygame.locals import *
from Values import *
from character import spriteSheet

class Game:

#	WindowSurface = 0
#	BackGround = 0
#	Ground = 0
#	BackGroundCorX = 0
#	GroundCorX = 0
#	GROUNDHEIGHT = 0

	def getGroundHeight(self):
		return self.GROUNDHEIGHT

	def __init__(self, PG):

		pygame = PG
		self.WindowSurface = pygame.display.set_mode((ScreenWidth, ScreenHight))
		self.BackGround = pygame.image.load("sources/mountain.bmp").convert()
		self.Ground = pygame.image.load("sources/ground.bmp").convert()
		self.BackGroundCorX = 0
		self.GroundCorX = 0
		self.GROUNDHEIGHT = self.Ground.get_rect().height
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
		self.WindowSurface.blit(self.Ground, (GroundRelativeX - self.Ground.get_rect().width, ScreenHight - self.GROUNDHEIGHT))
		if GroundRelativeX < ScreenWidth:
			self.WindowSurface.blit(self.Ground, (GroundRelativeX, ScreenHight - self.GROUNDHEIGHT))	

	def drawCharacter(self, Character, animationStart, animationLength):
		action = Character.getCharacterState()
		timeInAction = Character.getTimeInAction()

		if action == RUNNING:
			Character.draw(self.WindowSurface, timeInAction % animationLength + animationStart, Character.getPlayer() * 30 + 100, ScreenHight - self.GROUNDHEIGHT, (0,0))
		elif action == JUMPINGUP or action == JUMPINGDOWN:
			Character.draw(self.WindowSurface, timeInAction % animationLength + animationStart, Character.getPlayer() * 30 + 100, ScreenHight - self.GROUNDHEIGHT, (0,0))