#Let's make another compiler because why not.

#so our basic ingredients:
file = open('File3.hx')
out  = open('File3.lx', 'w', encoding = 'UTF-16')

char = ''

def read():
	global char
	char = file.read(1)
	return char

def word():
	while char in '\n\t\r ':
		read()
		if char == '': return ''
	word = ''
	while char.isalnum(): word += char; read()
	return word

def call(name):
	loc = file.tell()
	file.seek(names[name])
	block()
	file.seek(loc+1)

#the main ingredient
def block():
	while 1:
		name = word()

		if name:	#checks if there's any word
			#we should check if it is a literal (and write)
			try: out.write(chr(int(name, 16))); continue
			except ValueError as e:
				print('There was a VALUE ERROR')
				print(e)
			#next, we know it's a word
			#so we check if it's a call or a definition

			if char == '{':
				#in the definiton, we save the current location
				names[name] = file.tell()

				#then, we keep reading until we come out because it's 
				#meaningful only when it's called, not right now.
				
				level = 1	#how many brackets inside we are

				while level:
					read()
					if   char == '{': level += 1	# going in a level
					elif char == '}': level -= 1	#going out a level
					elif char == '#':				#if we encounter a comment
						#'not in' because it provides support for EOF too
						while char not in '\n': read()
					elif char == '': print('UNEXPECTED EOF'); quit()

			#when it's not a definition, we call it:
			else: call(name)

		else:	#when we haven't read a word
			read()
			if char == '#':	# for comments
				while char not in '\n': read()
			# this stuff's for ending the block
			elif char in '}': return

			else: print(f'INVALID SYNTAX at {file.tell()}'); quit()


names = {}	#locations of definitions

#finally, we actually do something:
block()
