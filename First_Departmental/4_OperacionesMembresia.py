import numpy as np
import matplotlib.pyplot as plt

#Variables
t = [0, 1, 2, 3, 4, 5]
mF = [0, 0.3, 0.7, 0.8, 0.9, 1]
mR = [0, 0.2, 0.4, 0.6, 0.8, 1]
union = np.zeros(len(t))
intersecion = np.zeros(len(t))
C_mF = np.zeros(len(t))
C_mR = np.zeros(len(t))
C_inter = np.zeros(len(t))

for i in range(0, len(t)):
    union[i] = max(mF[i], mR[i])
    intersecion[i] = min(mF[i], mR[i])
    C_mF[i] = 1 - mF[i]
    C_mR[i] = 1 - mR[i]
    C_inter[i] = 1 - intersecion[i]
print(union)
print(intersecion)

plt.figure(1)
fig, ax = plt.subplots()
ax.plot(t, mF, 'k--', color='b', label='mF')
ax.plot(t, mR, 'k:', color='r', label='mR')
legend = ax.legend(loc='center right')
plt.xlabel('x')
plt.ylabel('Pertenencia (μ)')
plt.title('Graficas')
plt.margins(0.1)
plt.grid()
plt.show()

plt.figure(2)
fig, ax = plt.subplots()
ax.plot(t, C_mF, 'k--', color='b', label='C_mF')
ax.plot(t, C_mR, 'k:', color='r', label='C_mR')
legend = ax.legend(loc='center right')
plt.xlabel('x')
plt.ylabel('Pertenencia (μ)')
plt.title('Complemento')
plt.margins(0.1)
plt.grid()
plt.show()

plt.figure(3)
fig, ax = plt.subplots()
ax.plot(t, union, color='r')
plt.xlabel('x')
plt.ylabel('Pertenencia (μ)')
plt.title('Union')
plt.margins(0.1)
plt.grid()
plt.show()

plt.figure(4)
fig, ax = plt.subplots()
ax.plot(t, intersecion, 'k--', color='b')
plt.xlabel('x')
plt.ylabel('Pertenencia (μ)')
plt.title('Intersecion')
plt.margins(0.1)
plt.grid()
plt.show()

plt.figure(5)
fig, ax = plt.subplots()
ax.plot(t, C_inter, color='r')
plt.xlabel('x')
plt.ylabel('Pertenencia (μ)')
plt.title('Complemento de Intersecion')
plt.margins(0.1)
plt.grid()
plt.show()