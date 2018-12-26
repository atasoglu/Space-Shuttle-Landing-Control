"""
      main.py

      ~ Expirement on Space Shuttle Landing Control with Machine Learning
        by using the kNN algorithm to predictions.
        metric: Euclidean
        for more detail, read the document on /docs directory.
        ###
      ~ Uzay Mekiği İniş Kontrolü üzerine deney
        tahmin için kNN (En yakın komşuluk) algoritması kullanılmıştır.
        ölçüm: Öklid uzaklık formülü
        daha fazla detay için, /docs dizinideki dökümanı okuyabilirsiniz.
        
        author: ahmet atasoglu @ 2018

        # for testing the algorithm, please follow the instroductions #
        # algoritmayı sınamak için, adımları takip edin #
"""

print(__doc__)

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
kNN = knn(1, data, 7)
train = []

# creating training set by your answers...
a = input("1) STABILITY: stab or xstab\n'1' to stab, '2' to xstab: ")
train.append(int(a))
a = input("2) ERROR: XL, LX, MM or SS\n'1' to XL, '2' to LX, '3' to MM, '4' to SS: ")
train.append(int(a))
a = input("3) SIGN: pp or nn\n'1' to pp, '2' to nn: ")
train.append(int(a))
a = input("4) WIND: head or tail\n'1' to head, '2' to tail: ")
train.append(int(a))
a = input("5) MAGNITUDE: Low, Medium, Strong or OutOfRange\n'1' to Low, '2' to Medium, '3' to Strong, '4' to OutOfRange: ")
train.append(int(a))
a = input("6) VISIBILITY: yes or no\n'1' to yes, '2' to no: ")
train.append(int(a))

        
# ...and machine answers the human's question :)

print("\n### Machine Says: ###")
result = kNN.get_nn(kNN.fit_nn(train))
if kNN.classes[result] == 1:
        print("shuttle must be manuel controlled!")
elif kNN.classes[result] == 2:
        print("shuttle must be auto controlled!")

"""
# use to show newly dataset with repaired datas
for i in data:
        print(i)
"""
