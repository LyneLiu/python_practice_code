#! /usr//bin/env python
# -*- coding:utf-8 -*-
# @author:lyne

"idcheck01.py -- Identifier Checker v2.0"

import string,keyword

alphas = string.letters + '_'
nums = string.digits

def idCheck():
	print "Welcome to Identifier Checker v1.0."
	print "Testees must be at least 2 characters long."

	myInput = raw_input("Identifier to test? ")

	if len(myInput) > 1:
		if myInput[0] not in alphas:
			print """invalid:first character must be alphabetic."""
		else:
			for otherChar in myInput[1:]:
				if otherChar not in alphas + nums:
					print """invalid:other character must be alphanumeric."""
					break
			else:
				if myInput not in keyword.kwlist:
					print "Okey as an identifier."
				else:
					print """invalid:identifier can not be keyword."""

def test():
	"Identifier Checker v1.0 test."
	idCheck()


if __name__ == '__main__':
	test()