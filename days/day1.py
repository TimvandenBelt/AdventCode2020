from util import fileUtil


class Day1:
	numbers = []
	numberToForm = 2020
	calculated = False
	twoString = False
	threeString = False

	def setNumbers(self):
		self.numbers = fileUtil.returnArrayOfLinesForOfFile(fileLocation='./inputs/inputday1', withIntParse=True)

	def calculate(self):
		if not self.calculated:
			self.setNumbers()

		for number in self.numbers:
			if self.twoString and self.threeString:
				break

			self.numbers.pop()

			result = self.checkIfTwoNumbersIsTogether(number)
			if result and not self.twoString:
				self.twoString = "{} * {} = {}".format(result[0], result[1], result[0] * result[1])

			result = self.checkIfThreeNumbersIsTogether(number)
			if result and not self.threeString:
				self.threeString = "{} * {} * {} = {}".format(result[0], result[1], result[2], result[0] * result[1] * result[2])

		self.calculated = True

	def part1(self):
		if not self.calculated:
			self.calculate()

		if self.twoString:
			print('Found {} with two numbers'.format(self.numberToForm))
			print(self.twoString)

	def part2(self):
		if not self.calculated:
			self.calculate()

		if self.threeString:
			print('Found {} with three numbers'.format(self.numberToForm))
			print(self.threeString)

	def checkIfTwoNumbersIsTogether(self, number):
		for number2 in self.numbers:
			if number + number2 == self.numberToForm:
				result = [number, number2]
				return result
		return False

	def checkIfThreeNumbersIsTogether(self, number):
		for number2 in self.numbers:
			for number3 in self.numbers:
				if number == number3 or number2 == number3:
					continue
				if number + number2 + number3 == self.numberToForm:
					result = [number, number2, number3]
					return result
		return False
