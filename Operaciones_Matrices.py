
import numpy as np

#SUMA
print("SUMA")
AS = np.array([[3, 2], [1, 4]])
BS = np.array([[1, 3], [2, 5]])
print(AS)
print(BS)

C = AS + BS
print("Resultado de la suma AS + BS:")
print(C)
print()

#RESTA
print("RESTA")
AR = np.array([[1, 2, 0], [2, 3, 4], [3, 1, 2]])
BR = np.array([[2, 3, 5], [3, 2, 3], [4, 1, 0]])
print(AR)
print(BR)

C = AR - BR
print("Resultado de la resta AR - BR:")
print(C)
print()

#MULTIPLICACIÓN
print("MULTIPLICACIÓN")
AM = np.array([[3, 2, 5, 6]])
BM = np.array([[1, 2, 4, 0]])
print(AM)
print(BM)

C = AM * BM
print("Resultado de la multiplicacion AM * BM:")
print(C)