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
        
    
        
        """
        arr = sample_values # incoming example
        sum_distances 
        min_distance = self.default_min
        for i in range(1, self.f_num):
            for ele in arr: # each example
                distances = []
                j=0 # row number of specified column's data
                
                for dt in self.get_col_elements(i): # each data on specified dataset
                    temp_distance = self.get_distance(int(ele), int(dt))
                    distances.append(temp_distance)
                    if temp_distance < min_distance:
                        count = j
        """            

                

        """
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
        """
        
            


