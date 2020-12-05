from util import file
import math


class BoardingPass:
	string = ''

	def __init__(self, string):
		self.row = [0, 127]
		self.column = [0, 7]
		self.string = string
		self.findLocation()

	def getColumn(self):
		return self.column[0]

	def getRow(self):
		return self.row[0]

	def getID(self):
		return self.getRow() * 8 + self.getColumn()

	def findLocation(self):
		chars = list(self.string)
		for char in chars:
			self.processChar(char)

	# @TODO can be done prettier and more efficient
	def processChar(self, char):
		middleY = (self.row[0] + self.row[1]) / 2
		middleX = (self.column[0] + self.column[1]) / 2
		if char == 'F':
			self.row[1] = math.floor(middleY)
			return
		if char == 'B':
			self.row[0] = math.ceil(middleY)
			return
		if char == 'L':
			self.column[1] = math.floor(middleX)
			return
		if char == 'R':
			self.column[0] = math.ceil(middleX)
			return


class Day5:
	highestID = 0
	boardingPasses = []
	seatIDs = []

	def __init__(self):
		self.test()
		self.loadBoardingPasses()

	def loadBoardingPasses(self):
		self.boardingPasses = []
		self.highestID = 0
		array = file.fileToArray(fileLocation='./inputs/inputday5')
		self.proccessBoardingPasses(array)

	def proccessBoardingPasses(self, array):
		for line in array:
			boardingPass = BoardingPass(line)
			self.boardingPasses.append(boardingPass)
			self.seatIDs.append(boardingPass.getID())
			if boardingPass.getID() >= self.highestID:
				self.highestID = boardingPass.getID()

	def test(self):
		examples =[
			"BFFFBBFRRR",
			"FFFBBBFRRR",
			"BBFFBBFRLL",
		]

		results = []
		for example in examples:
			boardpass = BoardingPass(example)
			results.append([boardpass.getRow(), boardpass.getColumn(), boardpass.getID()])

		correctResults = [
			[70, 7, 567],
			[14, 7, 119],
			[102, 4, 820]
		]

		for i in range(0, len(results)):
			if results[i][0] != correctResults[i][0] or results[i][1] != correctResults[i][1] or results[i][2] != correctResults[i][2]:
				print('Day 5 test: \033[31failed\033[0m')
				print('Received: {}'.format(results[i]))

		print("Day 5 - test: \033[32msuccess\033[0m")


	def part1(self):
		print('Day 5 - part 1 result: {}'.format(self.highestID))

	# @TODO can be done prettier and more efficient
	def part2(self):
		prevId = 8
		found = False
		id = 0
		for row in range(1,127):
			if found:
				break
			for column in range(1,7):
				if found:
					break
				id = row * 8 + column
				if id not in self.seatIDs:
					if prevId + 1 == id or prevId + 3 == id:
						prevId = id
						continue
					found = True
		print('Day 5 - part 2 result: {}'.format(id))






