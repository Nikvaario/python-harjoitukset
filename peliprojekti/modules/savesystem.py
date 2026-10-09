import json

# Saves player progress from given data and saves a .json file to savefiles folder
def savePlayer(name=str, age=int, inventory=[], location="", area1E=bool, area2E=bool, area3E=bool, area5E=bool, area2I=bool, area3I=bool, area4I=bool, area5I=bool):
    data = {
        "name": name,
        "age": age,
        "inventory": inventory,
        "location": location,
        "area1Explore": area1E,
        "area2Explore": area2E,
        "area3Explore": area3E,
        "area5Explore": area5E,
        "area2Interact": area2I,
        "area3Interact": area3I,
        "area4Interact": area4I,
        "area5Interact": area5I,
    }
    try:
        with open(f"peliprojekti/savefiles/{name}Data.json", "w") as file:
            json.dump(data, file)
            print(f"Created a savefile with the name {name}. See you again!")
    except FileNotFoundError:
        print("Couldn't create a safe file, because savefiles folder doesn't exists or had been modified.")

# loads a savefile to the game by a given name from savefiles data
def loadPlayer():
    name = input("Please input the player name of your save file: ")
    while True:
        try:
            with open(f"peliprojekti/savefiles/{name}Data.json", "r") as file:
                data = json.load(file)
                return data
            break
        except FileNotFoundError:
            name = input(f"Data not found with name {name}. Please try again: ")
