from pygame.locals import *

class spriteSheet:
	def __init__(self, PG, filename, coloms, rows):
		#coloms = 8
		#rows = 0
		pygame = PG
		
		self.Sheet = pygame.image.load(filename).convert_alpha()
		self.Coloms = coloms
		self.Rows = rows
		self.CellCount = self.Coloms * self.Rows
		self.SheetPixSize = self.Sheet.get_rect()
		self.TimeInAction = 0

		self.CellWidth = self.SheetPixSize.width / self.Coloms
		self.CellHeight = self.SheetPixSize.height / self.Rows

		self.Cells = list([(index %self. Coloms * self.CellWidth, index / self.Coloms * self.CellHeight, self.CellWidth, self.CellHeight) for index in range(self.CellCount)])

	def draw(self, surface, spriteNr, x, y, offset = (0,0)):

		self.TimeInAction += 1
		surface.blit(self.Sheet, (x + offset[0], y + offset[1] - self.CellHeight), self.Cells[spriteNr])

	def resetTimeInAction(self):
		self.TimeInAction = 0

	def getTimeInAction(self):
		return self.TimeInAction