#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import sys
import csv
import os
import math
from functools import reduce


def read_observation_data(filename):
    data = []
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in reader:
            data.append(row)
    return data


def reduce_time_resolution(data):
    attendance_data = np.zeros((24, 7))
    hour_marked_data = list(map(lambda x: (x[0], math.floor(int(x[1]) / 60.0), x[2]), data))
    for day in range(0, 7):
        day_data = list(filter(lambda x: day == int(x[0]), hour_marked_data))
        for hour in range(0, 24):
            hour_data = list(filter(lambda x: hour == x[1], day_data))
            attendance_data[hour][day] = calculate_normalized_attendance(day, hour, hour_data)
    return attendance_data


def calculate_normalized_attendance(day, hour, data):
    """
    Calculate percental attendance as a value in [0, 1] for a given day and hour
    :returns a tuple consisting of (day, hour, attendance)
    """
    summing_lambda = lambda x, y: (day, hour, int(x[2]) + int(y[2]))
    zero_tuple = (day, hour, 0)

    summed_attendance = reduce(summing_lambda, data, zero_tuple)
    return summed_attendance[2] / len(data) if len(data) else 0


"""
PREPROCESSING
"""
data_filename = os.path.abspath(sys.argv[1])
observation_data = read_observation_data(data_filename)
reduced_data = reduce_time_resolution(observation_data)

"""
VISUALISATION
"""
plt.imshow(reduced_data, cmap='hot', interpolation='nearest')
plt.show()