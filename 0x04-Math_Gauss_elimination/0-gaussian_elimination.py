#!/usr/bin/python3

import sys
import numpy as np


def gaussian_elimination(A, b):

    try:
        if not np.any(b):
            x = [0, 0, 0]
            return x
        else:
            x = np.linalg.solve(A, b)
            return x
    except Exception as e:
        if e.__class__.__name__ == "LinAlgError":
            if not np.any(b):
                x = [0, 0, 0]
                return x
            else:
                print("You can't divide by zero!")
        else:
            print(e)
            print(e.__class__.__name__)
