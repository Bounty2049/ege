for A in range(128):
    for x in range(128):
        if (x & 49 != 0 or (x & 28 == 0 or x & A != 0)) == 0:
            break
    else:
        print(A)
