import sys
#a = float(input('Podaj pierwszą liczbę:'))
#b = float(input('Podaj drugą liczbę:'))
try:
	a, b = [float(x) for x in input('Podaj pierwszą i drugą liczbę rozdzielone spacją: ').split()]
	operacja = input('Podaj rodzaj operacji:')
except Exception as e:
	print(f'Nastąpił błąd: {e}')
	sys.exit(1)
	


	
	
def kalkulator(a,b, operacja):
	if operacja == '+':
		print(f'Wynik: {a+b}')
	elif operacja == '-':
		print(f'Wynik: {a-b}')
	elif operacja == '*':
		print(f'Wynik: {a*b}')
	elif operacja == '/':
		try:
			print(f'Wynik: {a/b}')
		except:
			print('Dzielenie przez zero niemożliwe!')
	else:
		raise ValueError(f'Nieprawidłowa operacja {operacja}! Obsługiwane operacje: +, -, *, /')
	
kalkulator(a,b,operacja)
