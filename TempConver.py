#! /usr/bin/env python
# @author:lyne

import easygui

while True:
    converType = easygui.buttonbox("Please choose your conversion typy!",\
            "Temperature Conversion",choices = ["Cel","Fah"])
    if not converType:break
    if converType == "Fah":
        cel = float(easygui.enterbox("Enter your celsius temperature:"))
        fah = cel * 9 / 5 + 32
        easygui.msgbox(str(cel) + " celsius convered to " + str(fah) + " fahrenheit")
    elif converType == "Cel":
        fah = float(easygui.enterbox("Enter your fahrenheit temperature:"))
        cel = (fah - 32) * 5 / 9
        easygui.msgbox(str(fah) + " fahrenheit convered to " + str(cel) + " celsius")
