import numpy as np
import matplotlib.pyplot as plt
from math import e

# Variables
t = np.arange(0, 50, 0.1)
u = lambda t: np.piecewise(t, t >= 0, [1, 0])
names = ['Tringular', 'Trapezoidal', 
'Gaussiana', 'Campana', 'Sigmoide']

# Functions
def triangulo(t, a, b, c):
    if t <= a:
        r = 0.0
    elif a < t <= b:
        r = (t - a) / (b - a)
    elif b < t <= c:
        r = (c - t) / (c - b)
    elif c < t:
        r = 0.0
    return r

def trapezio(t, a, b, c, d):
    if t <= a:
        r = 0.0
    elif a < t <= b:
        r = (t - a) / (b - a)
    elif b < t <= c:
        r = 1
    elif c < t <= d:
        r = (d - t) / (d - c)
    elif d < t:
        r = 0.0
    return r

def gaussiana(t, c, v):
    return e ** ((-1 / 2) * ((t - c) / v) ** 2)

def campana(t, a, b, c):
    return 1 / (1 + (abs((t - c) / a) ** (2 * b)))

def sigmoide(t, a, c):
    return 1 / (1 + e ** (-a * (t - c)))

def plotear(t, y):
 plt.figure(1)
 plt.plot(t, y)
 plt.xlabel('t')
 plt.ylabel('Pertenencia')
 plt.title(name)
 plt.margins(0.1)
 plt.grid()
 plt.show()
while True:
    print('Funciones de membresia')
    print('1) Tringular')
    print('2) Trapezoidal')
    print('3) Gaussiana')
    print('4) Campana')
    print('5) Sigmoide')
    print('6) Salir')
    print('Que operacion quieres ver?')
    opc = int(input())
    if opc == 1:
        y = np.array([triangulo(x, 15 ,25, 35) for x in t])
        name = names[0]
        plotear(t, y)
    if opc == 2:
        y = np.array([trapezio(x, 10 ,20, 30, 40) for x in t])
        name = names[1]
        plotear(t, y)
    if opc == 3:
        y = np.array([gaussiana(x, 25, 5) for x in t])
        name = names[2]
        plotear(t, y)
    if opc == 4:
        y = np.array([campana(x, 10, 5, 25) for x in t])
        name = names[3]
        plotear(t, y)
    if opc == 5:
        y = np.array([sigmoide(x, 1, 25) for x in t])
        name = names[4]
        plotear(t, y)
    if opc == 6:
        break