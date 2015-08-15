#! /usr/bin/env python
# @author:lyne

string = "hello world!"
sub = raw_input("Input your string:")
if sub in string:
	print "Substring!"
else:
	print "Not substring!"