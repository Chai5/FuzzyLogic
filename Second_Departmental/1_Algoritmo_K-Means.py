import matplotlib.pyplot as plt
import numpy as np

#muestras
x = np.array([[1, 1], [4, 1], [4, 2], [5.5, 1]])

#matriz inicial de clusters
U0 = np.array([[0, 0, 1, 1], [1, 1, 0, 0]])

#nueva matriz de clusters
U = np.zeros(shape = U0.shape)
d = np.zeros(shape = (x.shape))

while True:
    opr1 = U0[0] * x.T
    v1 = np.sum(opr1, axis=1) / np.sum(U0[0])
    opr2 = U0[1] * x.T
    v2 = np.sum(opr2, axis=1) / np.sum(U0[0])
    for xindex in range(x.shape[0]):
        d[xindex, 0] = np.sqrt((x[xindex][0] - v1[0]) ** 2 + (x[xindex][1] - v1[1]) ** 2)
        d[xindex, 1] = np.sqrt((x[xindex][0] - v2[0]) ** 2 + (x[xindex][1] - v2[1]) ** 2)
    k = np.amin(d, axis=1)
    for xindex in range(x.shape[0]):
        if k[xindex] == d[xindex][0]:
            U[0, xindex] = 1
        else:
            U[0, xindex] = 0
        if k[xindex] == d[xindex][1]:
            U[1, xindex] = 1
        else:
            U[1, xindex] = 0
    if (not np.array_equal(U, U0)):
        U0 = U
        U = np.zeros(shape=U0.shape)
    else:
        break

plt.figure(1)
plt.title("Muestras")
for xitem in x:
    plt.scatter(xitem[0], xitem[1], c='g')
plt.xlabel('x')
plt.ylabel('y')

plt.figure(2)
plt.title("Clusters")
for xitem in x:
    plt.scatter(xitem[0], xitem[1], c='g')
plt.scatter(v1[0], v1[1], c='c', marker="D")
plt.scatter(v2[0], v2[1], c='r', marker="D")
plt.xlabel('x')
plt.ylabel('y')
plt.show()
