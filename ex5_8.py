#! /usr//bin/env python
# @author:lyne

"ex5_8.py -- remainder test"

def findEvenNum():
	for i in xrange(0,20):
		if i % 2 == 0:
			print i,
		else:
			pass

def findOddNum():
	for i in xrange(0,20):
		if i % 2 != 0:
			print i,
		else:
			pass

def isDivisible(numA,numB):
	if (numA % numB) == 0:
		return True
	elif (numB % numA) == 0:
		return True
	else:
		return False


def test():
	print "find the even number of 0~20:"
	findEvenNum()
	print "\nfind the odd number of 0~20:"
	findOddNum()
	a = int(raw_input("\nnumber a:"))
	b = int(raw_input("number b:"))
	print "judge the divisible relation of the two number:",
	print a,b
	print "judge result is:",isDivisible(a,b)

if __name__ == '__main__':
	test()
