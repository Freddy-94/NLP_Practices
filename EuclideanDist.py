"""
Author: Alfredo Bernal Luna
Date: 06/03/23
Title: Euclidean Distance - Angle between vectors similarities
Description: The purpose of this program is to show how we can implement
             the concept of "vectorization" to perform classifications tasks.
Relevant classes: "Buildings_similarities" -> Class that implement the attributes
                   we consider relevant of a building. This class implements a 
                   vectorization method, so we can show explicitly how any object
                   can be understand via some of its internal attributes built upon             
                   a vector in the field of Real numbers.
Relevant functions: euclidean_dist -> Compute the Euclidean distance of two input building
                    vectors.
                    vect_norm -> Compute the norm of the input building vector.
                    normalized_build_vector -> Normalize all of the building vectors passed
                    in the input list.
                    compute_cos_angle -> Compute the angle between the two input building
                    vectors.    
"""

import numpy as np
import math
import itertools

class Buildings_similarities:
    """
    Buildings_similarities Class. The purpose of this class is to obtain relevant attributes 
                                  for different buildings, and "vectorize" the buildings
                                  considering the selected attributes.
    """
    def __init__(self, name, num_floors, num_rooms, num_bathrooms,
                 num_elevators, num_pools, num_movie_theaters):
        self.name = name
        self.num_floors = num_floors 
        self.num_rooms = num_rooms
        self.num_bathrooms = num_bathrooms
        self.num_elevators = num_elevators
        self.num_pools = num_pools
        self.num_movie_theaters = num_movie_theaters

    def vectorize(self):
        return [self.name, self.num_floors, self.num_rooms, self.num_bathrooms,
                self.num_elevators, self.num_pools, self.num_movie_theaters]

def euclidean_dist(x, y):
    """
    Euclidean distance to compute how building are similar with each other. 
    """
    euclidean_dist = 0
    for i in range(1, len(x)):
        euclidean_dist += (x[i] - y[i])**2
    euclidean_dist = math.sqrt(euclidean_dist)
    return euclidean_dist

def compute_distances(building_list):
    building_list = normalized_build_vector(building_list) 
    for building1, building2 in itertools.combinations(building_list, 2):
        euclid_dist = euclidean_dist(building1, building2)
        print(f"Distance similarity between {building1[0]} and {building2[0]} is of: {euclid_dist}\n")       

def vect_norm(build_vector):
    norm = 0
    for i in range(1, len(build_vector)):
        norm += build_vector[i]**2
    norm = math.sqrt(norm)
    return norm

def normalized_build_vector(building_list):
    for build_vector in building_list:
        build_vector_norm = vect_norm(build_vector)
        # print(build_vector_norm)
        for i in range(1, len(build_vector)):
            build_vector[i] = build_vector[i] / build_vector_norm
    # print(building_list)
    return building_list 

def dot_prod(build_vector1, build_vector2):
    dot = 0
    for i in range(1, len(build_vector1)):
        dot += build_vector1[i]*build_vector2[i]
    return dot    
  
def angle_opening(x, y):
    cos_theta = dot_prod(x, y) / (vect_norm(x) * vect_norm(y))
    theta = math.acos(cos_theta)
    return theta  

def compute_angles(building_list):
    building_list = normalized_build_vector(building_list) 
    for building1, building2 in itertools.combinations(building_list, 2):
        theta = angle_opening(building1, building2)
        print(f"Angle similarity between {building1[0]} and {building2[0]} is of: {theta}\n")       

def main():
    torre_latino = Buildings_similarities("Torre Latinoamericana", 43, 12, 8, 6, 0, 0).vectorize()
    torre_bbva = Buildings_similarities("Torre BBVA", 46, 15, 12, 6, 0, 0).vectorize()
    cineteca_nacional = Buildings_similarities("Cineteca Nacional", 3, 15, 8, 0, 0, 8).vectorize()
    kaufmann_desert_house = Buildings_similarities("Kaufmann Desert House", 3, 8, 3, 0, 2, 2).vectorize()
    cine_tonala = Buildings_similarities("Cine Tonalá", 2, 12, 8, 0, 0, 6).vectorize()
    villa_majorelle = Buildings_similarities("Villa Majorelle", 2, 10, 4, 0, 2, 2).vectorize()
    building_list = [torre_latino, torre_bbva, cineteca_nacional, kaufmann_desert_house, cine_tonala, villa_majorelle]
    print("==========================================================================================================")
    print("                                     EUCLIDEAN DISTANCE SIMILARITIES                        ")
    print("==========================================================================================================")
    compute_distances(building_list)
    print("==========================================================================================================")
    print("                                     ANGLES OPENING SIMILARITIES COMPUTATION                ")
    print("==========================================================================================================")    
    compute_angles(building_list)
if __name__ == '__main__':
    main()
    

    
