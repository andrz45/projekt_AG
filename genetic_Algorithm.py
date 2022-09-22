from cmath import acos, asin, pi, sqrt
from cmath import cos
from math import fabs
import pylab as lab

import random
from random import randint
from random import sample
from variables import *
from functions import *
import numpy as np


class individual():

    def __init__(self, start_point, end_point):
        self.start_point = start_point
        self.end_point = end_point

    def wayPoints(self):
        way_points = [(randint(0, 10), randint(0, 10), randint(0, 10)) for i in range(number_of_wayPoints)] # współrzędne x,y,z  w zakresie od 0-200 oraz ilość punktów pośrednich 
        set_wayPoints = []
        for i in range(len(way_points)):
            set_wayPoints.append(way_points[i])
        return set_wayPoints  

    def first_population_generator(self):
        return [(start_point + sample(self, len(self)) + end_point) for _ in range(size_of_population)]

def mutation(individual):
    if(random.random() < mutation_rate):
        one = randint(1, len(individual) - 2) 
        two = randint(1, len(individual) - 2)
        individual[one], individual[two] = individual[two], individual[one]
    return individual

def crossover(route1, route2):
    child_point = []
    child_point=route1[1:int(len(route1) / 2)]
    for point in route2:
        if point not in child_point and point not in end_point + start_point:
            child_point.append(point)
    return (end_point + child_point + start_point)
 

def energy_cost_of_route(first_population): 
    for route in first_population:
        movement_angle(route)
        # print(distance_between_point)
        # print(angle_table)    
        cost.append(energy_cost(distance_between_point,angle_table))
    return cost


def fitness(first_population, cost):
    best_individual = []
    value_of_fitness = 100000
    for i in range(len(first_population)):
        cost_one_route = cost[i]
        if cost_one_route < value_of_fitness:
            value_of_fitness = cost_one_route
            best_individual = first_population[i]
    return [best_individual, value_of_fitness]


def selection(routes_and_cost, size_of_population, size_of_best_individual):
    next_population = []
    best_routes = []
    for i in range(size_of_best_individual):
        x = routes_and_cost.pop(0)
        best_routes.append(x[0])

    population = []
    fitness = []
    for route in routes_and_cost:
        population.append(route[0])
        fitness.append(route[1])

    ratio = []
    sum_fitness=sum(fitness)
    for i in range(len(fitness)):
        ratio.append(sum_fitness/fitness[i])

    next_population = random.choices(population, weights=ratio, k=size_of_population-size_of_best_individual)
    next_population.extend(best_routes)

    return next_population



def next_population(first_population, size_of_population, size_of_best_individual):
    routes_and_cost = []
    for i in range(len(first_population)):
        routes_and_cost.append((first_population[i], cost[i]))

    sorted_population = sorted(routes_and_cost, key=lambda x: x[1])
    next_population = selection(sorted_population, size_of_population, size_of_best_individual)

    return next_population



def algorytm():

    first_individual = individual(start_point, end_point).wayPoints() #instancje klasy individual, wszystkie punkty przez które ma przelecieć dron oraz startowy i końcowy
    first_population = individual.first_population_generator(first_individual)

    # result = [[],10,0]
    result = []
    for population_num in range(number_of_population):

        energy_cost_of_route(first_population)

        

        best_route = fitness(first_population, cost)
        best_route.append(population_num)
        # if best_route[1] < result[1]:
            # result = best_route
        result.append(best_route)
        


        distance_between_point.clear()
        angle_table.clear()
        cost.clear()

        x = randint(0, len(first_population)-1)
        first_population[x] = mutation(first_population[x])

        y = crossover(first_population[randint(0, len(first_population)-1)],first_population[randint(0, len(first_population)-1)])
        first_population.append(y)

        energy_cost_of_route(first_population)
        first_population = next_population(first_population, size_of_population, size_of_best_individual)

        distance_between_point.clear()
        angle_table.clear()
        cost.clear()

    return result

a = algorytm()
print(a)



x = []
y = []
for i in range(len(a)):
    x.append(a[i][2])

for i in range(len(a)):
    y.append(a[i][1])



lab.plot(x,y)
lab.show()
