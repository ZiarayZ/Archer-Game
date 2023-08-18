from pygame import sprite, Surface, math


class Entity(sprite.Sprite):
    force = 0.5
    friction = -0.12

    def __init__(self, width: int = 50, height: int = 50):
        super().__init__()
        self.surf = Surface((width, height))
        self.rect = self.surf.get_rect()

        self.pos = math.Vector2((0, 0))
        self.vel = math.Vector2(0, 0)
        self.acc = math.Vector2(0, 0)

    def render(self, display: Surface):
        display.blit(self.surf, self.rect)


class Entities(sprite.AbstractGroup):
    def __init__(self, *sprites: Entity):
        sprite.AbstractGroup.__init__(self)
        self.add(*sprites)

    # Used so iter knows type
    def sprites(self) -> list[Entity]:
        return list(self.spritedict)

    def __iter__(self):
        return iter(self.sprites())
