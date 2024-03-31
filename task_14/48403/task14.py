for x in range(0, 100):
    if (int(f'2AB{x}', 12) + int(f'{x}8E', 17)) % 27 == 0:
        print((int(f'2AB{x}', 12) + int(f'{x}8E', 17)) // 27)
