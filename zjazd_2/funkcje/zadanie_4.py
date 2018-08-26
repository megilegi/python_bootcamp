cena = 10

napis1 = 'koszt $cena PLN'

napis2 = 'kwota $cena brutto'

# wróć do tego!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1
# def formatuj(*arg, cena = 10):
#     for a in arg:
#         b = a.replace('$cena', str(cena))
#     arg =
#     return "\n".join(arg)
#     #     #napis2 = napis2.replace('$cena', str(cena))
#     #     return (napis1, '\n')
#     # return (napis1, '\n')

print(formatuj('koszt $cena PLN', 'kwota $cena brutto', cena = 15))


# def test_formatuj_1():
#     assert formatuj('koszt $cena PLN', 'kwota $cena brutto', cena=10) == ('koszt 10 PLN', '\n','kwota 10 brutto')
#
#
# def test_formatuj_2():
#     assert formatuj('', '') == ('', '\n', '')
#
#
# def test_formatuj_3():
#     assert formatuj('10', '10') == ('10', '\n', '10')
#
# def test_formatuj_4():
#     assert formatuj('$cena', '$cena', 'ss') == ('$cena', '\n', '$cena')
