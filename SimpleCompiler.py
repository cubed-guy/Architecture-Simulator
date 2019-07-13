file = open("File3.hx", 'r')
out  = open("File.lx" , 'wb')

while file.read(1) != '': out.write(bytes([int(file.read(2), 16)]))