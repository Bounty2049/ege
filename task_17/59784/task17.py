count = 0
m = 100000000
f = open('17.txt')
l = [int(i) for i in f]
        
max15 = max([i for i in l if i % 100 == 15])

for i in range(len(l) - 2):
    c = 0
    s = [l[i], l[i+1],  l[i+2]]
    for x in s:
        if 999 < abs(x) < 10000:
            c += 1
    if c == 1 and sum(s) < max15:
        m = min(m, (l[i] + l[i+1] + l[i+2]))
        count += 1
print(count, m)
print(len(s), min(s))