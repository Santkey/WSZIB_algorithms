import  math
 
lista_15 = [32, -906, 21, -99, 11, 1, 90, 680, -87]
print ('Lista: ', lista_15)
 
def minimum_15 (list_15):
    ind_min_15 = 0
    val_min_15 = list_15[0]
    licz_15 = 0
    while licz_15 < len (list_15):
        if list_15[licz_15] < val_min_15:
            val_min_15 = list_15[licz_15]
            ind_min_15 = licz_15
        licz_15 += 1
    return ind_min_15, val_min_15
 
var_15=len(lista_15)
for element in lista_15:
    ind_min_15, val_min_15 = minimum_15 (lista_15[0:var_15])
    del lista_15 [ind_min_15]
    lista_15.append(val_min_15)
    var_15 = var_15-1
 
print ("lista posortowana: ", lista_15)
    
 
 
 
 

