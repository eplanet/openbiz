
class Route:
    def __init__(self, orig, dest, distance):
        self.orig = orig
        self.dest = dest
        self.distance = distance
        self.planes = 1
        self.balance = 0

    def get_cost(self):
        return 15 * self.distance * self.planes

    def get_profit(self):
        return 