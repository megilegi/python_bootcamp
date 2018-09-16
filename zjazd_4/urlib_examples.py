import urllib.request
import json

f = urllib.request.urlopen("http://api.nbp.pl/api/exchangerates/tables/a?format=json")
content = f.read()
data = json.loads(content)

kursy = data[0]['rates']

for kurs in kursy:
    print(f"{kurs['currency']}, {kurs['code']}, {kurs['mid']}")
