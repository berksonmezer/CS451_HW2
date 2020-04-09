from RouteManager import RouteManager
from Route import Route

import numpy as np


class GeneticAlgorithmSolver:
    def __init__(self, cities, population_size=50, mutation_rate=0.2, tournament_size=10, elitism=False):
        self.cities = cities
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.tournament_size = tournament_size
        self.elitism = elitism

    def evolve(self, routes):
        # YOUR CODE HERE
        child = self.crossover(routes.routes[0], routes.routes[1])
        return None

    def crossover(self, route_1, route_2):
        # YOUR CODE HERE
        # implement order crossover

        # create route instance to return
        child_route_instance = Route(route_1.cities)

        # get routes as lists from route instances
        route1 = route_1.route
        route2 = route_2.route

        # create sub route from route 1
        sub_route_start_index = 0
        sub_route_finish_index = 0
        indices = [sub_route_start_index, sub_route_finish_index]
        while not indices[0] < indices[1]:
            indices = np.random.randint(low=0, high=len(route1), size=2)
        sub_route_start_index = indices[0]
        sub_route_finish_index = indices[1]
        sub_route = route1[sub_route_start_index: sub_route_finish_index]

        # remove the sub route cities in route 2
        for city in route2:
            if city in sub_route:
                route2.remove(city)

        # create child route
        child_route = list()
        child_route.extend(route2[0:sub_route_start_index])
        child_route.extend(sub_route)
        child_route.extend(route2[sub_route_start_index::])

        # assign child route list to the instance returned
        child_route_instance.route = child_route
        return child_route_instance

    def mutate(self, route):
        # YOUR CODE HERE
        return

    def tournament(self, routes):
        # YOUR CODE HERE
        return None
