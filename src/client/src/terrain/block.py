"""Renderer"""
import pygame


class Block(pygame.sprite.Sprite):
    def __init__(self, dim=(50, 50)):
        super().__init__()
        self.surf = pygame.Surface(dim)
        self.rect = self.surf.get_rect()
