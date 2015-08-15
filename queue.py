#! /usr/bin/env python
# @author:lyne

"queue.py -- queue demo."

queue = []

def enQ():
	queue.append(raw_input("Enter new string:").strip())

def delQ():
	if len(queue) == 0:
		print "Can't pop item from empty queue!"
	else:
		print "Removed [",repr(queue.pop(0)),"]"

def viewQueue():
	print queue

CMDs = {'e':enQ,'d':delQ,'v':viewQueue}

def showMenu():
	pr =  """
Command Menu:
1.(E)nqueue
2.(D)equeue
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
			if choice not in 'edvq':
				print "Invalid option!please try again."
			else:
				break

		if choice == 'q':
			break
		CMDs[choice]()

if __name__ == '__main__':
	showMenu()
