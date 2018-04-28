from controller import Controller
from company import Company

if __name__ == "__main__":
    c = Controller("resources/airports.yml")
    user = Company("Air France")
    c.add_company(user)
    while True:
        action = input("What to do? (route/buy/sell/next)")
        if action == "next":
            c.next_turn()
        if action == "route":
            list_airports = c.get_airports_list()
            city_a, city_b = None
            while not city_a in list_airports:
                city_a = input("City of departure (%s):" % (list_airports))
            while not city_b in list_airports:
                city_b = input("City of arrival (%s):" % (list_airports))