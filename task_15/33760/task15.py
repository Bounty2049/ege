def Del(n, m):
    return n % m == 0

for a in range(1, 100):
    for x in range(1, 100):
        if not(Del(120, a) and (Del(x, 36) <= ((not(Del(x, a))) <= (not(Del(x, 45)))))):
            break
    else:
        print(a)