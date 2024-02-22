import json
import os
"""This module defines the class object that represents a cashier"""
class Cashier:
    cashier_number = 0

    def __init__(self, active=False, user=None, number=None) -> None:
        if not isinstance(active, bool):
            raise TypeError("Unknown Type for cashier activity")

        if not number or not isinstance(number, int):
            Cashier.cashier_number += 1
            self.number = Cashier.cashier_number
        else:
            self.number = Cashier.cashier_number = number

        if not isinstance(active, bool):
            raise TypeError("The cashier activity must be: (True/False)")

        if isinstance(user, str) or not user:
            self.user = user
        else:
            print("Invalid user, setting user to None")
            self.user = None

        self.current_cart = {}
        self.daily_sells = 0.00
        self.active = active
        self.__cash = 0
    
    @classmethod
    def from_json(cls, filename):
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                loaded_data = json.load(file)
            return loaded_data
        else:
            raise FileExistsError("File [{}] was not found".format(filename))
    @classmethod
    def getTransactions(cls, Transactions):
        Total_transactions = 0
        if not isinstance(Transactions, list) and all(isinstance(ele, dict) for ele in Transactions):
            raise TypeError("The recipts must be a list of dictionarys")
        for num, i in enumerate(Transactions, start=1):
            print("\n>>>>>>CART {}".format(num))
            total = 0
            for j in i:
                print("{} = {}".format(j, i[j]))
                total += i[j]
            Total_transactions += float("{:.2f}".format(total))
            print("Total of: {:.2f}".format(total))
        print("\nTotal in transactions was {:.2f}".format(Total_transactions))
        return float("{:.2f}".format(Total_transactions))

    def CashOut(self):
        if self.__cash >= 1000.00:
            print("Calling manager, cashout needed")
            self.__cash = 200.00

    def getDailySells(self):
        rounded_amount = "{:.2f}".format(self.daily_sells)
        return rounded_amount

    def update_daily_sells(self, amount=0) -> None:
        self.daily_sells += amount

    def clearCart(self) -> None:
        self.current_cart = []

    def recipt(self, items={}) -> None:
        if items:
            self.clearCart()
            self.current_cart = items

    def uploadRecipt(self) -> None:
        filename = "Transactions_" + str(self.number) + ".json"
        existing_data = []
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                existing_data = json.load(file)
        existing_data.append(self.current_cart)
        with open(filename, 'w') as file:
            json.dump(existing_data, file, indent=2)

    @property
    def getUser(self):
        return self.user
    @getUser.setter
    def setUser(self, name):
        if isinstance(name, str):
            self.user = name
        else:
            print("Fail setting user name, INVALID USER")

    @property
    def getCash(self):
        return "{:.2f}".format(self.__cash)
    @getCash.setter
    def addCash(self, value):
        if isinstance(value, float):
            to_check = str(value).split('.')
            valid = len(to_check) == 2 and len(to_check[1]) <= 2
        if valid:
            passcode = input("Entere the admin password: ")
            if passcode == "ADMIN":
                self.__cash = value
                self.CashOut()
            else:
                raise ValueError("Incorrect password, notifing manager. Please wait.")
        else:
            print("Invalid amount given, please entere a valid amount")

    def power(self):
        if self.active:
            name = input("Enter Cashier Name: ")
            if name:
                print("Turning off, bye :D")
                self.active = False
            else:
                print("Invalid name, denided Activation")
        else:
            print("Turning on, Welcome! :D")
            self.active = True

    def charge(self, items={}):
        total = 0.00
        if isinstance(items, dict):
            self.recipt(items)
            for item in items:
                total += items[item]
        else:
            raise ValueError("ERROR, scanning items")
        return total

    def pay(self, amount_to_charge):
        self.update_daily_sells(amount_to_charge)
        while amount_to_charge != 0:
            amount_to_charge = float("{:.2f}".format(amount_to_charge))
            #recive = float(input("Enter given amount: "))
            recive = amount_to_charge
            change = 0.00
            if recive > amount_to_charge:
                change = recive - amount_to_charge
                self.__cash += amount_to_charge
                amount_to_charge = 0
                print("Return {:.2f}".format(change))
            elif recive < amount_to_charge:
                amount_to_charge -= recive
                self.__cash += recive
                print("New total is {:.2f}".format(amount_to_charge))
            elif recive == amount_to_charge:
                amount_to_charge = 0
                self.__cash += recive
        self.uploadRecipt()

    def scan_cart(self, cart):
        if not isinstance(cart, dict):
            raise TypeError("Invalid, cart must be a dict")
        amount_to_charge = self.charge(cart)
        #print("Your total is: {:.2f}".format(amount_to_charge))
        #is_paying = input("--->>> Do you want to charge: ")
        #if is_paying.lower() == "yes":
        #    self.pay(float("{:.2f}".format(amount_to_charge)))
        #else:
        #    pass
        self.pay(float("{:.2f}".format(amount_to_charge)))

    def amountSold(self):
        sentence = "Cashier " + self.user + " sold today: {:.2f}".format(self.daily_sells)
        print(sentence)
        return float("{:.2f}".format(self.daily_sells))