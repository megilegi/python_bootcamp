import math

miastoA = input('Miasto A: ')
miastoB = input('Miasto B: ')
dystans = float(input(f'Dystans {miastoA}-{miastoB}:' ))
cena_paliwa = float(input('Cena paliwa: '))
spalanie = float(input('Spalanie na 100 km: '))
koszt = int(round(cena_paliwa*spalanie*dystans/100,0))

print(f'Koszt przejazdu {miastoA}-{miastoB} to {koszt}')

	