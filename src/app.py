from client.client import Client
from server.server import Server


class App:
    def __init__(self):
        self.Client = Client()
        self.Server = Server()  # everyone communicates from local server

    def run(self):
        self.Client.run()


if __name__ == "__main__":
    App().run()
