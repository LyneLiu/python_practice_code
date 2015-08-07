# -*- coding:utf-8 -*-
# sum the list or tuple
# @author:lyne

i = 0
j = 0
total = 0
a = [1,2,3,4,5]
b = (1,2,3,4,5)

print "sum the list with while:"
while i < len(a):
	total = total + a[i]
	i += 1

print "total sum:%d" % total

print "sum the tuple with for:"
total = 0
for num in b:
	total = total + num

print "total sum:%d" % total

