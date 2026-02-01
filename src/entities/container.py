from entity import Entity
from inventories import SlottedInventory


class Container(Entity):
    def __init__(self, name, description, capacity):
        super().__init__(name, description)
        self.inventory = SlottedInventory(capacity)
