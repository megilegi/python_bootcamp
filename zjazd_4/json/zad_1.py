import json


def dodaj_pracownika(ob):
    try:
        with open(r"lista.json", 'r') as f:
            data = json.load(f)
            data.append(ob)
        with open("lista.json", 'w') as f:
            json.dump(data, f)


    except FileNotFoundError:
        with open(r"lista.json", 'w') as f:
            lista = []
            lista.append(ob)
            json.dump(lista, f)


def wypisz_pracownika():
    with open("lista.json", 'r') as f:
        data = json.load(f)
        for nr, pracownik in enumerate(data, start = 1):
            print(f"- [{nr}] {pracownik['imie']} {pracownik['nazwisko']}"
                  f" - rok: {pracownik['rok']}, pensja: {pracownik['pensja']} PLN"
                )


admin = input("Co chcesz zrobić? [d - dodaj, w - wypisz]: ")
if admin == 'd':
    imie = input(f'Imię: ')
    nazwisko = input(f'Nazwisko: ')
    rok = input(f'Rok urodzenia: ')
    pensja = input(f'Pensja: ')
    ob = {"imie": imie, "nazwisko": nazwisko, "rok": rok, "pensja": pensja}
    dodaj_pracownika(ob)
if admin == 'w':
    wypisz_pracownika()
