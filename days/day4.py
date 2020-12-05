from util import file
import re


class Passport:
	byr = None
	iyr = None
	eyr = None
	hgt = None
	hcl = None
	ecl = None
	pid = None
	cid = None  # not required

	def hasAllBesidesCID(self):
		if self.byr and self.iyr and self.eyr and self.hgt and self.hcl and self.ecl and self.pid:
			return True
		return False

	def verifyAllBesidesCID(self):
		if not self.verifyBYR():
			return False
		if not self.verifyIYR():
			return False
		if not self.verifyEYR():
			return False
		if not self.verifyHGT():
			return False
		if not self.verifyHCL():
			return False
		if not self.verifyECL():
			return False
		if not self.verifyPID():
			return False

		return True

	def verifyPID(self):
		m = re.search('(\d\d\d\d\d\d\d\d\d)', self.pid)
		try:
			if m.group(1):
				return True
		except AttributeError:
			return False
		return False

	def verifyECL(self):
		array = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
		if self.ecl in array:
			return True
		return False

	def verifyHCL(self):
		m = re.search('(#[0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f])', self.hcl)
		try:
			if m.group(1):
				return True
		except AttributeError:
			return False
		return False

	def verifyHGT(self):
		m = re.search('(\d\d\d?)(cm|in)', self.hgt)
		try:
			length = int(m.group(1))
			type = m.group(2)
			if type == 'cm':
				if 150 <= length <= 193:
					return True
			if type == 'in':
				if 59 <= length <= 76:
					return True
		except AttributeError:
			return False
		return False

	def verifyEYR(self):
		m = re.search('(\d\d\d\d)', self.eyr)
		try:
			value = int(m.group(1))
			if 2020 <= value <= 2030:
				return True
		except IndexError:
			return False
		return False

	def verifyIYR(self):
		m = re.search('(\d\d\d\d)', self.iyr)
		try:
			value = int(m.group(1))
			if 2010 <= value <= 2020:
				return True
		except AttributeError:
			return False
		return False

	def verifyBYR(self):
		m = re.search('(\d\d\d\d)', self.byr)
		try:
			value = int(m.group(1))
			if 1920 <= value <= 2002:
				return True
		except AttributeError:
			return False
		return False

	def processLine(self, line):
		items = line.split(' ')
		for item in items:
			m = re.search('([a-z][a-z][a-z]):(.*)', item)
			key = m.group(1)
			value = m.group(2)
			self.processesKeyValue(key, value)

	def processesKeyValue(self, key, value):
		if key == 'byr':
			self.byr = value
			return

		if key == 'iyr':
			self.iyr = value
			return

		if key == 'eyr':
			self.eyr = value
			return

		if key == 'hgt':
			self.hgt = value
			return

		if key == 'hcl':
			self.hcl = value
			return

		if key == 'ecl':
			self.ecl = value
			return

		if key == 'pid':
			self.pid = value
			return

		if key == 'cid':
			self.cid = value
			return


class Day4:
	input = []
	passports = []
	countCorrectBesidesCID = 0
	countCorrectValuesBesidesCID = 0

	def __init__(self):
		self.test()
		self.loadPassports()

	def verifyPassports(self):
		self.countCorrectBesidesCID = 0
		self.countCorrectValuesBesidesCID = 0
		self.passports = []

		passport = Passport()
		for line in self.input:
			if line == '':
				self.passports.append(passport)
				if passport.hasAllBesidesCID():
					self.countCorrectBesidesCID += 1
					if passport.verifyAllBesidesCID():
						self.countCorrectValuesBesidesCID += 1
				passport = Passport()
				continue

			passport.processLine(line)

		self.passports.append(passport)
		if passport.hasAllBesidesCID():
			self.countCorrectBesidesCID += 1
			if passport.verifyAllBesidesCID():
				self.countCorrectValuesBesidesCID += 1

	def loadPassports(self, array=None):
		if not array:
			array = file.fileToArray(fileLocation='./inputs/inputday4')
		self.input = array
		self.verifyPassports()

	def test(self):
		example1 = [
			"ecl:gry pid:860033327 eyr:2020 hcl:#fffffd",
			"byr:1937 iyr:2017 cid:147 hgt:183cm",
			"",
			"iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884",
			"hcl:#cfa07d byr:1929",
			"",
			"hcl:#ae17e1 iyr:2013",
			"eyr:2024",
			"ecl:brn pid:760753108 byr:1931",
			"hgt:179cm",
			"",
			"hcl:#cfa07d eyr:2025 pid:166559648",
			"iyr:2011 ecl:brn hgt:59in",
		]

		self.loadPassports(example1)

		if self.countCorrectBesidesCID != 2:
			print('Day 4 test: \033[31mfailed\033[0m')
			print('Received: {}'.format(self.countCorrectBesidesCID))
			return

		example2 = [
			"eyr:1972 cid:100",
			"hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926",
			"",
			"iyr:2019",
			"hcl:#602927 eyr:1967 hgt:170cm",
			"ecl:grn pid:012533040 byr:1946",
			"",
			"hcl:dab227 iyr:2012",
			"ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277",
			"",
			"hgt:59cm ecl:zzz",
			"eyr:2038 hcl:74454a iyr:2023",
			"pid:3556412378 byr:2007",
		]

		self.loadPassports(example2)

		if self.countCorrectValuesBesidesCID != 0:
			print('Day 4 test: \033[31mfailed\033[0m')
			print('Received: {}'.format(self.countCorrectValuesBesidesCID))
			return

		example3 = [
			"pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980",
			"hcl:#623a2f",
			"",
			"eyr:2029 ecl:blu cid:129 byr:1989",
			"iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm",
			"",
			"hcl:#888785",
			"hgt:164cm byr:2001 iyr:2015 cid:88",
			"pid:545766238 ecl:hzl",
			"eyr:2022",
			"",
			"iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719",
		]

		self.loadPassports(example3)

		if self.countCorrectValuesBesidesCID != 4:
			print('Day 4 test: \033[31mfailed\033[0m')
			print('Received: {}'.format(self.countCorrectValuesBesidesCID))
			return

		print("Day 4 - test: \033[32msuccess\033[0m")


	def part1(self):
		print('Day 4 - part 1 result: {}'.format(self.countCorrectBesidesCID))

	def part2(self):
		print('Day 4 - part 2 result: {}'.format(self.countCorrectValuesBesidesCID))
