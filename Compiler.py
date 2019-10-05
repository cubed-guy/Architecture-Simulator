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
	print(char, end = '')
	return char

def word():		#returns one word
	print('Searching for words...')
	while read() in '\n\t\r ': pass
	print('\nWhitespaces eliminated.')
	word = ''
	while char in ascii_letters: word = read()
	print('\nWord:', repr(word))
	return word

def write(name):	#writes the hex value or calls the identifier
	if len(name)==2 and False not in [i in hexdigits for i in name]:
		out.write(chr(int(name, 16)))
	else: call(name)

def call(identifier):	#writes the value refered by the identifier
	print('\nCalling', repr(identifier))
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
	print('Is it a word?')
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
	elif char == '{': block()
	elif char == '': break
	else: print("NO.")