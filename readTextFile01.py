#! /usr/bin/env python
# @author:lyne

"readTextFile01.py -- read text file and display it."

# get file name
fname = raw_input("Enter the file name:")
print

# attemp to open the file for reading
try:
	fobj = open(fname,'r')
except Exception, e:
	print("***Error:file open error:",e)
else:
	for eachline in fobj:
		print eachline,
	fobj.close()