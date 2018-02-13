import pygame
import sys
import time

from pygame.locals import *
from Values import *
from game import *
import character


#initialize
pygame.init()
game = Game(pygame)

character1 = spriteSheet(pygame, "sources/kirby.png", 8, 1, 1)
character1.setAnimationStart(RUNNING, 0)
character1.setAnimationLength(RUNNING, 8)
character1.setAnimationStart(JUMPINGUP, 7)
character1.setAnimationLength(JUMPINGUP, 1)
character1.setAnimationStart(JUMPINGDOWN, 7)
character1.setAnimationLength(JUMPINGDOWN, 1)

character2 = spriteSheet(pygame, "sources/mario.png", 5, 1, 2)
character2.setAnimationStart(RUNNING, 0)
character2.setAnimationLength(RUNNING, 5)
character2.setAnimationStart(JUMPINGUP, 4)
character2.setAnimationLength(JUMPINGUP, 1)
character2.setAnimationStart(JUMPINGDOWN, 4)
character2.setAnimationLength(JUMPINGDOWN, 1)

Clock = pygame.time.Clock()


#game loop
while True:

	for event in pygame.event.get():
		if event.type == QUIT:
			print(SCORE)
			pygame.quit()
			sys.exit()

	#if a key is pressed
	k = pygame.key.get_pressed()
	if k[K_UP]:
		character1.jumpPressed()
	else :
		character1.jumpNotPressed()

	game.moveBackGround()
	game.moveGround()

	#draw Running
	character1.animateCharacter(game.getWindowSurface(), ScreenHeight - game.getGroundHeight())
	character2.animateCharacter(game.getWindowSurface(), ScreenHeight - game.getGroundHeight())


	game.moveThorns()
	game.spawnThorn()
	game.moveThorns()

	pygame.display.update()
	Clock.tick(FPS)
	SCORE += 1



	#TODO: collision met blokken
	#TODO: blokken spawnen
	#TODO: character laten lopen