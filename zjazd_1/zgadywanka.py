try:
	while True:
		liczba = int(input('Podaj kolejną liczbę: '))
		if liczba%7==0:
			print(f'Liczba, którą podałeś to: {liczba}. Jest ona podzielna przez 7. Koniec programu!')
			break
except Exception as e:
	print(f'Należy podać liczbę, a nie inny znak! Błąd: {e}')