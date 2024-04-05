from math import dist
from random import sample
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv("IrisDataBase.csv", sep="\t", names=["Data 1", "Data 2", "Data 3", "Data 4", "Tipo"])
data[["Data 1", "Data 2", "Data 3", "Data 4"]] = data[["Data 1", "Data 2", "Data 3", "Data 4"]].astype(float, copy=True)
# por que la maestra dijo
Muestras = data[["Data 2", "Data 3", "Data 4"]].values
c0 = np.array(sample(Muestras.tolist(), k=3))
c = np.copy(c0)
U = np.zeros(shape=(c.shape[0], 
Muestras.shape[0]))
U0 = np.zeros(shape=(c.shape[0], Muestras.shape[0]))

# Metodo de jang
while True:
    for i in range(U.shape[0]):
        for j in range(U.shape[1]):
            flag = 0
            for k in range(c.shape[0]):
                if i != k:
                    if dist(Muestras[j], c[i]) ** 2 <= dist(Muestras[j], c[k]) ** 2:
                        flag = 1
                    else:
                        flag = 0
                        break
            U[i, j] = flag
    G = np.zeros(U.shape[0])
    for uindex, uvalues in enumerate(U):
        G[uindex] = sum(uvalues)
    for uindex, uvalue in enumerate(U):
        c[uindex] = np.sum(Muestras.T * uvalue, axis=1) / G[uindex]
    if (np.array_equal(U0, U)):
        break
    else:
        U0 = U
        U = np.zeros(shape=(c.shape[0], Muestras.shape[0]))

cluster1 = Muestras.T * U[0]
cluster2 = Muestras.T * U[1]
cluster3 = Muestras.T * U[2]
notvalue = np.array(np.where(cluster1[0] == 0))
cluster1 = np.array(np.delete(cluster1, notvalue, axis=1))
notvalue = np.array(np.where(cluster2[0] == 0))
cluster2 = np.array(np.delete(cluster2, notvalue, axis=1))
notvalue = np.array(np.where(cluster3[0] == 0))
cluster3 = np.array(np.delete(cluster3, notvalue, axis=1))

fig = plt.figure(1)
ax = plt.axes(projection="3d")
ax.scatter3D(cluster1[0], cluster1[1], cluster1[2], color='c')
ax.scatter3D(cluster2[0], cluster2[1], cluster2[2], color='c')
ax.scatter3D(cluster3[0], cluster3[1], cluster3[2], color='c')
plt.title("Muestras")

fig = plt.figure(2)
ax = plt.axes(projection="3d")
ax.scatter3D(c0[0, 0], c0[0, 1], c0[0, 2], s=40, color='r', marker="^", label="Cluster 1")
ax.scatter3D(cluster1[0], cluster1[1], cluster1[2], s=10, color='r')
ax.scatter3D(c0[1, 0], c0[1, 1], c0[1, 2], s=40, color='b', marker="^", label="Cluster 2")
ax.scatter3D(cluster2[0], cluster2[1], cluster2[2], s=10, color='b')
ax.scatter3D(c0[2, 0], c0[2, 1], c0[2, 2], s=40, color='g', marker="^", label="Cluster 3")
ax.scatter3D(cluster3[0], cluster3[1], cluster3[2], s=10, color='g')
plt.legend()
plt.title("Clusters iniciales")

fig = plt.figure(3)
ax = plt.axes(projection="3d")
ax.scatter3D(c[0, 0], c[0, 1], c[0, 2], s=40, color='r', marker="D", label="Cluster 1")
ax.scatter3D(cluster1[0], cluster1[1], cluster1[2], s=10, color='r')
ax.scatter3D(c[1, 0], c[1, 1], c[1, 2], s=40, color='b', marker="D", label="Cluster 2")
ax.scatter3D(cluster2[0], cluster2[1], cluster2[2], s=10, color='b')
ax.scatter3D(c[2, 0], c[2, 1], c[2, 2], s=40, color='g', marker="D", label="Cluster 3")
ax.scatter3D(cluster3[0], cluster3[1], cluster3[2], s=10, color='g')
plt.legend()
plt.title("Clusters finales")
plt.show()
