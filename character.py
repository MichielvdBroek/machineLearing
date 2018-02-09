from pygame.locals import *
from Values import RUNNING, JUMPINGUP, JUMPINGDOWN, JUMPHEIGHT

class spriteSheet:
	def __init__(self, PG, filename, coloms, rows, playerNr):
		#coloms = 8
		#rows = 0
		pygame = PG

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

		self.Cells = list([(index %self. Coloms * self.CellWidth, index / self.Coloms * self.CellHeight, self.CellWidth, self.CellHeight) for index in range(self.CellCount)])

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


	def draw(self, surface, spriteNr, x, y, offset = (0,0)):

		self.TimeInAction += 1
		surface.blit(self.Sheet, (x + offset[0], y + offset[1] - self.JumpOffset - self.CellHeight), self.Cells[spriteNr])

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