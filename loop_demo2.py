#! /usr/bin/env python
# @author:lyne

print "The first time try!"
for i in xrange(1,6):
    print
    print "i =",i,
    print "Hello,how",
    if i == 3:
        continue
    print "are you today?"

print "The second time try!"
for i in xrange(1,6):
    print
    print "i =",i,
    print "Hello,how",
    if i == 3:
        break
    print "are you today?"
