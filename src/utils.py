from enum import Enum


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
