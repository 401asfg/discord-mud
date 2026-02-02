from src.inventory import Inventory


class SlottedInventory(Inventory):
    def __init__(self, capacity):
        super().__init__()
        self.capacity = capacity
    
    @property
    def num_items(self):
        return len(self._items)

    def can_add_item(self, item):
        return self.num_items < self.capacity
