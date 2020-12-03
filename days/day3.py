from util import fileUtil


class TreeRow:
	spots = []

	def __init__(self, row):
		self.spots = list(row)

	def getSpotLength(self):
		return len(self.spots)

	def getSpotPosition(self, x):
		return self.spots[(x % self.getSpotLength()) - 1]

	def isTreeAtPosition(self, x):
		char = self.getSpotPosition(x)
		if char == '#':
			return True
		return False


class Day3:
	inputArray = []
	treeRows = []

	def __init__(self):
		self.setTreeRows()

	def setTreeRows(self):
		self.inputArray = fileUtil.returnArrayOfLinesForOfFile(fileLocation='./inputs/inputday3')
		for line in self.inputArray:
			self.treeRows.append(TreeRow(line))

	def calculate(self, dy, dx):
		count = 0
		rows = len(self.treeRows)
		y = 0
		x = 1
		while rows > y:
			y += dy
			x += dx
			try:
				if self.treeRows[y].isTreeAtPosition(x):
					count += 1
			except IndexError:
				break
		return count

	def part1(self):
		count = self.calculate(1, 3)
		print('Amount of Trees found default pattern')
		print(count)

	def part2(self):
		slopes = [[1, 1], [1, 3], [1, 5], [1, 7], [2, 1]]
		count = None
		for slope in slopes:
			if count is None:
				count = self.calculate(slope[0], slope[1])
				continue
			count *= self.calculate(slope[0], slope[1])

		print('Amount of Trees found with other patterns')
		print(count)
