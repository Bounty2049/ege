count = m = 0
f = open('17.txt')
l = [int(i) for i in f]
mini = min([l[i] for i in range(len(l)) if abs(l[i]) % 10 == 7])

for i in range(len(l) - 1):
    x = abs(l[i])
    y = abs(l[i + 1])
    if ((x % 10 == 7 and y % 10 != 7) or (x % 10 != 7 and y % 10 == 7)) and ((l[i] ** 2 + l[i + 1] ** 2) < mini ** 2):
        count += 1
        m = max(m, (l[i] ** 2 + l[i+1] ** 2))
        
print(count, m)