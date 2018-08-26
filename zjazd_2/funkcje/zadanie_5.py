
def silnia(liczba):
    if liczba > 1:
        return liczba * silnia(liczba - 1)
    else:
        return 1


def test_silnia():
    assert silnia(2) == 2
    assert silnia(0) == 1
    assert silnia(4) == 24