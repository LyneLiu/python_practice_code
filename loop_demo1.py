#! /usr/bin/env python
# @author:lyne

import time

for i in [1,2,3,4,5]:
    print i,"Hello."


for i in range(1,6):
    print i,"times 8 =",i * 8


for i in xrange(10,-1,-2):
    print i
    time.sleep(1)
print "BLASH OFF!"

for cool_guy in ["Spongebob","Spiderman","Justin Timberlake","My dad"]:
    print cool_guy,"is the coolest guy ever!"


print "Type 3 to continue,anything else to quit."
someInput = raw_input()
while someInput == "3":
    print "Thank you for the 3.Very kind of you."
    print "Type 3 to continue,anthing else to quit."
    someInput = raw_input()
print "That's not 3,so I'm quiting now."
