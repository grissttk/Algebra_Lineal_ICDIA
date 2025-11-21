
import numpy as np

#SUMA
print("SUMA")
AS1 = np.array([[1, 3], [2, 5]])
BS1 = np.array([[3, 2], [1, 4]])
print(AS1)
print(BS1)
print()

C = AS1 + BS1
print("Resultado de la suma A + B:")
print(C)
print()

print("SUMA")
AS2 = np.array([[2, 5, 1], [3, 1, 0]])
BS2 = np.array([[1, 2, 3], [3, 4, 1]])
print(AS2)
print(BS2)
print()

C = AS2 + BS2
print("Resultado de la suma A + B:")
print(C)
print()

print("SUMA")
AS3 = np.array([[3, 2], [1, 4]])
BS3 = np.array([[1, 3], [2, 5]])
print(AS3)
print(BS3)
print()

C = AS3 + BS3
print("Resultado de la suma A + B:")
print(C)
print()


#RESTA
print("RESTA")
AR = np.array([[1, 2, 0], [2, 3, 4], [3, 1, 2]])
BR = np.array([[2, 3, 5], [3, 2, 3], [4, 1, 0]])
print(AR)
print(BR)

C = AR - BR
print("Resultado de la resta A - B:")
print(C)
print()

#MULTIPLICACIÓN
print("MULTIPLICACIÓN")
AM1 = np.array([[3, 2, 5, 6]])
BM1 = np.array([[1, 2, 4, 0]])
print(AM1)
print(BM1)
print()

C = AM1 * BM1
print("Resultado de la multiplicacion A * B:")
print(C)
print()

print("MULTIPLICACIÓN")
AM2 = np.array([[3, 2], [1, 4]])
BM2 = np.array([[1, 3], [2, 5]])
print(AM2)
print(BM2)
print()

C = AM2 * BM2
print("Resultado de la multiplicacion A * B:")
print(C)
print()

print("MULTIPLICACIÓN")
AM3 = np.array([[2, 3], [5, 1], [0,2]])
BM3 = np.array([[4, 1, 2], [5, 2, 3]])
print(AM3)
print(BM3)
print()

C = AM3.dot(BM3)
print("Multiplicacion matricial de A * B:")
print(C)