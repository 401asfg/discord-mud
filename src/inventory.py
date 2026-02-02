from abc import ABC, abstractmethod


class InventoryCapacityException(Exception):
    pass


class ItemNotFoundException(Exception):
    pass


class Inventory(ABC):
    def __init__(self):
        self._items = set()
    
    def __contains__(self, item):
        return item in self._items

    @abstractmethod
    def can_add_item(self, item):
        pass
    
    def add_item(self, item):
        if not self.can_add_item(item):
            raise InventoryCapacityException("Cannot add item to inventory.")

        self._items.add(item)
    
    def remove_item(self, item):
        if item not in self._items:
            raise ItemNotFoundException(f"Item {item} not found in inventory.")

        return self._items.remove(item)
    
    def list_items(self):
        return self._items
    
    @staticmethod
    def _transact(sending_inventory, receiving_inventory, item, capacity_exception_msg):
        if not receiving_inventory.can_add_item(item):
            raise InventoryCapacityException(capacity_exception_msg)

        item = sending_inventory.remove_item(item)
        receiving_inventory.add_item(item)
    
    def send(self, receiving_inventory, item, capacity_exception_msg):
        # TODO: test
        self._transact(self, receiving_inventory, item, capacity_exception_msg)
    
    def receive(self, sending_inventory, item, capacity_exception_msg):
        # TODO: test
        self._transact(sending_inventory, self, item, capacity_exception_msg)