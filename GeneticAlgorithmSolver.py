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

        return None

    def crossover(self, route_1, route_2):
        # YOUR CODE HERE
        # implement order crossover
        child_route_instance = Route(route_1.cities)

        route1 = route_1.route
        route2 = route_2.route
        child_route = child_route_instance.route

        sub_route_start_index = 0
        sub_route_finish_index = 0
        indices = [sub_route_start_index, sub_route_finish_index]
        while not indices[0] < indices[1]:
            indices = np.random.randint(low=0, high=len(route1), size=2)
        sub_route_start_index = indices[0]
        sub_route_finish_index = indices[1]

        sub_route = route1[sub_route_start_index: sub_route_finish_index]
        for i in range[0, len(route2)]:
            if route2[i] in sub_route:
                route2.remove(i)

        # create child route
        index = 0
        while index < sub_route_start_index:
            child_route.append(route2.pop(index))
            index += 1
        child_route.append(sub_route)
        while len(route2) > 0:
            child_route.append(route2.pop(index))
            index += 1

        return child_route_instance

    def mutate(self, route):
        # YOUR CODE HERE
        return

    def tournament(self, routes):
        # YOUR CODE HERE
        return None
