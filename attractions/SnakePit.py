class SnakePit():

    def __init__(self, attraction_name, description):
        self.attraction_name = attraction_name
        self.description = description
        self.animals = []

    def addAnimals(self, coll):
        self.animals.extend(coll)
