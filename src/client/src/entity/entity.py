"""Renderer"""
import pygame


class Entity(pygame.sprite.Sprite):
    force = 0.5
    friction = -0.12

    def __init__(self, width: int = 50, height: int = 50):
        super().__init__()
        self.surf = pygame.Surface((width, height))
        self.rect = self.surf.get_rect()

        self.pos = pygame.math.Vector2((0, 0))
        self.vel = pygame.math.Vector2(0, 0)
        self.acc = pygame.math.Vector2(0, 0)
