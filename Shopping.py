from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @abstractmethod
    def calculate_discount(self):
        pass

    def final_price(self):
        return self.price - self.calculate_discount()
class Electronics(Product):
    def calculate_discount(self):
        return self.price * 0.10

class Clothing(Product):
    def calculate_discount(self):
        return self.price * 0.15

class Grocery(Product):
    def calculate_discount(self):
        return self.price * 0.05
        
class Shoppingcart:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        self.items.append(product)
        print(f"{product.name} added to cart.")

    def remove_product(self, product_name):
        for item in self.items:
            if item.name == product_name:
                self.items.remove(item)
                print(f"{product_name} removed from cart.")
                return
        print("Item not found")

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item.final_price()
        return total

    def checkout(self):
        if not self.items:
            print("Cart is empty")
            return

        print("\n--- Checkout ---")
        for item in self.items:
            print(f"{item.name} → Rs {item.final_price():.2f}")

        print(f"\nTotal Bill: Rs {self.calculate_total():.2f}")
        print("Thank you for shopping!")
        
cart = Shoppingcart()

p1 = Electronics("Mobile", 30000)
p2 = Clothing("Jacket", 5500)
p3 = Grocery("RiceBag", 4500)

cart.add_product(p1)
cart.add_product(p2)
cart.add_product(p3)

cart.remove_product("RiceBag")

cart.checkout()

