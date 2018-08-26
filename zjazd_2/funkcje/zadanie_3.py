def policz_znaki(tekst, znak_start='<', znak_stop='>'):
    lista = []
    if znak_start and znak_stop in tekst:
        for i in tekst:
            lista.append(i)
        for i in tekst:
            if i == znak_start:
                start = lista.index(znak_start)

            if i == znak_stop:
                stop = lista.index(znak_stop)
        return (stop - start - 1)
    else:
        return 0


print(policz_znaki('ala ma <kota> a kot ma ale'))


def test_policz_znaki_0():
    assert policz_znaki('ala ma kota a kot ma ale') == 0


def test_policz_znaki_1():
    assert policz_znaki('ala ma <kota> a kot ma ale') == 4


def test_policz_znaki_2():
    assert policz_znaki('ala ma [kota [a kot]] ma [ale]', '[', ']') == 18


def test_policz_znaki_3():
    assert policz_znaki('a <a<a<a>>>') == 6


def test_policz_znaki_kwadratowy_nawias():
    assert policz_znaki('ala ma [kota] a kot ma ale', '[', ']') == 4
