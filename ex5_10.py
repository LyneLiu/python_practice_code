#! /usr//bin/env python
# -*- coding:utf-8 -*-
# @author:lyne

"time conversion"

def conversionTime():
	time = raw_input("please input your time(eg:HH:MM):")
	time = time.split(":")
	hour = time[0]
	minute = time[1]
	sumMinutes = int(hour) * 60 + int(minute)
	return sumMinutes

def test():
	sumMinutes = conversionTime()
	print "the time conversion result:%d" % sumMinutes

if __name__ == '__main__':
	test()