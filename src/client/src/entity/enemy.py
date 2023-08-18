from entity.entity import Entity, Entities


class Enemy(Entity):
    def __init__(self):
        Entity.__init__((50, 50))
