# Created by Hannah at 29.01.2024 15:10
import numpy as np
import matplotlib.pyplot as plt


def plot_arrays(arr1, arr2, s1, s2, title):
    fig, ax = plt.subplots()
    ax.plot(arr1, label=s1)
    ax.plot(arr2, label=s2)
    ax.set_xlabel('Index')
    ax.set_ylabel('Value')
    plt.title(title)
    ax.legend()
    plt.show()


N = 100

def py_solver(d1, d2, d3, b):
    A = np.diag(d1, -1) + np.diag(d2, 0) + np.diag(d3, 1)
    print("Matrix:")
    print(A)
    return np.linalg.solve(A, b)

def progonka_func(d1, d2, d3, b, N):
    #прямой ход
    d3_new = np.zeros(N-1)
    b_new = np.zeros(N)
    d3_new[0] = d3[0] / d2[0]
    b_new[0] = b[0] / d2[0]
    for i in range(1, N):
        m = 1/(d2[i] - d1[i-1]*d3_new[i-1])
        if i < N - 1:
            d3_new[i] = d3[i] * m
        b_new[i] = (b[i] - d1[i-1] * b_new[i-1]) * m

    #b_new[N - 1] = (b[N - 1] - d1[N - 2] * b_new[N - 2]) / (d2[N - 1] - b[N - 2] * d3_new[N - 2])

    x = np.zeros(N)
    x[N-1] = b_new[N-1]
    for i in range(N-2, -1, -1):
        x[i] = b_new[i] - d3_new[i]*x[i+1]
    return x

if __name__ == '__main__':
    d1 = np.random.randint(0, 100, size=N-1)
    d2 = np.random.randint(0, 100, size=N)
    d3 = np.random.randint(0, 100, size=N-1)
    b = np.random.randint(0, 100, size=N)
    res_a = py_solver(d1, d2, d3, b)
    res_my = progonka_func(d1, d2, d3, b, N)
    plot_arrays(res_a, res_my, "py_solver", "my_solver", N)
    plot_arrays(np.zeros(N), res_my-res_a, "zeros", "difference", ".......")
    print("Max error:", max(abs(res_a-res_my)))
