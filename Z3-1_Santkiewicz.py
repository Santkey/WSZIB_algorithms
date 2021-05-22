import time, math
def funkcja (x): 
    wart_15 = x**2 - x + 1
    return wart_15

def pole (a, b, n): 
    suma_15 = 0
    val_15 = a
    delta_15 = (b - a)/n
    while val_15 < b:
        suma_15 =  suma_15 + (funkcja(val_15) + funkcja(val_15+delta_15)) * delta_15/2
        val_15 = val_15 + delta_15       
    return suma_15

def calka (a, b, epsilon):
    roznica_15 = 1
    n = 1
    val_1_15 = pole (a, b, n)
    licznik_15 = 0
    while roznica_15 > epsilon:
        licznik_15 = licznik_15 + 1
        n *= 2
        val_2_15 = pole (a, b, n)
        roznica_15 = math.fabs ((val_2_15 - val_1_15)/val_2_15)
        val_1_15 = val_2_15
    return val_2_15, n, licznik_15
    
gor_gr_15 = 10 
epsilon_15 = 10**-8
dol_gr_15 = 0 
t0=time.time()
integral_15, n_15, licznik_15 = calka (dol_gr_15, gor_gr_15, epsilon_15)
t1=time.time()
print ('Wartość całki oznaczonej w przedziale od',dol_gr_15,'do',gor_gr_15,'wynosi:',integral_15)
print('Przedział został podzielony na:',n_15,' odcinków')
print('Liczba iteracji wynosi:',licznik_15)
print ("Czas obliczania to:", t1 - t0, "sekund")