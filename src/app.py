"""Module for rendering everything."""
import pygame


class App:
    """Class for whole app"""

    def __init__(self, name="Game", dim=(400, 450), fps=60):
        pygame.init()
        (self.width, self.height), self.fps = dim, fps
        self.clock = pygame.time.Clock()
        self.display = pygame.display.set_mode((self.width, self.height))
        self.name = name
        pygame.display.set_caption(name)


if __name__ == "__main__":
    app = App(name="Archer Game")
