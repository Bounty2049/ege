for a in range(0, 100000):
    for x in range(0, 9):
        if (int(f'842{x}5', 9) + a) % int(f'8{x}725', 9) == 0:
            print(a) 