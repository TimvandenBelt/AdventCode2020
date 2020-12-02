import fileinput


def returnArrayOfLinesFromFileInput(fileLocation, withIntParse=False):
	with fileinput.input(files=(fileLocation)) as fileInput:
		lines = []
		for line in fileInput:
			line = line.rstrip("\n")
			if withIntParse:
				line = int(line)
			lines.append(line)
		return lines


def returnArrayOfLinesForOfFile(fileLocation, withIntParse=False):
	return returnArrayOfLinesFromFileInput(fileLocation, withIntParse)
