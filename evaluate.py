#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

hours_per_day = 24
days_per_week = 7
a = np.random.random((hours_per_day, days_per_week))
plt.imshow(a, cmap='hot', interpolation='nearest')
plt.show()