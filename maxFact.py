#! /usr/bin/env python
# @author:lyne

def showMaxFactor(num):
    count = num / 2
    while count > 1:
        if num % count == 0:
            print "largest factor of %d is %d." % (num,count)
            # when break, go to the end
            break
        count -= 1
    else:
        print "%d is prime." % num

if __name__ == '__main__':
    for eachNum in range(10,21):
        showMaxFactor(eachNum)

