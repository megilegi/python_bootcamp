lista = [1, -5, 5, -8, 6, -7, -10]

count_minus = []
count_plus = []

for liczba in lista:
    if liczba >= 0:
        count_plus.append(liczba)
    else:
        count_minus.append(liczba)

print(f'W liście występuje {len(count_plus)} liczb(y) dodatnich oraz {len(count_minus)} liczb(y) ujemnych')
