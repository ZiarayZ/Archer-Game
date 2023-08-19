import pygame
import client.src.entity.player as player
import client.src.entity.entity as entity
from server.server import Server


class App:
    fps = 60
    dim = (1920, 1080)

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.display = pygame.display.set_mode(self.dim)  # , pygame.FULLSCREEN)
        self.set_name("StickMario: Remastered")
        self.player = player.Player()

        self.otherPlayers = entity.Entities()
        self.enemies = entity.Entities()
        self.Server = Server()  # everyone communicates from local server

    def set_name(self, name: str = "Game"):
        pygame.display.set_caption(name)

    def main_menu(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            self.display.fill((255, 255, 255))

            pygame.display.update()
            self.clock.tick(self.fps)

    def pause_menu(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            self.display.fill((255, 255, 255))

            pygame.display.update()
            self.clock.tick(self.fps)

    def game_run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            self.display.fill((255, 255, 255))

            for entity in [*self.otherPlayers, *self.enemies]:
                # more to think on here
                entity.render(self.display)

            pygame.display.update()
            self.clock.tick(self.fps)


if __name__ == "__main__":
    App().main_menu()
