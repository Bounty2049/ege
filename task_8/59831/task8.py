import pprint
from itertools import product

cnt = 0
for i in product('012345678', repeat=5):
    x = ''.join(i)
    if x.count('5') == 1 and x[0] != '0' and '15' not in x and '35' not in x \
            and '75' not in x and '51' not in x and '53' not in x and '57' not in x:
        cnt += 1

print(cnt)