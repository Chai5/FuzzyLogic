import numpy as np
import matplotlib.pyplot as plt
from math import e

#Functions
def gaussiana(t, c, v):
    return e ** ((-1 / 2) * ((t - c) / v) ** 2)

def campana(t, a, b, c):
    return 1 / (1 + (abs((t - c) / a) ** (2 * b)))

#Variables
t = np.arange(0, 100, 1)
u = lambda t: np.piecewise(t, t >= 0, [1, 0])
y = np.array([campana(x, 17, 3, 0) for x in t])
j = np.array([gaussiana(x, 50, 10) for x in t])
z = np.array([campana(x, 17, 3, 100) for x in t])

#Plot
fig, ax = plt.subplots()
ax.plot(t, y, 'k--', color='g', label='baja')
ax.plot(t, j, 'k', color='r', label='media')
ax.plot(t, z, 'k:', color='b', label='alta')
legend = ax.legend(loc='center right')
plt.xlabel('x<0 25<x<75 100<x')
plt.ylabel('Pertenencia (μ)')
plt.title('Temperatura del agua °C')
plt.margins(0.1)
plt.grid()
plt.show()