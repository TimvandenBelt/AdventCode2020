from util import file


class Day1:
	numbers = []
	numberToForm = 2020
	twoResult = None
	threeResult = None

	def __init__(self):
		self.test()
		self.setNumbers()

	def setNumbers(self, array=None):
		self.numbers = []

		if not array:
			array = file.fileToArray(fileLocation='./inputs/inputday1', withIntParse=True)

		self.numbers = array
		self.calculate()

	def calculate(self):
		for number in self.numbers:
			if self.twoResult and self.threeResult:
				break

			self.numbers.pop()

			result = self.checkTwoNumbers(number)
			if result and not self.twoResult:
				self.twoResult = result[0] * result[1]

			result = self.checkThreeNumbers(number)
			if result and not self.threeResult:
				self.threeResult = result[0] * result[1] * result[2]

	def test(self):
		example = [
			1721,
			979,
			366,
			299,
			675,
			1456,
		]
		self.setNumbers(example)
		if self.twoResult and self.twoResult == 514579:
			print("Day 1 - test: \033[32msuccess\033[0m")
		else:
			print('Day 1 test: \033[31failed\033[0m')
			print('Received: {}'.format(self.twoResult))

	def part1(self):
		if self.twoResult:
			print('Day 1 - part 1 result: {}'.format(self.twoResult))
		else:
			print("Day 1 - part 1 result: \033[31failed\033[0m")

	def part2(self):
		if self.threeResult:
			print('Day 1 - part 2 result: {}'.format(self.threeResult))
		else:
			print("Day 1 - part 2 result: \033[31failed\033[0m")

	# @TODO make the functions recursive
	def checkTwoNumbers(self, number):
		for number2 in self.numbers:
			if number + number2 == self.numberToForm:
				result = [number, number2]
				return result
		return False

	def checkThreeNumbers(self, number):
		for number2 in self.numbers:
			for number3 in self.numbers:
				if number == number3 or number2 == number3:
					continue
				if number + number2 + number3 == self.numberToForm:
					result = [number, number2, number3]
					return result
		return False
