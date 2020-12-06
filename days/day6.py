from util import file


class AnswerGroup:
	lines = []
	uniqueChars = []
	chars = []
	personsWithChars = []

	def __init__(self):
		self.lines = []
		self.uniqueChars = []
		self.chars = []
		self.personsWithChars = []

	def addLine(self, line):
		self.lines.append(line)
		charsInLine = list(line)
		self.personsWithChars.append(charsInLine)

		for char in charsInLine:
			if char not in self.uniqueChars:
				self.uniqueChars.append(char)
			self.chars.append(char)

	def getNumberOfUniqueChars(self):
		return len(self.uniqueChars)

	# @TODO can probably be optimized
	def getNumberOfYesOnAll(self):
		count = 0
		for char in self.uniqueChars:
			allYes = True

			for personChars in self.personsWithChars:
				if char not in personChars:
					allYes = False
					break

			if allYes:
				count += 1

		return count



class Day6:
	input = []
	anwerGroups = []
	amountOfYes = 0
	amountOfAllYes = 0

	def __init__(self):
		self.test()
		self.loadInput()

	def test(self):
		examples = [
			"abc",
			"",
			"a",
			"b",
			"c",
			"",
			"ab",
			"ac",
			"",
			"a",
			"a",
			"a",
			"a",
			"",
			"b",
		]

		self.loadInput(examples)

		if self.amountOfYes != 11:
			print('Day 6 test: \033[31mfailed\033[0m')
			print('Received: {}'.format(self.amountOfYes))
		if self.amountOfAllYes != 6:
			print('Day 6 test: \033[31mfailed\033[0m')
			print('Received: {}'.format(self.amountOfAllYes))
		else:
			print("Day 6 - test: \033[32msuccess\033[0m")

	def loadInput(self, array=None):
		self.input = []
		if not array:
			array = file.fileToArray(fileLocation='./inputs/inputday6')
		self.input = array
		self.process()

	def process(self):
		self.anwerGroups = []
		self.amountOfYes = 0
		self.amountOfAllYes = 0

		answerGroup = AnswerGroup()

		for line in self.input:
			if line == "":
				self.calcAndPushGroup(answerGroup)
				answerGroup = AnswerGroup()
				continue

			answerGroup.addLine(line)

		self.calcAndPushGroup(answerGroup)

	def calcAndPushGroup(self, answerGroup):
		self.amountOfYes += answerGroup.getNumberOfUniqueChars()
		self.amountOfAllYes += answerGroup.getNumberOfYesOnAll()
		self.anwerGroups.append(answerGroup)

	def part1(self):
		print('Day 6 - part 1 result: {}'.format(self.amountOfYes))

	def part2(self):
		print('Day 6 - part 2 result: {}'.format(self.amountOfAllYes))
