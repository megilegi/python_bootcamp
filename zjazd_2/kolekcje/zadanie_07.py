napis = input('Podaj napis: ')

litery = napis.split()
samogloski = ('a', 'e', 'i', 'o', 'u', 'y')
suma = 0

for l in samogloski:
    liczba = napis.count(l)
    suma += liczba
    print(f'W napisie \'{napis}\' litera \'{l}\' występuje {liczba} raz(y)')

print(f'Natomiast mamy {suma} samogłosek')
