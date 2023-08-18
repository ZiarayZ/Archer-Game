from entity.entity import Entity, Entities


class Player(Entity):
    def __init__(self):
        Entity.__init__((50, 50))
