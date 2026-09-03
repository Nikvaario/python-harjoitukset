import sys

# Asks player's name and age
playerName = input("Please insert your name: ")
playerAge = input("Please insert your age: ")
cash = 250

# Checks if player is old enough to play the game
playerAge_int = int(playerAge)
if (playerAge_int <= 12):
    print("You are underage to play this game. Ending program!")
    sys.exit()

# Prints a welcome text and player stats
print("------------------")
print("Welcome, " + playerName)
print("Age: (" + playerAge + ")")
print("Cash: (" + str(cash) + ")")
print("Your inventory is half full")
print("------------------")

# Asks the player for different commands
command = input("What would you like to do? (Inventory, Check cash, Surrounding or Cancel): ")
print("------------------")
while command != "cancel":
    if command == "Inventory":
        print("You have a small rope, 5 days of rations and a survivor kit in your backbag!")
    elif command == "Check cash":
        print("You have 40 silver coins and 10 gold coins, totaling 250 cash")
    elif command == "Surrounding":
        print("You are in a spruce forest near your campsite, currently sitting next to a campfire with food warming up.")
    else:
        print("Unknown command, try again!")
    command = input("What would you like to do? (Inventory, Check cash, Surrounding or Cancel): ")
    print("------------------")

