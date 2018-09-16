import urllib.request
import json


def wczytaj_miasto():
    location = input("Pogoda w: ")
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

try:
    id = wczytaj_miasto()
    weather_data = pobierz_dane_pogodowe(id)
    wypisz_dane(weather_data)
except Exception as e:
    print(f"Błąd: {e}")
