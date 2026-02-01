from entity import Entity


class TravelException(Exception):
    pass


class Character(Entity):
    def __init__(self, name, description, level, room):
        # TODO: test
        if room not in level:
            raise ValueError(f"Room {room} does not exist in level.")

        super().__init__(name, description)
        self.level = level
        self.room = room
    
    def goto(self, room):
        # TODO: test
        if room == self.room:
            raise TravelException(f"Already in room {room}.")

        passageway_exits = self.level.get_passageway_exits(self.room)
        passageway_exit = None

        for pe in passageway_exits:
            if pe.room == room:
                passageway_exit = pe
                break

        if passageway_exit is None:
            raise TravelException(f"Room {room} is not accessible from room {self.room}.")
        
        door = passageway_exit.door
        
        if not door.is_traversable():
            raise TravelException(f"Door {door} to room {room} is locked.")
        
        self.room = room
    