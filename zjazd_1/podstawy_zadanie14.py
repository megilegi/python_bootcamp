min = 0
max = 0
i = 0

try:
	while True:
		wpis = input('Podaj liczbę lub zakończ program komendą KONIEC: ')
		if wpis == 'KONIEC':
			print('Koniec programu. Do widzenia!')
			break
		wpis = int(wpis)
		#nie trzeba robić else: po break (chyba, że zwiększa to czytelność)
		if i ==0:
			min = wpis
			max = wpis
		else:	
			if wpis < min:
				min = wpis
			if wpis > max:
				max = wpis

		i =+1
		print(f'Maksymalna liczba: {max}, a minimalna liczba: {min}')
			
except Exception as e:
	print(f'Należy wpisać liczbę lub KONIEC w celu zakończenia programu! Błąd: {e}')

		

