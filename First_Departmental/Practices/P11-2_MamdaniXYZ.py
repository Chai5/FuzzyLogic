import numpy as np
import matplotlib.pyplot as plt
from math import e
from mpl_toolkits.mplot3d import Axes3D

t = np.arange(0, 100, 1)
X, Y = np.meshgrid(t, t)    #Coordinates

def gaussiana(t, c, v):
    return e ** ((-1 / 2) * ((t - c) / v) ** 2)

def sigmoide(t, a, c):
    return 1 / (1 + e ** (-a * (t - c)))

#Function of CT graph
def F_CT(t,C1, C2, A_C1, A_C2):
    R_C1 = np.zeros(len(t))
    R_C2 = np.zeros(len(t))
    CT = np.zeros(len(t))   
    for i in range(0, len(t)):
        R_C1[i] = min(A_C1, C1[i])
        R_C2[i] = min(A_C2, C2[i])
        CT[i] = max(R_C1[i], R_C2[i])
        return CT

#Fuzzy certain value
def VCD(CT):
    aux1 = 0
    aux2 = 0
    for i in range(0, len(CT)):
        aux1 = (CT[i] * i) + aux1
        aux2 = CT[i] + aux2
        c = aux1 / aux2
        return c

#Function with coordinates
def Exten_C(x, y, Ext):
    C = Ext[x, y]
    return C

A1 = sigmoide(t, -0.3, 50)
A2 = sigmoide(t, 0.3, 50)
B1 = gaussiana(t, 25, 20)
B2 = gaussiana(t, 75, 20)
C1 = sigmoide(t, -0.3, 50)
C2 = gaussiana(t, 75, 20)
SC = np.zeros((len(t), len(t)))

for j in range(0, len(t)):
    Mb1_y = B1[j]
    Mb2_y = B2[j]
    for i in range(0, len(t)):
        Ma1_x = A1[i]
        Ma2_x = A2[i]
        A_C1 = max(min(Ma1_x, Mb1_y), min(Ma1_x, Mb2_y))
        A_C2 = max(min(Ma2_x, Mb1_y), min(Ma2_x, Mb2_y))
        CT = F_CT(t, C1, C2, A_C1, A_C2)
        z = VCD(CT)
        SC[i, j] = z
G_SC = Exten_C(X, Y, SC)

fig1 = plt.figure()
ax = Axes3D(fig1)
ax.plot_surface(X, Y, G_SC, cmap='viridis')
plt.show()