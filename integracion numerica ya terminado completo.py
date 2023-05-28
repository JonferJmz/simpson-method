import matplotlib.pyplot as plt
import numpy as np
import math

def f(x):
    return math.sin(x)

def rectangulo(x0):
    return f(x0 + h/2)

def trapecio(x0, h):
    return (f(x0) + f(x0 + h))

def simpson(x0):
    return  f(x0) + 4 * f(x0 + h/2) + f(x0 + h) 

def simpson_integracion(x0, N, h):
    integral_sum = 0.0
    for i in range(N):
        x = x0 + i * h
        integral_sum += simpson(x)
    return h * integral_sum / 6

def trapecio_integracion(x0, N, h):
    integral_sum = 0
    for i in range(N):
        x = x0 + i * h
        integral_sum += trapecio(x, h)
    return integral_sum * (h / 2)

def rectangulo_integracion(x0, N, h):
    integral_sum = 0
    for i in range(N):
        x = x0 + i * h
        integral_sum += f(x + h/2)  # Evaluar en el punto medio del intervalo
    return integral_sum * h

def integralnumerica(tipo, x0, N, h):
    if tipo == "simpson":
        return simpson_integracion(x0, N, h)
    elif tipo == "trapecio":
        return trapecio_integracion(x0, N, h)
    elif tipo == "rectangulo_medio":
        return rectangulo_integracion(x0, N, h)


# Simulación 
p = math.pi
x0 = 0.0
xf = p/2
N_values = list(range(4, 45, 4))
integrales_simpson = []
integrales_trapecio = []
integrales_rectangulo = []

for N in N_values:
    h = (xf - x0)/N
    integrales_simpson.append(integralnumerica("simpson", x0, N, h))
    integrales_trapecio.append(integralnumerica("trapecio", x0, N, h))
    integrales_rectangulo.append(integralnumerica("rectangulo_medio", x0, N, h))

plt.plot(N_values, integrales_simpson, marker='o', label='Simpson')
plt.plot(N_values, integrales_trapecio, marker='o', label='Trapecio')
plt.plot(N_values, integrales_rectangulo, marker='o', label='Rectángulo')

plt.xlabel('N')
plt.ylabel('Valor de la integral')
plt.legend()

plt.tight_layout()
plt.show()
