#! /usr//bin/env python
# -*- coding:utf-8 -*-
# @author:lyne

import sys

"print system information"
print "系统所能处理的整数范围："
print str(-sys.maxint - 1) + '<-->' + str(sys.maxint)

print "\n系统所能处理的长整数范围："
print str(sys.long_info)

print "\n系统所能处理的浮点数范围："
print str(sys.float_info)

