"""
      ~ main.py

      ~ Expirement on Space Shuttle Landing Control
        used to kNN algorithm to predictions.
        metric: Euclidean
        for more detail, read the document on /docs directory.
        ###
      ~ Uzay Mekiği İniş Kontrolü üzerine deney
        tahmin için kNN (En yakın komşuluk) algoritması kullanılmıştır.
        ölçüm: Öklid uzaklık formülü
        daha fazla detay için, /docs dizinideki dökümanı okuyabilirsiniz.
        
        author: ahmet atasoglu @ 2018
"""

# print(__doc__)

import csv
from imputing import *
from knn import *

data = []
file_path = "data\shuttle-landing-control.csv"

with open(file_path) as csv_file:
        reader = csv.reader(csv_file, quoting=csv.QUOTE_NONE)
        for row in reader:
                data.append(row)
        
imp = imputing(data)
# missing_vals = imp.find_missing() # use to get locations and total of missing values on dataset
# print(missing_vals)

data = imp.handle_missing() # missing values will be change by this operation
# the method that we use to change values is the mod. 
# for more, look ~ imputing.py
k = knn(2, data, 7)
s = [1,2,3,4,6,7]
k.find_nn(s)
"""
# use to show newly dataset with repaired datas
for i in data:
        print(i)
"""
