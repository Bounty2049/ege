def Del(n, m):
    if n % m == 0:
        return True
    
    return False

for a in range(1, 1000):
    for x in range(1, 1000):
        if not((Del(x, 2) <= (not(Del(x, 3)))) or (x + a >= 100)):
            break
    else:
        print(a)