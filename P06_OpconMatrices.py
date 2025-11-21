#SUMA y RESTA
#Requiere que el orden de las matrices sea el mismo
#Pueden ser CUADRADAS o RECTANGULARES

import numpy as np
A = np.array([[1, 2], [2, 3]])
B = np.array([[3, 4], [5, 2]])
print(A)
print(B)

C = A + B
print("Resultado de la suma A + B:")
print(C)

C = A - B
print("Resultado de la subtraca A - B:")
print(C)

C = A * B
print("Resultado de la multiplicacion A * B:")
print(C)

C = A.dot(B)
print("Mulplicacion matricial de A * B:")
print(C)