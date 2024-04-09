import matplotlib.pyplot as plt
import numpy as np

x = np.array([[1, 1], [4, 1], [4, 2], [5.5, 1]])
U0 = np.array([[0, 0, 1, 1], [1, 1, 0, 0]])
U = np.zeros(shape=U0.shape)
d = np.zeros(shape=(x.T.shape))

# Parametro que controla la cantidad de difusificacion en el proceso de
# clasificacion, se emplean valores de 1 o 2.
# se indetermina si lo pongo en 1
m = 2

while True:
    opr1 = U0[0] ** 2 * x.T
    v1 = np.sum(opr1, axis=1) / np.sum(U0[0]**2)
    opr2 = U0[1] ** 2 * x.T
    v2 = np.sum(opr2, axis=1) / np.sum(U0[1]**2)
    for xindex in range(x.shape[0]):
        d[0, xindex] = np.sqrt((x[xindex][0] - v1[0]) ** 2 + (x[xindex][1] - v1[1]) ** 2)
        d[1, xindex] = np.sqrt((x[xindex][0] - v2[0]) ** 2 + (x[xindex][1] - v2[1]) ** 2)
    for xindex in range(U.shape[0]):
        for kindex in range(U.shape[1]):
            for jindex in range(d.shape[0]):
                U[xindex, kindex] += (d[xindex, kindex] / d[jindex, kindex]) ** (2 / (m - 1))
            U[xindex, kindex] = U[xindex, kindex] ** -1
    Val=np.sum((U0-U)**2,axis=0)
    Val=np.sum(Val,axis=0)
    if (Val>=0.005):
        U0 = U
        U = np.zeros(shape=U0.shape)
    else:
        break

print(U0)

#Asignar las pertenencias de las muestras
cluster1 = np.round(x.T * U[0])
cluster2 = np.round(x.T * U[1])
notvalue = np.array(np.where(cluster1[0] == 0))
cluster1 = np.array(np.delete(cluster1, notvalue, axis=1))
notvalue = np.array(np.where(cluster2[0] == 0))
cluster2 = np.array(np.delete(cluster2, notvalue, axis=1))

plt.figure(1)
plt.title("Muestras")
for xitem in x:
    plt.scatter(xitem[0], xitem[1], c='g')
plt.xlabel('x')
plt.ylabel('y')

plt.figure(2)
plt.scatter(cluster1[0], cluster1[1], s=20, color='r')
plt.scatter(v1[0], v1[1], s=40, color='r', marker="D", label="Cluster 1")
plt.scatter(cluster2[0], cluster2[1], s=20, color='b')
plt.scatter(v2[0], v2[1], s=40, color='b', marker="D", label="Cluster 2")
plt.legend()
plt.title("Ponce con CMeans")
plt.show()