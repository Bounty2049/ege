f = open('./17.txt')
a = [int(i) for i in f]

cnt = 0
max_by_sum = 0
for i in range(len(a) - 1):
    for j in range(i + 1, len(a)):
        if (a[i] + a[j]) % 2 != 0 and (a[i] * a[j]) % 5 == 0:
            cnt += 1
            max_by_sum = max(max_by_sum, a[i] + a[j])

print(cnt, max_by_sum)
