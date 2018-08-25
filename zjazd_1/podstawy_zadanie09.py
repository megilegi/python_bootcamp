import datetime as d

rok = int(d.datetime.now().year)
rok_urodzenia = int(input('Podaj rok urodzenia:'))
wiek = rok -rok_urodzenia
if wiek >= 18:
	print('Jesteś pełnoletni')
else:
	print('Jesteś małolat!')
 