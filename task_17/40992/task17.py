f = open('17.txt', encoding='utf-8')

a = [int(i) for i in f]
s = [int(a[i]) for i in range(len(a)) if a[i] % 2 == 1]
n = sum(s) / len(s)

cnt = maxi = 0

for i in range(len(a) - 1):
    if (a[i] % 5 == 0 or a[i + 1] % 5 == 0) and (a[i] < n or a[i + 1] < n):
        cnt += 1
        maxi = max(maxi, (a[i] + a[i + 1]))

print(cnt, maxi)