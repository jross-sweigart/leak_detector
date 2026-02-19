"""Equivalent of detector2a.py"""

import numpy as np
from tracemalloc import start, take_snapshot, stop

SNAPSHOT = None

def func(x,y,z):
    try:
        start()
        dataset1 = np.empty((100, ), dtype=np.float64)
        print('x',x)
        dataset1 = np.empty((1000, ), dtype=np.float64)

        l = [i for i in range(100000)]

        if x == 0:
            dataset4a = np.empty((100000, ), dtype=np.float64)
            return 0
        elif x == 1:
            dataset4b = np.empty((100000, ), dtype=np.float64)
            return 1

        dataset3 = np.empty((3000, ), dtype=np.float64)
        return 2

    finally:
        global SNAPSHOT
        SNAPSHOT = take_snapshot()
        stop()
