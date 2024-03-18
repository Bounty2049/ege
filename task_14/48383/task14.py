for x in range(0, 9):
    if (int(f'88{x}4{x}', 9) + int(f'7{x}344', 9)) % 67 == 0:
        print((int(f'88{x}4{x}', 9) + int(f'7{x}344', 9)) // 67)