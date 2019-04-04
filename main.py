# -*- coding: utf-8 -*-
'''
      ~ main.py
      ~ Expirement on Space Shuttle Landing Control
        used to kNN algorithm to predictions.
        for more detail, read the document on /docs directory.
      ~ Uzay Mekiği İniş Kontrolü üzerine deney
        tahmin için kNN (En yakın komşuluk) algoritması kullanılmıştır.
        daha fazla detay için, /docs dizinideki dökümanı okuyabilirsiniz.
        @author: ahmet atasoglu
        # for testing the algorithm, please follow the instroductions
        # algoritmayı sınamak için, talimatları takip edin
'''
import csv
from knn import kNNeighbors
from imputing import imputing

questions = [ # questions to ask the user
        "1) STABILITY: stab or xstab\n'1' to stab, '2' to xstab: ",
        "2) ERROR: XL, LX, MM or SS\n'1' to XL, '2' to LX, '3' to MM, '4' to SS: ",
        "3) SIGN: pp or nn\n'1' to pp, '2' to nn: ",
        "4) WIND: head or tail\n'1' to head, '2' to tail: ",
        "5) MAGNITUDE: Low, Medium, Strong or OutOfRange\n'1' to Low, '2' to Medium, '3' to Strong, '4' to OutOfRange: ",
        "6) VISIBILITY: yes or no\n'1' to yes, '2' to no: "
]

# including dataset...
file_path = 'doc/shuttle.csv'
with open(file_path) as csv_file:
    data, reader = [], csv.reader(csv_file, quoting=csv.QUOTE_NONE)
    for row in reader: data.append(row)

# imputing for missing values...
imp = imputing(data)
data = imp.handle_missing()

# parsing dependent and independent variables... 
x, y = [], []
for row in data:
    x.append(row[:6])
    y.append(row[6:])

# creating knn object...
knn = kNNeighbors(k_value = 3, distance = kNNeighbors.euclid)

# collecting test datas from user...
x_test = []
for question in questions:
    x_test.append(input(question))

# prediction...
y_pred = knn.predict_lazy(x_test, x, y)

# and machine answers human's question :)
try:
    print("\n>>> Machine Says:")
    if y_pred[0] is '1':
        print("shuttle must be manuel controlled!")
    elif y_pred[0] is '2':
        print("shuttle must be auto controlled!")

except Exception as ex:
    print("[Error Message]\t", ex)



