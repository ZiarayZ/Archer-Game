import src.entity.entity as entity


class Enemy(entity.Entity):
    def __init__(self):
        entity.Entity.__init__((50, 50))
