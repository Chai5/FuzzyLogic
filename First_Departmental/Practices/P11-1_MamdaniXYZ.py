import numpy as np
import matplotlib.pyplot as plt
from math import e

def gaussiana(t, c, v):
    return e ** ((-1 / 2) * ((t - c) / v) ** 2)
def sigmoide(t, a, c):
    return 1 / (1 + e ** (-a * (t - c)))

#Valor certero difuso
def VCD(CT):
    aux1 = 0
    aux2 = 0
    for i in range(0, len(CT)):
        aux1 = (CT[i] * i) + aux1
        aux2 = CT[i] + aux2
        c = aux1 / aux2
        return c

t = np.arange(0, 100, 1)
A1 = sigmoide(t, -0.3, 50)
A2 = sigmoide(t, 0.3, 50)
B1 = gaussiana(t, 25, 20)
B2 = gaussiana(t, 75, 20)
C1 = sigmoide(t, -0.3, 50)
C2 = gaussiana(t, 75, 20)

#define the places of the matrix
Ma1_x = A1[60]
Ma2_x = A2[60]
Mb1_y = B1[35]
Mb2_y = B2[35]
A_C1 = max(min(Ma1_x, Mb1_y), min(Ma1_x, Mb2_y))
A_C2 = max(min(Ma2_x, Mb1_y), min(Ma2_x, Mb2_y))
R_C1 = np.zeros(len(t))
R_C2 = np.zeros(len(t))
CT = np.zeros(len(t))

for i in range(0, len(t)):
    R_C1[i] = min(A_C1, C1[i])
    R_C2[i] = min(A_C2, C2[i])
    CT[i] = max(R_C1[i], R_C2[i])

plt.figure(1)
fig, ax = plt.subplots()
ax.plot(t, A1, color='r', label='A1')
ax.plot(t, A2, color='c', label='A2')
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
ax.plot(t, B2, color='c', label='B2')
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
ax.plot(t, C2, color='c', label='C2')
legend = ax.legend(loc='center right')
plt.xlabel('Universo z')
plt.ylabel('Pertenencia (μ)')
plt.title('Conujntos')
plt.margins(0.1)
plt.grid()
plt.show()

plt.figure(4)
fig, ax = plt.subplots()
ax.plot(t, R_C1, color='r', label='R_C1')
ax.plot(t, R_C2, color='c', label='R_C2')
legend = ax.legend(loc='center right')
plt.xlabel('Universo z')
plt.ylabel('Pertenencia (μ)')
plt.title('Conujntos')
plt.margins(0.1)
plt.grid()
plt.show()

plt.figure(5)
fig, ax = plt.subplots()
ax.plot(t, CT, label='R_C1')
legend = ax.legend(loc='center right')
plt.xlabel('Universo z')
plt.ylabel('Pertenencia (μ)')
plt.title('Conujntos')
plt.margins(0.1)
plt.grid()
plt.show()