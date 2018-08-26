lista = [1, 2, 5, 8, 10, 13, 58888, 620, 795, 15, 8, 8, 620, 620, 12, 16, 1599998]
print(lista)
zbior = set(lista)
print(zbior)
suma = 0
zbior1 = set(range(101))
print('zbior1: ', zbior1)
print('zbior: ', zbior)
zbior3 = set()

lista = []

for liczba in zbior:
    if liczba in zbior1:
        if liczba % 2 == 0:
            suma += 1
            lista.append(liczba)


# set(range(0,101,2))


print(suma)
print(lista)
