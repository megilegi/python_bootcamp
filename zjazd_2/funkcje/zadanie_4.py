cena = 10

napis1 = 'koszt $cena PLN'

napis2 = 'kwota $cena brutto'


def formatuj(napis1, napis2, cena = 10):
    if isinstance(cena, int) == True:
        napis1 = napis1.replace('$cena', str(cena))
        napis2 = napis2.replace('$cena', str(cena))
        return (napis1, '\n', napis2)
    return (napis1, '\n', napis2)

formatuj(napis1, napis2)

# def formatuj(napis1, napis2, cena : int):
#
#     napis1 = napis1.replace('$cena', str(cena))
#     napis2 = napis2.replace('$cena', str(cena))
#
#     return (napis1, '\n', napis2)
#
# formatuj(napis1, napis2)

def test_formatuj_1():
    assert formatuj('koszt $cena PLN', 'kwota $cena brutto', cena=10) == ('koszt 10 PLN', '\n','kwota 10 brutto')


def test_formatuj_2():
    assert formatuj('', '') == ('', '\n', '')


def test_formatuj_3():
    assert formatuj('10', '10') == ('10', '\n', '10')

def test_formatuj_4():
    assert formatuj('$cena', '$cena', 'ss') == ('$cena', '\n', '$cena')
