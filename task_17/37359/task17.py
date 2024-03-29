count = maxi = 0
f = open('./17.txt', encoding='utf-8')

a = [int(i) for i in f]

for i in range(len(a) - 1):
    for j in range(i + 1, len(a)):
        if (a[i] + a[j]) % 117 == 0:
            count += 1
            maxi = max(maxi, a[i] + a[j])

print(count, maxi)