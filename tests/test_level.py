import pytest

from src.level import Level, build_level, DuplicateInstanceException, RoomNotInLevelException
from src.room import Room
from src.entities.door import Door
from src.entity import EntityStatus
from src.passageway import Passageway, PassagewayExit, Direction


class MockRoom(Room):
    def __init__(self):
        super().__init__("Name", "Purpose", "Description", [])


class MockDoor(Door):
    def __init__(self):
        super().__init__("Name", "Description", EntityStatus(10, 10))


class MockPassageway(Passageway):
    door: Door = MockDoor()


ROOM_WITH_NO_DIRECTIONS = MockRoom()
ROOM_WITH_NO_PASSAGEWAY_EXITS = MockRoom()
ROOM_WITH_ONE_DIRECTION_WITH_PES = MockRoom()
ROOM_WITH_MULTIPLE_DIRS_WITH_PES = MockRoom()
ROOM_WITH_ALL_DIRS_WITH_PES = MockRoom()


ROOM_DIRECTIONAL_PES = {
    ROOM_WITH_NO_DIRECTIONS: {},
    ROOM_WITH_NO_PASSAGEWAY_EXITS: {
        Direction.NORTH: [],
        Direction.SOUTH: [],
        Direction.EAST: [],
        Direction.WEST: [],
    },
    ROOM_WITH_ONE_DIRECTION_WITH_PES: {
        Direction.NORTH: [
            PassagewayExit(MockDoor(), ROOM_WITH_MULTIPLE_DIRS_WITH_PES),
            PassagewayExit(MockDoor(), ROOM_WITH_MULTIPLE_DIRS_WITH_PES),
            PassagewayExit(MockDoor(), ROOM_WITH_MULTIPLE_DIRS_WITH_PES),
        ],
    },
    ROOM_WITH_MULTIPLE_DIRS_WITH_PES: {
        Direction.SOUTH: [
            PassagewayExit(MockDoor(), ROOM_WITH_ONE_DIRECTION_WITH_PES),
            PassagewayExit(MockDoor(), ROOM_WITH_ONE_DIRECTION_WITH_PES),
            PassagewayExit(MockDoor(), ROOM_WITH_ONE_DIRECTION_WITH_PES),
            PassagewayExit(MockDoor(), ROOM_WITH_ALL_DIRS_WITH_PES),
        ],
        Direction.WEST: [
            PassagewayExit(MockDoor(), MockRoom()),
            PassagewayExit(MockDoor(), MockRoom()),
            PassagewayExit(MockDoor(), MockRoom()),
            PassagewayExit(MockDoor(), MockRoom()),
            PassagewayExit(MockDoor(), MockRoom()),
        ],
    },
    ROOM_WITH_ALL_DIRS_WITH_PES: {
        Direction.NORTH: [
            PassagewayExit(MockDoor(), ROOM_WITH_MULTIPLE_DIRS_WITH_PES),
        ],
        Direction.SOUTH: [
            PassagewayExit(MockDoor(), MockRoom()),
            PassagewayExit(MockDoor(), MockRoom()),
            PassagewayExit(MockDoor(), MockRoom()),
        ],
        Direction.EAST: [
            PassagewayExit(MockDoor(), MockRoom()),
            PassagewayExit(MockDoor(), MockRoom()),
            PassagewayExit(MockDoor(), MockRoom()),
            PassagewayExit(MockDoor(), MockRoom()),
            PassagewayExit(MockDoor(), MockRoom()),
            PassagewayExit(MockDoor(), MockRoom()),
        ],
        Direction.WEST: [
            PassagewayExit(MockDoor(), MockRoom()),
            PassagewayExit(MockDoor(), MockRoom()),
        ],
    }
}


class TestLevel:
    @pytest.fixture
    def level(self):
        return Level(ROOM_DIRECTIONAL_PES)

    def test__get_passageway_exits__empty(self):
        level = Level({})

        with pytest.raises(RoomNotInLevelException):
            level.get_passageway_exits(MockRoom())

    @pytest.mark.parametrize(
        ("room", "direction"),
        [
            (MockRoom(), None),
            (MockRoom(), Direction.NORTH),
            (MockRoom(), Direction.SOUTH),
            (MockRoom(), Direction.EAST),
            (MockRoom(), Direction.WEST),
        ]
    )
    def test__get_passageway_exits__room_not_in_level(self, room, direction, level):
        with pytest.raises(RoomNotInLevelException):
            level.get_passageway_exits(room, direction)

    @pytest.mark.parametrize(
        ("room", "direction", "expected_pes"),
        [
            (ROOM_WITH_NO_DIRECTIONS, None, []),
            (ROOM_WITH_NO_DIRECTIONS, Direction.NORTH, []),
            (ROOM_WITH_NO_DIRECTIONS, Direction.SOUTH, []),
            (ROOM_WITH_NO_DIRECTIONS, Direction.EAST, []),
            (ROOM_WITH_NO_DIRECTIONS, Direction.WEST, []),

            (ROOM_WITH_NO_PASSAGEWAY_EXITS, None, []),
            (ROOM_WITH_NO_PASSAGEWAY_EXITS, Direction.NORTH, []),
            (ROOM_WITH_NO_PASSAGEWAY_EXITS, Direction.SOUTH, []),
            (ROOM_WITH_NO_PASSAGEWAY_EXITS, Direction.EAST, []),
            (ROOM_WITH_NO_PASSAGEWAY_EXITS, Direction.WEST, []),

            (
                ROOM_WITH_ONE_DIRECTION_WITH_PES,
                None,
                ROOM_DIRECTIONAL_PES[ROOM_WITH_ONE_DIRECTION_WITH_PES][Direction.NORTH]),
            (
                ROOM_WITH_ONE_DIRECTION_WITH_PES,
                Direction.NORTH,
                ROOM_DIRECTIONAL_PES[ROOM_WITH_ONE_DIRECTION_WITH_PES][Direction.NORTH]
            ),
            (ROOM_WITH_ONE_DIRECTION_WITH_PES, Direction.SOUTH, []),
            (ROOM_WITH_ONE_DIRECTION_WITH_PES, Direction.EAST, []),
            (ROOM_WITH_ONE_DIRECTION_WITH_PES, Direction.WEST, []),

            (
                ROOM_WITH_MULTIPLE_DIRS_WITH_PES,
                None,
                (
                    ROOM_DIRECTIONAL_PES[ROOM_WITH_MULTIPLE_DIRS_WITH_PES][Direction.SOUTH]
                    + ROOM_DIRECTIONAL_PES[ROOM_WITH_MULTIPLE_DIRS_WITH_PES][Direction.WEST]
                )
            ),
            (ROOM_WITH_MULTIPLE_DIRS_WITH_PES, Direction.NORTH, []),
            (
                ROOM_WITH_MULTIPLE_DIRS_WITH_PES,
                Direction.SOUTH,
                ROOM_DIRECTIONAL_PES[ROOM_WITH_MULTIPLE_DIRS_WITH_PES][Direction.SOUTH]
            ),
            (ROOM_WITH_MULTIPLE_DIRS_WITH_PES, Direction.EAST, []),
            (
                ROOM_WITH_MULTIPLE_DIRS_WITH_PES,
                Direction.WEST,
                ROOM_DIRECTIONAL_PES[ROOM_WITH_MULTIPLE_DIRS_WITH_PES][Direction.WEST]
            ),

            (
                ROOM_WITH_ALL_DIRS_WITH_PES,
                None,
                (
                    ROOM_DIRECTIONAL_PES[ROOM_WITH_ALL_DIRS_WITH_PES][Direction.NORTH]
                    + ROOM_DIRECTIONAL_PES[ROOM_WITH_ALL_DIRS_WITH_PES][Direction.SOUTH]
                    + ROOM_DIRECTIONAL_PES[ROOM_WITH_ALL_DIRS_WITH_PES][Direction.EAST]
                    + ROOM_DIRECTIONAL_PES[ROOM_WITH_ALL_DIRS_WITH_PES][Direction.WEST]
                )
            ),
            (
                ROOM_WITH_ALL_DIRS_WITH_PES,
                Direction.NORTH,
                ROOM_DIRECTIONAL_PES[ROOM_WITH_ALL_DIRS_WITH_PES][Direction.NORTH]
            ),
            (
                ROOM_WITH_ALL_DIRS_WITH_PES,
                Direction.SOUTH,
                ROOM_DIRECTIONAL_PES[ROOM_WITH_ALL_DIRS_WITH_PES][Direction.SOUTH]
            ),
            (
                ROOM_WITH_ALL_DIRS_WITH_PES,
                Direction.EAST,
                ROOM_DIRECTIONAL_PES[ROOM_WITH_ALL_DIRS_WITH_PES][Direction.EAST]
            ),
            (
                ROOM_WITH_ALL_DIRS_WITH_PES,
                Direction.WEST,
                ROOM_DIRECTIONAL_PES[ROOM_WITH_ALL_DIRS_WITH_PES][Direction.WEST]
            ),
        ]
    )
    def test__get_passageway_exits(self, room, direction, expected_pes, level):
        assert level.get_passageway_exits(room, direction) == expected_pes


class TestBuildLevel:
    def test__no_passageways(self):
        level = build_level([])
        assert level._room_directional_passageway_exits == {}

    def test__duplicate_doors(self):
        door_a = MockDoor()
        door_b = MockDoor()
        door_c = MockDoor()

        room_a = MockRoom()
        room_b = MockRoom()
        room_c = MockRoom()
        room_d = MockRoom()

        passageway_a = Passageway(door_a, Direction.EAST, room_a, room_b)
        passageway_b = Passageway(door_a, Direction.WEST, room_b, room_a)
        passageway_c = Passageway(door_b, Direction.NORTH, room_b, room_c)
        passageway_d = Passageway(door_c, Direction.WEST, room_c, room_d)

        with pytest.raises(DuplicateInstanceException):
            build_level([
                passageway_a,
                passageway_b,
                passageway_c,
                passageway_d
            ])

        passageway_e = Passageway(door_a, Direction.WEST, room_c, room_d)

        with pytest.raises(DuplicateInstanceException):
            build_level([
                passageway_a,
                passageway_c,
                passageway_e
            ])
    
    def test__unique_doors(self):
        """
        A   ->   B        C
        ^   ->   |        
        |   <-   v        |
                          v
        D   ->   E   <-   F
        ^
        |                ||
                         vv
        G   <-   H   <-   I
        """

        room_a = MockRoom()
        room_b = MockRoom()
        room_c = MockRoom()
        room_d = MockRoom()
        room_e = MockRoom()
        room_f = MockRoom()
        room_g = MockRoom()
        room_h = MockRoom()
        room_i = MockRoom()

        passageways = [
            MockPassageway(
                direction=Direction.EAST,
                entrance_room=room_a,
                exit_room=room_b
            ),
            MockPassageway(
                direction=Direction.EAST,
                entrance_room=room_a,
                exit_room=room_b
            ),
            MockPassageway(
                direction=Direction.WEST,
                entrance_room=room_b,
                exit_room=room_a
            ),
            MockPassageway(
                direction=Direction.NORTH,
                entrance_room=room_d,
                exit_room=room_a
            ),
            MockPassageway(
                direction=Direction.SOUTH,
                entrance_room=room_b,
                exit_room=room_e
            ),
            MockPassageway(
                direction=Direction.SOUTH,
                entrance_room=room_c,
                exit_room=room_f
            ),
            MockPassageway(
                direction=Direction.EAST,
                entrance_room=room_d,
                exit_room=room_e
            ),
            MockPassageway(
                direction=Direction.WEST,
                entrance_room=room_f,
                exit_room=room_e
            ),
            MockPassageway(
                direction=Direction.NORTH,
                entrance_room=room_g,
                exit_room=room_d
            ),
            MockPassageway(
                direction=Direction.SOUTH,
                entrance_room=room_f,
                exit_room=room_i
            ),
            MockPassageway(
                direction=Direction.SOUTH,
                entrance_room=room_f,
                exit_room=room_i
            ),
            MockPassageway(
                direction=Direction.WEST,
                entrance_room=room_i,
                exit_room=room_h
            ),
            MockPassageway(
                direction=Direction.WEST,
                entrance_room=room_h,
                exit_room=room_g
            ),
        ]

        ... # TODO: write
