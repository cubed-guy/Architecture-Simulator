'''V3 - block definition
main ::= *(def | data)
def ::= identifier block
data ::= block | num | identifier
block ::= "{" *data "}"
'''
from string import *

def read():		#returns one character and stores it in <char>
	global char
	char = file.read(1)
	print('    Read', repr(char))
	return char

def word():		#returns one word
	print('Getting Word...')
	while char in '\n\t\r ':
		read()
		if char == '': print('** EOF **'); return ''
	word = ''
	while char in ascii_letters+digits and char != '': word += char; read()
	if char == '': print('    ** EOF **')
	print('    Word:', repr(word))
	return word

def write(name):	#writes the hex value or calls the identifier
	if len(name)==2 and False not in [i in hexdigits for i in name]:
		out.write(chr(int(name, 16))); print('    (hex)')
	else: call(name)

def call(identifier):	#writes the value refered by the identifier
	print('Calling', repr(identifier))
	global char
	pos = file.tell()
	file.seek(defs[identifier])
	block()
	print('Returned from', repr(identifier))
	file.seek(pos)

def block():		#compiles the contents of a block
	print(f'Entered a block at {file.tell()%(2**64)}.')
	global char
	branch = 1
	while branch > 0:
		print('    Still in the block, char =', repr(char))
		if read() == '{': branch += 1
		elif char == '}': branch -= 1
		elif char == '': print('Unexpected EOF.'); quit()
		else: write(word())
		read()
		print('    Branch level:', branch)
	print(f'Exited block at {file.tell()}.')

file = open('File.hx')
out  = open('File.lx', 'w')
char = ''
defs = {}

while 1:
	name = word()
	if not name: print('Not a word.')
	if name:
		print("It's a word.")
		if char == '{':
			defs[name] = file.tell()
			branch = 1
			while branch > 0:
				if read() == '{': branch += 1
				elif char == '}': branch -= 1
				elif char == '': print('Unexpected EOF.'); quit()
			read()
		else: write(name)
	elif char == '#':
		print('    (Comment)')
		while read() not in '\n': pass
	elif char == '{': block()
	elif char == '': print('Compiled successfully!'); break
	else: print("NO.")