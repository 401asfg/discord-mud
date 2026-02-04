from src.entities.character import Character, entity_interaction
from src.inventories.weighted_inventory import WeightedInventory
from src.inventory import ItemNotFoundException


class Player(Character):
    def __init__(
        self,
        name,
        description,
        entity_status,
        room,
        unarmed_damage,
        max_carry_weight,
    ):
        super().__init__(name, description, entity_status, unarmed_damage, room)
        self.inventory = WeightedInventory(max_carry_weight)
        self.weapon = None
    
    @property
    def damage(self):
        return self.weapon.damage if self.weapon else super().damage

    def examine_room_purpose(self):
        return self.room.purpose
    
    def examine_room_description(self):
        # FIXME: describe floor inventory items
        return self.room.description
    
    @entity_interaction
    def examine_entity(self, entity):
        # TODO: test
        return entity.description
    
    @entity_interaction
    def search(self, container):
        # TODO: test
        return container.show_contents()
    
    @entity_interaction
    def loot(self, container, item):
        # TODO: test
        self.inventory.receive(
            container.inventory,
            item,
            "Cannot loot item without going over inventory capacity."
        )
    
    @entity_interaction
    def deposit(self, container, item):
        # TODO: test
        self.inventory.send(
            container.inventory,
            item,
            "Cannot deposit item into container without going over its capacity."
        )
    
    @entity_interaction
    def give(self, player, item):
        # TODO: test
        self.inventory.send(
            player.inventory,
            item,
            "Cannot give item without the other player going over inventory capacity."
        )
    
    def pickup(self, item):
        # TODO: test
        self.inventory.receive(
            self.room.floor_inventory,
            item,
            "Cannot pick up item without going over inventory capacity."
        )
    
    def drop(self, item):
        # TODO: test
        self.inventory.send(
            self.room.floor_inventory,
            item,
            "There is no more room on the floor to drop items."
        )
    
    # TODO: implement
    """
    - different levels of examination
    - examining the exits of a room
    - examining entity statuses
    - examining an item in own inventory
    - examining an item in a container
    """
    
    def equip(self, weapon):
        # TODO: test
        if weapon not in self.inventory:
            raise ItemNotFoundException(f"Weapon {weapon} not found in inventory.")

        self.weapon = weapon
    
    def dequip(self):
        # TODO: test
        self.weapon = None
