from random import randint

ZAKRES = 10

x_skarb = randint(1,ZAKRES)
y_skarb = randint(1,ZAKRES)


x_gracz = randint(1,ZAKRES)
y_gracz = randint(1,ZAKRES)


print(f'Twoja początkowa pozycja to: {x_gracz}, {y_gracz}')

start_odleglosc_x = abs(x_skarb - x_gracz)
start_odleglosc_y = abs(y_skarb - y_gracz)


while (x_skarb != x_gracz or y_skarb!=y_gracz):
	
	kierunek_x = input('Podaj ruch wzdłuż osi x: prawo lub lewo lub brak: ')
	if kierunek_x == 'prawo':
		x_gracz +=1
	elif kierunek_x == 'lewo':
		x_gracz -=1
	elif kierunek_x == 'brak':
		x_gracz -=0
	else:
		print('Nie ma takiej komendy')
		continue
	
	if x_gracz < 0 or x_gracz > 10:
		print('Jesteś poza planszą! Koniec gry')
		break

		
	kierunek_y = input('Podaj ruch wzdłuż osi y: góra lub dół lub brak: ')
	if kierunek_y == 'góra':
		y_gracz -=1
	elif kierunek_y == 'dół':
		y_gracz +=1
	elif kierunek_y == 'brak':
		y_gracz +=0
	else:
		print('Nie ma takiej komendy')
		continue
		
	if y_gracz < 0 or y_gracz > 10:
		print('Jesteś poza planszą! Koniec gry')
		break

		
	if x_skarb-x_gracz <= start_odleglosc_x and y_skarb-y_gracz <= start_odleglosc_y:
		print('Jesteś bliżej!')
		if x_skarb-x_gracz == start_odleglosc_x and y_skarb-y_gracz == start_odleglosc_y:
			print('Gratulacje! Zdfobyłes skarb')
			break
	else:
		print('Jesteś dalej :(')
	print(f'Twoja aktualna pozycja: {x_gracz}, {y_gracz}')
	