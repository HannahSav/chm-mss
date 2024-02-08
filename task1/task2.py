# Created by Hannah at 29.01.2024 15:10
import numpy as np
import matplotlib.pyplot as plt
from progonka import progonka_func, plot_arrays


def f_analytics(x):
    return np.sin(np.pi * x)


def solver_for_steps(steps):
    N = steps + 1

    x = np.linspace(0, 1, N)
    h = x[1] - x[0]

    d1 = np.full((N-1), 1)
    d2 = np.full(N, -2)
    d3 = np.full((N-1), 1)

    # # Для неймана
    d2[0] = 1
    # # * h^-2

    b = np.zeros(N)
    for i in range(N):
        b[i] = - np.pi ** 2 * h**2 * np.sin(np.pi*x[i])


    # #Нейман
    b[0] += np.pi * np.cos(np.pi * x[0]) * h
    # # Дирихле

    b[-1] += np.sin(np.pi * x[-1])

    res_a = f_analytics(x)

    res_my = progonka_func(d1, d2, d3, b, N)
    plot_arrays(res_my, res_a, "progonka", "analytic", steps)
    return res_a, res_my


errors = []
N_s = np.logspace(1, 4, num=5, dtype=int)
print(N_s)
for n in N_s:
    res_a, res_prog = solver_for_steps(n)
    errors.append(max(abs(res_a - res_prog)))
plt.loglog(1/N_s, errors, marker='o')
plt.xlabel("log(steps)")
plt.ylabel("log(error)")
plt.grid(True)
plt.show()

print(errors)


