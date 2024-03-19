def Del(n, m):
    return n % m == 0


for a in range(1, 100):
    for x in range(1, 100):
        if not(Del(x, a) <= ((not(Del(x, 21))) + Del(x, 35))):
            break
    else:
        print(a)