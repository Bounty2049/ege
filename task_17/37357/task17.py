f = open('./17.txt')
a = [int(i) for i in f]

suit = []
for i in range(len(a) - 1):
    for j in range(i + 1, len(a)):
        if (a[i] + a[j]) % 8 == 0:
            suit.append(a[i] + a[j])

print(len(suit), max(suit))
