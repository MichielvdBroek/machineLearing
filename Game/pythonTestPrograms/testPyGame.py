import pygame
import sys
import time
from pygame.locals import *

# set up pygame
pygame.init()

# set up the window
windowSurface = pygame.display.set_mode((1800, 400), 0, 32)
pygame.display.set_caption('Hello world!')

# set up the colors
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
RED = [255, 0, 0]
GREEN = [0, 255, 0]
BLUE = [0, 0, 255]
COLORS = [BLACK, WHITE, RED, GREEN, BLUE]

# set up fonts
basicFont = pygame.font.SysFont(None, 48)

# set up the text
text = basicFont.render('press alt+f4 to close', True, BLACK, WHITE)
textRect = text.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery

# draw the window onto the screen
pygame.display.update()

# run the game loop
i = 0
intervalTime = time.time()

del COLORS[4]
del COLORS[3]
del COLORS[2]
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	if time.time() > intervalTime:
		intervalTime = time.time() + 0.4
		printingColor = (COLORS[i][0], COLORS[i][1], COLORS[i][2])
		text = basicFont.render('background color is ' + str(COLORS[i][0]) + ':' + str(COLORS[i][2]) + ':' + str(COLORS[i][2]), True, COLORS[i% 2], COLORS[ 1 -(i % 2)])		
		windowSurface.fill(printingColor)
		windowSurface.blit(text, textRect)
		i += 1

		if i == len(COLORS):
			
			if BLACK[0] <= 245:
				BLACK[0] += 10
			else: BLACK[0] = 0
			
			if BLACK[1] <= 245:
				BLACK[1] += 10
			else: BLACK[1] = 0
			
			if BLACK[2] <= 245:
				BLACK[2] += 10
			else: BLACK[2] = 0

			if WHITE[0] >= 10:
				WHITE[0] -= 10
			else: WHITE[0] = 255
			
			if WHITE[1] >= 10:
				WHITE[1] -= 10
			else: WHITE[1] = 255
			
			if WHITE[2] >= 10:
				WHITE[2] -= 10
			else: WHITE[2] = 255

			i = 0

		pygame.display.update()