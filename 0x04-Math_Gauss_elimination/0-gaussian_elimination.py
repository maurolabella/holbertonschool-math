#!/usr/bin/python3
import numpy as np


def gaussian_elimination(A, b):

    try:
        x = np.linalg.solve(A, b)
        return x
    except:
        print("You can't divide by zero!")
