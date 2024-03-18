for y in range(0, 12):
    for x in range(0, 12):
        if (int(f'{y}AA{x}', 12) + int(f'{x}02{y}', 14)) % 80 == 0:
            print((int(f'{y}AA{x}', 12) + int(f'{x}02{y}', 14)) // 80)