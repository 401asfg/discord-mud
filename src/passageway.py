from enum import Enum
from dataclasses import dataclass

from src.room import Room
from src.entities.door import Door


class Direction(Enum):
    NORTH = "north"
    SOUTH = "south"
    EAST = "east"
    WEST = "west"

    def reverse(self):
        match self:
            case Direction.NORTH: return Direction.SOUTH
            case Direction.SOUTH: return Direction.NORTH
            case Direction.EAST: return Direction.WEST
            case Direction.WEST: return Direction.EASt


@dataclass(frozen=True)
class Passageway:
    door: Door
    direction: Direction
    entrance_room: Room
    exit_room: Room


@dataclass(frozen=True)
class PassagewayExit:
    door: Door
    room: Room
