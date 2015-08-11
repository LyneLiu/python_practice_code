#! /usr/bin/env python
# @author:lyne

def convert(dollar):
	"convert the dollar to cents."
	if dollar >= 1:
		print "money is too large."
	elif 0 < dollar < 1:
		print "you can convert your money to",
		cent = int(dollar * 100)
		(num25,remain) = divmod(cent,25)
		if num25:
			print "%d 25-cents" % int(num25),
		(num10,remain) = divmod(remain,10)
		if num10:
			print "and %d 10-cents" % int(num10),
		(num5,remain) = divmod(remain,5)
		if num5:
			print "and %d 5-cents" % int(num5),
		(num1,remain) = divmod(remain,1)
		if num1:
			print "and %d 1-cents" % int(num1)
		print ".\n"
	else:
		print "your input must be larger than 0."

def test():
	try:
		dollar = float(raw_input("Please input your money:"))
		convert(dollar)
	except ValueError, e:
		print "you must input a digit."

if __name__ == '__main__':
	while True:
		test()
