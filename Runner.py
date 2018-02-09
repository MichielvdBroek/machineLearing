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
character2 = spriteSheet(pygame, "sources/mario.png", 5, 1, 2)
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
	game.drawCharacter(character1, 0, 8)
	game.drawCharacter(character2, 0, 5)

	pygame.display.update()
	Clock.tick(FPS)
	SCORE += 1



	#TODO: collision met blokken
	#TODO: blokken spawnen
	#TODO: character laten lopen