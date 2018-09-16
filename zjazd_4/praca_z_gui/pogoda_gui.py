import zjazd_4.pogoda as pgd
import tkinter

root = tkinter.Tk()
root.title("Pogoda")
root.columnconfigure(1, weight=1)

city_label = tkinter.Label(master=root, text="Podaj miasto")
city_label.grid(row=0, column=0)
city_entry = tkinter.Entry(master=root)
city_entry.grid(row=0, column=1)


def prognoza():
    lokalizacja = city_entry.get()
    id = pgd.wczytaj_miasto(lokalizacja)
    weather_data = pgd.pobierz_dane_pogodowe(id)
    wynik = pgd.wypisz_dane(weather_data)
    wynik_label.configure(text=wynik)


pogoda_button = tkinter.Button(master=root, text="Prognoza pogody", command=prognoza)
pogoda_button.grid(row=2, column=0)

wynik_label = tkinter.Label(master=root, text="-")
wynik_label.grid(row=4, column=0)

root.mainloop()
