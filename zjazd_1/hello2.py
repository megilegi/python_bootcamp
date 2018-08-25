x = 'Hello World'
y = 'Pozdrowienia z Warszawy w słoneczny, sobotni ranek'
z = 'Ala\'s kot'
a = 'Ala\'s \tkot'
b = 'Jedna linia\nDruga linia'
print(x,y,z)
print(x)
print(y)
print(x,'\n', y)
print(z)
print(b)

#\t znak tabulacji - wielokrotność ósemki
# \n znak nowej lini
# z end nie przechodzi print do nowej linii, domyslna wartość
#dla parametru end jest \n
print('Ala', end = ' ')
print('Ola', end = ' ')
print('Ela')
#rozdzielenie wartości spacjami
print('Ala', 'Ela', 'Ola')
#pritn z separatorem ';'
print('Ala', 'Ela', 'Ola', sep = ';', end = '*\n')