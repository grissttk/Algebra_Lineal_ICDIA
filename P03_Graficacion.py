
x = [] #lista
y = [] #lista

#x -10 a 10
X = [v for v in range(-10, 11, 1)] #De -10 a 10 (se pone 11 para que llegue a 10 y va de 1 en 1)
print(X)

#y = x^2
y = [x**2 + 3 for x in X]
print(y)

from matplotlib import pyplot as plt
plt.plot(X,y)
plt.grid(True)
plt.show()