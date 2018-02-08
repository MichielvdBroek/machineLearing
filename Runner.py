import pygame
import sys
import time
from pygame.locals import *
from Values import *

pygame.init()

WindowSurface = pygame.display.set_mode((ScreenWidth, ScreenHight))
BackGround = pygame.image.load("sources/mountain.bmp").convert()
Ground = pygame.image.load("sources/ground.bmp").convert()
BackGroundCorX = 0
GroundCorX = 0
GROUNDHEIGHT = Ground.get_rect().height
pygame.display.set_caption('Runner')
Clock = pygame.time.Clock()


#game loop
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	#if a key is pressed
	k = pygame.key.get_pressed() 


	#move backGround and ground
	BackGroundCorX -= 1
	GroundCorX -= 5
	BackGroundRelativeX = BackGroundCorX % BackGround.get_rect().width
	GroundRelativeX = GroundCorX % Ground.get_rect().width

	#draw infinite backGround
	WindowSurface.blit(BackGround, (BackGroundRelativeX - BackGround.get_rect().width, 0))
	if BackGroundRelativeX < ScreenWidth:
		WindowSurface.blit(BackGround, (BackGroundRelativeX, 0))

	#draw infinite Ground
	WindowSurface.blit(Ground, (GroundRelativeX - Ground.get_rect().width, ScreenHight - GROUNDHEIGHT))
	if GroundRelativeX < ScreenWidth:
		WindowSurface.blit(Ground, (GroundRelativeX, ScreenHight - GROUNDHEIGHT))	

	
	pygame.display.update()
	Clock.tick(FPS)



	#TODO: collision met blokken
	#TODO: blokken spawnen
	#TODO: character laten lopen