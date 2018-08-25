napis = input('Podaj napis: ')

zbior = set(napis)
suma = 0
slownik = {}

for litera in zbior:
    suma = napis.count(litera)
    slownik[litera] = suma

print(slownik)


