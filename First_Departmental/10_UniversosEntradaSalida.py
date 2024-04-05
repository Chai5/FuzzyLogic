import numpy as np
import matplotlib.pyplot as plt
from math import e

def gaussiana(t, c, v):
 return e ** ((-1 / 2) * ((t - c) / v) ** 2)
def sigmoide(t, a, c):
 return 1 / (1 + e ** (-a * (t - c)))

t = np.arange(0, 100, 0.1)
A1 = sigmoide(t, -0.3, 50)
A2 = sigmoide(t, 0.3, 50)
B1 = gaussiana(t, 25, 20)
B2 = gaussiana(t, 75, 20)
C1 = sigmoide(t, -0.3, 50)
C2 = gaussiana(t, 75, 20)

plt.figure(1)
fig, ax = plt.subplots()
ax.plot(t, A1, color='r', label='A1')
ax.plot(t, A2, color='b', label='A2')
legend = ax.legend(loc='center right')
plt.xlabel('Universo x')
plt.ylabel('Pertenencia (μ)')
plt.title('Conujntos')
plt.margins(0.1)
plt.grid()
plt.show()

plt.figure(2)
fig, ax = plt.subplots()
ax.plot(t, B1, color='r', label='B1')
ax.plot(t, B2, color='b', label='B2')
legend = ax.legend(loc='center right')
plt.xlabel('Universo y')
plt.ylabel('Pertenencia (μ)')
plt.title('Conujntos')
plt.margins(0.1)
plt.grid()
plt.show()

plt.figure(3)
fig, ax = plt.subplots()
ax.plot(t, C1, color='r', label='C1')
ax.plot(t, C2, color='b', label='C2')
legend = ax.legend(loc='center right')
plt.xlabel('Universo z')
plt.ylabel('Pertenencia (μ)')
plt.title('Conujntos')
plt.margins(0.1)
plt.grid()
plt.show()