'''Zdefiniować listę zawierającą liczby naturalne i wydrukować te
 elementy listy, które są mniejsze od dowolnej zdefiniowanej wartości.'''

naturalne = []
mniejsze = 7

lista = [13,2,6,800,300,910,37,55,73,92,-6,18]
for element in lista:
    if element<mniejsze:
        naturalne.append(element)

print(naturalne)
