lista = []


for i in range(101):
    if i % 3 == 0 or i % 5 == 0:
        lista.append(i)

print(f'W zadanym przedziale występuje {len(lista)} liczb podzielnych przez 3 lub 5')



