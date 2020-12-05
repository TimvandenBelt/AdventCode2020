from util import file


class DayObject:
	line = ""

	def __init__(self, line):
		self.line = line


class Day:
	input = []
	objects = []

	def __init__(self):
		self.test()
		self.loadInput()

	def test(self):
		examples = [
			"",
		]

		self.loadInput(examples)

		if range(0, 1):
			print("Day x - test: \033[32msuccess\033[0m")
		else:
			print('Day x test: \033[31failed\033[0m')
			print('Received: {}'.format(input))

	def loadInput(self, array=None):
		self.input = []
		if not array:
			array = file.fileToArray(fileLocation='./inputs/inputday3')
		self.input = array
		self.process()

	def process(self):
		self.objects = []
		for line in self.input:
			dayObject = DayObject(line)
			self.objects.append(dayObject)

	def part1(self):
		print('Day x - part 1 result: {}'.format(self.input))

	def part2(self):
		print('Day x - part 2 result: {}'.format(self.input))
