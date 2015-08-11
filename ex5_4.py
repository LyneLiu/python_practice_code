#! /usr/bin/env python
# @author:lyne

def leapYear(year):
	"judge that the year is leap year or not."
	if year % 4 == 0 and year % 100 != 0:
		return True
	elif year % 400 == 0:
		return True
	else:
		return False

def test():
	try:
		year = int(raw_input("Please input a year:"))
		if leapYear(year):
			print "%d is a leap year." % year
		else:
			print "%d is not a leap year." % year
	except ValueError, e:
		print "you must input a digit."

if __name__ == '__main__':
	while True:
		test()