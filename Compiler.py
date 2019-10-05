'''V3 - block definition
main ::= *(def | data)
def ::= identifier block
data ::= block | num | identifier
block ::= "{" *data "}"
'''

from string import *
file = open('File.hx')
out  = open('File.lx', 'wb')
scope_level = 0
while 1:
	char = file.read(1)
	if char == '': break
	elif char == '#':
		while char in '\n': file.read(1)
	elif char == '{':
		scope_level += 1
	elif char == '}':
		if scope_level <= 0: print("Unexcpected closing braces '}'."); break
		scope_level -= 1
	elif char in ascii_letters:
		word = ''
		while char in ascii_letters: word += char; char = file.read(1)
		if word in hexdigits: out.write(bytes([int(char+file.read(1), 16)]))
	elif char not in'\n\t\r ':print(f"Unsupported character '{char}'."); break