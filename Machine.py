with open("Test.hx", "rb") as f: file = f.read()
print(file)
size = len(file)
mem = ""
ws = [9, 10, 13, 32]
i = 0
print("Reading...")
while i < size:
	while file[i] in ws: i += 1	
	if file[i] in [48, 49]:
		mem += chr(file[i])
		i += 1
	elif file[i] == 35:
		while file[i] != 10: i += 1
	else:
		print("Invalid character:", file[i])
		quit()
