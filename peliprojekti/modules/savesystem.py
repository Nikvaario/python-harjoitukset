import json

def savePlayer(name, age, cash, inventory, location, area1, area2, area3 ):
    data = {
        "name": name,
        "age": age,
        "cash": cash,
        "inventory": inventory,
        "location": location,
        "area1trash": area1,
        "area2trash": area2,
        "area3trash": area3,
    }
    with open("playerData.json", "w") as file:
        json.dump(data, file)

def loadPlayer():
    with open("playerData.json", "r") as file:
        data = json.load(file)
        return data
