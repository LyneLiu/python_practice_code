#! /usr/bin/env python
# @author:lyne

num = raw_input("Enter a number:")
try:
        numList = list(num)
        dic = {'0':'zero','1':'one','2':'two','3':'three','4':'four','5':'five','6':'six',\
               '7':'seven','8':'eight','9':'nine'}
        
        result = ""
        for i in numList:
                result = result + dic[i] + "-"
        result = result[:-1]
        print result
except Exception, e:
	print "Input Error:",e
