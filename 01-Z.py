'''Proszę w Pythonie:
1. Zdefiniować 3  listy tej samej długości (np. zest_1, zest_2, zest_3). Eelementami 2 list są liczby naturalne. Lista 3. jest pusta.
2. Listę 3. wypełnić sumami kwadratów kolejnych elementów listy 1. i 2 - np. zest_3[2] = zest_1[2]**2 + zest_2[2]**2
3. Elementy listy 3. należy zsumować i dla tej sumy obliczyć pierwiastek kawdratowy.
4. Wydrukować (z opisami) listy, sumę z listy 3. i pierwiastek kwadratowy.

Plik .py należy zapisać w SAKE jako rozwiązanie tego zadania.'''

import math

zest_1_15 = [2,4,6,8,10]
zest_2_15 = [8,64,108,512,1000]
zest_3_15 = []

print("Lista 1: ",zest_1_15)
print("Lista 2: ",zest_2_15)
print("Lista 3: ",zest_3_15)

zest_3_15.append(zest_1_15[0]**2 + zest_2_15[0]**2)
zest_3_15.append(zest_1_15[1]**2 + zest_2_15[1]**2)
zest_3_15.append(zest_1_15[2]**2 + zest_2_15[2]**2)
zest_3_15.append(zest_1_15[3]**2 + zest_2_15[3]**2)
zest_3_15.append(zest_1_15[4]**2 + zest_2_15[4]**2)

suma_15 = zest_3_15[0]+zest_3_15[1]+zest_3_15[2]+zest_3_15[3]+zest_3_15[4]

print("Lista uzupełniona kwadratami liczb: ",zest_3_15)
print("Suma liczb z listy 3: ",suma_15)

pierw_15 = math.sqrt(suma_15)

print("Pierwiastek kwadratowy z sumy: ",pierw_15)