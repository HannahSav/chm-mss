# Created by Hannah at 30.01.2024 11:59
from progonka import plot_arrays
import numpy as np
from scipy.sparse.linalg import spsolve
from scipy.sparse import csr_matrix
import matplotlib.pyplot as plt


def analytics(x, Pe):
    return (np.e**(Pe*x) - 1)/(np.e**Pe - 1)


def decision(d0, d1, d2, d3, b):
    A = np.diag(d0, -2) + np.diag(d1, -1) + np.diag(d2, 0) + np.diag(d3, 1)
    # print(A)
    A_csr = csr_matrix(A)
    # print(b)
    #print(A_csr)
    x = spsolve(A_csr, b)
    # print(x)
    return x


def solver_for_steps(steps, Pe):
    N = steps + 1
    x = np.linspace(0, 1, N)
    h = x[1] - x[0]

    print(N, h)

    d0 = np.full((N-2), 1/2*h*Pe)
    d1 = np.full((N-1), -2*h*Pe - 1)
    d2 = np.full(N, 3/2*h*Pe + 2)
    d3 = np.full((N-1), -1)

    #первая строка матрицы
    d2[0] = 1
    d3[0] = 0

    # последняя строка матрицы
    d2[-1] = 1
    d1[-1] = 0
    d0[-1] = 0

    #вторая срока матрицы
    d1[0] = -Pe*h-1
    d2[1] = Pe*h+2
    d3[1] = -1

    b = np.zeros(N)
    b[-1] = 1

    ans = decision(d0, d1, d2, d3, b)
    ans_analyt = analytics(x, Pe)

    plot_arrays(ans, ans_analyt, "My", "analytics", f"for steps = {steps}, Pe = {Pe}")
    return max(abs(ans_analyt - ans))


def differense_steps():
    errors = []
    const_pe = 10
    Steps_s = np.array([10, 50, 100, 500 ,1000, 2000])
    for n in Steps_s:
        errors.append(solver_for_steps(n, const_pe))
    plt.plot(Steps_s, errors, marker='o')
    plt.xlabel("step")
    plt.ylabel("error")
    plt.grid(True)
    plt.show()


def difference_pe():
    errors = []
    const_steps = 100
    Pe_s = np.array([1, 10, 25, 50, 75, 100])
    for pe in Pe_s:
        errors.append(solver_for_steps(const_steps, pe))
    plt.plot(Pe_s, errors, marker='o')
    plt.xlabel("Pe")
    plt.ylabel("error")
    plt.grid(True)
    plt.show()


#print(solver_for_steps(5, 10))
differense_steps()
difference_pe()