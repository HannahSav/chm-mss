import numpy as np
from scipy.sparse import csr_matrix

'''
FOR N = 3

Matrix P:
  g   g   g
  ___ ___ ___
g |k=0|k=1|k=2| g
   ___ ___ ___
g |k=3|k=4|k=5| g
   ___ ___ ___
g |k=6|k=7|k=8| g
   ___ ___ ___ 
    g   g   g
    
matrix of coef for P:
  0  1  2  3  4  5  6  7  8  
____________________________
0|+  c  0  c  0  0  0  0  0
1|c  +  c  0  c  0  0  0  0
2|0  c  +  _  0  c  0  0  0
3|c  0  _  +  c  0  c  0  0
4|0  c  0  c  +  c  0  c  0
5|0  0  c  0  c  +  -  0  c
6|0  0  0  c  0  -  +  c  0
7|0  0  0  0  c  0  c  +  c
8|0  0  0  0  0  c  0  c  +

Но как потом такую систему решать методом МКО????

U:
 |    |    |    |    |    |
 |   g=2  g=2  g=2  g=2   |
 |    |    |    |    |    |
_______________________________ U = (1, 0)
 |    |    |    |    |    |
g=0  u=0  u=0  u=0  u=0  g=0
 |    |    |    |    |    |
_______________________________
 |    |    |    |    |    |
g=0  u=0  u=0  u=0  u=0  g=0
 |    |    |    |    |    |
_______________________________ 
 |    |    |    |    |    |
g=0  u=0  u=0  u=0  u=0  g=0
 |    |    |    |    |    |
 _______________________________ U = (0, 0)
 |    |    |    |    |    |
 |   g=0  g=0  g=0  g=0   |
 |    |    |    |    |    |
 
 
 For V - transpose U

'''

def create_matrix_start(N):
    V = np.zeros((N - 1,N))
    U = np.zeros((N,N - 1))
    P = np.zeros((N,N))
    return P, V, U


def remake(P, V, U, tau):
    return


N = int(input("Input N:"))
P, V, U = create_matrix_start(N)
diff = 1
tau = 0.01
while diff > 0.001:
    remake(P, V, U, tau)
    print("Matrix P:")
    print(P)
    print("\nMatrix V:")
    print(V)
    print("\nMatrix U:")
    print(U)
