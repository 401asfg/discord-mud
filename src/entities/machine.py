from entity import Entity


class Machine(Entity):
    def __init__(self, name, purpose, description):
        super().__init__(name, description)
        self.purpose = purpose