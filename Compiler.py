file = open("Test.hx", "rb")
ln   = 0

ws = [9, 10, 13, 32]
names = {}
mem = []

def word():
	global line, col, ws
	word = ""
	while not(line[col] in ws):
		word += chr(line[col])
		col  += 1
	return word
	
while 1:
	line = file.readline()
	ln += 1
	if line[0] != 35:
		col = 0
		source = word()
		while line[col] in ws: col += 1
		target = word()
		print(ln, line)
		while line[col] in ws: col += 1
		if line[col] == 36:
			col += 1
			names[word()] = ln
	print(line)
	# print(ln, line)