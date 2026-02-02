import pytest

from src.item import Item, WeightException


def test__init__valid_weight():
    item = Item("Sword", "A sharp blade.", 10)
    assert item.name == "Sword"
    assert item.description == "A sharp blade."
    assert item.weight == 10

def test__init_zero_weight():
    item = Item("Feather", "A light feather.", 0)
    assert item.name == "Feather"
    assert item.description == "A light feather."
    assert item.weight == 0

def test__init_negative_weight():
    with pytest.raises(WeightException):
        Item("Rock", "A heavy rock.", -5)
