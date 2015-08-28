#! /usr/bin/env python
# @author:lyne


while True:
    num1 = float(raw_input("Enter the first number:"))
    num2 = float(raw_input("Enter the second number:"))
    if num1 < num2:
        print num1,"is less than",num2
    if num1 > num2:
        print num1,"is greater than",num2
    if num1 == num2:
        print num1,"is equal to",num2
    if num1 != num2:
        print num1,"is not equal to",num2

    answer = int(raw_input("Enter your answer(from 1 to 15):"))
    if answer >= 10:
        print "You got at least 10."
    elif answer >= 5:
        print "You got at least 5."
    elif answer >= 3:
        print "You got at least 3."
    else:
        print "You got less than 3."

    age = float(raw_input("Enter your age:"))
    grade = int(raw_input("Enter your grade:"))
    if age >= 8:
        if grade >= 3:
            print "You can play this game."
    else:
        print "Sorry,you can't play the game."

    print "Game over!"
    break
