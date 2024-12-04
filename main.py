import json

with open('data/user.json', 'r') as file:
    data = json.load(file)
    data.append({
        "name": "Petar Petrovic",
        "age": 35,
        "height": 190,
        "gender": "Male"
    })
    print(data)

with open('data/user.json', 'w') as file:
    json.dump(data, file, indent=4)