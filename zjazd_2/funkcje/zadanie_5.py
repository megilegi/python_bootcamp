
def silnia(liczba):
    i = 1
    silnia = 1
    while i <= liczba:
        silnia = silnia * i
        i += 1
    return silnia


def test_silnia():
    assert silnia(2) == 2
    assert silnia(0) == 1
    assert silnia(4) == 24