# Design a class Item with name, price, and quantity. Then, design a ShoppingCart class that
# manages a list of items. Implement methods to add items, remove items by name, and calculate the total
# bill. If an item already exists, updating its quantity is preferred.
# EXAMPLE INPUT
# cart = ShoppingCart()
# cart.add_item("Laptop", 50000, 1)
# cart.add_item("Mouse", 1500, 2)
# cart.remove_item("Mouse")
# print(cart.calculate_total())
# EXPECTED OUTPUT
# 50000
class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
class ShoppingCart:
    def __init__(self):
        self.items = []
    def add_item(self, name, price, quantity):
        for item in self.items:
            if item.name == name:
                item.quantity += quantity   # Update quantity
                return
        new_item = Item(name, price, quantity)
        self.items.append(new_item)
    def remove_item(self, name):
        for item in self.items:
            if item.name == name:
                self.items.remove(item)
                print(name, "removed from cart.")
                return
        print(name, "not found in cart.")
    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item.price * item.quantity
        return total
cart = ShoppingCart()
cart.add_item("Laptop", 50000, 1)
cart.add_item("Mouse", 1500, 2)
cart.remove_item("Mouse")
print("Total Bill =", cart.calculate_total())