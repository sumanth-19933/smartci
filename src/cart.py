<<<<<<< HEAD
from src.pricing import apply_discount, add_tax
=======
"""A cart applies a discount before adding tax."""

from src.pricing import add_tax, apply_discount
>>>>>>> 7bda9eb743e7361eae97187a6b33504083fb40ed


class Cart:
    def __init__(self):
        self.items = []

    def add(self, name, price, qty=1):
<<<<<<< HEAD
        self.items.append((name, price, qty))

    def total(self, discount=0):
        subtotal = sum(p * q for _, p, q in self.items)
        return add_tax(apply_discount(subtotal, discount))
=======
        """Append an item with its unit price and quantity."""
        self.items.append((name, price, qty))

    def total(self, discount=0):
        """Calculate the subtotal, discount it, then apply default tax."""
        subtotal = sum(price * qty for _, price, qty in self.items)
        return add_tax(apply_discount(subtotal, discount))
>>>>>>> 7bda9eb743e7361eae97187a6b33504083fb40ed
