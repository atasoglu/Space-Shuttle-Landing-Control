# -*- coding: utf-8 -*-
from math import sqrt, floor
from random import random
class kNNeighbors:
    
    # distance methods
    euclid, manhattan = 'e', 'm', 
    
    # init function
    def __init__(self, k_value, distance):
        '''
        k_value: nbr of neighbors
        distance: distance method to calculate the distance for each specified neighbors
        '''
        self.k = k_value
        self.distance_method = distance

    def fit(self, x_train, y_train):
        if self.distance_method is self.euclid:           
            pass
        elif self.distance_method is self.manhattan:
            pass

    def predict_lazy(self, X_input, X, Y):
        # for 'lazy learning' use only this function !
        neighbors, dist = [], []
        if self.distance_method is self.euclid:
            for x in X:
                dist.append(self.get_distance_euclid(X_input, x))
        elif self.distance_method is self.manhattan:
            for x in X:
                dist.append(self.get_distance_manhattan(X_input, x))
        for i in range(self.k):
            min_dist = max(dist)
            for dis, index_of_min in zip(dist, range(len(dist))):
                if dis < min_dist:
                    min_dist = dis
                    min_index = index_of_min
            dist.pop(min_index)
            neighbors.append(Y[min_index])
        return self.get_nearest_neighbor(neighbors)
        
    def get_nearest_neighbor(self, arr): 
        return max(arr, key=arr.count)
        
    def get_distance_euclid(self, x_input, x_in_row):
        sum = 0
        for x_inp, x_inrow in zip(x_input, x_in_row):
            sum += pow(float(x_inp) - float(x_inrow), 2)
        return sqrt(sum)

    def get_distance_manhattan(self, x_input, x_in_row):
        sum = 0
        for x_inp, x_inrow in zip(x_input, x_in_row):
            sum += abs(float(x_inp) - float(x_inrow))
        return sum

class preprocessing:

    def __init__(self):
        pass
    
    def shuffle(self, X, Y):
        x_new, y_new = [], []
        for i in range(len(Y)):
            rand_index = floor(random() * len(Y))
            x_new.append(X[rand_index])
            y_new.append(Y[rand_index])
            X.pop(rand_index)
            Y.pop(rand_index)
        return x_new, y_new
    
    def train_test(self, X, Y, test_size = 0.33):
        x_train, x_test, y_train, y_test = [], [], [], []
        for i in range(round(len(Y) * test_size)):
            x_test.append(X[i])
            y_test.append(Y[i])
            X.pop(i)
            Y.pop(i)
        x_train = X
        y_train = Y
        return x_train, x_test, y_train, y_test 
