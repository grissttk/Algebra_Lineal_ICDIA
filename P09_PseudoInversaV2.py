
import numpy as np

x = np.array([[48,	34,	54,	77,	90,	30,	84],
[36,	11,	52,	34,	21,	58,	32],
[74,	100,	91,	22,	69,	62,	98],
[87,	60,	52,	62,	23,	20,	27]])

x = np.array(x)
print(x)
print()

#xinv = np.linalg.inv(x)
#print(xinv)

#Pseudoinversa
xpseudoinversa = np.linalg.pinv(x)
print(xpseudoinversa)
print()

c = x.dot(xpseudoinversa)
c2 = xpseudoinversa.dot(x)

print("x.dot(Pseudox)")
print(c)
print()
print("xpseudoinversa.dot(x)")
print(c2)