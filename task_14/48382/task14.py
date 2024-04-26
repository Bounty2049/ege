for x in range(16):
    if (int(f'8{x}84{x}', 16) + int(f'78{x}34', 16)) % 23 == 0:
        print((int(f'8{x}84{x}', 16) + int(f'78{x}34', 16)) // 23)