from pygame import sprite, Surface


class Block(sprite.Sprite):
    def __init__(self, width: int = 50, height: int = 50):
        sprite.Sprite.__init__()
        self.surf = Surface((width, height))
        self.rect = self.surf.get_rect()
