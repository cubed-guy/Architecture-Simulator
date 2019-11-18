'''
main ::= *(data|def)
def ::= identifier block
data ::= block | num | identifier
block ::= "{" main "}"
'''
from string import *

file = open('File.hx')
out  = open('File.lx')
char = ''

def read():
	global char
	char = file.read()
	print('    Read', repr(char))
	return char
def write():
	if len(name)==2 and False not in [i in hexdigits for i in name]:
		out.write(chr(int(name, 16))); print('    (hex)')
	else: call(name)
def call(defs, identifier):
	print('Calling', repr(identifier))
	global char
	pos = file.tell()
	file.seek(defs[identifier])
	block()
	print('Returned from', repr(identifier))
	file.seek(pos)

def block():
	defs = {}
	global char
	branch = 1
	while branch > 0:
		if   char == '{': branch += 1
		elif char == '}': branch -= 1
		elif char == '' : print('Unexpected EOF'); quit()
		else: word(defs)
		read()
def word(defs):
	while char.isspace(): read()
	word = ''
	while char.isalnum(): word += char; read()
	if word:
		if char == '{':
			defs[word] = file.tell()
			block(defs)

			