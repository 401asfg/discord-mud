from src.inventories.slotted_inventory import SlottedInventory
from src.item import Item


def test__can_add_item():
    inventory = SlottedInventory(capacity=2)

    item_a = Item("Item A", "", 5)
    item_b = Item("Item B", "", 0)
    item_c = Item("Item C", "", 30)

    assert inventory.can_add_item(item_a) is True
    assert inventory.can_add_item(item_b) is True
    assert inventory.can_add_item(item_c) is True

    inventory.add_item(item_a)
    assert inventory.can_add_item(item_a) is True
    assert inventory.can_add_item(item_b) is True
    assert inventory.can_add_item(item_c) is True

    inventory.add_item(item_b)
    assert inventory.can_add_item(item_a) is False
    assert inventory.can_add_item(item_b) is False
    assert inventory.can_add_item(item_c) is False

    inventory.remove_item(item_a)
    assert inventory.can_add_item(item_a) is True
    assert inventory.can_add_item(item_b) is True
    assert inventory.can_add_item(item_c) is True

    inventory.add_item(item_b)
    assert inventory.can_add_item(item_a) is True
    assert inventory.can_add_item(item_b) is True
    assert inventory.can_add_item(item_c) is True

    inventory.remove_item(item_b)
    assert inventory.can_add_item(item_a) is True
    assert inventory.can_add_item(item_b) is True
    assert inventory.can_add_item(item_c) is True

    inventory.add_item(item_c)
    assert inventory.can_add_item(item_a) is True
    assert inventory.can_add_item(item_b) is True
    assert inventory.can_add_item(item_c) is True

    inventory.add_item(item_b)
    assert inventory.can_add_item(item_a) is False
    assert inventory.can_add_item(item_b) is False
    assert inventory.can_add_item(item_c) is False
