#! /usr//bin/env python
# -*- coding:utf-8 -*-
# @author:lyne

db = {}

def newUser():
	"create a new user."
	prompt = 'login desired:'
	while True:
		name = raw_input(prompt)
		if name in db:
			prompt = "name taken,try another:"
			continue
		else:
			break
	pwd = raw_input('passwd:')
	db[name] = pwd

def oldUser():
	"old user login."
	name = raw_input("login:")
	if name in db:
		pwd = raw_input("passwd:")
		passwd = db[name]
		if pwd == passwd:
			print "Welcome back",name
		else:
			print "login passwd incorrect!"
	else:
		print "login name incorrect!"

def showMenu():
	prompt = """
(N)ew User Login 
(E)xisting User Login
(Q)uit

Enter choice:"""
	done = False
	while not done:
		chosen = False
		while not chosen:
			try:
				choice = raw_input(prompt).strip()[0].lower()
			except Exception, e:
				choice = 'q'
			print "\nchoice is [%s]" % choice
			if choice not in "neq":
				print "Invalid option,try again!"
			else:
				chosen = True
		if choice == 'n':
			newUser()
		if choice == 'e':
			oldUser()
		if choice == 'q':
			done = True

if __name__ == '__main__':
	showMenu()