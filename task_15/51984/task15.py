for A in range(0, 100):
    for x in range(1, 100):
        for y in range(1, 100):
            if not(((144 % x == 0) <= (x % y != 0)) or (x + y > 100) or (A - x > y)):
                break
        if not (((144 % x == 0) <= (x % y != 0)) or (x + y > 100) or (A - x > y)):
            break
    else:
        print(A)

print(A)