slownik = {
    "mięso": 30.3,
    "jabłka": 4.50,
    "gruszki": 3.90,
    "pomarańcze": 9.99,
    "ser": 25.55
}

stan = {
    "mięso": 5,
    "jabłka": 8,
    "gruszki": 8,
    "pomarańcze": 8,
    "ser": 8
}


try:
    while True:
        nazwa = input('Napisz, co chcesz kupić: ')

        if nazwa in slownik:
            waga = float(input('Napisz, ile kilogramów chcesz kupić: '))
            if waga > stan[nazwa]:
                print(f"Produktu {nazwa} nie ma tyle w magazynie! Jest jedynie {stan[nazwa]}")
                continue
            print(f'Cena za kilogram wynosi: {slownik[nazwa]}')
            print(f'Należność to: {(waga * slownik[nazwa]):.2f}')
            stan[nazwa] -= waga
            print('Dostępne w sklepie produkty to:')
            for produkt in slownik:
                print(f'Produkt: {produkt}, Cena produktu: {slownik[produkt]} PLN, W magazynie: {stan[produkt]} kg')
            break
        else:
            print('Nie ma takiego produktu')
            continue
   # print(stan)



except Exception as e:
    print(f'Błąd: {e}')
