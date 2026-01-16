import numpy as np

A = np.array([
    [5,-6],
    [-6,2]
])

B = np.array([
    [-4,-1],
    [6,3]
])

C = A + B

D = np.array([
    [-2,3],
    [9,4]
])

E = C * D
print(E)