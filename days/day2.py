from util import fileUtil
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
		min = self.parameters[0]
		max = self.parameters[1]
		if min <= count <= max:
			return True
		return False

	def isCorrectCharPossition(self):
		password = self.password
		pos1 = self.parameters[0] - 1
		pos2 = self.parameters[1] - 1
		character = self.character
		try:
			if (password[pos1] is character and password[pos2] is not character) or (
					password[pos1] is not character and password[pos2] is character):
				return True
		except IndexError:
			return False
		return False


class Day2:
	inputArray = []
	passwordLines = []
	correctCount = 0
	correctPos = 0
	calculated = False

	def __init__(self):
		self.inputArray = fileUtil.returnArrayOfLinesFromFileInput('./inputs/inputday2')
		for line in self.inputArray:
			self.passwordLines.append(PasswordLine(line))

	def calculate(self):
		if self.calculated:
			self.correctPos = 0
			self.correctCount = 0

		for passwordLine in self.passwordLines:
			if passwordLine.isCorrectCharCount():
				self.correctCount += 1
			if passwordLine.isCorrectCharPossition():
				self.correctPos += 1

		self.calculated = True

	def part1(self):

		if not self.calculated:
			self.calculate()

		print('Number of correct min max chat count')
		print(self.correctCount)

	def part2(self):
		if not self.calculated:
			self.calculate()

		print('Number of correct char possition')
		print(self.correctPos)
