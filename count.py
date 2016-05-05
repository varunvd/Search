import os
a=raw_input("Enter the filename\n")
b=raw_input("Enter the word that is to be counted\n")
data=open(a, 'r')
count=0
for each_line in data:
	if b in each_line:
		each_line=str(each_line)
		each_line=each_line.lower()
		count=count+each_line.count(b)
print count
data.close()		



