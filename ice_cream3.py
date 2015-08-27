#! /usr/bin/env python
# @author:lyne

import easygui

flavor = easygui.enterbox("What's your favorite ice cream flavor?",\
                        default = "Coco")
if flavor != None:
    easygui.msgbox("You picked " + flavor)
else:
    easygui.msgbox("You canceled it!")
