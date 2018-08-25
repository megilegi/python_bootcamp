try:
    i = 1
    lista = []

    while i <= 10:
        liczba = int(input(f'Wprowadź liczbę nr {i}: '))
        lista.append(liczba)
        i += 1

    suma = sum(lista)
    srednia = suma / i
    print(f'Średnia wprowadzonych liczb wynosi: {srednia:.2f}')
except ValueError as e:
    print(f'Błąd: {f}')
