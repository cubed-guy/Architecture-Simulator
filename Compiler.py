#start compiler boilerplate
file = open('File.hx', 'rb')
out  = open('File.lx', 'wb')

names = {}
ws = b"\n\t \r"
lit = b'0123456789abcdef'
ltr = [[a]+[a+32] for a in range(65, 91)]+[a for a in range(48, 58)]
print(ltr)
stack = []

def err(msg="ERROR"): print(msg); quit()

def word():
	global char, file, ltr
	name = ''
	while 1:
		char = file.read(1)
		if not(ord(char) in ltr) or char == b'': break
		name += chr(ord(char))
		print(name)
	return name

while 1:
	char = file.read(1)
	print(char)					
	if   char == b'': break
	elif char in ws: pass
	#pause compiler boilerplate
	#-----------------------------*** MAIN LOGIC ***---------------------------

	#word
	elif ord(char) in ltr:
		name = chr(ord(char))
		name += word()
		print("Final name:", name)
		print(len(name))
		#byte
		print([ord(a) in (l for l in lit) for a in name])
		if len(name) == 2 and not(False in [ord(a) in (l for l in lit) for a in name]):
			val = int(char + file.read(1), 16)
			out.write(bytes([val]))
		#identifier
		else:
			if name in (el[0] for el in stack): err(38)
			stack.append((name, file.tell()))
			file.seek(names[name])

	#definition
	elif char == b'+':
		name = word()
		if name == '': err(45)
		if name in names: err(46)
		while char in ws and char != b'': char = file.read(1)
		if char == b'{':
			names[name] = file.tell()
			while 1:
				char = file.read(1)
				if   char == b'' : err(52)
				elif char == b'{': err(53)
				elif char == b'+': err(54)
				elif char == b'}': break
		else: err(56)

	#exit
	elif char == b'}':
		file.seek(stack[-1][1])
		if len(stack) > 0: del stack[-1]
		else: err(62)

	#comment
	elif char == b'/':
		char = file.read(1)
		if char == b'/':
			while not(char in b'\n'): char = file.read()
		else: err(69)

#resume compiler boilerplate
	else: err(72)

file.close()
out.close()
#end compiler boilerplate