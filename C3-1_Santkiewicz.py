import time, random
tab = []
for i in range(0, 99):
    tab.append(random.randint(1,1000))
print(tab)
for i in range(0,99):
    for j in range(i, 99):
        if tab[i] > tab[j]:
            tab[i], tab[j] = tab[j], tab[i]
print(tab)
