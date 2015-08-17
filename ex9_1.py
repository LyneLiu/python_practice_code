#! /usr/bin/env python
# @author:lyne

def dealLine(eachLine):
    "deal with each line."
    aList = []
    lineList = list(eachLine)
    for ch in lineList:
        if ch != '#':
            aList.append(ch)
        else:
            break
    eachLine = "".join(aList)
    return eachLine

def fileInfo(filename):
    "read file context."
    fobj = open(filename,'r')
    for eachLine in fobj:
        eachLine = dealLine(eachLine.strip())
        if len(eachLine) != 0:
            print eachLine
        else:
            continue

if __name__ == '__main__':
    filename = raw_input("Enter file name:")
    fileInfo(filename)

