cnt = 0
for a in range(1, 100):
    for x in range(0, 100):
        for y in range(0, 100):
            if not(((x < a) <= (x ** 2 < 100)) and ((y ** 2 <= 64) <= (y <= a))):
                break
        if not(((x < a) <= (x ** 2 < 100)) and ((y ** 2 <= 64) <= (y <= a))):
                break
    else:
        cnt += 1

print(cnt)   