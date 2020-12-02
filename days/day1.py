from util import fileUtil


class Day1:
	numbers = []
	numberToForm = 2020

	def setNumbers(self):
		self.numbers = fileUtil.returnArrayOfLinesForOfFile(fileLocation='./inputs/inputday1', withIntParse=True)

	def part1(self):
		self.setNumbers()

		for number in self.numbers:
			self.numbers.pop()
			result = self.checkIfTwoNumbersIsTogether(number)
			if result:
				print('Found {}'.format(self.numberToForm))
				print("{} - {}".format(result[0], result[1]))
				return

	def part2(self):
		self.setNumbers()
		for number in self.numbers:
			self.numbers.pop()
			result = self.checkIfThreeNumbersIsTogether(number)
			if result:
				print('Found {}'.format(self.numberToForm))
				print("{} - {} - {}".format(result[0], result[1], result[2]))
				return

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
