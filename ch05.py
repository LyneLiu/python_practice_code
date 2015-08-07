# -*- coding:utf-8 -*-
# enumerate demo
# @author:lyne


foo = {'host':'lyne.com','port':80}

for i,ch in enumerate(foo):
	print ch,'(%d)' % i
