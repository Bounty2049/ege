from itertools import product

cnt = 0

for i in product('МАНГУСТ', repeat=6):
    s = ''.join(i)
    if s[0] != 'А' and s.count('У') >= 1 and s.count('М') == 2:
        cnt += 1

print(cnt)