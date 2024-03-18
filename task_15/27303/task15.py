for a in range(0, 100):
    for x in range(0, 100):
        for y in range(0, 100):
            if not((4 * x + 3 * y < a) or (x >= y) or (y >= 13)):
                break
        if not((4 * x + 3 * y < a) or (x >= y) or (y >= 13)):
                break
        
    else:
        print(a)