import sys

file = sys.argv[1]
assert file == r'C:\Users\kurs\PycharmProjects\bootcamp\zjazd_4\dane.txt', "Zły plik lub jego brak!"

with open(file, 'r', encoding='utf8') as f:

    for i, line in enumerate(f, start=1):
        print(f'{i}: {line}', end = "")


