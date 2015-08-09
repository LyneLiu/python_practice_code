#! /usr/bin/env python
# @author:lyne

"readNmakeTextFile.py -- create text file and read text file."

import os
from string import join
ls = os.linesep


def makeTextFile():
	"create text file and write lines to the file."
	# get filename
	fname = raw_input("please enter your filename:")
	if os.path.exists(fname):
		print "\n***Error: %s already exists." % fname
	else:
		# get file context lines
		all = []
		print "\nEnter lines ('.' by itself to quit).\n"

		# loop until user terminate input
		while True:
			entry = raw_input(">>")
			if entry == '.':
				break
			else:
				all.append(entry)

		# write lines to file with NEWLINE line terminate
		fobj = open(fname,'w')
		fobj.write(join(all,ls))
		fobj.close()
		print "Done!"


def readTextFile():
	"read text file and display it."
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
		print
		fobj.close()

def test():
	while True:
		print """\nyou can choose what to do:\n
		a -- make text file.\n
		b -- read text file.\n"""
		choice = raw_input("choice is:")
		print
		if choice == 'a':
			makeTextFile()
		elif choice == 'b':
			readTextFile()

if __name__ == '__main__':
	test()
