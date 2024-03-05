from client import Client
from server import Server

if __name__ == '__main__':
    server = Server('127.0.0.1', 8989)
    client = Client('127.0.0.1', 8989)
