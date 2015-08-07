# -*- coding:utf-8 -*-
# judge the num
# @author:lyne

num = int(raw_input("please input the number:"))
if num > 0:
	print "%d is positive number." % num
elif num == 0:
	print "%d is zero number."
else:
	print "%d is negative number." % num
