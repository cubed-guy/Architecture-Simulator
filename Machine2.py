CU = 1+[0]*255

# def getPU():
# 	for i in PU: yield i

def asn(sequence, destination, source):
 sequence[destination] = sequence[source]

while 1:
	size  = CU[0]>>7
	fetch = CU[0]&127
	CU[0]+=2*size
	for i in range(size): asn(CU, CU[fetch+2*i], CU[fetch+1+2*i])
	# if CU[0] == fetch: raise RecursionError('Stagnating fetch')