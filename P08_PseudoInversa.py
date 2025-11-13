
import numpy as np

x = np.array([[27, 78,	50,	97,	30,	57],
[16,	43,	85,	35,	92,	5],
[78,	92,	45,	65,	40,	24],
[39,	79,	6,	73,	79,	26],
[97,	57,	84,	68,	49,	66],
[22,	75,	73,	64,	18,	28],])

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