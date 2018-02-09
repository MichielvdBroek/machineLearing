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
character1 = spriteSheet(pygame, "sources/mario.png", 5, 1)
character2 = spriteSheet(pygame, "sources/kirby.bmp", 8, 1)
Clock = pygame.time.Clock()


#game loop
while True:

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	#if a key is pressed
	k = pygame.key.get_pressed()
	if k[K_UP]:
		print("pressed up")

	game.moveBackGround()
	game.moveGround()

	game.drawCharacter(character1, RUNNING, character1.getTimeInAction(), 5)
	#game.drawCharacter(character2, RUNNING, character1.getTimeInAction(), 8)

	pygame.display.update()
	Clock.tick(FPS)
	SCORE += 1
	print(SCORE)



	#TODO: collision met blokken
	#TODO: blokken spawnen
	#TODO: character laten lopen