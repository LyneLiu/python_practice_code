#! /usr//bin/env python
# @author:lyne

"temperature conversion -- use the true division"

from __future__ import division

def conversion(fahrenheit):
	celsius = (fahrenheit - 32) * (5 / 9)
	return celsius

def test():
	try:
		fahrenheit = float(raw_input("please input the fahrenheit:"))
		result = conversion(fahrenheit)
		print "temperature conversion from fahrenheit to celsius: %f" % result
	except ValueError,e:
		print "Error Input:",e

if __name__ == '__main__':
	test()