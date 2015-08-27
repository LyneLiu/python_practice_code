#! /usr/bin/env python
# @author:lyne

import easygui

flavor = easygui.choicebox("What's your favorite ice cream flavor?",\
        choices = ["Vanllia","Chocolate","Strawbetty"])

if flavor != None:
    easygui.msgbox("You picked " + flavor)
else:
    easygui.msgbox("You canceled the choice!")

