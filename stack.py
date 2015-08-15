#! /usr/bin/env python
# @author:lyne

"stack.py -- stack demo."

stack = []

def pushIt():
	stack.append(raw_input("Enter new string:").strip())

def popIt():
	if len(stack) == 0:
		print "Can't pop item from empty stack!"
	else:
		print "Removed [",repr(stack.pop()),"]"

def viewStack():
	print stack

CMDs = {'u':pushIt,'o':popIt,'v':viewStack}

def showMenu():
	pr =  """
Command Menu:
1.p(U)sh
2.p(O)p
3.(V)iew
4.(Q)uit

Enter your choice:"""
	while True:
		while True:
			"initiate the choice."
			try:
				choice = raw_input(pr).strip()[0].lower()
			except (EOFError,KeyboardInterrupt,IndexError,KeyError),e:
				choice = 'q'

			print "\nYour choice is:[%s]" % (choice)
			if choice not in 'uovq':
				print "Invalid option!please try again."
			else:
				break

		if choice == 'q':
			break
		CMDs[choice]()

if __name__ == '__main__':
	showMenu()
