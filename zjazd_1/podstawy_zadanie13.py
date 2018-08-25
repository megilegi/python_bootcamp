ILE_DNI = 7
i = 1
sum_temp = 0
while i in range(ILE_DNI +1 ):
	temp = float(input(f'Podaj temperaturę dla dnia tygodnia {i}: '))
	sum_temp = sum_temp + temp
	i += 1

print(f'Średnia temperatura dla tygodnia wynosi: {sum_temp/ILE_DNI:.2f} stopni Celsjusza')