from entity import Entity


class Door(Entity):
    def __init__(self, name, description, is_locked=False):
        super().__init__(name, description)
        self.is_locked = is_locked
    
    def is_traversable(self):
        return not self.is_locked
        