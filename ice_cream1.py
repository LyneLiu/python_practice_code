#! /usr/bin/env python
# @author:lyne

import easygui

flavor = easygui.buttonbox("What's your favorite ice cream flavor?",\
        choices = ['Vanilla','Chocolate','Strawberry'])
easygui.msgbox("you picked " + flavor)

