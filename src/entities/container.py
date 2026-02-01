from entity import Entity


class CapacityException(Exception):
    pass


class Container(Entity):
    def __init__(self, name, description, capacity, items=[]):
        # TODO: test
        if capacity <= 0:
            raise ValueError("Capacity must be greater than zero")

        super().__init__(name, description)
        self.capacity = capacity
        self.items = items
    
    def add_item(self, item):
        # TODO: test
        if len(self.items) == self.capacity:
            raise CapacityException("Container is full")

        self.items.append(item)
    
    def remove_item(self, item):
        # TODO: test
        return self.items.remove(item)
    
    def list_items(self):
        # TODO: test
        return self.items
