
x = [
[3, 5, 2],
[1, 4, 6],
]

import numpy as np

x = np.array(x)
print(x)
print()

#xinv = np.linalg.inv(x)
#print(xinv)

#Pseudoinversa
xpseudoinv = np.linalg.pinv(x)
print(xpseudoinv)
print()

print('Comprobacion:')
C = x.dot(xpseudoinv)
C = np.round(C, 2)
C2 = xpseudoinv.dot(x)
C2 = np.round(C2, 2)

print('X.dot(PseudoX)')
print(C)
print('Xpseudo.dot(X)')
print(C2)