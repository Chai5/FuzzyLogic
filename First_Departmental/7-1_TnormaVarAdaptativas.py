import numpy as np
import matplotlib.pyplot as plt

def campana(t, a, b, c):
    return 1 / (1 + (abs((t - c) / a) ** (2 * b)))

def Dombi(a, b, L):
    c = (1+((((1/a)-1)**L)+(((1/b)-1)**L))**(1/L))**-1
    return c

def Hamacher(a, b, r):
    c = (a*b)/(r+(1-r)*(a+b-(a*b)))
    return c

def SS(a, b, p): #Schweizer & Skalr 1
    c = (max(0,(a**p)+(b**p)-1))**(1/p)
    return c

t = np.arange(-15, 15, .001)
mA = campana(t, 7.5, 2, -5)
mB = campana(t, 5, 1, 5)
Lambda = [0.5, 1, 2]
R = [0.5, 1, 2]
P = [-1, 1, 1.5]
y_1 = np.zeros(len(t))
y_2 = np.zeros(len(t))
y_3 = np.zeros(len(t))
x_1 = np.zeros(len(t))
x_2 = np.zeros(len(t))
x_3 = np.zeros(len(t))
z_1 = np.zeros(len(t))
z_2 = np.zeros(len(t))
z_3 = np.zeros(len(t))

for i in range(0, len(t)):
    y_1[i] = Dombi(mA[i], mB[i], Lambda[0])
    y_2[i] = Dombi(mA[i], mB[i], Lambda[1])
    y_3[i] = Dombi(mA[i], mB[i], Lambda[2])
    x_1[i] = Hamacher(mA[i], mB[i], R[0])
    x_2[i] = Hamacher(mA[i], mB[i], R[1])
    x_3[i] = Hamacher(mA[i], mB[i], R[2])
    z_1[i] = SS(mA[i], mB[i], P[0])
    z_2[i] = SS(mA[i], mB[i], P[1])
    z_3[i] = SS(mA[i], mB[i], P[2])

plt.figure(1)
fig, ax = plt.subplots()
ax.plot(t, mA, color='r', label='mA')
ax.plot(t, mB, color='b', label='mB')
legend = ax.legend(loc='center right')
plt.xlabel('x')
plt.ylabel('Pertenencia (μ)')
plt.title('Conujntos')
plt.margins(0.1)
plt.grid()
plt.show()

plt.figure(2)
fig, ax = plt.subplots()
ax.plot(t, mA, color='m', label='mA')
ax.plot(t, mB, color='c', label='mB')
ax.plot(t, y_1, 'k--', color='g', label='Lambda = 0.5')
ax.plot(t, y_2, 'k:', color='b', label='Lambda = 1')
ax.plot(t, y_3, 'k-.', color='r', label='Lambda = 2')
legend = ax.legend(loc='center right')
plt.xlabel('x')
plt.ylabel('Pertenencia (μ)')
plt.title('T-norma (Dombi[1982])')
plt.margins(0.1)
plt.grid()
plt.show()

plt.figure(2)
fig, ax = plt.subplots()
ax.plot(t, mA, color='m', label='mA')
ax.plot(t, mB, color='c', label='mB')
ax.plot(t, x_1, 'k--', color='g', label='R = 0.5')
ax.plot(t, x_2, 'k:', color='b', label='R = 1')
ax.plot(t, x_3, 'k-.', color='r', label='R = 2')
legend = ax.legend(loc='center right')
plt.xlabel('x')
plt.ylabel('Pertenencia (μ)')
plt.title('T-norma (Hamacher[1978])')
plt.margins(0.1)
plt.grid()
plt.show()

plt.figure(2)
fig, ax = plt.subplots()
ax.plot(t, mA, color='m', label='mA')
ax.plot(t, mB, color='c', label='mB')
ax.plot(t, z_1, 'k--', color='g', label='P = -1')
ax.plot(t, z_2, 'k:', color='b', label='P = 1')
ax.plot(t, z_3, 'k-.', color='r', label='P = 1.5')
legend = ax.legend(loc='center right')
plt.xlabel('x')
plt.ylabel('Pertenencia (μ)')
plt.title('T-norma (Schweizer & Skalr 1[1963])')
plt.margins(0.1)
plt.grid()
plt.show()