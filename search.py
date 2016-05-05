#!/usr/bin/python

import os
#Reads the string
a=raw_input("Enter the string\n")
a=a.lower()
f=[]
#Creates a list of all the files in the current directory
for (dirs , subdir, files) in os.walk('./'):
	f.extend(files)
list_of_files=[] #Holds the list of files in which the string is found
for i in f:
	data=open(i, 'r')
	for each_line in data:
		if a in each_line.lower():
			list_of_files.append(i)
			data.close()
			break
	data.close()
print list_of_files	
#end		
			
