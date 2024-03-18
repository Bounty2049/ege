for x in '0123456789ABC':
    if (int(f'4C{x}4', 15) + int(f'{x}62A', 13)) % 121 == 0:
        print((int(f'4C{x}4', 15) + int(f'{x}62A', 13)) // 121)