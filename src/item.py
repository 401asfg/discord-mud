class WeightException(Exception):
    pass


class Item:
    def __init__(self, name, description, weight):
        if weight < 0:
            raise WeightException("Item weight cannot be negative.")

        self.name = name
        self.description = description
        self.weight = weight
