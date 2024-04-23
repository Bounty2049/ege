from math import ceil, log

N = 11
A = 26 * 2
i = ceil(log(A, 2))
V = ceil(N * i / 8)
V_all = 2400
V_1 = V_all / 40
X = V_1 - V
print(X)
