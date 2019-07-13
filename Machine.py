Ghz = 3.0 #Billion cycles per second

with open("File.lx", 'rb') as file:
	def give(string):
		if len(string): return ord(string)
		else: return 0
	mem = [1]+list(map(lambda x: give(file.read(1)), [None]*255))
	del give

cycles = 0
fetch = 1
print(f"{fetch}: {mem[mem[fetch]]} from {mem[fetch+1]} to {mem[fetch]}")
print(mem)
while mem[0] != mem[mem[fetch]]:
	if mem[0]>=255: break
	fetch = mem[0]
	mem[0] += 2
	mem[mem[fetch]] = mem[mem[fetch+1]]
	print(f"{fetch}: {mem[mem[fetch]]} from {mem[fetch+1]} to {mem[fetch]}")

	

	cycles += 1
else: print("InfiniteLoopError: Fetch assigning to itself.")
print(f"Process completed in {cycles} cycles.\
	({cycles/Ghz} nanoseconds on {Ghz}Ghz)")
print(mem)