
from src.account import Account

class Company:
    def __init__(self, name):
        self.name = name
        self.account = Account()
        self.account.deposit(100000)
        self.routes = []
        self.slots = dict()

    def __eq__(self, other):
        return self.name == other.name

    def add_route(self, route):
        self.routes.append(route)
