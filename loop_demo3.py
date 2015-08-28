#! /usr/bin/env python
# @author:lyne

print "Which multiplication table would you like?"
num = int(raw_input())
print "How high do you want to go?"
high = int(raw_input())

print "Here's your table:"
for i in xrange(1,high+1):
    print "%d x %d = %d" % (num,i,num * i)


print "Let's try again!"
loop = 1
while loop <= high:
    print "%d x %d = %d" % (num,loop,num * loop)
    loop += 1

print "The End."
