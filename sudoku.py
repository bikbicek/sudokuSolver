#Sudoku -Kryštof Kořínek 2017

import numpy as np
import matplotlib.pyplot as plt


class Sudoku:
	def __init__(self, file = None):
		if file != None:
			try:
				self.fileData = file.read()
				print("File is readable")
			except:
				print("Unable to read the file!")

		else:
			print("No file was loaded. Please load a file[path]")
		


	def formData(self):
		print("Starting formating data")

		l = self.fileData.splitlines()

		if len(l) != 9:
			print("Invalid number of lines")
			return False
		for line in l:
			if len(line) != 9:
				print("Invalid line",line)
				return False

		counter = 0
		intList = []
		nums = "123456789"
		for line in l:
			newLine = ""
			for char in range(9):
				if not line[char] in nums:
					newLine += "0"
					counter += 1
				else:
					newLine += line[char]
			intList.append(newLine)
		l = intList
		print(l)


		bigLines = [list(l[0:3]),list(l[3:6]),list(l[6:9])]
		newList = []
		for bl in bigLines:
			for i in range(0,9,3):
				for line in bl:
					newList.append(list(line[i:i+3]))

		self.sudoMap = np.array(newList).reshape(3,3,3,3).astype(np.int)

		print("Formating done! Number of variables",counter)

		return True


	def checkSqr(self, number, index):
		line = int(index/3)
		sqr = index%3
		print("Checking square line",line,"square",sqr)
		if number in self.sudoMap[line,sqr]:
			return True
		else:
			return False


	def checkCol(self, number, index):
		sqr = int(index/3)
		col = index%3
		print("Checking column", index)
		if number in self.sudoMap[:,sqr,:,col]:
			return True
		else:
			return False


	def checkRow(self, number, index):
		Sline = int(index/3)
		line = index%3
		print("Checking row", index)
		if number in self.sudoMap[Sline,:,line,:]:
			return True
		else:
			return False


	def showSudo(self):
		return


file = open("sudoku.txt")
x = Sudoku(file)
x.formData()
print(x.checkRow(5,8))