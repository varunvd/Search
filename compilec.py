import os
f=[]
# This takes all the file name in the current directory 
for (dirpath, dirname, filename) in os.walk('./'):
	f.extend(filename)
for i in f:
	i=str(i)
	if i.find('.c') == -1:
		f.remove(i)
d=[]
for i in f:
	d.append('./script.sh '+i+' '+i[0:len(i)-2])

os.system('chmod 777 script.sh')
for i in d:
	os.system(i)
f=[]
for (dirpath, dirname, filename) in os.walk('./'):
	f.extend(filename)

d=[]
for i in f:
	if 'error_' in i:
		d.append(i)

for i in d:
	data=open(i)
	if 'ld' in data.readline() or data.readline() == '' :
		str="rm "+i
		data.close()
		os.system(str)
	data.close()
