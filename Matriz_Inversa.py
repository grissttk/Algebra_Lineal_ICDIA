
import numpy as np

A = [
    [191, 123, 12397, 0.91],
    [297, 187, 13348, 0.88],
    [221, 176, 9245, 0.82],
    [251, 305, 14695, 0.94]
]

A = np.array(A)
print(A)
print()

Ainv = np.linalg.inv(A)
print("A inversa:")
print(Ainv)
print()

print("Comprobación A * Ainv:")
print(A.dot(Ainv))