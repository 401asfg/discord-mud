from passageway import Passageway, PassagewayExit
from typing import List


class DuplicateInstanceException(Exception):
    pass


class RoomNotInLevelException(Exception):
    pass


class Level:
    def __init__(self, room_directional_passageway_exits):
        self._room_directional_passageway_exits = room_directional_passageway_exits
    
    def __contains__(self, room):
        return room in self._room_directional_passageway_exits
    
    def get_passageway_exits(self, room, direction=None):
        # TODO: test
        if room not in self:
            raise RoomNotInLevelException("Room is not in this level.")

        directional_passageway_exits = self._room_directional_passageway_exits.get(room, {})

        if direction is not None:
            return directional_passageway_exits.get(direction, [])
        
        all_passageway_exits = []

        for passageway_exits in directional_passageway_exits.values():
            all_passageway_exits.extend(passageway_exits)
        
        return all_passageway_exits


def build_level(passageways: List[Passageway]) -> Level:
    # TODO: test
    # TODO: validate all rooms are reachable from starting_room?
    room_directional_passageway_exits = {}

    def add_passageway_exit(entrance_room, direction, passageway_exit):
        if entrance_room not in room_directional_passageway_exits:
            room_directional_passageway_exits[entrance_room] = {}
        
        directional_passageway_exits = room_directional_passageway_exits[entrance_room]

        if direction not in directional_passageway_exits:
            directional_passageway_exits[direction] = set()
        
        passageway_exits = directional_passageway_exits[direction]
        passageway_exit = PassagewayExit(door, exit_room)
        passageway_exits.add(passageway_exit)

    doors = set()

    for passageway in passageways:
        door = passageway.door

        if door in doors:
            raise DuplicateInstanceException(f"Duplicate door found: {door}")
        
        doors.add(door)
        
        direction = passageway.direction
        entrance_room = passageway.entrance_room
        exit_room = passageway.exit_room

        add_passageway_exit(entrance_room, direction, PassagewayExit(door, exit_room))
        add_passageway_exit(exit_room, direction.reverse(), PassagewayExit(door, entrance_room))
    
    return Level(room_directional_passageway_exits)
