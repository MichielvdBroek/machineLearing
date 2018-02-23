import sys
import os
import shutil

class FIO :
	def __init__(self):

		self.Path = "scores/"

	def newGame(self):
		try:
			file = open(self.Path + "FIO.txt", "r")
		except:
			file = open(self.Path + "FIO.txt", "w").close
			file = open(self.Path + "FIO.txt", "r")
		string = file.readline()
		try:
			lastgame = int(string)
		except:
			lastgame = 0
		file.close()

		file = open(self.Path + "FIO.txt", "w")
		self.currentGame = lastgame + 1
		file.write(str(self.currentGame))
		file.close

	def appendToFile(self, name, value):
		file = open(self.Path + str(self.currentGame) + name, "a")
		file.write(value)
		file.write("\n")
		file.close

	def readFromFile(self, name):
		file = open(self.Path + str(self.currentGame) + name, "r")
		val = file.read()
		close(file)
		return val

	def sortFile(self, name):
		os.rename(self.Path + str(self.currentGame) + name, "unsorted.txt")
		file = open(self.Path + "unsorted.txt", "r")
		scores = []
		for line in file:
			scores.append(int(file.readline()))

		# sort scores

		file = open(self.Path + str(self.currentGame) + name, 'w')
		file.close
		file = open(self.Path + str(self.currentGame) + name, "a")

		for score in scores:		
			file.write(score)
			file.write("\n")
		file.close

	def resetFiles(self):
		shutil.rmtree(self.Path)
		os.mkdir(self.Path)

