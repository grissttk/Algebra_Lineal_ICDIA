
#Libreria = Modulo en Python
#Numpy - Operaciones matematicas

mA = [3, 4, 5] #Lista

mB = [1, 4, 6] #Lista

print(mA)
print(mB)

import numpy as np #as = alias
mA = np.array(mA) #Convierte a la lista en una matriz unidimensional
mB = np.array(mB)

print(mA)
print(mB)

C = [[2, 4],[1, 5]] #C en forma de lista Python
print(C)

C = np.array(C) #C en forma matricial
print(C)