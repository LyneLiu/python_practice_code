#! /usr/bin/env python
# @author:lyne

def printMyAddress(someName,houseNum):
    "multiple arguments"
    print someName
    print houseNum
    print "Main Street"
    print "Ottawa, Ontario, Canda"
    print "K2M 2E9"
    print

printMyAddress("lyne","45")
printMyAddress("bella","64")
printMyAddress("Tom Green","22")

def calculateTax(price,tax_rate):
    "if my_price exists,change it to global variable;else create a new global variable my_price"
    global my_price
    my_price = 4000
    total = price + (price * tax_rate)
    return total

my_price = float(raw_input("Enter a price:"))

totalPrice = calculateTax(my_price,0.06)
print "price =",my_price,"Total price =",totalPrice
