#! /usr/bin/env python
# @author:lyne

"typechk01.py -- type() and isinstance() demo"

def displayNumType(num):
	"display the type of argument"
	print num,'is',
	if type(num) == type(0):
		print "an integer"
	elif type(num) == type(0L):
		print "a long"
	elif type(num) == type(0.0):
		print "a float"
	elif type(num) == type(0 + 0j):
		print "a complex number"
	else:
		print "not a number at all!"

def test():
	displayNumType(-69)
	displayNumType(9999999999999999999L)
	displayNumType(98.6)
	displayNumType(-5.2 + 1.9j)
	displayNumType('xxxx')

if __name__ == '__main__':
	test()