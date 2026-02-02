import pytest

from src.inventory import Inventory, InventoryCapacityException, ItemNotFoundException
from src.item import Item


class MockInventory(Inventory):
    def can_add_item(self, item):
        return True


@pytest.fixture
def inventory():
    return MockInventory()

@pytest.fixture
def item_a():
    return Item("Item A", "", 5)    

@pytest.fixture
def item_b():
    return Item("Item B", "", 0)    

@pytest.fixture
def item_c():
    return Item("Item C", "", 30)    

def test__init(inventory):
    assert inventory.list_items() == set()

def test__add_item__success(inventory, item_a, item_b, item_c):
    inventory.add_item(item_a)
    assert inventory.list_items() == {item_a}
    inventory.add_item(item_b)
    assert inventory.list_items() == {item_a, item_b}

    inventory.add_item(item_a)
    assert inventory.list_items() == {item_a, item_b}

    inventory.add_item(item_c)
    assert inventory.list_items() == {item_a, item_b, item_c}

def test__add_item__failure(inventory, item_a):
    class FailingInventory(Inventory):
        def can_add_item(self, item):
            return False

    failing_inventory = FailingInventory()

    with pytest.raises(InventoryCapacityException):
        failing_inventory.add_item(item_a)

def test__remove_item(inventory, item_a, item_b, item_c):
    inventory.add_item(item_a)

    with pytest.raises(ItemNotFoundException):
        inventory.remove_item(item_b)

    assert inventory.list_items() == {item_a}

    inventory.remove_item(item_a)
    assert inventory.list_items() == set()


    with pytest.raises(ItemNotFoundException):
        inventory.remove_item(item_a)

    assert inventory.list_items() == set()

    inventory.add_item(item_a)
    inventory.add_item(item_b)
    inventory.remove_item(item_a)
    assert inventory.list_items() == {item_b}

    with pytest.raises(ItemNotFoundException):
        inventory.remove_item(item_a)

    assert inventory.list_items() == {item_b}

    inventory.add_item(item_c)
    inventory.add_item(item_a)
    inventory.remove_item(item_b)
    assert inventory.list_items() == {item_c, item_a}

    inventory.remove_item(item_c)
    assert inventory.list_items() == {item_a}

    inventory.add_item(item_c)
    inventory.add_item(item_b)
    inventory.remove_item(item_c)
    assert inventory.list_items() == {item_a, item_b}