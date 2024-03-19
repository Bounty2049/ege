for a in range(0, 1001):
    for x in range(0, 1001):
        for y in range(0, 1001):
            if not((x >= 12) or (3 * x < y) or (x * y < a)):
                break
        if not((x >= 12) or (3 * x < y) or (x * y < a)):
                break
    else:
        print(a)