#! /usr/bin/env python
# @author:lyne

from __future__ import division

def grade(score):
	"according the score,give a mark."
	if 90 <= score <= 100:
		return 'A'
	elif 80 <= score <= 89:
		return 'B'
	elif 70 <= score <= 79:
		return 'C'
	elif 60 <= score <= 69:
		return 'D'
	else:
		return 'F'

def aveScore():
	scores = raw_input("Enter your scores:")
	scoreList = scores.split()
	scoreList = [float(x) for x in scoreList]
	gradeList = [grade(x) for x in scoreList]
	print scoreList
	print gradeList
	print grade(sum(scoreList) / len(scoreList))

if __name__ == '__main__':
	aveScore()

