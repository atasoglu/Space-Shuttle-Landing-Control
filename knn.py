"""
    ~ knn.py
    ~ kNN (k - Nearest Neighbors) Algorithm

"""

# print(__doc__)

from math import sqrt, pow

class knn:
    
    def __init__(self, k_value, target_value, feature_num):
        self.k = k_value # k parameter - how many neighbors to algorithm will consider
        # will be added soon!
        self.data = target_value
        self.f_num = feature_num
        self.default_min = 10
        self.classes = [2, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 1, 2]
        self.value_of_nn = 0
        # print(self.k)

    def get_distance(self, dist, examp_val):
        
        x = 0
        for y,z in zip(dist, examp_val):
            x += pow(int(y)-int(z), 2)
        return sqrt(x)

    def fit_nn(self, sample_values):
        
        arr = sample_values
        temp_sum = 0 # temporary sum of on a row
        result_arr = []
        for row in self.data:
            row.pop(0)
            temp_sum = self.get_distance(row, arr)
            result_arr.append(temp_sum)
        """
        # to show all values
        for t in result_arr:
            print(t)
        """

        return result_arr
        
    def get_nn(self, results):
        
        arr = results
        # print(arr, len(arr))
        min_val = self.default_min
        i=0
        for x in arr:
            if x < min_val:
                min_val = x
                count = i
            i+=1
        self.value_of_nn = arr[count]
        return count
        
            


