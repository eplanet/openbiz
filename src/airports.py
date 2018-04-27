import yaml
import geopy.distance

class Airports:
    def __init__(self, config):
        with open(config) as cfg:
            self.airports = yaml.load(cfg.read())
    def get_distance(self, name_a, name_b):
        lat_a = float(self.airports[name_a]["lat"])
        lat_b = float(self.airports[name_b]["lat"])
        long_a = float(self.airports[name_a]["long"])
        long_b = float(self.airports[name_b]["long"])
        return geopy.distance.vincenty((lat_a, long_a), (lat_b, long_b)).km