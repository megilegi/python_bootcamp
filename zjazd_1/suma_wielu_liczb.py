
suma = 0
i = 0
srednia = 0

try:
	while True:
		liczba = input('Podaj kolejną liczbę całkowitą lub koniec, żeby zakończyć: ')
		if liczba == 'koniec':
			print(f'Koniec programu, suma to: {suma}, liczba liczb: {i}, średnia to: {srednia}')
			break
		else:
			liczba = int(liczba)
			suma += liczba
			i += 1
			srednia = suma/i
except ValueError as e:
	print(f'Wprowadź liczbę albo koniec, błąd: {e}')
	
	