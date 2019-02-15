with open("File.hx", "rb") as f: file = f.read()

size = len(file)
ws = b"\t\n\r "
letters = [a for a in range(65, 91) + range(97, 123)]

i = 0
line = 1

names = {'mem':""}
hier = ['mem']						#path of hierarchy

def noRead():						#for skipping comments and white space
	global i, file, ws, size, line
	# stay = file[i] in ws or file[i:(i+2)] == b'//'
	# while stay:
		# i += 1
		# if i >= size: break
		# if file[i:(i+2)] == b'//':		#for commenting 
			# i += 2
			# while file[i] != 13:		# ord(13) -> carriage return character
				# i += 1
				# line += 1
				# if i >= size: break
	space = file[i] in ws
	comment = file[i:(i+2)] == b'//'
	while space or comment:
		i += 1
		if i >= size: break
		
		
while i < size:
	if file[i] in b'01':   				#adding bits
		names[name] += chr(file[i])
		i += 1
	elif file[i] == 36:					# ord(36) -> '$'
		name = ""
		i += 1
		while file[i] in letters:
			name += file[i]
			i += 1
		if name in names:
			print("Name", name, "already exists.")
		names[name] = ""
		noRead()
	else:
		print("Invalid character:", chr(file[i]))
		print(file[i:(i+1)])
		quit()
	noRead()

mSize = len(mem)

i = 0

out = open("File.lx", "wb")
while i < mSize:
	out.write(bytes([int(mem[i:(i+7)], 2)]))
	i += 8
out.close()