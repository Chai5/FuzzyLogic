import numpy as np
import matplotlib.pyplot as plt

x = np.arange(2, 10, 1)
Ca = np.zeros(len(x))
Cb = np.zeros(len(x))
A = np.zeros(len(x))
Cbc = np.zeros(len(x))
intAB = np.zeros(len(x))
Tmin = np.zeros(len(x))

def ConA(t):
    if 2 <= t < 5:
        c = (t-2)/3
    elif 5 <= t <= 8:
        c = (8-t)/3
    else:
        c = 0
    return c

def ConB(t):
    if 3 <= t < 6:
        c = (t-3)/3
    elif 6 <= t <= 9:
        c = (9-t)/3
    else:
        c = 0
    return c

for i in range(0, len(x)):
 Ca[i] = ConA(x[i])
 Cb[i] = ConB(x[i])

#Complement
for i in range(0, len(x)):
 A[i] = (Ca[i])/(x[i])
 Cbc[i] = 1 - Cb[i]

#intersection
for i in range(0, len(x)):
 intAB[i] = min(Ca[i], Cbc[i])

#Tmin
for i in range(0, len(x)):
 Tmin[i] = min(Ca[i], Cbc[i])

print(A)
print(intAB)

plt.figure(1)
fig, ax = plt.subplots()
ax.plot(x, Ca, 'k--', color='b', label='Ca')
ax.plot(x, Cb, 'k:', color='r', label='Cb')
legend = ax.legend(loc='center right')
plt.xlabel('x')
plt.ylabel('Pertenencia (μ)')
plt.title('Graficas')
plt.margins(0.1)
plt.show()

plt.figure(2)
plt.plot(x, A)
plt.xlabel('x')
plt.ylabel('Pertenencia')
plt.title('A={Ca(x)/x}')
plt.margins(0.1)
plt.show()

plt.figure(3)
plt.plot(x, intAB)
plt.xlabel('x')
plt.ylabel('Pertenencia')
plt.title('Interseccion A con B complemento)')
plt.margins(0.1)
plt.grid()
plt.show()

plt.figure(4)
plt.plot(x, Tmin)
plt.xlabel('x')
plt.ylabel('Pertenencia')
plt.title('Tmin de A con B complemento')
plt.margins(0.1)
plt.show()