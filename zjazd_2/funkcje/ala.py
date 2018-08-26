napis = 'ala ma kota a kot ma ale'
liczba = 3

def wiecej_niz(napis, liczba):
    zbior = set()
    for litera in napis:
        ilosc = napis.count(litera)
        if ilosc > liczba:
            zbior.update(litera)

    return zbior


print(wiecej_niz('ala ma kota a kot ma ale', 3))
