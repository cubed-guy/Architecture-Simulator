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
	return char

def word():		#returns one word
	print('\nGetting Word...')
	print(repr(read()))
	print(end = 'Whitespaces:')
	while char in '\n\t\r ': print(repr(read())[1:-1], end = '')
	word = ''
	while char in ascii_letters+digits: word += char; read()
	print('\nWord:', repr(word))
	return word

def write(name):	#writes the hex value or calls the identifier
	if len(name)==2 and False not in [i in hexdigits for i in name]:
		out.write(chr(int(name, 16)))
	else: call(name)

def call(identifier):	#writes the value refered by the identifier
	print('Calling', repr(identifier))
	global char
	pos = file.tell()
	file.seek(defs[identifier])
	block()
	file.seek(pos)

def block():		#compiles the contents of a block
	print(f'Entered a block at {file.tell()}.')
	branch = 1
	while branch > 0:
		if read() == '{': branch += 1
		elif char == '}': branch -= 1
		elif char == '': print('Unexpected EOF.'); quit()
		else: write(word())
	print(f'Exited block at {file.tell()}.')

file = open('File2.hx')
out  = open('File.lx', 'w')
char = ''
defs = {}

while 1:
	name = word()
	print('Char:', repr(char))

	print('Is it a word?', end = ' ')
	if name:
		print('YES!')
		if char == '{':
			defs[name] = file.tell()
			branch = 1
			while branch > 0:
				if read() == '{': branch += 1
				elif char == '}': branch -= 1
				elif char == '': print('Unexpected EOF.'); quit()
		else: write(name)
	else: print("No")
	if char == '#':
		print('**Comment')
		while read() not in '\n': pass
	elif char == '{': block()
	elif char == '': break
	else: print("NO.")