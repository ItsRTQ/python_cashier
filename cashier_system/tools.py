import random
"""This module contains useful methods to test the Cashier class"""
def store_items():
    items = {
        "milk" : 4.14,
        "bread" : 2.00,
        "m&m" : 1.21,
        "juice" : 2.33,
        "ice_cream" : 6.68,
        "beer" : 8.17,
        "water" : 1.28,
        "cake" : 14.44,
        "Ice_cream_cake" : 22.32,
        "doritos" : 2.16,
        "water_melon" : 5.55,
        "cookies" : 2.31,
        "yogurt" : 6.36,
        "jam" : 8.99,
        "chicken_jam" : 9.32,
        "turky" : 32.27,
        "cheess" : 5.35,
        "tortilla" : 4.24
    }
    return items

def generate_Cart(amount=0) -> dict:
    if not isinstance(amount, int) or amount == 0:
        amount = random.randint(1, 15)
    new_cart = {}
    for i in range(amount):
        item, value = random.choice(list(store_items().items()))
        new_cart[item] = value
    return new_cart