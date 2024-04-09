from math import dist
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv("IrisDataBase.csv", sep="\t", names=["Data 1", "Data 2", "Data 3", "Data 4", "Tipo"])
data[["Data 1", "Data 2", "Data 3", "Data 4"]] = data[["Data 1", "Data 2", "Data 3", "Data 4"]].astype(float, copy=True)
x = data[["Data 2", "Data 3", "Data 4"]].values
F = np.arange(0, 4.5, 1.5)
C = np.arange(0, 8, 2)
D = np.arange(0, 3, 1)
alpha = 4.5
beta = 4.5
M = np.zeros(shape=(F.shape[0], C.shape[0], 
D.shape[0]))
sum = 0

for xindex in range(F.shape[0]):
    for yindex in range(C.shape[0]):
        for dindex in range(D.shape[0]):
            for zindex in range(x.shape[0]):
                d = np.sqrt(((x.T[0, zindex] - F[xindex]) ** 2) + ((x.T[1, zindex] - C[yindex]) ** 2) + ((x.T[2, zindex] - D[dindex]) ** 2))
                m = np.exp(-alpha * d)
                M[xindex, yindex, dindex] = sum + m
                sum = M[xindex, yindex, dindex]
            sum = 0
print(M)

pfc = []
k = 0
M2 = np.zeros(shape=(F.shape[0], 
C.shape[0], D.shape[0]))
MAc = []
delta = [0]
c0 = []
fig = plt.figure()
ax = plt.axes(projection="3d")
c = []

while delta[k] < 3:
    c.append(np.max(M))
    for xindex in range(F.shape[0]):
        for yindex in range(C.shape[0]):
            for dindex in range(D.shape[0]):
                if M[xindex, yindex, dindex] == c[k]:
                    pfc.append([xindex, yindex, dindex])
    for xindex in range(F.shape[0]):
        for yindex in range(C.shape[0]):
            for dindex in range(D.shape[0]):
                g = 0
                for zindex in range(k + 1):
                    dc = np.sqrt(((F[pfc[zindex][0]] - F[xindex]) ** 2) + ((C[pfc[zindex][1]] - C[yindex]) ** 2) + ((D[pfc[zindex][2]] - D[dindex]) ** 2))
                    g += np.exp(-beta * dc)
                val = M[xindex, yindex, dindex] - M[pfc[k][0], pfc[k][1], pfc[k][2]] * g
                if val >= 0:
                    M2[xindex, yindex, dindex] = val
                else:
                    M2[xindex, yindex, dindex] = 0
    MAc.append(np.copy(M2))
    delta.append((c[0] / np.max(M2)))
    M = np.copy(M2)
    c0.append([F[pfc[k][0]], C[pfc[k][1]], D[pfc[k][2]]])
    ax.scatter3D(F[pfc[k][0]], C[pfc[k][1]], D[pfc[k][2]], s=40, marker="D")
    k += 1

ax.scatter(x.T[0], x.T[1], x.T[2], s=10)
plt.grid(linewidth=1)
plt.title("Mountain")
print(MAc)
plt.show()