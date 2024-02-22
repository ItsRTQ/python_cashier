import json
import os
"""This module defines the class object that represents a cashier"""
class Cashier:
    cashier_number = 0
    current_cart = []
    daily_sells = 0

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

        self.active = active
        self.__cash = 0

    @classmethod
    def getDailySells(cls):
        rounded_amount = "{:.2f}".format(cls.daily_sells)
        return rounded_amount

    @classmethod
    def update_daily_sells(cls, amount=0) -> None:
        cls.daily_sells += amount

    @classmethod
    def clearCart(cls) -> None:
        cls.current_cart = []

    @classmethod
    def recipt(cls, items) -> None:
        cls.clearCart()
        for item in items:
            cls.current_cart.append(item)

    @classmethod
    def uploadRecipt(cls) -> None:
        filename = "Transactions.json"
        if os.path.exists(filename):
            with open(filename, 'a') as file:
                if os.stat(filename).st_size != 0:
                    file.write(",\n")

                for item in cls.current_cart:
                    json.dump(item, file)
                    file.write('\n')
        else:
            with open(filename, 'w') as file:
                for item in cls.current_cart:
                    json.dump(item, file)
                    file.write('\n')

    @property
    def getUser(self):
        return self.user
    @getUser.setter
    def setUset(self, name):
        if isinstance(name, str):
            self.user = name
        else:
            print("Fail setting user name, INVALID USER")

    @property
    def getCash(self):
        return self.__cash
    @getCash.setter
    def addCash(self, value):
        if isinstance(value, float):
            to_check = str(value).split('.')
            valid = len(to_check) == 2 and len(to_check[1]) <= 2
        if valid:
            passcode = input("Entere the admin password: ")
            if passcode == "ADMIN":
                self.__cash = value
            else:
                raise ValueError("Incorrect password, notifing manager. Please wait.")
        else:
            print("Invalid amount given, please entere a valid amount")

    def power(self):
        if self.active:
            print("Turning off, bye :D")
            self.active = False
        else:
            print("Turning on, Welcome! :D")
            self.active = True

    def charge(self, items):
        total = 0.00
        if isinstance(items, list):
            if all(isinstance(item, dict) for item in items):
                for item in items:
                    for element in item:
                        total += item[element]
            else:
                raise TypeError("Fail counting items total")
        else:
            raise ValueError("ERROR, scanning items")
        Cashier.update_daily_sells(total)
        return total
