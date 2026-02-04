from dataclasses import dataclass


class MortalityException(Exception):
    pass


@dataclass
class EntityStatus:
    def __init__(self, max_hp, hp, is_alive=True):
        # TODO: test
        if max_hp <= 0:
            raise ValueError("Maximum HP must be greater than 0.")
        
        if hp < 0:
            raise ValueError("HP must be greater than 0.")

        if hp > max_hp:
            raise ValueError("Current HP cannot exceed maximum HP.")
        
        if not is_alive and hp > 0:
            raise ValueError("An entity cannot have HP greater than 0 if they are not alive.")
        
        if is_alive and hp <= 0:
            raise ValueError("An entity cannot be alive and have hp remaining.")

        self.max_hp = max_hp
        self.hp = hp
        self.is_alive = is_alive
    
    def take_damage(self, damage):
        # TODO: test
        if damage < 0:
            raise ValueError("Damage must be a non-negative value.")

        self.hp -= damage

        if self.hp <= 0:
            self.hp = 0
            self.is_alive = False
    
    def heal(self, hp):
        # TODO: test
        if hp < 0:
            raise ValueError("Heal amount must be a non-negative value.")

        if not self.is_alive:
            raise MortalityException("Cannot heal an entity that is not alive.")

        self.hp += hp

        if self.hp > self.max_hp:
            self.hp = self.max_hp


class Entity:
    def __init__(self, name, description, entity_status):
        self.name = name
        self.description = description
        self.entity_status = entity_status
    
    def take_damage(self, damage):
        self.entity_status.take_damage(damage)
    
    def heal(self, hp):
        self.entity_status.heal(hp)
