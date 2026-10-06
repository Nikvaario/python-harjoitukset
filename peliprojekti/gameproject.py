import sys
from modules import savesystem

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

# Menu
print("|| Trash Collector's Day ||")

def printMainMenu():
    print("------------------")
    print("New game: N")
    print("Load game: L")
    print("Quide: Q")
    print("Quit: E")

def askMenuCommands():
    command = input("How do you want to proceed: ")
    startingGame = False
    while startingGame == False:
        if command == "N":
            startingGame == True
            return True
        elif command == "L":
            startingGame == True
            return False
        elif command == "Q":
            with open("quide.txt", "r") as file:
                print(file.read())
        elif command == "E":
            sys.exit()
        else:
            print("Unknown command, try again!")
        printMainMenu()
        command = input("How do you want to proceed: ")

printMainMenu()
newPlayer = askMenuCommands()

# Initializes trash and rooms
trash1 = Trash("tin can")
trash2 = Trash("cardboard box")
trash3 = Trash("plastic package")

area1 = Area("the Park", trash1)
area2 = Area("a Shop Entrance", trash2)
area3 = Area("Bridge", trash3)

areas = (area1, area2, area3)

# Player variables
playerName = ""
playerAge = 0
cash = 250
inventory = []
playerLocation = area1

# Starts a new player and goes through any checks before allowing play
if (newPlayer == True):
    playerName = input("Please insert your name: ")
    while True:
        try:
            playerAge = int(input("Please insert your age: "))
            break
        except ValueError:
            print("Please input a number value!")

    if (playerAge <= 12):
        print("You are underage to play this game. Ending program!")
        sys.exit()

    print("------------------")
    with open("intro.txt", "r") as file:
        print(file.read())
    
else:
    data = savesystem.loadPlayer()
    playerName = data["name"]
    playerAge = data["age"]
    cash = data["cash"]
    inventory = data["inventory"]
    location = data["location"]
    area1.trashPickedUp = data["area1trash"]
    area2.trashPickedUp = data["area2trash"]
    area3.trashPickedUp = data["area3trash"]

    for area in areas:
        if area.name == location:
            playerLocation = area

player = Player(playerName, int(playerAge), inventory, cash, playerLocation)

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

# Confirms whether player wants to save their progress and exits the program
def exitProgram():
    print("------------------")
    confirmation = input("Do you want to save your progress? This will overwrite any existing save data. (Yes or No): ")
    if confirmation == "Yes": 
        savesystem.savePlayer(player.name, player.age, player.cash, player.inventory, player.location.name,
                              area1.trashPickedUp, area2.trashPickedUp, area3.trashPickedUp)
    else: pass
    sys.exit()

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
    command = input("What would you like to do? (Inventory, Surrounding, Statistics, Move or Exit): ")
    while command != "Exit":
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
        command = input("What would you like to do? (Inventory, Surrounding, Statistics, Move or Exit): ")

    exitProgram()

# Start program
printStatistics()
askCommands()
