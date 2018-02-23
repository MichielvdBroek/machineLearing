import pygame
import sys
import time

from pygame.locals import *
from Values import *
from game import *
import character

endProgram = False
while (endProgram == False):
	#initialize
	pygame.init()
	game = Game(pygame)
	characterNr = 0
	Score = INITIALSCORE

	characterNr += 1
	character1 = spriteSheet(pygame, "sources/kirby.png", 8, 1, characterNr, game.getGroundHeight())
	character1.setAnimationStart(RUNNING, 0)
	character1.setAnimationLength(RUNNING, 8)
	character1.setAnimationStart(JUMPINGUP, 7)
	character1.setAnimationLength(JUMPINGUP, 1)
	character1.setAnimationStart(JUMPINGDOWN, 7)
	character1.setAnimationLength(JUMPINGDOWN, 1)

	characterNr += 1
	character2 = spriteSheet(pygame, "sources/kirby.png", 8, 1, characterNr, game.getGroundHeight())
	character2.setAnimationStart(RUNNING, 0)
	character2.setAnimationLength(RUNNING, 8)
	character2.setAnimationStart(JUMPINGUP, 7)
	character2.setAnimationLength(JUMPINGUP, 1)
	character2.setAnimationStart(JUMPINGDOWN, 7)
	character2.setAnimationLength(JUMPINGDOWN, 1)

	characterNr += 1
	character3 = spriteSheet(pygame, "sources/mario.png", 5, 1, characterNr, game.getGroundHeight())
	character3.setAnimationStart(RUNNING, 0)
	character3.setAnimationLength(RUNNING, 5)
	character3.setAnimationStart(JUMPINGUP, 4)
	character3.setAnimationLength(JUMPINGUP, 1)
	character3.setAnimationStart(JUMPINGDOWN, 4)
	character3.setAnimationLength(JUMPINGDOWN, 1)

	Clock = pygame.time.Clock()
	GameTicks = 0

	#game loop
	gameRunning = True
	while gameRunning:
		endGame = False


		for event in pygame.event.get():
			if event.type == QUIT:
				endGame = True
				endProgram = True

		if GameTicks % 25 == 0:
			game.spawnThorn()
		
		game.moveBackGround()
		game.moveGround()
		game.moveThorns()
		game.drawThorns()

		#if a key is pressed
		k = pygame.key.get_pressed()
		if k[K_UP]:
			character1.jumpPressed()
		else :
			character1.jumpNotPressed()
		if k[K_w]:
			character2.jumpPressed()
		else:
			character2.jumpNotPressed()

		charactersAlive = False

		if (character1.getAlive()):
			charactersAlive = True
			character1.animateCharacter(game.getWindowSurface())
			if game.checkCollision(character1):
				character1.Die()
				#save Score

		if (character2.getAlive()):
			charactersAlive = True
			character2.animateCharacter(game.getWindowSurface())
			if game.checkCollision(character2):
				character2.Die()
				#save Score

		if (character3.getAlive()):
			charactersAlive = True
			character3.animateCharacter(game.getWindowSurface())
			if game.checkCollision(character3):
				character3.Die()
				#save Score


		if (charactersAlive == False):
			endGame = True

		if endGame:
			gameRunning = False

		pygame.display.update()
		Clock.tick(FPS)
		GameTicks += 1
		Score += 1

pygame.quit()
sys.exit()

