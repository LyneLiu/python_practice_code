#! /usr/bin/env python
# @author:lyne

class GameObject:
    def __init__(self,name):
        self.name = name

    def pickUp(self,player):
        pass
        # put code here to add the oject
        # to the player's collection

class Coin(GameObject):
    def __init__(self,value):
        GameObject.__init__(self)
        self.value = value

    def spend(self,buyer,seller):
        pass
        # put code here to remove the coin
        # remove the buyer's money and
        # add it to the saller's money


