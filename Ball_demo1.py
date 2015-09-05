#! /usr/bin/env python
# @author:lyne

class Ball:
    def __init__(self,color,size,direction):
        self.color = color
        self.size = size
        self.direction = direction

    def __str__(self):
        str = "This is a Ball class."
        return str

    def bounce(self):
        if self.direction == "down":
            self.direction = "up"


myBall = Ball("red","small","down")
print "I just created a ball."
print "My ball is",myBall.size
print "My ball is",myBall.color
print "My ball's direction is",myBall.direction
print "Now I'll bounce the ball."
print
myBall.bounce()
print "My ball's direction is",myBall.direction
print
print myBall
