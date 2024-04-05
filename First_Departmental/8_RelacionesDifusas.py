import numpy as np
import matplotlib.pyplot as plt
from math import e
from mpl_toolkits.mplot3d import Axes3D

#Functions
def gaussiana(t, c, v):
    return e ** ((-1 / 2) * ((t - c) / v) ** 2)

def campana(t, a, b, c):
    return 1 / (1 + (abs((t - c) / a) ** (2 * b)))

def Exten_C(x, y, Ext):     #coordinates functions
    C = Ext[x, y]
    return C

x = np.arange(0, 20, 1)     #range of x
y = np.arange(0, 30, 1)     #range of y
X, Y = np.meshgrid(x, y)    #coordinates

Ca = np.array([gaussiana(z, 10, 2) for z in x])     #a set
Cb = np.array([campana(z, 4, 5, 10) for z in y])    #b set

ECa = np.zeros((len(x), len(y)))
ECb = np.zeros((len(x), len(y)))
PCz = np.zeros((len(x), len(y)))

#Cylindrical Extension of a
for i in range(0, len(y)):
    for j in range(0, len(x)):
        ECa[j, i] = Ca[j]

#Cylindrical Extension of b
for i in range(0, len(x)):
    for j in range(0, len(y)):
        ECb[i, j] = Cb[j]

#Extensiones with coordinates
G_ECa = Exten_C(X, Y, ECa)
G_ECb = Exten_C(X, Y, ECb)

#Cartesian Product 
for i in range(0, len(x)):
    for j in range(0, len(y)):
        PCz[i, j] = min((ECa[i, j]), (ECb[i, j]))

#Cartesian Product with coordinates
G_PCz = Exten_C(X, Y, PCz)

plt.figure(1)
plt.plot(x, Ca)
plt.xlabel('t')
plt.ylabel('Pertenencia')
plt.title('Conjunto difuso A en X')
plt.margins(0.1)
plt.grid()
plt.show()

plt.figure(2)
plt.plot(y, Cb)
plt.xlabel('t')
plt.ylabel('Pertenencia')
plt.title('Conjunto difuso B en Y')
plt.margins(0.1)
plt.grid()
plt.show()

fig1 = plt.figure()
ax = Axes3D(fig1)
ax.plot_surface(X, Y, G_ECa, cmap='viridis')
plt.show()

fig2 = plt.figure()
ax = Axes3D(fig2)
ax.plot_surface(X, Y, G_ECb, cmap='viridis')
plt.show()

fig3 = plt.figure()
ax = Axes3D(fig3)
ax.plot_surface(X, Y, G_PCz, cmap='viridis')
plt.show()