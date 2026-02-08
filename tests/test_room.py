import pytest

from src.room import Room, NotAssignedToLevelException
from src.level import Level


class TestLevel:
    @pytest.fixture
    def room(self):
        return Room("Name", "Purpose", "Description")

    def test__no_levels(self, mocker, room):
        ... # TODO: write

    def test__not_assigned(self, mocker, room):
        ... # TODO: write

    def test__not_cached(self, mocker, room):
        ... # TODO: write

    def test__cached(self, mocker, room):
        ... # TODO: write

    def test__room_appears_in_multiple_levels(self, mocker, room):
        ... # TODO: write


class TestContains:
    def test__is_not_in_room(self):
        ... # TODO: write

    def test__is_basic_room_entity(self):
        ... # TODO: write
    
    def test__is_character__not_in_room(self):
        ... # TODO: write
    
    def test__is_character__in_room(self):
        ... # TODO: write
    
    def test__is_door__not_in_room(self):
        ... # TODO: write
    
    def test__is_door__in_room(self):
        ... # TODO: write
