#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import sys
import csv
import os


def read_observation_data(filename):
    data = []
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in reader:
            data.append(row)
    return data


data_filename = os.path.abspath(sys.argv[1])
read_observation_data(data_filename)

hours_per_day = 24
days_per_week = 7
a = np.random.random((hours_per_day, days_per_week))
plt.imshow(a, cmap='hot', interpolation='nearest')
plt.show()