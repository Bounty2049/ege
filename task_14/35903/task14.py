x = 729 ** 6 + 3 ** 14 - 36

s = []
while x > 0:
    s.append(x % 9)
    x //= 9
s = s[::-1]
print(s.count(0))