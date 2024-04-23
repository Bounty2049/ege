import math

N = 60
A = 9 + 250
i = math.ceil(math.log(A, 2))
V_1 = math.ceil(N * i / 8)
V_all = 65536 * V_1 / (2 ** 10)
print(V_all)