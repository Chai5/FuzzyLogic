import numpy as np
import matplotlib.pyplot as plt

# Variables
t = np.arange(0, 100, 0.1)                         # espacio muestra
u = lambda t : np.piecewise(t, t >= 0, [1, 0])

a = 10
b = 40
c = 25
d = 55

# Señales
u1 = u(t-a)
u2 = u(t-b)
u3 = u(t-c)
u4 = u(t-d)
rectangular_1 = u1 - u2
rectangular_2 = u3 - u4

while True:
    print('Operaciones con conjuntos certeros')
    print('1) Ver conjuntos')
    print('2) Union')
    print('3) Interseccion')
    print('4) Complemento')
    print('5) Diferencia')
    print('6) Salir')
    print('Que operacion quieres ver?')
    opc = int(input())
    if opc == 1:
        plt.figure(1)
        plt.plot(t, rectangular_1)
        plt.plot(t, rectangular_2)
        plt.xlabel('x')
        plt.ylabel('Amplitud')
        plt.title('Señales')
        plt.margins(0.1)
        plt.grid()
        plt.show()

    if opc == 2:
        plt.figure(1)
        u_aux1 = u(t - a)
        u_aux2 = u(t - d)
        rectangular_3 = u_aux1 - u_aux2
        plt.plot(t, rectangular_3)
        plt.xlabel('x')
        plt.ylabel('Amplitud')
        plt.title('Union')
        plt.margins(0.1)
        plt.grid()
        plt.show()

    if opc == 3:
        plt.figure(1)
        u_aux1 = u(t - c)
        u_aux2 = u(t - b)
        rectangular_3 = u_aux1 - u_aux2
        plt.plot(t, rectangular_3)
        plt.xlabel('x')
        plt.ylabel('Amplitud')
        plt.title('Interseccion')
        plt.margins(0.1)
        plt.grid()
        plt.show()

    if opc == 4:
        plt.figure(1)
        u_aux1 = u(t - d)
        u_aux2 = u(t - a)
        rectangular_3 = u_aux1 - u_aux2
        plt.plot(t, rectangular_3)
        plt.xlabel('x')
        plt.ylabel('Amplitud')
        plt.title('Complemento')
        plt.margins(0.1)
        plt.grid()
        plt.show()

    if opc == 5:
        plt.figure(1)
        u_aux1 = u(t - a)
        u_aux2 = u(t - c)
        rectangular_3 = u_aux1 - u_aux2
        plt.plot(t, rectangular_3)
        plt.xlabel('x')
        plt.ylabel('Amplitud')
        plt.title('Diferencia')
        plt.margins(0.1)
        plt.grid()
        plt.show()

    if opc == 6:
            break

    print('Adios')

