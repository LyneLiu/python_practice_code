#! /usr/bin/env python
# @author:lyne

class HotDog:
    def __init__(self):
        "when create a hog dog instance,we initiate it."
        self.cookied_level = 0
        self.cookied_string = "raw"
        self.condiments = []

    def __str__(self):
        msg = "hot dog"
        if len(self.condiments) > 0:
            msg = msg + " with"
        for i in self.condiments:
            msg = msg + i + ", "
        msg = msg.strip(", ")
        msg = self.cookied_string + " " + msg + "."
        return msg

    def cook(self,time):
        "cookie the hog dog,we need to change the attributes"
        self.cookied_level = self.cookied_level + time
        if self.cookied_level > 8:
            self.cookied_string = "Charcoal"
        elif self.cookied_level > 5:
            self.cookied_string = "Well-done"
        elif self.cookied_level > 3:
            self.cookied_string = "Medium"
        else:
            self.cookied_string = "Raw"

    def addCondiment(self,condiment):
       self.condiments.append(condiment)


myDog = HotDog()
print myDog
print "Cooking hot dog for 4 minutes..."
myDog.cook(4)
print myDog
print "Cooking hot dog for 3 more minutes..."
myDog.cook(3)
print myDog
print "What happens if I cook it for 10 more minutes?"
myDog.cook(10)
print myDog
print "Now,I'm going to add some stuff on my hot dog"
myDog.addCondiment("ketchup")
myDog.addCondiment("mustard")
print myDog
