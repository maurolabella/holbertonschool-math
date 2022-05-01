#!/usr/bin/env python3
import numpy as np

def gaussian_elimination(A, b):
    try:
        return (np.linalg.solve(A, b))
    except np.linalg.LinAlgError:
        print("You can't divide by zero!")
        return None

# import sys
# import numpy as np

# def gaussian_elimination(A, b):
#     n = len(b)
#     x = np.zeros(n, float)

#     if np.linalg.det(A) == 0:
#         print("You can't divide by zero!")
#         return None

#     # first loop specifies the fixed row
#     for k in range(n-1):
#         if np.fabs(A[k, k]) < 1.0e-12:

#             for i in range(k+1, n):
#                 if np.fabs(A[i, k]) > np.fabs(A[k, k]):
#                     A[[k, i]] = A[[i, k]]
#                     b[[k, i]] = b[[i, k]]
#                     break

#     # elimination below fixed row
#         for i in range(k+1, n):
#             if A[i, k] == 0:
#                 continue

#             factor = A[k, k]/A[i, k]
#             for j in range(k, n):
#                 A[i, j] = A[k, j]*factor
#                 # also take into account the b vector
#             b[i] = b[k] - b[i]*factor

#     x[n-1] = b[n-1] / A[n-1, n-1]
#     for i in range(n-2, -1, -1):
#         sum_ax = 0

#         for j in range(i+1, n):
#             sum_ax += A[i, j]*x[j]

#             x[i] = (b[i]-sum_ax)/A[i, i]
#     return x

# try:
#     if not np.any(b):
#         x = [0, 0, 0]
#         return x
#     else:
#         x = np.linalg.solve(A, b)
#         return x
# except Exception as e:
#     if e.__class__.__name__ == "LinAlgError":
#         if not np.any(b):
#             x = [0, 0, 0]
#             return x
#         else:
#             print("You can't divide by zero!")
#     else:
#         print(e)
#         print(e.__class__.__name__)
