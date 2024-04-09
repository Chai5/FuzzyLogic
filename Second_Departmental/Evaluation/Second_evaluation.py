from math import dist
import numpy as np
from matplotlib import pyplot as plt
from skimage import io
from skimage.color import rgb2gray
from skimage.transform import resize
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist

# Img
original = io.imread('exa_8.jpg')
# Resize de la img
original = resize(original, (600, 500), 
anti_aliasing=True)
# Img a gris
img = rgb2gray(original)
# Img binarizada
binarize = img < 0.63
#Obtencion de muestras de los objetos
x = []
for yindex in range(binarize.shape[0]):
    for xindex in range(binarize.shape[1]):
        if binarize[yindex, xindex]:
            x.append([xindex, yindex])
x = np.array(x)
plt.figure(1)
plt.imshow(original)
plt.figure(2)
plt.imshow(img, cmap=plt.cm.gray)
plt.figure(3)
plt.imshow(binarize, cmap=plt.cm.gray)
plt.show()

# Ploteo de los objetos con sus posibles clusteres
plt.figure(4)
plt.scatter(x.T[0], 600 - x.T[1], s=40)
plt.title("Muestras")
plt.grid(True)
plt.show()

### Metodo del codo
distortions = []
inertias = []
mapping1 = {}
mapping2 = {}
K = range(1, 10)
for k in K:
    # Building and fitting the model
    kmeanModel = KMeans(n_clusters=k).fit(x)
    kmeanModel.fit(x)
    distortions.append(sum(np.min(cdist(x, kmeanModel.cluster_centers_, 'euclidean'), axis=1)) / x.shape[0])
    inertias.append(kmeanModel.inertia_)
    mapping1[k] = sum(np.min(cdist(x, kmeanModel.cluster_centers_, 'euclidean'), axis=1)) / x.shape[0]
    mapping2[k] = kmeanModel.inertia_

plt.figure(5)
plt.plot(K, distortions, 'bo-')
plt.xlabel('Valores de K')
plt.ylabel('Distortion')
plt.title('Metodo del codo usando distorsion')
plt.grid(True)
plt.show()
plt.figure(6)
plt.plot(K, inertias, 'bo-')
plt.xlabel('Valores de K')
plt.ylabel('Inertia')
plt.title('Metodo del codo usando inersia')
plt.grid(True)
plt.show()

### Metodo de mountain
# grid largo /5
C = np.arange(0, 600, 120)
# grid ancho /5
F = np.arange(0, 500, 100)
# MOVER
alpha = .009
beta = .009
# Matriz de la funcion mountain
M = np.zeros(shape=(C.shape[0], F.shape[0]))
for yindex in range(C.shape[0]):
    for xindex in range(F.shape[0]):
        for zindex in range(x.shape[0]):
            d = np.sqrt(((x[zindex, 0] - F[xindex]) ** 2) + ((x[zindex, 1] - C[yindex]) ** 2))
            M[yindex, xindex] += np.exp(-alpha * d)
k = 0
# Matriz ajustable para montañas
M2 = np.zeros(shape=M.shape)
MAc = []
pfc = list()
delta = [0]
c0 = list()
c = []
k2 = 3

while delta[k] < k2:
    c.append(np.amax(M))
    for yindex in range(C.shape[0]):
        for xindex in range(F.shape[0]):
            if M[yindex, xindex] == c[k]:
                pfc.append((xindex, yindex))
                break
    for yindex in range(C.shape[0]):
        for xindex in range(F.shape[0]):
            g = 0
            for zindex in range(k + 1):
                dc = np.sqrt(((F[pfc[zindex][0]] - F[xindex]) ** 2) + ((F[pfc[zindex][1]] - C[yindex]) ** 2))
                g += np.exp(-beta * dc)
            val = M[yindex, xindex] - M[pfc[k][1], pfc[k][0]] * g
            if val >= 0:
                M2[yindex, xindex] = val
            else:
                M2[yindex, xindex] = 0
    MAc.append(np.copy(M2)) # Agregado de nueva matriz con montaña unica
    delta.append(c[0] / np.amax(M2)) # Control de flujo de las figuras encontradas
    M = np.copy(M2)
    # Ubicacion de los clusteres uniciales para Jang
    c0.append((F[pfc[k][0]], C[pfc[k][1]]))
    k += 1

c0 = set(c0)
c0 = np.array([list(x) for x in c0])
# Centros de los objetos
plt.figure(7)
plt.scatter(x.T[0], 599 - x.T[1], s=40)
plt.scatter(c0.T[0], 599 - c0.T[1], s=60, 
marker="D")
plt.grid(linewidth=1)
plt.title("Metodo de mountain")
plt.show()

# Coordenadas para 3d
plotx, ploty = np.meshgrid(F, C)
plt.figure(8)
ax = plt.axes(projection='3d')
ax.plot_surface(plotx, ploty, M, 
cmap='viridis')
ax.grid(True)
plt.title("Montaña 1")
plt.show()

# Montañas de los objetos
for xindex in range(len(c0) - 1):
 plt.figure(9 + xindex)
 ax = plt.axes(projection='3d')
 ax.plot_surface(plotx, ploty, MAc[xindex], cmap='viridis')
 ax.grid(True)
 plt.title("Montaña {}".format(xindex + 2))
 plt.show()

### K-Means Jang
#clusters iniciales
U = np.zeros(shape=(c0.shape[0], x.shape[0]))
U0 = np.zeros(shape=(c0.shape[0], x.shape[0]))
while True:
    for i in range(U.shape[0]):
        for j in range(U.shape[1]):
            flag = 0
            for k in range(c0.shape[0]):
                if i != k:
                    if dist(x[j], c0[i]) ** 2 <= dist(x[j], c0[k]) ** 2:
                        flag = 1
                    else:
                        flag = 0
                        break
            U[i, j] = flag
    G = np.zeros(U.shape[0])
    for uindex, uvalues in enumerate(U):
        G[uindex] = np.sum(uvalues)
    for uindex, uvalue in enumerate(U):
        c0[uindex] = np.sum(x.T * uvalue, axis=1) / G[uindex]
        if (np.array_equal(U0, U)):
            break
        else:
            U0 = U
            U = np.zeros(shape=(c0.shape[0], x.shape[0]))

objects = []
clusters = []

plt.figure(10)
for index in range(c0.shape[0]):
    clusters.append(x.T * U[index]) # Conjunto de datos con clusteres finales
    plt.scatter(clusters[index][0], 599 - clusters[index][1], s=40)
    objects.append("Objeto {}".format(index))
plt.legend(objects)
plt.scatter(c0.T[0], 599 - c0.T[1], s=60, color='k', marker="D") # Clusteres finales por objeto
plt.title("K-means Jang")
plt.show()