import pygame


class Entity:
    force = 0.5
    friction = -0.12

    def __init__(self):
        self.surf = pygame.Surface((50, 50))
        self.rect = self.surf.get_rect()

        self.pos = pygame.math.Vector2((0, 0))
        self.vel = pygame.math.Vector2(0, 0)
        self.acc = pygame.math.Vector2(0, 0)

    def render(self, display: pygame.Surface):
        display.blit(self.surf, self.rect)


class Entities:
    # dummy val to identify sprite groups, and avoid infinite recursion
    _spritegroup = True

    def __init__(self):
        self.spritedict = {}
        self.lostsprites = []

    def sprites(self) -> list[Entity]:
        return list(self.spritedict)

    def add_internal(self, sprite: Entity):
        self.spritedict[sprite] = None

    def remove_internal(self, sprite: Entity):
        lost_rect = self.spritedict[sprite]
        if lost_rect:
            self.lostsprites.append(lost_rect)
        del self.spritedict[sprite]

    def has_internal(self, sprite: Entity):
        return sprite in self.spritedict

    def __iter__(self):
        return iter(self.sprites())

    def __contains__(self, sprite: Entity):
        return self.has(sprite)

    def add(self, *sprites: Entity):
        for sprite in sprites:
            if not self.has_internal(sprite):
                self.add_internal(sprite)

    def remove(self, *sprites: Entity):
        for sprite in sprites:
            if self.has_internal(sprite):
                self.remove_internal(sprite)

    def __bool__(self):
        return bool(self.sprites())

    def __len__(self):
        return len(self.sprites())

    def __repr__(self):
        return f"<{self.__class__.__name__}({len(self)} sprites)>"
