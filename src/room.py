from src.game import levels
from src.inventories.slotted_inventory import SlottedInventory


class Room:
    INVENTORY_SLOT_COUNT = 5

    def __init__(self, name, purpose, description, non_door_entities=[]):
        self.name = name
        self.purpose = purpose
        self.description = description
        self.non_door_entities = non_door_entities

        self.floor_inventory = SlottedInventory(self.INVENTORY_SLOT_COUNT)
        self._level = None

    @property
    def level(self):
        if self._level is not None:
            return self._level
        
        for level in levels:
            if self in level:
                self._level = level
                return self._level
        
        return None
    
    def __contains__(self, entity):
        # TODO: test
        in_non_door_entities = entity in self.non_door_entities

        if in_non_door_entities or self.level is None:
            return in_non_door_entities

        passageway_exits = self.level.get_passageway_exits(self)
        doors = [passageway_exit.door for passageway_exit in passageway_exits]
        return entity in doors
