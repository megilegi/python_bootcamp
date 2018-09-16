import json

ob1 = ["AAA", 2, 3, ["Rafał", "Magda"]]

print(json.dumps(ob1))

# zapis do pliku
with open("example.json", 'w') as f:
    json.dump(ob1, f)

with open(r"example.json", 'r') as f:
    data = json.load(f)
    print(data)
    print(type(data))
    data.append("coś tam")

print(data)
with open("example.json", 'w') as f:
    json.dump(data, f)
