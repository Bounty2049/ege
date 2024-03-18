for x in '0123456789AB':
    for y in '0123456789AB':
        if (int(f'{x}231{y}', 12) + int(f'78{x}98{y}', 14)) % 99 == 0:
            print((int(f'{x}231{y}', 12) + int(f'78{x}98{y}', 14)) // 99) 