from src.entity import Entity
from src.entities.door import LockedException


class NotInRoomException(Exception):
    pass


class TravelException(Exception):
    pass


def entity_interaction(interact):
    def wrapper(self, entity, *args, **kwargs):
        if entity not in self.room:
            raise NotInRoomException(f"Entity {entity} is not in the same room.")
        return interact(entity, *args, **kwargs)
    return wrapper


class Character(Entity):
    def __init__(self, name, description, entity_status, damage, room):
        super().__init__(name, description, entity_status)
        self._damage = damage
        self.room = room
    
    @property
    def damage(self):
        return self._damage
    
    def goto(self, room):
        # TODO: test
        if room == self.room:
            raise TravelException(f"Already in room {room}.")

        passageway_exit = None

        for pe in self.room.get_exits():
            if pe.room == room:
                passageway_exit = pe
                break

        if passageway_exit is None:
            raise TravelException(f"Room {room} is not accessible from room {self.room}.")
        
        door = passageway_exit.door
        
        if not door.is_traversable():
            raise LockedException(f"Door {door} to room {room} is locked.")
        
        self.room = room

    @entity_interaction
    def attack(self, entity):
        # TODO: test
        entity.take_damage(self.damage)
    