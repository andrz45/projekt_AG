from variables import *
from cmath import acos, asin, pi, sqrt
from cmath import cos
from math import fabs


# def distance_point(population):
#     for individual in population:
#         table = []
#         for i in range(len(individual)-1):
#             distance = sqrt((individual[i + 1][0] - individual[i][0])**(2) + (individual[i + 1][1]-individual[i][1])**(2) + (individual[i + 1][2]-individual[i][2])**(2))  #------> wzór na odległość między ptk w 3D
#             table.append(distance.real)
#         distance_between_point.append(table)
#     return distance_between_point


def distance_point(individual):
    for i in range(len(individual)-1):
        distance = sqrt((individual[i + 1][0] - individual[i][0])**(2) + (individual[i + 1][1]-individual[i][1])**(2) + (individual[i + 1][2]-individual[i][2])**(2))  #------> wzór na odległość między ptk w 3D
        distance_between_point.append(distance.real)
    return distance_between_point


def movement_angle(individual):
        angle_table.clear()
        distance_between_point.clear()
        xxxx = []
        xxxx = distance_point(individual)
        for i in range(len(individual)-1):
            if (individual[i][2]-individual[i+1][2]) == 0:
                if (individual[i][1]-individual[i+1][1]) == 0:
                    angle = 0
                else:
                    angle = 0
            else:
                if individual[i][2] > individual[i+1][2]:
                    sin_angle = ((individual[i+1][2]-individual[i][2])/xxxx[i])
                    angle = asin(sin_angle)*180/(pi)
                else:
                    sin_angle = (fabs(individual[i][2]-individual[i+1][2])/xxxx[i])
                    angle = asin(sin_angle)*180/(pi) 
            angle_table.append(angle.real)
        return  angle_table


# def movement_angle(population, distance_between_point):
#     for route in population:
#         xxxx = []
#         xxxx = distance_point(route)
#         table = []
#         for i in range(len(route)-1):
#             if (route[i][2]-route[i+1][2]) == 0:
#                 if (route[i][1]-route[i+1][1]) == 0:
#                     angle = 0
#                 else:
#                     angle = 0
#             else:
#                 if route[i][2] > route[i+1][2]:
#                     sin_angle = ((route[i+1][2]-route[i][2])/xxxx[i])
#                     angle = asin(sin_angle)*180/(pi)
#                 else:
#                     sin_angle = (fabs(route[i][2]-route[i+1][2])/xxxx[i])
#                     angle = asin(sin_angle)*180/(pi) 
#             table.append(angle.real) 
#         angle_table.append(table)
#         return  angle_table


# def energy_cost(distance_between_point, angle_table):
#     sum_energy = 0
#     for distance in distance_between_point:
#         for i in range(len(distance)):
#             if angle_table[i] > 45:
#                 energy = ((((angle_table[i]*up_90)/90)*distance[i])/100)
#             elif angle_table[i] < 45 and angle_table[i] > 0:
#                 energy = ((((angle_table[i]*up_45)/90)*distance[i])/100)
#             elif angle_table[i] == 0:
#                 energy = ((distance[i]*forward_0)/100)
#             elif angle_table[i] < 0 and angle_table[i] > -45:
#                 energy = (((fabs(angle_table[i]*down_45)/90)*distance[i])/100)    
#             else:
#                 energy = ((((fabs(angle_table[i])*down_90)/90)*distance[i])/100)      
#             sum_energy += energy
#         return sum_energy


def energy_cost(distance_between_point, angle_table):
    sum_energy = 0
    for i in range(len(distance_between_point)):
        if angle_table[i] > 45:
            energy = ((((angle_table[i]*up_90)/90)*distance_between_point[i])/100)
        elif angle_table[i] < 45 and angle_table[i] > 0:
            energy = ((((angle_table[i]*up_45)/90)*distance_between_point[i])/100)
        elif angle_table[i] == 0:
            energy = ((distance_between_point[i]*forward_0)/100)
        elif angle_table[i] < 0 and angle_table[i] > -45:
            energy = (((fabs(angle_table[i]*down_45)/90)*distance_between_point[i])/100)    
        else:
            energy = ((((fabs(angle_table[i])*down_90)/90)*distance_between_point[i])/100)      
        sum_energy += energy
    return sum_energy



