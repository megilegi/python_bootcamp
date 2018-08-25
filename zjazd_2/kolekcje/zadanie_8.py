napis = input('Podaj napis: ')

if napis.count('<') == 1 and napis.count('>') == 1:
    for i in napis:
        ile_start = napis.index('<')
        ile_end = napis.index('>')
    ile = ile_end - ile_start - 1
    print(f'Długość napisu wynosi: {ile}')
else:
    print('Nawias <> może wystąpić tylko raz!')

