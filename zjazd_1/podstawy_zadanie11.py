try:
	x = int(input('Podaj pozycję gracza X: '))
	y = int(input('Podaj pozycję gracza Y: '))
except Exception as e:
	print(f'Wystąpił następujący błąd: {e}')


if x<0 or x>100 or y<0 or y >100:
	print('Jesteś poza planszą!')
elif  x <9:
	if y < 9:
		print('Lewy górny róg')
	elif y >=9 and y < 91:
		print('Lewa krawędź')
	elif y >=91:
		print('Lewy dolny róg')
elif x >= 9 and x <91:
	if y < 9:
		print('Górna krawędź')
	elif y >=9 and y < 91: 
		print('Centrum')
	elif y >=91:
		print('Dolna krawędź')
elif x >= 91:
	if y < 9:
		print('Prawy górny róg')
	elif y >=9 and y < 91: 
		print('Prawa krawędź')
	elif y >=91:
		print('Dolny prawy róg')
