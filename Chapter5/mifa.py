import math
import copy
import numpy as np

#A = [[8, 1, 6], [3, 5, 7], [4, 9, 2]]
#A = [[5, -4, 1], [-4, 6, -4], [1, -4, 7]]
A = [[25, -41, 10, -6], [-41, 68, -17, 10], [10, -17, 5, 3], [-6, 10, -3, 2]]

#A = np.asarray(np.matrix(np.array([[-1, 2, 1], [2, -4, 1], [1, 1, -6]])).I)
#print A
u = [1, 1, 1]
l = 0
l2 = 10
while abs(l - l2) > 1e-5:
    l2 = copy.deepcopy(l)
    v = [0, 0, 0]
    for i in range(3):
        for j in range(3):
            v[i] += A[i][j] * u[j]
    l = 1.0 * max(v[0], max(v[1], v[2]))
    #l = 1.0 / max(v[0], max(v[1], v[2]))
    for i in range(3):
        #u[i] = 1.0 * v[i] * l
        u[i] = 1.0 * v[i] / l
    # print l, l2, v
print l, v
