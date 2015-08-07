# -*- coding:utf-8 -*-
# judge the num
# @author:lyne

str = raw_input("please input the string:")
print "Display in for loop:"
i = 0
while i < len(str):
	print str[i],
	i += 1

print "\nDisplay in while loop:"
for ch in str:
	print ch,
