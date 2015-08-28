#! /usr/bin/env python
# @author:lyne

price = float(raw_input("Enter your price:"))
account = 0

if price <= 10:
    print "you can take 10% payoff."
    count = 0.9
    print "payoff price result:",price * count
else:
    print "you can take 20% payoff."
    count = 0.8
    print "payoff price result:",price * count

