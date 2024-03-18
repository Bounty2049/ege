for a in range(0, 1000):
    for x in range(0, 1000):
        for y in range(0, 1000):
            if not((x + 3 * y > a) or (x < 30) or (y < 30)):
                break
        if not((x + 3 * y > a) or (x < 30) or (y < 30)):
                break
    else:
        print(a)