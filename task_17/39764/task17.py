f = open('17.txt', encoding='utf-8')

a = [int(i) for i in f]

maxi = cnt = 0

for i in range(len(a) - 2):
    l = sorted([a[i], a[i + 1], a[i + 2]])
    if l[0] ** 2 + l[1] ** 2 == l[2] ** 2:
        cnt += 1
        maxi = max(maxi, sum(l))

print(cnt, maxi)