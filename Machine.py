mem = [1] + [255]*255

print("Reading...")

with open("File.lx", 'rb') as file:
	i = 1
	while 1:
		char = file.read(1)
		if char == b'': break
		mem[i] = ord(char)

op = []
for o in mem[196:]: op += [bool(a) for a in o]

print("Running...")

while 1:
	fetch = mem[0]
	destination, source = mem[fetch], mem[fetch+1]
	mem[0] = fetch + 2
	data = mem[destination] = mem[source]
	if destination >= 196:
		loc = (destination - 196)*8
		data = [bool(int(a)) for a in str(data, 2)]
		for a in range(8): op[loc+a] = data[a]
	for main in range(16):
		val = False

	cycles += 1