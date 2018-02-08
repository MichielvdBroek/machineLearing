import pygame
import sys
import time
from pygame.locals import *
from Values import *

class Game:

#	WindowSurface = 0
#	BackGround = 0
#	Ground = 0
#	BackGroundCorX = 0
#	GroundCorX = 0
#	GROUNDHEIGHT = 0

	def getGroundHeight(this):
		global GROUNDHEIGHT
		return GROUNDHEIGHT

	def initialize(this, PG):
		global WindowSurface 
		global BackGround
		global Ground
		global BackGroundCorX
		global GroundCorX
		global GROUNDHEIGHT

		pygame = PG
		WindowSurface = pygame.display.set_mode((ScreenWidth, ScreenHight))
		BackGround = pygame.image.load("sources/mountain.bmp").convert()
		Ground = pygame.image.load("sources/ground.bmp").convert()
		BackGroundCorX = 0
		GroundCorX = 0
		GROUNDHEIGHT = Ground.get_rect().height
		pygame.display.set_caption('Runner')

	def moveBackGround(this):
		#movebackground 
		global WindowSurface
		global BackGround
		global BackGroundCorX

		BackGroundCorX -= 1
		BackGroundRelativeX = BackGroundCorX % BackGround.get_rect().width

		#draw infinite backGround
		WindowSurface.blit(BackGround, (BackGroundRelativeX - BackGround.get_rect().width, 0))
		if BackGroundRelativeX < ScreenWidth:
			WindowSurface.blit(BackGround, (BackGroundRelativeX, 0))

	def moveGround(this):
		#move backGround and ground
		global WindowSurface
		global Ground
		global GroundCorX

		GroundCorX -= 5
		GroundRelativeX = GroundCorX % Ground.get_rect().width

		#draw infinite Ground
		WindowSurface.blit(Ground, (GroundRelativeX - Ground.get_rect().width, ScreenHight - GROUNDHEIGHT))
		if GroundRelativeX < ScreenWidth:
			WindowSurface.blit(Ground, (GroundRelativeX, ScreenHight - GROUNDHEIGHT))	
