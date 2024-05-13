f = open('17.txt', encoding='utf-8')
a = [int(i) for i in f]

count = maxi = 0
for i in range(len(a) - 1):
    if (a[i] * a[i + 1]) % 15 == 0 and (a[i] + a[i + 1]) % 7 == 0:
        count += 1
        maxi = max(maxi, a[i] + a[i + 1])

print(count, maxi)