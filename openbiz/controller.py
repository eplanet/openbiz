from datetime import datetime

from openbiz.company import Company
from openbiz.airports import Airports

class Controller:
    def __init__(self, config):
        self.companies = dict()
        self.airports = Airports(config)
        self.start_date = datetime.utcnow()
    
    def add_company(self, company):
        self.companies[company.name] = company

    def get_airports_list(self):
        return self.airports.keys()

    def create_route(self, company_name, orig, dest):
        if not company_name in self.companies:
            raise ValueError
        else:
            route = Route(orig, dest, self.airports.get_distance())
            self.companies[company_name].add_route(route)

    def next_turn(self):
        for company in self.companies:
            for route in company.routes:
                pass
