a = {0: 'А', 1: 'Н', 2: 'Д', 3: 'Р', 4: 'Е', 5: 'Й'}

cnt = 0
for i in range(len(a)):
    for j in range(len(a)):
        for k in range(len(a)):
            for y in range(len(a)):
                for x in range(len(a)):
                    for z in range(len(a)):
                        st = f'{a[i]}{a[j]}{a[k]}{a[y]}{a[x]}{a[z]}'
                        if st.count('А') >= 1 and st.count('Й') <= 1:
                            cnt += 1

print(cnt)