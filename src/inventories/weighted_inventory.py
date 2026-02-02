from src.inventory import Inventory


class WeightedInventory(Inventory):
    def __init__(self, max_weight):
        super().__init__()
        self.max_weight = max_weight
    
    @property
    def weight(self):
        return sum(item.weight for item in self._items)
    
    def can_add_item(self, item):
        return self.weight + item.weight <= self.max_weight
