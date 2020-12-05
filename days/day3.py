from util import file


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
	treeRows = []

	def __init__(self):
		self.test()
		self.setTreeRows()

	def setTreeRows(self, array=None):
		self.treeRows = []
		if not array:
			array = file.fileToArray(fileLocation='./inputs/inputday3')
		for line in array:
			self.treeRows.append(TreeRow(line))

	def calculate(self, dy, dx):
		trees = 0
		rows = len(self.treeRows)
		y = 0
		x = 1
		while rows > y:
			y += dy
			x += dx
			try:
				if self.treeRows[y].isTreeAtPosition(x):
					trees += 1
			except IndexError:
				break
		return trees

	def test(self):
		example = [
			"..##.......",
			"#...#...#..",
			".#....#..#.",
			"..#.#...#.#",
			".#...##..#.",
			"..#.##.....",
			".#.#.#....#",
			".#........#",
			"#.##...#...",
			"#...##....#",
			".#..#...#.#",
		]
		self.setTreeRows(example)
		trees = self.calculate(1, 3)
		if trees == 7:
			print("Day 3 - test: \033[32msuccess\033[0m")
		else:
			print('Day 3 test: \033[31failed\033[0m')
			print('Received: {}'.format(trees))

	def part1(self):
		trees = self.calculate(1, 3)
		print('Day 3 - part 1 result: {}'.format(trees))

	def part2(self):
		slopes = [[1, 1], [1, 3], [1, 5], [1, 7], [2, 1]]
		trees = None
		for dy, dx in slopes:
			if trees is None:
				trees = self.calculate(dy, dx)
				continue
			trees *= self.calculate(dy, dx)

		print('Day 3 - part 2 result: {}'.format(trees))
