for x in range(16):
    if (int(f'2{x}BAD', 16) + int(f'3C{x}FE', 16)) % 15 == 0:
        print((int(f'2{x}BAD', 16) + int(f'3C{x}FE', 16)) // 15)