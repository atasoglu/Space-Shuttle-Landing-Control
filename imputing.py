"""
    ~ imputing.py
    ~ imputing missing values
    this orientation is for impute each one of the specified missing value on our dataset. 
    impute method: mod
    author: ahmet atasoglu @ 2018
"""

# print(__doc__)

class imputing:
    
    def __init__(self, target_data):
        self.data = target_data
    
    def find_missing(self, denoted_sign='*'): # returns positions of each missing values 
        marked = [] # marked missing values
        total_missing = 0 # total of missing values
        for row in self.data:
            i=0
            for val in row:
                if val == denoted_sign:
                    marked.append([self.data.index(row), i])
                    total_missing += 1
                i+=1
        # marked.append([None, total_missing])
        return marked 
    

    def mod_col(self, col_num, target_array, denoted_sign = '*'): # returns mod of specified col
        values = []
        mod = -1
        try:
            for row in target_array:
                if row[col_num] != denoted_sign: # is NOT  missing value ?
                    values.append(row[col_num])
                # count += int(row[col_num])
        
                for i in values:
                    if values.count(i) >= values.count(mod):
                        mod = i
        except Exception as ex:
            print("[Error Message]\t",ex)
        return mod 

    def handle_missing(self, denoted_sign = '*'): # handling missing values with calculated mod of specified column 

        i=0 # number of row
        arr = self.data
        for row in arr:
            j=0 # number of column
            for col in row:
                if j==0:
                    j+=1
                    continue
                elif col == denoted_sign:
                    curr_mod = self.mod_col(j, arr)
                    row[j] = curr_mod
                arr[i] = row
                j+=1
            i+=1
            # print(self.data[i])

        return self.data
            

            



    


