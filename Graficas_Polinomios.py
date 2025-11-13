
import numpy as np
import matplotlib.pyplot as plt

#x^4 - 3x^3 - 25x^2 + 75x
po1 = [1, -3, -25, 75]

p = np.poly1d(po1)

x = np.linspace(-5,5,400)

y = p(x)

plt.plot(x, y, label=f'f(x) = {p}')
plt.title('Grafica del Polinomio')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()
plt.show()

#x^3 + 8x^2 + 21x + 18
po2 = [1, 8, 21, 18]

p = np.poly1d(po2)

x = np.linspace(-5,5,400)

y = p(x)

plt.plot(x, y, label=f'f(x) = {p}')
plt.title('Grafica del Polinomio')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()
plt.show()

#x^4 - 6x^3 - x^2 + 30x
po3 = [1, -6, -1, 30]

p = np.poly1d(po3)

x = np.linspace(-5,5,400)

y = p(x)

plt.plot(x, y, label=f'f(x) = {p}')
plt.title('Grafica del Polinomio')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()
plt.show()