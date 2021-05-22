'''Proszę zdefiniować dwie listy zawierające łańcuchy (stringi) a następnie:

1. Wydrukować listy

2. Utworzyć listę będącą sumą tych dwu list i ją wydrukować

3. Dodać do listy wynikowej string 'Koniec' i wydrukować listę
'''
lista_1 = ['slowo','slowko','wyraz','wyrazik','wyrazenie']
lista_2 = ['slowo_2','slowko_2','wyraz_2','wyrazik_2','wyrazenie_2']

print(lista_1)
print(lista_2)

suma = lista_1 + lista_2
print(suma)

suma.append('Koniec')
print(suma)
