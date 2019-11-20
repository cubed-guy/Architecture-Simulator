bits = 10
cSize = 8
puLoops = 5
GHz  = 4.0
cycles = 0
with open('File.lx') as file: s = file.read(256)
mem = ([1]+[ord(i) for i in s]+[0]*((1<<bits)-1))[:257]
file = open('MachineLog.csv', 'w')
[file.write(str(i)+',') for i in range(1<<bits)], file.write('\n')
def asn(destination, source):
	if destination not in range(256, 261): mem[destination] |= mem[source]
	else: ei[destination-256] |= mem[source]
while 1:
	size  = (mem[0]>>cSize)+1
	fetch = mem[0]&(1<<cSize)-1	
	mem[0]+=2*size
	for i in range(size):
		if mem[fetch+2*i] not in range(256, 261):
			mem[mem[fetch+2*i]    ] = 0	# But what if it's one of my sources???
		else:ei[mem[fetch+2*i]-256] = 0
	for i in range(size):
		if mem[fetch+2*i] not in range(256, 261):
			mem[mem[fetch+2*i]    ] |= mem[mem[fetch+1+2*i]]
		else:ei[mem[fetch+2*i]-256] |= mem[mem[fetch+1+2*i]]
	for _ in range(puLoops):
		ins = mem[256:261]+[255^i for i in mem[256:261]]+ei
		gReg = 261
		for inReg in ins:
			for shifts in range(bits-1, -1, -1):
				if (inReg>>shifts)&1:
					for i in range(5):
					  mem[256+i] |= mem[gReg]
					  gReg += 1
				else: gReg += 5