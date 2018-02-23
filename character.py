from pygame.locals import *
from characterStates import *
from Values import ScreenHeight

class spriteSheet:
	def __init__(self, PG, filename, coloms, rows, playerNr, runningHeight):
		#coloms = 8
		#rows = 0
		pygame = PG

		self.Alive = True
		self.JumpOffset = 0
		self.RunningStart = 0
		self.RunningLength = 0
		self.JumpingUpStart = 0
		self.JumpingUpLength = 0
		self.JumpingDownStart = 0
		self.JumpingDownLength = 0
		
		self.PlayerNr = playerNr
		self.Sheet = pygame.image.load(filename).convert_alpha()
		self.Coloms = coloms
		self.Rows = rows
		self.CellCount = self.Coloms * self.Rows
		self.SheetPixSize = self.Sheet.get_rect()
		self.TimeInAction = 0
		self.State = RUNNING

		self.CellWidth = self.SheetPixSize.width / self.Coloms
		self.CellHeight = self.SheetPixSize.height / self.Rows

		self.x = 300 - self.PlayerNr * 30
		self.y = ScreenHeight - runningHeight
		self.Cells = list([(index %self. Coloms * self.CellWidth, index / self.Coloms * self.CellHeight, self.CellWidth, self.CellHeight) for index in range(self.CellCount)])

	def getSize(self):
		return self.Sheet.get_rect()

#	def getPosition(self):
#		return 

	def setAnimationStart(self, state, start):
		if state == RUNNING:
			self.RunningStart = start
		elif state == JUMPINGUP:
			self.JumpingUpStart = start
		elif state == JUMPINGDOWN:
			self.JumpingDownStart = start

	def getAnimationStart(self):
		if self.State == RUNNING:
			return self.RunningStart
		elif self.State == JUMPINGUP:
			return self.JumpingUpStart
		elif self.State == JUMPINGDOWN:
			return self.JumpingDownStart

	def setAnimationLength(self, state, length):
		if state == RUNNING:
			self.RunningLength = length
		elif state == JUMPINGUP:
			self.JumpingUpLength = length
		elif state == JUMPINGDOWN:
			self.JumpingDownLength = length


	def getAnimationLength(self):
		if self.State == RUNNING:
			return self.RunningLength
		elif self.State == JUMPINGUP:
			return self.JumpingUpLength
		elif self.State == JUMPINGDOWN:
			return self.JumpingDownLength


	def animateCharacter(self, windowSurface):

		if self.State == RUNNING:
			self.draw(windowSurface, self.TimeInAction % self.getAnimationLength() + self.getAnimationStart(), (0,0))
		elif self.State == JUMPINGUP or self.State == JUMPINGDOWN:
			self.draw(windowSurface, self.TimeInAction % self.getAnimationLength() + self.getAnimationStart(), (0,0))


	def draw(self, surface, spriteNr, offset):

		self.TimeInAction += 1
		surface.blit(self.Sheet, (self.x + offset[0], self.y + offset[1] - self.JumpOffset - self.CellHeight), self.Cells[spriteNr])

	def getCollission(self):
		collission = []
		#bottom left point of character image
		collission.append(self.x) 
		collission.append(self.y - self.JumpOffset - self.CellHeight)
		#bottom right point of character image 
		collission.append(self.x + (self.CellWidth))
		collission.append(self.y - (self.CellHeight) - self.JumpOffset - self.CellHeight)
		return collission

	def getPlayer(self):
		return self.PlayerNr

	def resetTimeInAction(self):
		self.TimeInAction = 0

	def getTimeInAction(self):
		return self.TimeInAction

	def setCharacterState(self, state):
		self.State = state

	def getCharacterState(self):
		return self.State


	def jump(self):
		if self.State == JUMPINGUP:
			self.JumpOffset += 35 - self.JumpOffset * 30 / JUMPHEIGHT

		if self.State == JUMPINGDOWN:
			self.JumpOffset -= 35  - self.JumpOffset * 30 / JUMPHEIGHT

		if self.JumpOffset < 0:
			self.JumpOffset = 0

	def jumpPressed(self):
		if self.JumpOffset < JUMPHEIGHT and self.State != JUMPINGDOWN:
			self.State = JUMPINGUP

		elif self.JumpOffset >= JUMPHEIGHT:
			self.State = JUMPINGDOWN

		if self.JumpOffset <= 0 and self.State == JUMPINGDOWN:
			self.State = RUNNING

		self.jump()

	def jumpNotPressed(self):
		if self.JumpOffset > 0:
			self.State = JUMPINGDOWN
		else:
			self.State = RUNNING

		self.jump()

	def getAlive(self):
		return self.Alive

	def Die(self):
		self.Alive = False