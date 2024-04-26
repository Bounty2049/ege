for x in '0123456789A':
    for y in '0123456789A':
        if (int(f'{x}341{y}', 11) + int(f'56{x}1{y}', 19)) % 305 == 0:
            print((int(f'{x}341{y}', 11) + int(f'56{x}1{y}', 19)) // 305)