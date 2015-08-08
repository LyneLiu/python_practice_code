#! /usr/bin/env python

"makeTextFile.py -- create text file and write lines to the file"

import os
ls = os.linesep

# get filename
while True:
	fname = raw_input("please enter your filename:")
	if os.path.exists(fname):
		print "\n***Error: %s already exists." % fname
	else:
		break

# get file context lines
all = []
print "\nEnter lines ('.' by itself to quit).\n"

# loop until user terminate input
while True:
	entry = raw_input(">")
	if entry == '.':
		break
	else:
		all.append(entry)

# write lines to file with NEWLINE line terminate
fobj = open(fname,'w')
# checkout another method from the file:makeTextFile01.py
fobj.writelines(["%s%s" % (x,ls) for x in all])
fobj.close()
print "Done!"
