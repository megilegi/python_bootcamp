lista = ["A", "B", "C"]
print(lista)

imiona = ("Robert", "Kamil", "Piotrek", "Magda", lista)
lista.append("D")

print(imiona)

print('Count: ', imiona.count("Magda"))
print('Index: ', imiona.index("Magda"))

print(type(imiona))
print(imiona)
print(len(imiona))
print("Robert" in imiona)
print("Tomasz" in imiona)

for x in imiona:
    print(x)

# wybranie pierwszego imienia z listy:
print(imiona[0])

# wybranie ostatniego imienia z listy:
print(imiona[-1])

# wybór imion z zakresu:
print(imiona[1:3])
