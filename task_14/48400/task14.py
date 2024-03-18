for x in range(0, 100):
    if (int(f'95{x}2', 11) + int(f'{x}458', 12)) % 136 == 0:
        print(x, (int(f'95{x}2', 11) + int(f'{x}458', 12)) // 136)