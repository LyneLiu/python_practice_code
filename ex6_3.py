#! /usr/bin/env python
# @author:lyne

def sortList():
	numStr = raw_input("Enter your number list:")
	aList = numStr.split()

	numList = []
	choice = raw_input("Enter your choice:")
	if choice == 'a':
		for i in aList:
			num = int(i)
			numList.append(num)
		print sorted(numList)
	elif choice == 'b':
		print sorted(aList)
	else:
		print "Input Error!"

if __name__ == '__main__':
	sortList()
