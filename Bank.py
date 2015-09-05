#! /usr/bin/env python
# @author:lyne

class BankAccount():
    def __init__(self,acct_number,acct_name):
        self.acct_number = acct_number
        self.acct_name = acct_name
        self.balance = 0.0

    def dispalyBalance(self):
        print "The account balance is:",self.balance

    def deposit(self,amount):
        self.balance = self.balance + amount
        print "You deposited",amount
        print "The new balance is:",self.balance

    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
            print "You withdraw",amount
            print "The new balance is:",self.balance
        else:
            print "You tried to withdraw",amount
            print "The account balance is:",self.balance
            print "Withdraw denied.Not enough funds."

class InterestAccount(BankAccount):
    "extend to BankAccount"
    def __init__(self,acct_number,acct_name,rate):
        BankAccount.__init__(self,acct_number,acct_name)
        self.rate = rate

    def addInterest(self):
        interest = self.balance * self.rate
        print "adding interest to account,",self.rate * 100,"percent"
        self.deposit(interest)


if __name__ == '__main__':
    myAccount = BankAccount(234567,"Lyne")
    print "Account name:",myAccount.acct_name
    print "Account number:",myAccount.acct_number
    myAccount.dispalyBalance()

    myAccount.deposit(100.34)
    myAccount.withdraw(80.98)
    myAccount.withdraw(30.96)

    print "Now we create a InterestAccount."
    myInterestAccount = InterestAccount(234567,"Bella",0.11)
    print "Account name:",myInterestAccount.acct_name
    print "Account number:",myInterestAccount.acct_number
    myInterestAccount.dispalyBalance()
    myInterestAccount.deposit(34.52)
    myInterestAccount.addInterest()
