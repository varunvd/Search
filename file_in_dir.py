import os
f=[]
for (dirpath, dirname, filename) in os.walk('./'):
	f.extend(filename)
a=raw_input("Enter the filename\n")
if a in f:
	print "The file "+a+" exists in the current directory"