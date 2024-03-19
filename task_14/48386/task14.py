for x in range(16):
    for y in range(16):
        if (int(f'90{x}4{y}', 15) + int(f'91{x}{y}2', 16)) % 56 == 0:
            print((int(f'90{x}4{y}', 15) + int(f'91{x}{y}2', 16)) // 56)