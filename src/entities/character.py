from src.entity import Entity
from src.entities.door import LockedException


class TravelException(Exception):
    pass


class Character(Entity):
    def __init__(self, name, description, entity_status, room):
        super().__init__(name, description, entity_status)
        self.room = room

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
    