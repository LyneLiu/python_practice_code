#! /usr/bin/env python
# @author:lyne

import urllib

fileDescription = urllib.urlopen("http://publicobject.com/helloworld.txt")
message = fileDescription.read()
print message
