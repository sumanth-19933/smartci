<<<<<<< HEAD
=======
"""In-memory inventory from Lab 1."""


>>>>>>> 7bda9eb743e7361eae97187a6b33504083fb40ed
class Inventory:
    def __init__(self):
        self.stock = {}

    def add_stock(self, name, qty):
        self.stock[name] = self.stock.get(name, 0) + qty

    def remove_stock(self, name, qty):
        if self.stock.get(name, 0) < qty:
<<<<<<< HEAD
            raise ValueError('not enough stock')
        self.stock[name] -= qty
=======
            raise ValueError("not enough stock")
        self.stock[name] -= qty
>>>>>>> 7bda9eb743e7361eae97187a6b33504083fb40ed
