#!/usr/bin/python
import sys 
import os
a=int(raw_input("Enter the number according to the operation that is to be performed\n1)Search the content of the file\n2)Search and compile all C program\n3)Search for the file using filename in the dirctory\n4)Count the occurance of the pattern in the file\n5)Search the encrypted file\n"))
if a==1:
	os.system('python search.py')
	exit
elif a==2:
	os.system('python compilec.py')
	exit
elif a==3:
	os.system('python file_in_dir.py')
	exit
elif a==4:
	os.system('python count.py')
	exit	
else:
	user=(raw_input("Enter the username "))
	password=(raw_input("Enter the password "))
	if user!='unix' or  password!='unix':
		print "Invalid username and password"
		exit
	else:
		os.system('python after_else.py')
		exit
