import sys

# Asks player's name and age + statistics variables
playerName = input("Please insert your name: ")
playerAge = input("Please insert your age: ")
cash = 250
inventory = ["Small rope", "Survivor kit", "5 Days of rations"]
inventoryMaxSize = 5

# Checks if player is old enough to play the game
playerAge_int = int(playerAge)
if (playerAge_int <= 12):
    print("You are underage to play this game. Ending program!")
    sys.exit()

# Prints player statistics
def printStatistics():
    print("------------------")
    print("Welcome, " + playerName)
    print("Age: (" + playerAge + ")")
    print("Cash: (" + str(cash) + ")")
    # print("Inventory space: "+str(len(inventory))+"/"+str(inventoryMaxSize))

# Prints player inventory
def printInventory():
    print("------------------")
    print("Your inventory has currently the following items:")
    for item in inventory:
        print("- "+item)

# Adds an item to player's inventory
def addItemToInventory():
    item = input("What item do you want to add to your inventory: ")
    print("Item added to inventory!")
    return item

# Confirms whether player wants to exit the game or not
def exitProgram():
    print("------------------")
    confirmation = input("Are you sure you want to exit the program? (Yes or No): ")
    if confirmation == "Yes": sys.exit()
    else: askCommands()

# Asks the player for different commands
def askCommands():
    print("------------------")
    command = input("What would you like to do? (Inventory, Check cash, Surrounding, Add Item, Statistics or Cancel): ")
    while command != "Cancel":
        if command == "Inventory":
            printInventory()
        elif command == "Check cash":
            print("You have 40 silver coins and 10 gold coins, totaling 250 cash")
        elif command == "Surrounding":
            print("You are in a spruce forest near your campsite, currently sitting next to a campfire with food warming up.")
        elif command == "Add item":
            inventory.append(addItemToInventory())
        elif command == "Statistics":
            printStatistics()
        else:
            print("Unknown command, try again!")
        
        print("------------------")
        command = input("What would you like to do? (Inventory, Check cash, Surrounding, Add Item, Statistics or Cancel): ")

    exitProgram()

# Start program
printStatistics()
askCommands()
