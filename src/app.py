from client.client import Client
from server.server import Server


class App:
    """Class for whole app"""

    def __init__(self):
        self.Client = Client()
        self.Server = Server()  # everyone communicates from local server

    def run(self):
        """Run"""


if __name__ == "__main__":
    app = App()
    app.run()
