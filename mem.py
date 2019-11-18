class mem(list):
	"""docstring for mem"""
	DEFAULT
	def __init__(self, arg):
		super(mem, self).__init__()
		with open('File.lx') as file: s = file.read(127)
		self.append(([1]+[ord(i) for i in s]+[0]*127)[:128])
	
	def asn(self, dest, src): self[dest] = self[src]

	def process(self, ins):
		T = ins+[255^i for i in ins]
		TBits = []
		# for t in T: TBits += [int(i) for i in bin(t)[2:].rjust(8, '0')]
		for t in range(len(T)):
			TBits += [i for i in t]
		for i in range(len(TBits)):
			opRegs = self[i*8:i*8+1]
			ins |= [TBits[i]*o for o in opRegs]
		