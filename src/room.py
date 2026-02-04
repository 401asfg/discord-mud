from src.game import levels, characters
from src.inventories.slotted_inventory import SlottedInventory


class NotAssignedToLevelException(Exception):
    pass


class Room:
    FLOOR_INVENTORY_SLOT_COUNT = 5

    def __init__(self, name, purpose, description, entities=[]):
        self.name = name
        self.purpose = purpose
        self.description = description
        self.entities = entities

        self.floor_inventory = SlottedInventory(self.FLOOR_INVENTORY_SLOT_COUNT)
        self._level = None

    @property
    def level(self):
        # TODO: test
        if self._level is not None:
            return self._level
        
        for level in levels:
            if self in level:
                self._level = level
                return self._level
        
        raise NotAssignedToLevelException(f"Room {self} has not been assigned to a level.")
    
    def get_exits(self):
        return self.level.get_passageway_exits(self)
    
    def __contains__(self, entity):
        # TODO: test
        in_basic_entities = entity in self.entities

        if in_basic_entities:
            return in_basic_entities
        
        for character in characters:
            if entity == character:
                return character.room == self

        doors = [passageway_exit.door for passageway_exit in self.get_exits()]
        return entity in doors
