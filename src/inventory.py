from abc import ABC, abstractmethod


class InventoryAddItemException(Exception):
    pass


class Inventory(ABC):
    def __init__(self):
        self._items = []

    @abstractmethod
    def can_add_item(self, item):
        pass
    
    def add_item(self, item):
        if not self.can_add_item(item):
            raise InventoryAddItemException("Cannot add item to inventory.")

        self._items.append(item)
    
    def remove_item(self, item):
        # TODO: test
        return self._items.remove(item)
    
    def list_items(self):
        # TODO: test
        return self._items
