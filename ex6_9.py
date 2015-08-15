#! /usr/bin/env python
# @author:lyne

def convertMinutes():
    "convert minutes to hours."
    minutes = int(raw_input("Enter your minutes:"))
    (hours,remainMinutes) = divmod(minutes,60)
    print """
%d minutes can be converted to %d hours and %d minutes.""" % \
(minutes,hours,remainMinutes)

if __name__ == "__main__":
    convertMinutes()
