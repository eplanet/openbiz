from company import Company
from city import City

class Controller:
    def __init__(self):
        self.companies = dict()
        self.cities = dict()
    
    def add_company(self, company_name):
        self.companies[company_name] = Company()

    def add_city(self, city_name):
        self.cities[city_name] = City()

    def create_route(self, company_name, origin, dest):
        if company_name in self.companies:
