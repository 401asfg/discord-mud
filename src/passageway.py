from dataclasses import dataclass

from src.room import Room
from src.entities.door import Door
from src.utils import Direction


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
