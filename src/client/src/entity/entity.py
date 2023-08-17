"""Renderer"""
import pygame


class Entity(pygame.sprite.Sprite):
    def __init__(self, width: int = 50, height: int = 50):
        super().__init__()
        self.surf = pygame.Surface((width, height))
        self.rect = self.surf.get_rect()
