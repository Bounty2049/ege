def f(n):
    if n == 0: return 0
    if n > 0 and n % 2 == 0: return f(n / 2)
    if n % 2 != 0: return 1 + f(n - 1)


for x in range(1, 901):
    if f(x) == 9:
        print(x)