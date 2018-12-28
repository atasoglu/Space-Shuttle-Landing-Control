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

        # for testing the algorithm, please follow the instroductions #
"""

print(__doc__)

import csv
from imputing import *
from knn import *


questions = [ # questions to ask the user
        "1) STABILITY: stab or xstab\n'1' to stab, '2' to xstab: ",
        "2) ERROR: XL, LX, MM or SS\n'1' to XL, '2' to LX, '3' to MM, '4' to SS: ",
        "3) SIGN: pp or nn\n'1' to pp, '2' to nn: ",
        "4) WIND: head or tail\n'1' to head, '2' to tail: ",
        "5) MAGNITUDE: Low, Medium, Strong or OutOfRange\n'1' to Low, '2' to Medium, '3' to Strong, '4' to OutOfRange: ",
        "6) VISIBILITY: yes or no\n'1' to yes, '2' to no: "
]

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

for question in questions:
        train.append(input(question))

# ...and machine answers the human's question :)

try:
        result = kNN.get_nn(kNN.fit_nn(train))
        print("\n /// Machine Says: \\\ ")
        if kNN.classes[result] == 1:
                print("shuttle must be manuel controlled!")
        
        elif kNN.classes[result] == 2:
                print("shuttle must be auto controlled!")
except Exception as ex:
        print("[Error Message]\t",ex)

"""
# use to show newly dataset with repaired datas
for i in data:
        print(i)
"""
