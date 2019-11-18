GHz = 4.0
with open('File.lx') as file: s = file.read(127)
mem = ([1]+[ord(i) for i in s]+[0]*127)[:128]
file = open('MachineLog.csv', 'w')
regs, cycles = 1, 0
[file.write(str(i)+',') for i in range(128)], file.write('\n')
[file.write(str(i)+',') for i in range(128, 256)], file.write('\n')
while mem[0]+2*regs<128:
	print()
	for m in mem: file.write(str(m)+',')
	file.write('\n')
	fetch = mem[0]&127
	regs = 2**((mem[0]&0b1*128)//128)	#(mem[0]&0b1*128)//128 -> size (z)
	print('regs:', regs)
	# ins = tuple(mem[mem[fetch+2*i]]^(127*((mem[fetch+2*i]   & 0b1*128)//128))
	# 							   ^(127*((mem[fetch+2*i+1] & 0b1*128)//128))
	# 							   for i in range(regs))
	ins = ()
	for i in range(regs):
		print(fetch+2*i, fetch+2*i+1)
		print(mem[fetch+2*i], mem[fetch+2*i+1])
		print(mem[mem[fetch+2*i]&127])
		print((mem[fetch+2*i]   & 0b1*128)//128)
		print((
			mem[mem[fetch+2*i]&127]^(127*((mem[fetch+2*i]   & 0b1*128)//128))
							   ^(127*((mem[fetch+2*i+1] & 0b1*128)//128)))
		)
		ins += tuple(
			[mem[mem[fetch+2*i]&127]^(127*((mem[fetch+2*i]   & 0b1*128)//128))
								^(127*((mem[fetch+2*i+1] & 0b1*128)//128))]
			)
	mem[0] += 2*regs
	for i in range(regs): mem[mem[fetch+1+i*2]&127] = 0
	for i in range(regs): mem[mem[fetch+1+i*2]&127] |= ins[i]
	cycles += 1
	if mem[0] == fetch:
		print("InfiniteLoopError: Fetch assigning to itself."); break
print(f'Process completed in {cycles} cycles.\
	({cycles/GHz} nanoseconds on {GHz}GHz)')