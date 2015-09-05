#! /usr/bin/env python
# @author:lyne

name = raw_input("Enter your name:")

def namePrint(name):
    for  letterArgv in name:
        if letterArgv == "a":
            print """
     A
    A A
   A   A
  AAAAAAA
 A       A
A         A""",
        elif letterArgv == "l":
            print """
L
L
L
L
L
LLLLLL""",
        elif letterArgv == "e":
            print """
EEEEEE
E
EEEE
E
E
EEEEEE""",
        elif letterArgv == "n":
            print """
N      N
N N    N
N  N   N
N   N  N
N    N N
N      N""",
        elif letterArgv == "y":
            print """
Y     Y
 Y   Y
  Y Y
   Y
   Y
   Y""",


namePrint(name)
