#! /usr//bin/env python
# -*- coding:utf-8 -*-
# @author:lyne

import random,math

def randomList():
	"number of elements:N(1 < N <= 100) and element range n(0 <= n <= 2e31 - 1)"
	aList = []
	N = random.randint(1,100)
	for i in range(N):
		n = random.randrange(0,2 ** 31 - 1)
		aList.append(n)

	aList.sort()
	return aList

def test():
	 aList = randomList()
	 print aList

if __name__ == '__main__':
	test()
