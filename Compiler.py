with open("File.hx", "rb") as f: file = f.read()

size = len(file)
ws = b"\t\n\r "
i = 0
mem = ""
names = {}

while i < size:
	if file[i] in b'01':   				#adding bits
		mem += chr(file[i])
		i += 1
	elif file[i:(i+2)] == b'//':		#for commenting 
		while file[i] != 13: i += 1		# ord(13) -> '\r'
	else:
		print("Invalid character:", chr(file[i]))
		print(file[i:(i+1)])
		quit()
	while file[i] in ws:
		i += 1
		if i >= size: break

mSize = len(mem)

i = 0

out = open("File.lx", "wb")
while i < mSize:
	out.write(bytes([int(mem[i:(i+7)], 2)]))
	i += 8
out.close()