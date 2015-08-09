#! /usr/bin/env python
# @author:lyne

"makeTextFile02.py -- create text file and write lines to the file"

import os
from string import join
ls = os.linesep

# get filename
while True:
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