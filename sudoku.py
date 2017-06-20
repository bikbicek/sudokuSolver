#SudokuSolver1.0 -Kryštof Kořínek 2017


import numpy as np
import sys


class Sudoku:
	def __init__(self, file = None, log = False):
		self.log = log
		if log:
			self.old_stdout = sys.stdout
			self.log_file = open("message.log","w")
			sys.stdout = self.log_file

		if file != None:
			try:
				self.fileData = file.read()
				print("File is readable")
			except:
				print("Unable to read the file!")

		else:
			print("No file was loaded. Please load a file[path]")


	def __del__(self):
		if self.log:
			sys.stdout = self.old_stdout

			self.log_file.close()
		


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
			return False
		else:
			return True


	def checkCol(self, number, index):
		sqr = int(index/3)
		col = index%3
		print("Checking column", index)
		if number in self.sudoMap[:,sqr,:,col]:
			return False
		else:
			return True


	def checkRow(self, number, index):
		Sline = int(index/3)
		line = index%3
		print("Checking row", index)
		if number in self.sudoMap[Sline,:,line,:]:
			return False
		else:
			return True


	def checkMap(self, times = 1):
		for rnd in range(times):
			col = 0
			row = 0
			sqr = 0
			lastSqr = sqr
			posibs = []
			for number in range(81):

				print("Number index: ",number,"["+str(self.sudoMap.item(number))+"]")
				print("Column:",col,"Row:",row,"Square:",sqr)
				print("Max column:",int(sqr%3)*3+2,"Max row:",int(sqr/3)*3+2)

				if self.sudoMap.item(number) == 0:
					posibNums = []
					for posib in range(1,10):
						if self.checkSqr(posib,sqr) and self.checkRow(posib,row) and self.checkCol(posib,col):
							posibNums.append(posib)
					posibs.append(posibNums)
					print("Possible numbers:",posibNums)

				else:
					posibs.append([])

				changeSqr = False
				if row == int(sqr/3)*3+2 and col == (sqr%3)*3+2:
					sqr += 1
					curIndex = 0
					newNum = 0
					print("All possible numbers:",posibs)
					for posib in posibs:
						lonely = False
						print("Current test possibles:",posib)
						if len(posib) == 0:
							curIndex += 1
							continue
						else:
							for posibNum in posib:
								newNum = posibNum
								for i in range(9):
									if i == curIndex:
										continue
									else:
										if posibNum in posibs[i]:
											lonely = False
											break
										else:
											lonely = True
								if lonely:
									self.sudoMap[int(lastSqr/3),lastSqr%3,int(curIndex/3),curIndex%3] = newNum
									print("Set number:",newNum)
									break
						curIndex += 1
					print("End index:",curIndex)
					print(self.sudoMap[int(lastSqr/3),lastSqr%3])
					posibs = []


				if row == int(lastSqr/3)*3+2 and col == (lastSqr%3)*3+2:
					row = int(sqr/3)*3
				elif col == (sqr%3)*3+2:
					row += 1

				if col == (lastSqr%3)*3+2:
					col = (sqr%3)*3
				else:
					col += 1
				lastSqr = sqr
				print("")


	def showSudo(self):
		return


file = open("sudoku.txt")
x = Sudoku(file, True)
x.formData()
x.checkMap(2)
print(x.sudoMap)

