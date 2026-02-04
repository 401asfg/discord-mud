import pytest

from src.entity import EntityStatus, MortalityException


class TestEntityStatus:
    @pytest.mark.parametrize(
        ("max_hp", "hp", "is_alive"),
        [
            (-5, -7, True),
            (-5, -5, True),
            (-5, -3, True),
            (-1, 0, True),
            (-1, 5, True),
            (-5, -7, False),
            (-5, -5, False),
            (-5, -3, False),
            (-1, 0, False),
            (-1, 5, False),
        ]
    )
    def test__init__max_hp_under_zero(self, max_hp, hp, is_alive):
        with pytest.raises(ValueError):
            EntityStatus(max_hp, hp, is_alive)

    @pytest.mark.parametrize(
        ("hp", "is_alive"),
        [
            (-2, True),
            (0, True),
            (5, True),
            (-2, False),
            (0, False),
            (5, False),
        ]
    )
    def test__init__max_hp_is_zero(self, hp, is_alive):
        with pytest.raises(ValueError):
            EntityStatus(0, hp, is_alive)

    @pytest.mark.parametrize(
        ("max_hp", "hp", "is_alive"),
        [
            (5, -1, True),
            (5, -1, False),
        ]
    )
    def test__init__hp_under_zero(self, max_hp, hp, is_alive):
        with pytest.raises(ValueError):
            EntityStatus(max_hp, hp, is_alive)
    
    @pytest.mark.parametrize(
        ("max_hp", "hp", "is_alive"),
        [
            (1, 2, True),
            (10, 20, True),
            (1, 2, False),
            (10, 20, False),
        ]
    )
    def test__init__hp_over_max_hp(self, max_hp, hp, is_alive):
        with pytest.raises(ValueError):
            EntityStatus(max_hp, hp, is_alive)

    @pytest.mark.parametrize(
        ("max_hp", "hp"),
        [
            (10, 5),
            (1, 1),
            (10, 10),
        ]
    )
    def test__init__not_alive_with_positive_hp(self, max_hp, hp):
        with pytest.raises(ValueError):
            EntityStatus(max_hp, hp, False)

    @pytest.mark.parametrize(
        ("max_hp", "hp"),
        [
            (10, 0),
        ]
    )
    def test__init__alive_with_non_positive_hp(self, max_hp, hp):
        with pytest.raises(ValueError):
            EntityStatus(max_hp, hp, True)
    
    @pytest.fixture
    def healthy_entity_status(self):
        return EntityStatus(10, 10)
    
    def test__take_damage__damage_under_zero(self, healthy_entity_status):
        with pytest.raises(ValueError):
            healthy_entity_status.take_damage(-5)
    
    def test__take_damage__damage_is_zero(self, healthy_entity_status):
        healthy_entity_status.take_damage(0)
        assert healthy_entity_status.hp == 10
        assert healthy_entity_status.is_alive
    
    def test__take_damage__non_fatal(self, healthy_entity_status):
        healthy_entity_status.take_damage(5)
        assert healthy_entity_status.hp == 5
        assert healthy_entity_status.is_alive
    
    def test__take_damage__fatal(self, healthy_entity_status):
        healthy_entity_status.take_damage(10)
        assert healthy_entity_status.hp == 0
        assert not healthy_entity_status.is_alive
    
    def test__take_damage__over_fatal(self, healthy_entity_status):
        healthy_entity_status.take_damage(20)
        assert healthy_entity_status.hp == 0
        assert not healthy_entity_status.is_alive

    def test__take_damage__already_dead(self):
        entity_status = EntityStatus(10, 0, is_alive=False)
        assert entity_status.hp == 0
        assert not entity_status.is_alive
    
    def test__heal__hp_under_zero(self, healthy_entity_status):
        with pytest.raises(ValueError):
            healthy_entity_status.heal(-5)
    
    def test__heal__hp_is_zero(self, healthy_entity_status):
        healthy_entity_status.heal(0)
        assert healthy_entity_status.hp == 10
        assert healthy_entity_status.is_alive
    
    def test__heal__not_alive(self):
        entity_status = EntityStatus(10, 0, is_alive=False)

        with pytest.raises(MortalityException):
            entity_status.heal(2)

        assert entity_status.hp == 0
        assert not entity_status.is_alive
    
    @pytest.fixture
    def wounded_entity_status(self):
        return EntityStatus(10, 5, is_alive=True)
    
    def test__heal__heal_when_already_full(self, healthy_entity_status):
        healthy_entity_status.heal(2)
        assert healthy_entity_status.hp == 10
        assert healthy_entity_status.is_alive

    def test__heal__partial_heal(self, wounded_entity_status):
        wounded_entity_status.heal(2)
        assert wounded_entity_status.hp == 7
        assert wounded_entity_status.is_alive
    
    def test__heal__full_heal(self, wounded_entity_status):
        wounded_entity_status.heal(5)
        assert wounded_entity_status.hp == 10
        assert wounded_entity_status.is_alive
    
    def test__heal__over_heal(self, wounded_entity_status):
        wounded_entity_status.heal(11)
        assert wounded_entity_status.hp == 10
        assert wounded_entity_status.is_alive
