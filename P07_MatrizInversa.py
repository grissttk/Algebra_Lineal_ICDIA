
import numpy as np

A = np.array([[1, 2], [2, 3]])
print(A)
print()

Ainv = np.linalg.inv(A) #Calcular la matriz inversa
print(Ainv)
print()

#Comprobación
print("Comprobación:") #A * Ainv = I = Ainv * A
c = A.dot(Ainv)
c2 = Ainv.dot(A)
print(c)
print()
print(c2)