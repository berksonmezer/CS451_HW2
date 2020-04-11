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

        children = list()
        for _ in range(self.population_size):
            routes_candidates = self.tournament(routes)
            best_route = routes_candidates.find_best_route()
            routes_candidates.routes.remove(best_route)
            second_best_route = routes_candidates.find_best_route()
            child_route = self.crossover(best_route, second_best_route)
            children.append(child_route)

        routes.routes = children
        for route in routes.routes:
            self.mutate(route)

        return routes

    def crossover(self, route_1, route_2):
        # YOUR CODE HERE

        # create route instance to return
        child_route_instance = Route(route_1.cities)

        # get routes as lists from route instances
        route1 = route_1.route
        route2 = route_2.route

        # # implement cycle crossover
        # cycle_indices = [0]
        # while len(cycle_indices) <= len(route1):
        #     index = cycle_indices[-1]
        #     next_index = route1.index(route2[index])
        #     if next_index == cycle_indices[0]:
        #         break
        #     cycle_indices.append(next_index)
        # child_route = [None for i in range(len(route1))]
        # for i in range(len(route1)):
        #     if i in cycle_indices:
        #         child_route[i] = route1[i]
        #     else:
        #         child_route[i] = route2[i]

        # implement position-based crossover
        size = np.random.randint(5, 15)
        cycle_indices = np.random.choice(range(len(route1)), size, replace=False)
        child_route = [None for i in range(len(route1))]
        for i in range(len(route1)):
            if i in cycle_indices:
                child_route[i] = route1[i]
            else:
                child_route[i] = route2[i]

        # # implement order crossover
        # # create sub route from route 1
        # sub_route_start_index = 0
        # sub_route_finish_index = 0
        # indices = [sub_route_start_index, sub_route_finish_index]
        # while not indices[0] < indices[1]:
        #     indices = np.random.randint(low=0, high=len(route1), size=2)
        # sub_route_start_index = indices[0]
        # sub_route_finish_index = indices[1]
        # sub_route = route1[sub_route_start_index: sub_route_finish_index]
        #
        # # remove the sub route cities in route 2
        # temp_route = list()
        # for city in route2:
        #     if city not in sub_route:
        #         temp_route.append(city)
        #
        # # create child route
        # child_route = list()
        # child_route.extend(temp_route[0:sub_route_start_index])
        # child_route.extend(sub_route)
        # child_route.extend(temp_route[sub_route_start_index::])

        # assign child route list to the instance returned
        child_route_instance.route = child_route
        return child_route_instance

    def mutate(self, route):
        # YOUR CODE HERE

        # swap the cities randomly according to mutation rate
        for _ in range(int(len(route.route) * self.mutation_rate)):
            city1_index = 0
            city2_index = 0
            while city1_index == city2_index and city1_index > 19 and city2_index > 19:
                city1_index = int(np.around(np.random.random() * len(route.route)))
                city2_index = int(np.around(np.random.random() * len(route.route)))
            temp_city = route.route[city1_index]
            route.route[city1_index] = route.route[city2_index]
            route.route[city2_index] = temp_city

    def tournament(self, routes):
        # YOUR CODE HERE

        routes_new = RouteManager(routes.cities, routes.population_size)
        routes_selected = list()
        # indices = np.random.randint(low=0, high=len(routes.routes), size=self.tournament_size)
        indices = np.random.choice(range(len(routes.routes)), self.tournament_size, replace=False)
        for index in indices:
            routes_selected.append(routes.routes[index])
        routes_new.routes.clear()
        routes_new.routes = routes_selected

        return routes_new
