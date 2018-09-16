import urllib.request
import json
import tkinter

def wczytaj_miasto(location):

    with urllib.request.urlopen(f"https://www.metaweather.com/api/location/search/?query={location}") as location_query:
        content = location_query.read()
        data = json.loads(content)
    id = data[0]['woeid']
    return id


def pobierz_dane_pogodowe(id):
    with urllib.request.urlopen(f"https://www.metaweather.com/api/location/{id}") as weather:
        weather_content = weather.read()
        weather_data = json.loads(weather_content)
    return weather_data


def wypisz_dane(weather_data):
    print(
f"- temperatura: {weather_data['consolidated_weather'][0]['the_temp']}\u00b0C\n",
f"- ciśnienie: {weather_data['consolidated_weather'][0]['air_pressure']} hPa\n",
f"- wilgotność: {weather_data['consolidated_weather'][0]['humidity']}%"
    )


if __name__ == "__main__":
    try:
        location = input("Pogoda w: ")
        id = wczytaj_miasto(location)
        weather_data = pobierz_dane_pogodowe(id)
        wypisz_dane(weather_data)
    except Exception as e:
        print(f"Błąd: {e}")

# if __name__ == "__main__":
#    id_ = wczytaj_miasto()
#    weather_data = pobierz_dane_pogodowe(id)
#    wypisz_dane(weather_data)



