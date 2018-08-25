lista = [5, 2, 1, 4, 3]
#
maksimum = lista.index(max(lista))
max_value = max(lista)
min_value = min(lista)

print(maksimum)
minimum = lista.index(min(lista))
print(minimum)
print(lista)
lista[minimum] = max_value
print(lista)
lista[maksimum] = min_value
print(lista)

for i in range(len(lista)):
    print(i, lista[i])