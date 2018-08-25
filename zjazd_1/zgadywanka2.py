from random import randint

ZAKRES  = 10
x = randint(1, ZAKRES)
y = randint(1, ZAKRES)

iloczyn_los = x * y

print(f'Wylosowane liczby x i y wynoszą: {x}, {y}')
i = 0
try:
	while True:
		iloczyn = int(input('Podaj iloczyn wylosowanych liczb: '))
		i += 1
		if iloczyn == iloczyn_los:
			print(f'Gratulacje! Odgadłeś prawidłowy iloczyn za {i} razem')
			break
			
except ValueError as e:
	print(f'Podaj liczby! Błąd: {e}')