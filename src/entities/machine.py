from entity import Entity


class Machine(Entity):
    def __init__(self, name, purpose, entity_status, description):
        super().__init__(name, description, entity_status)
        self.purpose = purpose