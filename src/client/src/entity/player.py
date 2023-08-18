import client.src.entity.entity as entity


class Player(entity.Entity):
    def __init__(self):
        entity.Entity.__init__((50, 50))
