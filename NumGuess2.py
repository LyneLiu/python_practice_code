#! /usr/bin/env python
# @author:lyne

import random,easygui

secret = random.randint(1,99)
guess = 0
tries = 0

easygui.msgbox("""AHOY! I'm the Dread Pirate Roberts, and I have a secret!
It is a number from 1 to 99. I'll give 6 tries to guess it!""")

while guess != secret and tries < 6:
    guess = easygui.integerbox("What is your guess,matey?")
    if not guess:break
    if guess < secret:
        easygui.msgbox(str(guess) + " is too low,ye scurvy dog!")
    elif guess > secret:
        easygui.msgbox(str(guess) + " is too high,landlubber!")
    tries += 1

if guess == secret:
    easygui.msgbox("Avast! Ye got it! Found my secret,you did it!")
else:
    easygui.msgbox("No more guesses!Better luck next time,matey!")
