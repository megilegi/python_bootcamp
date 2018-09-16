import tkinter

root = tkinter.Tk()
root.title("Kalkulator cen paliwa")
root.columnconfigure(1, weight=2)


def koszt_przejazdu():
    dystans = int(dystans_entry.get())
    spalanie = int(spalanie_entry.get())
    cena = int(cena_entry.get())
    wynik_label.configure(text=f"Wynik: {dystans*spalanie*cena/100}")

def zeruj_koszt():
    wynik_label.configure(text=f"Wynik:        -      ")


dystans_label = tkinter.Label(master=root, text=f"dystans [km]")
dystans_label.grid(row=0, column=0)
dystans_entry = tkinter.Entry(master=root)
dystans_entry.grid(row=0, column=1)

spalanie_label = tkinter.Label(master=root, text="spalanie na 100km [l/100 km]")
spalanie_label.grid(row=1, column=0)
spalanie_entry = tkinter.Entry(master=root)
spalanie_entry.grid(row=1, column=1)

cena_label = tkinter.Label(master=root, text="cena za litr paliwa [PLN/l]")
cena_label.grid(row=2, column=0)
cena_entry = tkinter.Entry(master=root)
cena_entry.grid(row=2, column=1)

koszt_button = tkinter.Button(master=root, text="Oblicz koszt przejazdu", command=koszt_przejazdu)
koszt_button.grid(row=3, column=0)

wynik_label = tkinter.Label(master=root, text="wynik: -")
wynik_label.grid(row=4, column=0)


zeruj_button = tkinter.Button(master=root, text="Zeruj koszt", command=zeruj_koszt)
zeruj_button.grid(row=3, column=1)


root.mainloop()

