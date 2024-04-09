from math import dist
import matplotlib.pyplot as plt
import numpy as np
import pylab as pl

x = np.array([[0.36, 0.85], [0.65, 0.89], [0.62, 0.55], 
              [0.50, 0.75], [0.35, 1.00], [0.90, 0.35], 
              [1.00, 0.24], [0.99, 0.55], [0.83, 0.36], [0.88, 0.43]])

ra = 1
rb = 1.5 * ra
D = np.zeros(shape=x.shape[0])
D2 = []
c = []
k = 0

for index, Xi in enumerate(x):
    for Xj in x:
        D[index] += np.exp(-(dist(Xi, Xj) ** 2) / ((ra / 2) ** 2))
print(D)

D2.append(np.amax(D))
print(D2)

c.append(x[np.where(D == D2[k])[0]][0])
#condicion de paro para 2 clusters

while len(D2) < 2:
    print(c[k][0])
    for index, xvalue in enumerate(x):
        D[index] -= D2[k] * np.exp(-(dist(xvalue, c[k]) ** 2) / ((rb / 2) ** 2))
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
pl.show()