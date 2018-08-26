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


def test_wiecej_niz_pusty():
    assert wiecej_niz("", 1) == set()


def test_wiecej_niz_pusty_3():
    assert wiecej_niz("ala ma kota a kot ma ale", 3) == {' ', 'a'}


def test_wiecej_niz_pusty_4():
    assert wiecej_niz("ala ma kota a kot ma ale", 4) == {'a'}


def test_wiecej_niz_pusty_4():
    assert wiecej_niz("ala ma kota a kot ma ale", 6) == {'a'}


