def Del(n, m):
    return n % m == 0

for A in range(1, 200):
    for x in range(1, 200):
        if ((Del(x, 3) <= (not(Del(x, 5)))) or (x + A >= 90)) == 0:
            break
    else:
        print(A)
        break