#! /usr//bin/env python
# @author:lyne

def evalExp(express):
	"evaluate the expression"
	express = express.split(' ')
	if len(express) == 3:
		if express[1] == '+':
			return float(express[0]) + float(express[2])
		elif express[1] == '-':
			return float(express[0]) - float(express[2])
		elif express[1] == '*':
			return float(express[0]) * float(express[2])
		elif express[1] == '/':
			return float(express[0]) / float(express[2])
		elif express[1] == '%':
			return float(express[0]) % float(express[2])
		elif express[1] == '**':
			return float(express[0]) ** float(express[2])
		else:
			return express
	else:
		return express

def test():
	express = raw_input("please input your expression:")
	try:
		result = evalExp(express)
		print float(result)
	except Exception, e:
		print "Input Error:",e

if __name__ == '__main__':
	test()
