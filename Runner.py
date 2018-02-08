import pygame
import sys
import time
from pygame.locals import *
from Values import *
from game import *

#initialize
game = Game()
pygame.init()
game.initialize(pygame)
Clock = pygame.time.Clock()


#game loop
while True:

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	#if a key is pressed
	k = pygame.key.get_pressed()
#	if k[K_UP]:
#		FPS = 30

	game.moveBackGround()
	game.moveGround()

	pygame.display.update()
	Clock.tick(FPS)



	#TODO: collision met blokken
	#TODO: blokken spawnen
	#TODO: character laten lopen