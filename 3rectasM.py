# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 19:25:41 2023

@author: Sistemas
"""

import matplotlib.pyplot as plt
import numpy as np

# Definir las ecuaciones de las rectas
def recta1(x):
    return 3 * x + 2

def recta2(x):
    return -2 * x + 3

def recta3(x):
    return -7 * x + 5

# Crear valores de x en el rango de -10 a 10
x = np.linspace(-10, 10, 100)
y = np.linspace(-20, 30, 17)

# Calcular los valores correspondientes de y para cada recta
y1 = recta1(x)
y2 = recta2(x)
y3 = recta3(x)

# Definir los puntos dados
x_puntos = [1, 2, 2, 3, 4, 4, 5, 6]
y_puntos = [2, 3, 4, 4, 4, 6, 5, 7]




# Graficar las rectas
plt.plot(x, y1, label='y = 3 * x + 2')
plt.plot(x, y2, label='y = -2 * x + 3')
plt.plot(x, y3, label='y = -7 * x + 5')

# Graficar los puntos
plt.scatter(x_puntos, y_puntos, color='red', label='Puntos dados')

# Añadir etiquetas y título
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gráfico de rectas y puntos dados')

# Mostrar la leyenda
plt.legend()

# Mostrar el gráfico
plt.grid(True)
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
plt.show()
