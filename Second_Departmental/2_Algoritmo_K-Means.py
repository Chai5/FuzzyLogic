from math import dist
import matplotlib.pyplot as plt
import numpy as np
import random

x = np.array([[1, 1], [4, 1], [4, 2], [5.5, 1]])
c = np.array(random.sample(x.tolist(), k=2))
# c = np.array([[0, 1], [1, 0]])

U = np.zeros(shape=x.T.shape)
U0 = np.zeros(shape=x.T.shape)
# print(c)
# print(c2)

plt.figure(1)
for xitem in x:
    plt.scatter(xitem[0], xitem[1], color='c')
plt.scatter(c[0, 0], c[0, 1], color='r', marker="D")
plt.scatter(c[1, 0], c[1, 1], color='g', marker="D")
plt.title("Clusters iniciales")
while True:
    for i in range(U.shape[0]):
        for j in range(U.shape[1]):
            for k in range(c.shape[0]):
                if i != k:
                    if dist(x[j], c[i]) ** 2 <= dist(x[j], c[k]) ** 2:
                        U[i, j] = 1
                    else:
                        U[i, j] = 0
    G = np.zeros(U.shape[0])
    for uindex, uvalues in enumerate(U):
        G[uindex] = sum(uvalues)
        for uindex, uvalue in enumerate(U):
            c[uindex] = np.sum(x.T * uvalue, axis=1) / G[uindex]
            if (np.array_equal(U0, U)):
                break
            else:
                U0 = U
                U = np.zeros(shape=x.T.shape)

plt.figure(2)
for xitem in x:
    plt.scatter(xitem[0], xitem[1], color='c')
plt.scatter(c[0, 0], c[0, 1], color='r', marker="D")
plt.scatter(c[1, 0], c[1, 1], color='g', marker="D")
plt.title("Clusters finales")
plt.show()