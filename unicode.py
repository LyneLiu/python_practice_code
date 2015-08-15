#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @author:lyne

"""
An example of reading and writing Unicode strings:
	writes a Unicode string to a file in utf-8 and read it back in.
"""

codec = 'utf-8'
fileName = 'unicode.txt'

"write the unicode to file"
hello_out = u"Hello World!"
bytes_out = hello_out.encode(codec)
f = open(fileName,'w')
f.write(bytes_out)
f.close()

"read the string from the file"
f = open(fileName,'r')
bytes_in = f.read()
hello_in = bytes_in.decode(codec)
f.close()
print hello_in
