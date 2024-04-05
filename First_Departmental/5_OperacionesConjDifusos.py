import numpy as np
import matplotlib.pyplot as plt
t = np.arange(0, 10, .1)

# sets
a = t/(t+2)
b = 2**(-t)
c = 1/(1+10*((t-2)**2))
min_a = min(a)
res_a = a-min_a
max_a = max(a)
norm_a = res_a/max_a
na = np.zeros(len(t))
nb = np.zeros(len(t))
nc = np.zeros(len(t))
ab = np.zeros(len(t))
ac = np.zeros(len(t))
bc = np.zeros(len(t))
i_ab = np.zeros(len(t))
i_ac = np.zeros(len(t))
i_bc = np.zeros(len(t))
c_anc = np.zeros(len(t))
c_nbc = np.zeros(len(t))
c_ac = np.zeros(len(t))


#conjuntos negados
for i in range(0, len(t)):
    na[i] = 1 - norm_a[i]
    nb[i] = 1 - b[i]
    nc[i] = 1 - c[i]
for i in range(0, len(t)):
    ab[i] = max(norm_a[i], b[i])
    ac[i] = max(norm_a[i], c[i])
    bc[i] = max(b[i], c[i])
for i in range(0, len(t)):
    i_ab[i] = min(norm_a[i], b[i])
    i_ac[i] = min(norm_a[i], c[i])
    i_bc[i] = min(b[i], c[i])
for i in range(0, len(t)):
    c_anc[i] = 1-(min(norm_a[i], nc[i]))
    c_nbc[i] = 1 - (min(nb[i], c[i]))
    c_ac[i] = 1 - (max(norm_a [i], c[i]))

plt.figure(1)
fig, ax = plt.subplots()
ax.plot(t, norm_a, 'k--', color='g', label='μa')
ax.plot(t, b, 'k', color='r', label='μb')
ax.plot(t, c, 'k:', color='b', label='μc')
legend = ax.legend(loc='center right')
plt.xlabel('x')
plt.ylabel('Pertenencia (μ)')
plt.title('Graficas')
plt.margins(0.1)
plt.grid()
plt.show()

plt.figure(2)
fig, ax = plt.subplots()
ax.plot(t, na, 'k--', color='g', label='C_μa')
ax.plot(t, nb, 'k', color='r', label='C_μb')
ax.plot(t, nc, 'k:', color='b', label='C_μc')
legend = ax.legend(loc='center right')
plt.xlabel('x')
plt.ylabel('Pertenencia (μ)')
plt.title('Complemento')
plt.margins(0.1)
plt.grid()
plt.show()

plt.figure(3)
fig, ax = plt.subplots()
ax.plot(t, ab, 'k--', color='g', label='ab')
ax.plot(t, ac, 'k', color='r', label='ac')
ax.plot(t, bc, 'k:', color='b', label='bc')
legend = ax.legend(loc='center right')
plt.xlabel('x')
plt.ylabel('Pertenencia (μ)')
plt.title('Union')
plt.margins(0.1)
plt.grid()
plt.show()

plt.figure(4)
fig, ax = plt.subplots()
ax.plot(t, i_ab, 'k--', color='g', label='ab')
ax.plot(t, i_ac, 'k', color='r', label='ac')
ax.plot(t, i_bc, 'k:', color='b', label='bc')
legend = ax.legend(loc='center right')
plt.xlabel('x')
plt.ylabel('Pertenencia (μ)')
plt.title('Interseccion')
plt.margins(0.1)
plt.grid()
plt.show()

plt.figure(5)
fig, ax = plt.subplots()
ax.plot(t, c_anc, 'k--', color='g', label='c_anc')
ax.plot(t, c_nbc, 'k', color='r', label='c_nbc')
ax.plot(t, c_ac, 'k:', color='b', label='c_ac')
legend = ax.legend(loc='center right')
plt.xlabel('x')
plt.ylabel('Pertenencia (μ)')
plt.title('Complemento de conjuntos')
plt.margins(0.1)
plt.grid()
plt.show()