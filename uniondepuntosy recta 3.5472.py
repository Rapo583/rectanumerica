# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 20:33:35 2023

@author: Sistemas
"""

import matplotlib.pyplot as plt
import numpy as np

# Datos proporcionados
x = np.array([1, 2, 2, 3, 4, 4, 5, 6])
y = np.array([2, 3, 4, 4, 4, 6, 5, 7])

# Recta de ajuste
def recta_ajuste(x):
    return 0.8491 * x + 1.5094

# Crear valores de x en el rango de los datos
x_range = np.linspace(min(x), max(x), 100)

# Calcular los valores correspondientes de y para la recta de ajuste
y_range = recta_ajuste(x_range)

# Graficar los puntos y la recta de ajuste
plt.scatter(x, y, color='blue', label='Puntos dados')
plt.plot(x_range, y_range, color='red', label='Recta de ajuste: y = 0.8491x + 1.5094')
plt.xlabel('x   Sr para la recta de ajuste es: 3.5472')
plt.ylabel('y')
plt.title('Unión de puntos y recta de ajuste')
plt.legend()
plt.grid(True)
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
plt.show()


# Recta de ajuste
m = 0.8491
b = 1.5094

# Calcular y_predicho
y_predicho = [m*x_i + b for x_i in x]

# Calcular residuos y sus cuadrados
residuos_cuadrados = [(y_i - y_pred_i)**2 for y_i, y_pred_i in zip(y, y_predicho)]

# Calcular Sr
Sr = sum(residuos_cuadrados)

print(f'El valor de Sr para la recta de ajuste es: {Sr:.4f}')
