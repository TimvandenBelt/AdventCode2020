from util import file
import re


class PasswordLine:
	parameters = []
	character = ''
	password = ''
	line = ''

	def __init__(self, line):
		self.line = line
		self.parameters = self.getParameters(line)
		self.character = self.getCharacter(line)
		self.password = self.getPassword(line)

	@staticmethod
	def getParameters(line):
		m = re.search('(\d\d?)-(\d\d?)', line)
		min = int(m.group(1))
		max = int(m.group(2))
		return min, max

	@staticmethod
	def getCharacter(line):
		m = re.search('([a-z]):', line)
		return m.group(1)

	@staticmethod
	def getPassword(line):
		m = re.search('\d\d?-\d\d? [a-z]: (.*)', line)
		return m.group(1)

	def countCharOccurance(self):
		return self.password.count(self.character)

	def isCorrectCharCount(self):
		count = self.countCharOccurance()
		min, max = self.parameters
		if min <= count <= max:
			return True
		return False

	def isCorrectCharPossition(self):
		password = self.password
		pos1, pos2 = self.parameters
		character = self.character
		pos1 -= 1
		pos2 -= 1
		try:
			# @TODO could be better / simpler to read
			if (password[pos1] is character and password[pos2] is not character) or (
					password[pos1] is not character and password[pos2] is character):
				return True
		except IndexError:
			return False
		return False


class Day2:
	passwordLines = []
	correctPasswords = 0
	correctPositions = 0

	def __init__(self):
		self.test()
		self.setPasswordLines()

	def setPasswordLines(self, array=None):
		self.passwordLines = []
		if not array:
			array = file.fileToArray('./inputs/inputday2')
		for line in array:
			self.passwordLines.append(PasswordLine(line))
		self.calculate()

	def calculate(self):
		self.correctPasswords = 0
		self.correctPositions = 0

		for passwordLine in self.passwordLines:
			if passwordLine.isCorrectCharCount():
				self.correctPasswords += 1
			if passwordLine.isCorrectCharPossition():
				self.correctPositions += 1

	def test(self):
		example = [
			"1-3 a: abcde",
			"1-3 b: cdefg",
			"2-9 c: ccccccccc",
		]
		self.setPasswordLines(example)
		if self.correctPasswords == 2:
			print("Day 2 - test: \033[32msuccess\033[0m")
		else:
			print('Day 2 test: \033[31failed\033[0m')
			print('Received: {}'.format(self.correctPasswords))

	def part1(self):
		print('Day 1 - part 1 result: {}'.format(self.correctPasswords))

	def part2(self):
		print('Day 1 - part 2 result: {}'.format(self.correctPositions))
