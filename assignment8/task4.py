class ShoppingCart:
    """ShoppingCart with add_item, remove_item, and total_cost methods."""

    def __init__(self):
        self.items = {}

    def add_item(self, name, price):
        if price < 0:
            return "Invalid price"
        self.items[name] = self.items.get(name, 0) + price
        return f"{name} added."

    def remove_item(self, name):
        if name in self.items:
            del self.items[name]
            return f"{name} removed."
        return "Item not found."

    def total_cost(self):
        return sum(self.items.values())


# --- AI-generated Test Cases ---
cart = ShoppingCart()
print("\n✅ ShoppingCart Test Results:")
print(cart.add_item("Apple", 50))      # Add
print(cart.add_item("Banana", 30))     # Add
print(cart.add_item("Apple", 50))      # Add duplicate (adds up)
print("Total:", cart.total_cost())     # 130 expected
print(cart.remove_item("Banana"))      # Remove
print(cart.remove_item("Orange"))      # Not found
print("Total:", cart.total_cost())     # 100 expected
