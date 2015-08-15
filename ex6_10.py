#! /usr/bin/env python
# @author:lyne


def exchangeNconvert():
    "exchange the string and reverse it."
    str_in = raw_input("Enter your string:")
    stroutList = []
    strinList = list(str_in)
    for i in strinList:
        if i.isalpha:
            if i < 'a':
                stroutList.append(i.lower())
            else:
                stroutList.append(i.upper())
        else:
            stroutList += i
    stroutList.reverse()
    print "".join(stroutList)

if __name__ == '__main__':
    exchangeNconvert()
