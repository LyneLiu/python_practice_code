# -*- coding:utf-8 -*-
# logfile demo: output of program
# @author:lyne

logfile = open('./tmp/mylog.txt','a')
print >> logfile, 'Fatal Error:invalid input'
logfile.close()
