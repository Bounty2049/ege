f = open('17.txt', encoding='utf-8')

a = [int(i) for i in f]

maxi = cnt = 0
for i in range(len(a) - 2):
    a1 = sorted([a[i], a[i + 1], a[i + 2]])
    if (a1[0] ** 2 + a1[1] ** 2) > (a1[2] ** 2):
        cnt += 1
        maxi = max(maxi, sum(a1))

print(cnt, maxi)