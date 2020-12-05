import fileinput

def fileToArray(fileLocation, withIntParse=False):
	with fileinput.input(files=(fileLocation)) as fileInput:
		lines = []
		for line in fileInput:
			line = line.rstrip("\n")
			if withIntParse:
				line = int(line)
			lines.append(line)
		return lines
