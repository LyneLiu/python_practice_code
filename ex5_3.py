#! /usr/bin/env python
# @author:lyne

def grade():
	"according the score,give a mark."
	score = int(raw_input("Enter the score:"))
	if 90 <= score <= 100:
		return 'A'
	elif 80 <= score <= 89:
		return 'B'
	elif 70 <= score <= 79:
		return 'C'
	elif 60 <= score <= 69:
		return 'D'
	else:
		return 'F'

def test():
	while True:
		mark = grade()
		print "your mark is %s.\n" % mark

if __name__ == '__main__':
	test()

