import pytest
from src.inventory import Inventory


def test_add_stock():
    inv = Inventory()
    inv.add_stock('pen', 10)
    assert inv.stock['pen'] == 10


def test_remove_stock():
    inv = Inventory()
    inv.add_stock('pen', 10)
    inv.remove_stock('pen', 5)
    assert inv.stock['pen'] == 5


def test_remove_too_much():
    inv = Inventory()
    inv.add_stock('pen', 5)

    with pytest.raises(ValueError):
        inv.remove_stock('pen', 10)