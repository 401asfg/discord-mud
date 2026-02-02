from entity import Entity


class Door(Entity):
    def __init__(self, name, description, entity_status, is_locked=False):
        super().__init__(name, description, entity_status)
        self.is_locked = is_locked
    
    def is_traversable(self):
        return not self.is_locked
        