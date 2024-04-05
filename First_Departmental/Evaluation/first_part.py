import numpy as np
import matplotlib.pyplot as plt
from math import e
from mpl_toolkits.mplot3d import Axes3D

cacao_g = np.arange(0, 150, 1)
leche_g = np.arange(0, 120, 1)
choco_g = np.arange(0, 270, 1)
X, Y = np.meshgrid(cacao_g, leche_g) 

#Coordenadas
def gaussiana(t, c, v):
    return e ** ((-1 / 2) * ((t - c) / v) ** 2)

def Muestras(i, Señal_P, Señal_I, Señal_M):
    M_S = np.zeros(3)
    M_S[0] = Señal_P[i]
    M_S[1] = Señal_I[i]
    M_S[2] = Señal_M[i]
    return M_S

#Señal1 es la leche y Señal2 es el cacao por ejes
def TablaI(Señal1, Señal2):
    Tabla = np.zeros((len(Señal1), len(Señal2)))
    for j in range(0, len(Señal1)):
        for i in range(0, len(Señal2)):
            Tabla[i, j] = min(Señal2[i], Señal1[j])
    return Tabla

#Reglas de la tabla de inferencia
def Reglas_tipo(Tabla):
    r = np.zeros(3)
    r[0] = max(Tabla[0, 1], Tabla[0, 2])
    r[1] = max(Tabla[1, 0], Tabla[1, 1], Tabla[1, 2])
    r[2] = max(Tabla[0, 0], Tabla[2, 0], Tabla[2, 1], Tabla[2, 2])
    return r

#Graficas recortadas
def Graficas_r(t, Señal1, Señal2, Señal3, r1, r2, r3):
    s_r1 = np.zeros(len(t))
    s_r2 = np.zeros(len(t))
    s_r3 = np.zeros(len(t))
    s_rT = np.zeros(len(t))
    for i in range(0, len(t)):
        s_r1[i] = min(r1, Señal1[i])
        s_r2[i] = min(r2, Señal2[i])
        s_r3[i] = min(r3, Señal3[i])
        s_rT[i] = max(s_r1[i], s_r2[i], s_r3[i])
    return s_rT

#Valor certero difuso
def VCD(CT):
    aux1 = 0
    aux2 = 0
    for i in range(0, len(CT)):
        aux1 = (CT[i] * i) + aux1
        aux2 = CT[i] + aux2
    if aux1==0 or aux2==0:
        c = 0
    else:
        c = aux1 / aux2
    return c

#Funciones con coordenadas
def Exten_C(x, y, Ext):
    C = Ext[x, y]
    return C

leche_p = gaussiana(leche_g, 0, 20)
leche_i = gaussiana(leche_g, 60, 20)
leche_m = gaussiana(leche_g, 120, 20)
cacao_p = gaussiana(cacao_g, 0, 25)
cacao_i = gaussiana(cacao_g, 75, 25)
cacao_m = gaussiana(cacao_g, 150, 25)
tipo_cl = gaussiana(choco_g, 0, 30)
tipo_sm = gaussiana(choco_g, 135, 30)
tipo_ag = gaussiana(choco_g, 270, 30)

#superficie de control
SC_tipo = np.zeros((len(cacao_g), len(leche_g)))
for j in range(0, len(leche_g)):
    p_l = Muestras(j, leche_p, leche_i, leche_m)
    for i in range(0, len(cacao_g)):
        p_c = Muestras(i, cacao_p, cacao_i, cacao_m)
        Tabla = TablaI(p_l, p_c)
        r_tipo = Reglas_tipo(Tabla)
        g_t_tipo = Graficas_r(choco_g, tipo_cl, tipo_sm, tipo_ag, r_tipo[0], r_tipo[1], r_tipo[2])
        z_tipo = VCD(g_t_tipo)
        SC_tipo[i, j] = z_tipo
G_SC_tipo = Exten_C(X, Y, SC_tipo)

plt.figure(1)
fig, ax = plt.subplots()
ax.plot(cacao_g, cacao_p, color='r', 
label='Poco')
ax.plot(cacao_g, cacao_i, color='c', 
label='Ideal')
ax.plot(cacao_g, cacao_m, color='g', 
label='Mucho')
legend = ax.legend(loc='center right')
plt.xlabel('Gramos cacao')
plt.ylabel('Pertenencia (μ)')
plt.title('Conjuntos')
plt.margins(0.1)
plt.grid()
plt.show()

plt.figure(2)
fig, ax = plt.subplots()
ax.plot(leche_g, leche_p, color='r', label='Poca')
ax.plot(leche_g, leche_i, color='c', label='Ideal')
ax.plot(leche_g, leche_m, color='g', label='Mucha')
legend = ax.legend(loc='center right')
plt.xlabel('Gramos Leche')
plt.ylabel('Pertenencia (μ)')
plt.title('Conjuntos')
plt.margins(0.1)
plt.grid()
plt.show()

plt.figure(3)
fig, ax = plt.subplots()
ax.plot(choco_g, tipo_cl, color='r', label='Chocolate con leche')
ax.plot(choco_g, tipo_sm, color='c', label='Semi-amargo')
ax.plot(choco_g, tipo_ag, color='g', label='Amargo')
legend = ax.legend(loc='center right')
plt.xlabel('Tipo chocolate')
plt.ylabel('Pertenencia (μ)')
plt.title('Conjuntos')
plt.margins(0.1)
plt.grid()
plt.show()
fig1 = plt.figure()
ax = Axes3D(fig1)
ax.plot_surface(X, Y, G_SC_tipo, cmap='viridis')
plt.show()