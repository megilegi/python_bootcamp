lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for x in lista:
    for y in lista:
        print(x * y, end="\t")
    print

for wiersz in range(0, 10):
    for kolumna in range(0, 10):
        print(wiersz * kolumna, end="\t")
    print()
