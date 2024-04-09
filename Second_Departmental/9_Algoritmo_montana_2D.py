from math import dist
from random import randint
import matplotlib.pyplot as plt
import numpy as np

x = []
for val in range(0, 20):
    xnum = randint(0, 40)
    ynum = randint(60, 100)
    x.append([xnum, ynum])
for val in range(0, 20):
    xnum = randint(30, 60)
    ynum = randint(0, 40)
    x.append([xnum, ynum])
for val in range(0, 20):
    xnum = randint(70, 100)
    ynum = randint(50, 90)
    x.append([xnum, ynum])
x = np.array(x)
plt.figure()

for xitem in x:
    plt.scatter(xitem[0], xitem[1], s=10, color='r')
plt.title("Muestras")
plt.grid(True)

F = np.arange(0, 110, 20)
C = np.arange(0, 110, 20)
alpha = .054
beta = .054
M = np.zeros(shape=(F.shape[0], C.shape[0]))
sum = 0

for xindex in range(F.shape[0]):
    for yindex in range(C.shape[0]):
        for zindex in range(x.shape[0]):
            d = np.sqrt(((x.T[0, zindex] - F[xindex]) ** 2) + ((x.T[1, zindex] - C[yindex]) ** 2))
            m = np.exp(-alpha * d)
            M[yindex, xindex] += m

plotx = np.tile(F, (len(M), 1))
ploty = plotx.T
plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(plotx, ploty, M, 
cmap='viridis')
ax.grid(True)
plt.title("Montaña 1")
# valores de la funcion de mountain
print(M)

pfc = []
k = 0
M2 = np.zeros(shape=(F.shape[0], 
C.shape[0]))
MAc = []
delta = [0]
c0 = []
plt.figure()

while len(delta) < 4:
    c = np.max(M)
    for xindex in range(F.shape[0]):
        for yindex in range(C.shape[0]):
            if M[xindex, yindex] == c:
                pfc.append([xindex, yindex])
    for xindex in range(F.shape[0]):
        for yindex in range(C.shape[0]):
            g = 0
            for zindex in range(k + 1):
                dc = np.sqrt(((F[pfc[zindex][0]] - F[xindex]) ** 2) + ((F[pfc[zindex][1]] - C[yindex]) ** 2))
                g += np.exp(-beta * dc)
            mc = g
            val = M[xindex, yindex] - M[pfc[k][0], pfc[k][1]] * mc
            if val >= 0:
                M2[xindex, yindex] = val
            else:
                M2[xindex, yindex] = 0
    MAc.append(np.copy(M2))
    delta.append((c / np.max(M2)))
    M = np.copy(M2)
    c0.append([C[pfc[k][1]], F[pfc[k][0]]])
    plt.scatter(C[pfc[k][1]], F[pfc[k][0]], s=40, marker="D")
    k += 1

plt.scatter(x.T[0], x.T[1], s=10)
plt.grid(linewidth=1)
plotx = np.tile(F, (len(MAc[0]), 1))
ploty = plotx.T

plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(plotx, ploty, MAc[0], cmap='viridis')
ax.grid(True)
plt.title("Montaña 2")
plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(plotx, ploty, MAc[1], cmap='viridis')
ax.grid(True)
plt.title("Montaña 3")
# valores de la funcion de mountain despues de remover el primer centro
print(MAc)
plt.show()