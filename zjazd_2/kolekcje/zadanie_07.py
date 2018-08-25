napis = input('Podaj napis: ')

litery = napis.split()
samogloski = ('a', 'e', 'i', 'o', 'u', 'y')

for l in samogloski:
    liczba = napis.count(l)
    print(f'W napisie \'{napis}\' litera \'{l}\' występuje {liczba} raz(y)')
