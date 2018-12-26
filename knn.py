"""
    ~ knn.py
    ~ kNN (k - Nearest Neighbors) Algorithm

"""

# print(__doc__)

from math import sqrt, pow

class knn:
    
    def __init__(self, k_value, target_value, feature_num):
        self.k = k_value # k parameter - how many neighbors to algorithm will consider
        self.data = target_value
        self.f_num = feature_num
        # print(self.k)

    def get_col_elements(self, col_num):
        val = []
        for row in self.data:
            val.append(row[col_num])
        return val

    def get_distance(self, x, y):
        return sqrt(pow(x-y, 2))

    def find_nn(self, sample_values):
        arr = sample_values
        dt = []
        nn_count = 0
        nn_index = [] # index of nearest neighbors
        for i in range(1,self.f_num): # satirlari 
            j=0
            dt = self.get_col_elements(i)
            min_dist = 6
            for y in dt:
                distance = self.get_distance(int(y), int(arr[i-1]))
                # distance : herbir sütunun uzaklık değerleri
                if distance <= min_dist:
                    min_dist = distance
                    nn_index.append([j ,i])
                    nn_count += 1
                    if nn_count==self.k:
                        # print(nn_index)
                j+=1
                # print(distance)
            # print("\n")
        
            


