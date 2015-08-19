#! /usr/bin/env python
# @author:lyne

"a easy math game."

from operator import add,sub
from random import randint,choice

opDict = {'+':add,'-':sub}
MaxNum = 2

def doprob():
    "operate the numbers and judge the user's answer."
    op = choice('+-')   # randomly choose the operator
    numList = [randint(1,10) for i in xrange(2)]
    numList.sort(reverse = True)
    ps = "%d %s %d = " % (numList[0],op,numList[1])
    oop = 0
    ans = opDict[op](*numList)
    while True:
        if int(raw_input(ps)) == ans:
            print "Correct.Well done!"
            break
        elif oop == MaxNum:
            print "Sorry.\nanswer is:",ps,ans
            break
        else:
            oop += 1

def main():
    while True:
        doprob()
        try:
            # Enter or input 'y' to play again
            choice = raw_input("Play again?[y]").lower()
            if choice and choice[0] == 'n':
                break
        except (KeyboardInterrupt,EOFError):
            break


if __name__ == '__main__':
    main()
