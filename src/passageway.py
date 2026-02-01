from enum import Enum
from dataclasses import dataclass


class Direction(Enum):
    NORTH = "north"
    SOUTH = "south"
    EAST = "east"
    WEST = "west"


REVERSE_DIRECTION_MAP = {
    Direction.NORTH: Direction.SOUTH,
    Direction.SOUTH: Direction.NORTH,
    Direction.EAST: Direction.WEST,
    Direction.WEST: Direction.EAST,
}


@dataclass
class Passageway:
    def __init__(self, door, direction, entrance_room, exit_room):
        self.door = door
        self.direction = direction
        self.entrance_room = entrance_room
        self.exit_room = exit_room


@dataclass
class PassagewayExit:
    def __init__(self, door, room):
        self.door = door
        self.room = room
