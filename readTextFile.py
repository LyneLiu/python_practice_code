#！/usr/bin/env python
# @author:lyne

"readTextFile.py -- read text file and display it."

import os

# get file name
while True:
	fname = raw_input("Enter your file name:")
	if os.path.exists(fname):
		"read and display the file."
		fobj = open(fname,'r')
		for readline in fobj.readlines():
			print readline,
	else:
		print("\n***Error:the file does not exist!")
