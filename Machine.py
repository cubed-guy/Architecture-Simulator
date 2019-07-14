GHz = 4.0 #Billion cycles per second
Loops = 5 #Loops OP is allowed to make per cycle

with open("File.lx", 'rb') as file:	#read file
	def give(string):
		if len(string): return ord(string)
		else: return 0
	mem = [1]+list(map(lambda x: give(file.read(1)), [None]*255))
	out = [0, 0, 0]
	del give

cycles = 0
fetch = 0
print(mem)

while mem[0] != fetch:
	fetch = mem[0]
	mem[0] += 2

	#getting data to be transferred
	if mem[fetch+1] in range(37, 40):
		Data = out[mem[fetch+1]-37]
	else: Data = mem[mem[fetch+1]]

	mem[mem[fetch]] = Data
	print(f"{fetch}: {Data} from {mem[fetch+1]} to {mem[fetch]}")
	print(f"OP output:{', '.join(list(map(lambda x: bin(x)[2:], out)))}")
	#
	#"".join(list(map(lambda x: bin(x)[2:], out)))
	#"".join([bin1, bin2, bin3])
	#bin1+bin2+bin3 -> str

	#OP starts from mem[37]
	#	mem[37:40]   -> IO
	#	mem[40:112]  -> OP inputs Grid
	#	mem[112:184] -> OP main Grid
	# 	mem[184:256] -> OP inverted Grid

	for i in range(Loops):

		

	cycles += 1
	if mem[0]>=255: break
	elif mem[0] == 0:
		print("FetchError: Fetch cannot be zero.")
		break
else: print("InfiniteLoopError: Fetch assigning to itself.")
print(f"Process completed in {cycles} cycles.\
	({cycles/GHz} nanoseconds on {GHz}GHz)")
print(mem)