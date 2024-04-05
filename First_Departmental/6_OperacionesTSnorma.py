import numpy as np
import matplotlib.pyplot as plt

t = [0, 1, 2, 3, 4, 5]
mT = [0, 0.3, 0.7, 0.8, 0.9, 1]
mR = [0, 0.2, 0.4, 0.6, 0.8, 1]
Tmin = np.zeros(len(t))
Tap = np.zeros(len(t))
Tbp = np.zeros(len(t))
Tdp = np.zeros(len(t))
Smax = np.zeros(len(t))
Sas = np.zeros(len(t))
Sbs = np.zeros(len(t))
Sdp = np.zeros(len(t))

#T norm
for i in range(0, len(t)):
    Tmin[i] = min(mT[i], mR[i])
    Tap[i] = mT[i]*mR[i]
    Tbp[i] = max(0, (mT[i]+mR[i]-1))
    if mT[i]<1 and mR[i]<1:
        Tdp[i] = 0
    if mT[i]==1:
        Tdp[i] = mR[i]
    if mR[i]==1:
        Tdp[i] = mT[i]

#S norm
for i in range(0, len(t)):
    Smax[i] = max(mT[i], mR[i])
    Sas[i] = (mT[i]+mR[i])-(mT[i]*mR[i])
    Sbs[i] = min(1, (mT[i]+mR[i]))
    if mT[i] == 0:
        Sdp[i] = mR[i]
    if mR[i] == 0:
        Sdp[i] = mT[i]
    if mT[i] > 0 and mR[i] > 0:
        Sdp[i] = 1

plt.figure(1)
fig, ax = plt.subplots()
ax.plot(t, mT, color='r', label='mT')
ax.plot(t, mR, color='b', label='mR')
legend = ax.legend(loc='center right')
plt.xlabel('x')
plt.ylabel('Pertenencia (μ)')
plt.title('Conujntos')
plt.margins(0.1)
plt.grid()
plt.show()

plt.figure(2)
fig, ax = plt.subplots()
ax.plot(t, mT, color='m', label='mT')
ax.plot(t, mR, color='c', label='mR')
ax.plot(t, Tmin, 'k--', color='g', label='Tmin')
ax.plot(t, Tap, 'k:', color='k', label='Tap')
ax.plot(t, Tbp, 'k-.', color='b', label='Tbp')
ax.plot(t, Tdp, 'k:', color='r', label='Tdp')
legend = ax.legend(loc='center right')
plt.xlabel('x')
plt.ylabel('Pertenencia (μ)')
plt.title('T-norma')
plt.margins(0.1)
plt.grid()
plt.show()

plt.figure(3)
fig, ax = plt.subplots()
ax.plot(t, mT, color='m', label='mT')
ax.plot(t, mR, color='c', label='mR')
ax.plot(t, Smax, 'k--', color='g', label='Smax')
ax.plot(t, Sas, 'k:', color='k', label='Sas')
ax.plot(t, Sbs, 'k-.', color='b', label='Sbs')
ax.plot(t, Sdp, 'k:', color='r', label='Sdp')
legend = ax.legend(loc='center right')
plt.xlabel('x')
plt.ylabel('Pertenencia (μ)')
plt.title('S-norma')
plt.margins(0.01)
plt.grid()
plt.show()