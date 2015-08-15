#! /usr/bin/env python
# @author:lyne

def int2address(num):
        "convert integer to ip address"
	s = []
	for i in range(4):
		s.append(str(num % 256))
		num /= 256
	return '.'.join(s[::-1])

def address2int(address):
        "convert ip address to integer"
	num = 0
	for i,j in enumerate(address.split(".")[::-1]):
		num += 256 ** i * int(j)
	return long(num)

if __name__ == '__main__':
	num = long(raw_input("Enter the number:"))
	ipAddress = int2address(num)
	num = address2int(ipAddress)
	print ipAddress
	print "%r" % num
