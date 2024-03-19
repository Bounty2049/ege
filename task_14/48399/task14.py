for x in '012345689ABCD':
    if (int(f'3D4{x}', 16) + int(f'4{x}C4', 14)) % 154 == 0:
        print((int(f'3D4{x}', 16) + int(f'4{x}C4', 14)) // 154)