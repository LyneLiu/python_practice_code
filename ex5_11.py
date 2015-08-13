#! /usr//bin/env python
# -*- coding:utf-8 -*-
# @author:lyne

def interest():
	"calculate the interest of deposited money "
	money = float(raw_input("please input the money you deposit:"))
	interest = 0.0001
	day = 1
	while day <= 365:
		money = (1 + interest) * money
		day += 1

	return money

def test():
	money = interest()
	print "your deposited money add up the interest is",money

if __name__ == '__main__':
	test()
