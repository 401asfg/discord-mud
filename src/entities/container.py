from entity import Entity
from inventories import SlottedInventory


class Container(Entity):
    def __init__(self, name, description, entity_status, capacity):
        super().__init__(name, description, entity_status)
        self.inventory = SlottedInventory(capacity)
    