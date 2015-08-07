# -*- coding:utf-8 -*-
# class demo
# @author:lyne

class FooClass(object):
    """ my first class:FooClass """
    version = 1.0   # class (data) attribute
    def __init__(self,nm='lyne'):
        """constructor"""
        self.name=nm  # class instance (data) attribute
        print "create the class instance for",nm
    def showname(self):
        """display instance attribute and class name"""
        print "your name is",self.name
        print "my name is",self.__class__.__name__
    def showver(self):
        """display the version of class"""
        print "class version",self.version     # references FooClass.version
    def addMe2Me(self,x):   # does not use self
        """apply + operation to argument"""
        return(x + x)

