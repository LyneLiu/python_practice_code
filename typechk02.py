# -*- coding:utf-8 -*-
# @author:lyne

"typechk02.py -- type() and isinstance() demo"

import types

def displayNumType(num):
	"display the type of argument"
	print num,'is',
	if type(num) == types.IntType:
		print "an integer"
	elif type(num) == types.LongType:
		print "a long"
	elif type(num) == types.FloatType:
		print "a float"
	elif type(num) == types.ComplexType:
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