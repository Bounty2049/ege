for x in '0123456789ABC':
    if (int(f'{x}A04', 13) + int(f'1D{x}3', 18)) % 184 == 0:
        print((int(f'{x}A04', 13) + int(f'1D{x}3', 18)) // 184)