for a in range(0, 100):
    for x in range(0, 100):
        for y in range(0, 100):
            if not((x * y < 121) or (y > a) or (x >= a)):
                break
        if not((x * y < 121) or (y > a) or (x >= a)):
                break
    else:
        print(a)