import sys

class Player():
    def __init__(self, name, age, inventory, cash, location):
        self.name = name
        self.age = age
        self.inventory = inventory
        self.cash = cash
        self.location = location
        pass

class Trash():
    def __init__(self, name):
        self.name = name
        pass

class Area():
    def __init__(self, name, trash):
        self.name = name
        self.trash = trash
        self.trashPickedUp = False
        pass

    # Gives the player this area's item if it hasn't been picked up
    def giveItem(self):
        if self.trashPickedUp == True:
            return "Nothing"
        else:
            self.trashPickedUp = True
            return self.trash
        

# Asks player's name and age + statistics variables
playerName = input("Please insert your name: ")
playerAge = input("Please insert your age: ")
cash = 250
inventory = []

# Checks if player is old enough to play the game
playerAge_int = int(playerAge)
if (playerAge_int <= 12):
    print("You are underage to play this game. Ending program!")
    sys.exit()

# Initializes player, trash and rooms
trash1 = Trash("tin can")
trash2 = Trash("cardboard box")
trash3 = Trash("plastic package")

area1 = Area("the Park", trash1)
area2 = Area("a Shop Entrance", trash2)
area3 = Area("Bridge", trash3)

areas = (area1, area2, area3)

player = Player(playerName, int(playerAge), inventory, cash, area1)

# Prints player statistics
def printStatistics():
    print("------------------")
    print(f"Welcome, {player.name}")
    print(f"Age: {player.age}")
    print(f"Cash: {player.cash}")
    print(f"Location: {player.location.name}")

# Prints player inventory
def printInventory():
    print("------------------")
    print("Your inventory has currently the following items:")
    for item in player.inventory:
        print("- "+item)

# Confirms whether player wants to exit the game or not
def exitProgram():
    print("------------------")
    confirmation = input("Are you sure you want to exit the program? (Yes or No): ")
    if confirmation == "Yes": sys.exit()
    else: askCommands()

# Checks if the current area has an item to pick up, and adds it to the player's inventory
def checkSurrounding():
    currentLocation = player.location
    print("------------------")
    if currentLocation.giveItem() == "Nothing":
        print(f"You're currently in {currentLocation.name}. You looked around you and didn't see any more trash.")
    else:
        print(f"You're currently in {currentLocation.name}. You looked around you and found a {currentLocation.trash.name}! You put it in your backpack.")
        player.inventory.append(currentLocation.trash.name)

# Moves the player to the next location if possible
def move():
    currentLocation = player.location
    locationIndexInAreas = areas.index(currentLocation)
    print("------------------")
    if locationIndexInAreas + 1 < len(areas):
        player.location = areas[locationIndexInAreas + 1]
        print(f"You moved forward to {player.location.name}.")
    else:
        print("Cannot move forward anymore. Your path is blocked by an obstacle.")

# Asks the player for different commands
def askCommands():
    print("------------------")
    command = input("What would you like to do? (Inventory, Surrounding, Statistics, Move or Cancel): ")
    while command != "Cancel":
        if command == "Inventory":
            printInventory()
        elif command == "Surrounding":
            checkSurrounding()
        elif command == "Statistics":
            printStatistics()
        elif command == "Move":
            move()
        else:
            print("Unknown command, try again!")
    
        print("------------------")
        command = input("What would you like to do? (Inventory, Surrounding, Statistics, Move or Cancel): ")

    exitProgram()

# Start program
printStatistics()
askCommands()
