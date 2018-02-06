import pygame
import sys
import time
from pygame.locals import *

# set up pygame
pygame.init()

# set up the window
windowSurface = pygame.display.set_mode((500, 400), 0, 32)
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
text = basicFont.render('press alt+f4 to close', True, WHITE, BLUE)
textRect = text.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery

# draw the window onto the screen
pygame.display.update()

# run the game loop
i = 0
intervalTime = time.time()
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	if time.time() > intervalTime:
		intervalTime = time.time() + 1
		printingColor = (COLORS[i][0], COLORS[i][1], COLORS[i][2])
		windowSurface.fill(printingColor)
		i += 1
		if i > 4:
			windowSurface.blit(text, textRect)
			BLACK[0] += 10
			BLACK[1] += 10
			BLACK[2] += 10
			i = 0

		pygame.display.update()