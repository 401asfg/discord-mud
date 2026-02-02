import pytest

from src.inventories.weighted_inventory import WeightedInventory
from src.inventory import InventoryCapacityException
from src.item import Item


@pytest.fixture
def item_a():
    return Item("Item A", "", 5)

@pytest.fixture
def item_b():
    return Item("Item B", "", 0)

@pytest.fixture
def item_c():
    return Item("Item C", "", 30)

@pytest.fixture
def item_d():
    return Item("Item D", "", 1)

def test__weight(item_a, item_b, item_c, item_d):
    inventory = WeightedInventory(max_weight=100)
    assert inventory.weight == 0

    inventory.add_item(item_a)
    assert inventory.weight == 5

    inventory.add_item(item_b)
    assert inventory.weight == 5

    inventory.add_item(item_c)
    assert inventory.weight == 35

    inventory.remove_item(item_a)
    assert inventory.weight == 30

    inventory.add_item(item_d)
    assert inventory.weight == 31

    inventory.remove_item(item_b)
    assert inventory.weight == 31

    inventory.add_item(item_a)
    assert inventory.weight == 36

    inventory.remove_item(item_c)
    assert inventory.weight == 6

    inventory.remove_item(item_a)
    assert inventory.weight == 1

    inventory.remove_item(item_d)
    assert inventory.weight == 0

def test__can_add_item(item_a, item_b, item_c, item_d):
    inventory = WeightedInventory(max_weight=31)
    assert inventory.can_add_item(item_a) is True
    assert inventory.can_add_item(item_b) is True
    assert inventory.can_add_item(item_c) is True
    assert inventory.can_add_item(item_d) is True

    inventory.add_item(item_a)
    assert inventory.can_add_item(item_a) is True
    assert inventory.can_add_item(item_b) is True
    assert inventory.can_add_item(item_c) is False
    assert inventory.can_add_item(item_d) is True

    inventory.add_item(item_b)
    assert inventory.can_add_item(item_a) is True
    assert inventory.can_add_item(item_b) is True
    assert inventory.can_add_item(item_c) is False
    assert inventory.can_add_item(item_d) is True

    with pytest.raises(InventoryCapacityException):
        inventory.add_item(item_c)

    assert inventory.can_add_item(item_a) is True
    assert inventory.can_add_item(item_b) is True
    assert inventory.can_add_item(item_c) is False
    assert inventory.can_add_item(item_d) is True

    inventory.remove_item(item_a)
    assert inventory.can_add_item(item_a) is True
    assert inventory.can_add_item(item_b) is True
    assert inventory.can_add_item(item_c) is True
    assert inventory.can_add_item(item_d) is True

    inventory.add_item(item_d)
    assert inventory.can_add_item(item_a) is True
    assert inventory.can_add_item(item_b) is True
    assert inventory.can_add_item(item_c) is True
    assert inventory.can_add_item(item_d) is True

    inventory.remove_item(item_b)
    assert inventory.can_add_item(item_a) is True
    assert inventory.can_add_item(item_b) is True
    assert inventory.can_add_item(item_c) is True
    assert inventory.can_add_item(item_d) is True

    inventory.add_item(item_b)
    assert inventory.can_add_item(item_a) is True
    assert inventory.can_add_item(item_b) is True
    assert inventory.can_add_item(item_c) is True
    assert inventory.can_add_item(item_d) is True

    inventory.add_item(item_c)
    assert inventory.can_add_item(item_a) is False
    assert inventory.can_add_item(item_b) is True
    assert inventory.can_add_item(item_c) is False
    assert inventory.can_add_item(item_d) is False

    inventory.remove_item(item_d)
    assert inventory.can_add_item(item_a) is False
    assert inventory.can_add_item(item_b) is True
    assert inventory.can_add_item(item_c) is False
    assert inventory.can_add_item(item_d) is True

    inventory.add_item(item_d)
    assert inventory.can_add_item(item_a) is False
    assert inventory.can_add_item(item_b) is True
    assert inventory.can_add_item(item_c) is False
    assert inventory.can_add_item(item_d) is False

    inventory.remove_item(item_c)
    assert inventory.can_add_item(item_a) is True
    assert inventory.can_add_item(item_b) is True
    assert inventory.can_add_item(item_c) is True
    assert inventory.can_add_item(item_d) is True
