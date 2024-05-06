for a in range(0, 10**5):
    for x in range(0, 10**5):
        if ((x & 21074 != 0) <= ((x & 12369 == 0) <= (x & a != 0)))==0:
            break
    else:
        print(a)
        break