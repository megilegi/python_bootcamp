napis = input('Podaj napis: ')

zbior = set(napis)

suma = 0
slownik = {}

# for litera in zbior:
#     suma = napis.count(litera)
#     slownik[litera] = suma


for litera in napis:
    # suma = napis.count(litera)
    # slownik[litera] = suma
    slownik[litera] = slownik.get(litera, 0) + 1

print(slownik)
