from random import randint
from math import dist
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

ra = 20
rb = 1.5 * ra
D = np.zeros(shape=x.shape[0])
D2 = []
c = []
k = 0

for index, Xi in enumerate(x):
    for Xj in x:
        D[index] += np.exp(-(dist(Xi, Xj) ** 2) / ((ra / 2) ** 2))
D2.append(np.amax(D))
c.append(x[np.where(D == D2[k])[0]][0])

while len(D2) < 3:
    for index, Xi in enumerate(x):
        D[index] -= D2[k] * np.exp(-(dist(Xi, c[k]) ** 2) / ((rb / 2) ** 2))
    D2.append(np.amax(D))
    k += 1
    c.append(x[np.where(D == D2[k])[0]][0])

plt.figure(1)
for xitem in x:
    plt.scatter(xitem[0], xitem[1], color='c')
plt.title("Muestras")
plt.grid(True)
c = np.array(c)

plt.figure(2)
plt.scatter(x.T[0], x.T[1], color='c')
plt.scatter(c.T[0], c.T[1], color='r')
plt.title("Centroides")
plt.grid(True)
plt.show()