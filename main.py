import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange
import math

# 1. Задаем параметры
def f(x):
    return np.sin(np.sin(x))

a = 0
b = 2 * np.pi
n = 12  # степень полинома
x_nodes = np.linspace(a, b, n + 1)
y_nodes = f(x_nodes)

# 2. Функция для вычисления полинома Лагранжа
def lagrange_poly(x, x_nodes, y_nodes):
    poly = lagrange(x_nodes, y_nodes)
    return poly(x)

# 3. Вычисляем практическую погрешность
x_range = np.linspace(a, b, 1000)
y_true = f(x_range)
y_lagrange = [lagrange_poly(x, x_nodes, y_nodes) for x in x_range]

practical_error = np.max(np.abs(np.array(y_true) - np.array(y_lagrange)))
print(f"Практическая погрешность: {practical_error:.6f}")

# 4. Вычисляем теоретическую погрешность
# Для n=5, нужна 6-я производная f^(6)(x)
# Можно численно найти максимум f^(6)(x) на отрезке
# Для простоты, допустим, что максимум производной |f^(6)(xi)| / 6! = C
# C = 1  # Заменим на реальное значение, если известно
C = 1  # Заменим на реальное значение, если известно

def poly_product(x, x_nodes):
    prod = 1
    for node in x_nodes:
        prod *= (x - node)
    return prod

theoretical_error_est = (C / math.factorial(n + 1)) * np.max(np.abs([poly_product(x, x_nodes) for x in x_range]))
print(f"Приближенная теоретическая погрешность: {theoretical_error_est:.6f}")

# 5. Построение графиков
plt.figure(figsize=(10, 6))
plt.plot(x_range, y_true, label='f(x) = sin(sin(x))', color='blue')
plt.plot(x_range, y_lagrange, label=f'Полином Лагранжа $L_{n}(x)$', color='red', linestyle='--')
plt.plot(x_nodes, y_nodes, 'o', label='Узлы интерполяции', color='green')
plt.title(f'Интерполяция полиномом Лагранжа (n={n})')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()