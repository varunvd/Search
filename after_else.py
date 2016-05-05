import os
file_name=raw_input("Enter the encrypted file name ")
find_it=raw_input("Enter the pattern to be searched ")
a="python code.py "+file_name
b="cat "+file_name
c="python decode.py "+file_name
os.system(c)
data=open(file_name, 'r')
for each_line in data:
	if find_it in each_line.lower():
		print 'Pattern Matched'
		os.system(b)
		print '\n'
		os.system(a)
		exit()
print 'Pattern not found'
os.system(a)