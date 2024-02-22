from cashier import Cashier
import tools
import random

cashier_1 = Cashier(True, "John Doe")
cashier_2 = Cashier(True, "Julian")
cashier_3 = Cashier(True, "Sam")

for i in range(random.randint(1,10)):
    example_cart = tools.generate_Cart()
    cashier_1.scan_cart(example_cart)

for i in range(random.randint(1,10)):
    example_cart2 = tools.generate_Cart()
    cashier_2.scan_cart(example_cart2)

for i in range(random.randint(1,10)):
    example_cart3 = tools.generate_Cart()
    cashier_3.scan_cart(example_cart3)

cashier_1.amountSold()
cashier_2.amountSold()
cashier_3.amountSold()

print("\n----->>>This are the total sales:")
sales1 = Cashier.from_json("Transactions_1.json")
sales2 = Cashier.from_json("Transactions_2.json")
sales3 = Cashier.from_json("Transactions_3.json")
print("\n\nFrom Cashier 1")
Cashier.getTransactions(sales1)
print("\n\nFrom Cashier 2")
Cashier.getTransactions(sales2)
print("\n\nFrom Cashier 3")
Cashier.getTransactions(sales3)
