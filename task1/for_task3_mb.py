# Created by Hannah at 02.02.2024 13:28
import numpy as np

L, N = 1.0, 100
h = L/N

x = np.linspace(0, L, N+1)
xmid = 0.5*(x[:-1]+x[1:])

dA = np.ones(N)*4
dA[0] = dA[-1] = 2
lA = np.ones(N-1)


B = np.zeros(shape=(N, N-1))
iB, jB = np.indices(B.shape)
B[iB == jB] = 1
B[iB - 1 == jB] = -1

O = np.zeros(shape=(N-1, N-1))
K = np.block(
    [[A, B],
    [B.T, 0]
     ]
)

F = np.hstack(
    [[A, B],
    [B.T, 0]]
)

Y = solve(K, F)
U, o = Y[:N], Y[N:]