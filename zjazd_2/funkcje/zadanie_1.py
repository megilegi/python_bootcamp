x = 5


def czy_jest_pierwsza(liczba):
    i = 2
    while i <= liczba:
        if liczba == 2:
            return True
        elif liczba % i == 0:
            return False
        else:
            return True
        i = +1


print(czy_jest_pierwsza(x))


def test_czy_jest_pierwsza_pierwsza():
    assert czy_jest_pierwsza(3)
    assert czy_jest_pierwsza(7)

def test_czy_jest_pierwsza_niepierwsza():
    assert not czy_jest_pierwsza(4)
    assert not czy_jest_pierwsza(6)
