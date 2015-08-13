#! /usr//bin/env python
# -*- coding:utf-8 -*-
# @author:lyne

"最大公约数 -- 辗转相除法是求两个自然数的最大公约数的一种方法，也叫欧几里德算法。"
"最小公倍数 -- 两个数的最小公倍数是他们的乘积除以最大公约数。"

def GCD(numA,numB):
	"greatest common divisor"
	if numA < numB:
		(numA,numB) = (numB,numA)
	r = numA % numB
	while r != 0:
		numA = numB
		numB = r
		r = numA % numB

	return numB

def LCM(numA,numB):
	"least common multiple"
	gcd = GCD(numA,numB)
	return numA * numB / gcd


def test():
	numA = int(raw_input("number a:"))
	numB = int(raw_input("number b:"))
	gcd = GCD(numA,numB)
	lcm = LCM(numA,numB)
	print "the GCD of numA %d and numB %d is:%d" % (numA,numB,gcd)
	print "the LCM of numA %d and numB %d is:%d" % (numA,numB,lcm)


if __name__ == '__main__':
	test()
