import pygame
import sys
import time

from pygame.locals import *
from Settings import *
from game import *
import character
from fileIO import *


pygame.init()
fileIO = FIO()
if (RESETFILESONBOOT):
		fileIO.resetFiles()

endProgram = False
gameRunning = True

while (endProgram == False):

	#initialize
	game = Game(pygame)
	
	characterNr = 0
	characters = []
	Score = INITIALSCORE

	playerCount = PLAYERS
	if (playerCount > 2):
		playerCount = 2

	npcCount = NPCS
	if (npcCount > 10):
		npcCount = 10
	
	while (playerCount > 0):
		characterNr += 1
		player = Character(pygame, "sources/kirby.png", 8, 1, characterNr, game.getGroundHeight(), True)
		player.setAnimationStart(RUNNING, 0)
		player.setAnimationLength(RUNNING, 8)
		player.setAnimationStart(JUMPINGUP, 7)
		player.setAnimationLength(JUMPINGUP, 1)
		player.setAnimationStart(JUMPINGDOWN, 7)
		player.setAnimationLength(JUMPINGDOWN, 1)
		characters.append(player)
		playerCount -= 1

	while(npcCount  > 0):
		characterNr += 1
		character = Character(pygame, "sources/mario.png", 5, 1, characterNr, game.getGroundHeight(), False)
		character.setAnimationStart(RUNNING, 0)
		character.setAnimationLength(RUNNING, 5)
		character.setAnimationStart(JUMPINGUP, 4)
		character.setAnimationLength(JUMPINGUP, 1)
		character.setAnimationStart(JUMPINGDOWN, 4)
		character.setAnimationLength(JUMPINGDOWN, 1)
		characters.append(character)
		npcCount -= 1

	Clock = pygame.time.Clock()
	GameTicks = 0

	k = pygame.key.get_pressed()
	if (k[K_SPACE]):
		gameRunning = True


	for event in pygame.event.get():
		if (event.type == QUIT):
			endProgram = True
	if (gameRunning):
		fileIO.newGame()
	#game loop
	while (gameRunning):
		endGame = False
		gameSpeed = FPS + Score / SPEEDUPDISTANCE
		if gameSpeed >= MAXSPEED:
			gameSpeed = MAXSPEED

		for event in pygame.event.get():
			if (event.type == QUIT):
				endGame = True
				endProgram = True

		if (GameTicks % THORNDISTANCE == 0):
			game.spawnThorn()
		
		game.moveBackGround()
		game.moveGround()
		game.moveThorns()
		game.drawThorns()

		#if a key is pressed
		k = pygame.key.get_pressed()
		if (PLAYERS >= 1):
			if (k[K_UP]):
				characters[0].jumpPressed()
			else :
				characters[0].jumpNotPressed()
		if (PLAYERS >= 2):
			if (k[K_w]):
				characters[1].jumpPressed()
			else:
				characters[1].jumpNotPressed()

		charactersAlive = False
		for character in characters:

			if (character.getAlive()):
				charactersAlive = True
				character.animateCharacter(game.getWindowSurface())
				if (game.checkCollision(character)):
					character.die()
					if (character.getIsPlayer()):
						fileIO.appendToFile("playerscores.txt", character.getCharacterString(Score))
					else:
						fileIO.appendToFile("AIscore.txt", character.getCharacterString(Score))
					#save Score

		if (charactersAlive == False):
			endGame = True

		if (endGame):
			gameRunning = False

		pygame.display.update()
		Clock.tick(gameSpeed)
		GameTicks += 1
		Score += 1

	gameRunning = AUTORESTART

pygame.quit()
sys.exit()

