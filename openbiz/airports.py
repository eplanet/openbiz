import yaml
import geopy.distance

class Airport():
    def __init__(self, name, lat, lng, traffic, pop):
        self.name = name
        self.lat = lat
        self.lng = lng
        self.traffic = traffic
        self.pop = pop
    def get_distance(self, other):
        return geopy.distance.vincenty((self.lat, self.lng), (other.lat, other.lng)).km

class Airports:
    def __init__(self, config):
        self.airports = dict()
        with open(config) as cfg:
            parsed_config = yaml.load(cfg.read())
            for airport in parsed_config:
                self.airports[airport] = Airport(
                    airport,
                    parsed_config[airport]["lat"],
                    parsed_config[airport]["long"],
                    parsed_config[airport]["traffic"],
                    parsed_config[airport]["population"]
                    )
    def get_distance(self, name_a, name_b):
        return self.airports[name_a].get_distance(self.airports[name_b])
    def get_rounded_distance(self, name_a, name_b):
        return int(self.get_distance(name_a, name_b))