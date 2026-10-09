import sys
from modules import savesystem
from modules import interactsystem

# Contais all data of the player in the game
class Player():
    def __init__(self, name, age, inventory, location):
        self.name = name
        self.age = age
        self.inventory = inventory
        self.location = location
        pass

# Used to create different types of trash
class Trash():
    def __init__(self, name):
        self.name = name
        pass

# Used to create all areas of the game. The class also contains all neccessary components for an area to work with the game and other objects
class Area():
    def __init__(self, name, trash, interaction="None", interactionText="", exploreText=""):
        self.name = name
        self.trash = trash
        self.exploreText = exploreText
        self.trashPickedUp = False
        self.interaction = interaction
        self.interactionText = interactionText
        self.interactionDone = False

        if self.interactionText == "":
            self.interactionDone = True
        if self.exploreText == "":
            self.trashPickedUp = True

    # Returns this area's item if it hasn't been picked up
    def giveItem(self):
        if self.trashPickedUp == True:
            pass
        else:
            self.trashPickedUp = True
            return self.trash

    # If area has an interaction not done, it begins it and returns a trash if possible
    def beginInteraction(self):
        if self.interactionDone == True:
            pass
        else:
            self.interactionDone = True
            return self.interaction.startInteraction()

# Start Menu
print("|| Trash Collector's Day ||")

# Prints start menu and every possible command
def printMainMenu():
    print("------------------")
    print("New game: N")
    print("Load game: L")
    print("Quide: Q")
    print("Quit: E")

# Asks the player for start menu commands, until game is started with a new or existing player
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
            print("------------------")
            try:
                with open("peliprojekti/quide.txt", "r") as file:
                    print(file.read())
            except FileNotFoundError:
                print("Cannot print a quide, because quide.txt cannot be accessed, has been modified or doesn't exists!")
        elif command == "E":
            sys.exit()
        else:
            print("Unknown command, try again!")
        printMainMenu()
        command = input("How do you want to proceed: ")

printMainMenu()
newPlayer = askMenuCommands()

# Initializes areas 1-4 and their trash & interactions
trash1 = Trash("tin can")
area1 = Area("the Park", trash1, exploreText="Look around the park")

trash2 = Trash("cardboard box")
trash3 = Trash("rusty nails")
interaction1Choice1 = interactsystem.Choice("Ask the old lady about the bag", True, trash3,
                                            "You asked the lady in front of you what they had in the bag. She told you there were a bunch of rusty nails.\nShe was looking for a way to get rid of them. You offered to take them and she gave them to you. You exit the shop.")
interaction1Choice2 = interactsystem.Choice("Don't ask the old lady about the bag", False,
                                            answerText="You didn't want to bother the old lady as it would have seemed really weird to ask for something like that.\nYou decidex to exit the shop.")
interaction1 = interactsystem.Interaction([interaction1Choice1, interaction1Choice2], 
                                          "You enter the shop, there wasn't so many people in currently. You spotted an old lady on the nearby section.\nShe has a small trashbag with her. You're interested in what is inside of it. What will you do?")
area2 = Area("a Shop Entrance", trash2, interaction1, "Enter the shop", "Check behind the shop")

trash4 = Trash("plastic package")
trash5 = Trash("Empty catfood box")
interaction2Choice1 = interactsystem.Choice("Get closer to the cat and try to pet it", False, 
                                            answerText="You walked closer to the cat and as you reached out with your hand to pet it, however it got scared of you.\nThe cat grapped the bag with them and ran away.")
interaction2Choice2 = interactsystem.Choice("Resist the urge to pet the cat", True, trash5,
                                            "After a while, the cat continued to eat the rest of the food from the pack. After it was done, they ran away.\nYou decided to pick up the empty pack left by the cat.")
interaction2 = interactsystem.Interaction([interaction2Choice1, interaction2Choice2], 
                                          "You walk closer to the cat. It seems to be eating from a box of catfood left by someone.\nThe cat notices you, stops eating and leans back a little. What will you do?")
area3 = Area("Bridge", trash4, interaction2, "Approach a nearby cat", "Look around the bridge")

trash6 = Trash("small hammer")
trash7 = Trash("cloth")
interaction3Choice1 = interactsystem.Choice("Choose the left bin", True, trash7,
                                            "You approached the left bin. However two other people with bags of trash appeared and chose the two bins left by you.\nYou opened the bin and found a cloth. You checked around you to see what the other two got, but could only see their reactions:\n The middle person looked disappointed and the right person looked rather happy.")
interaction3Choice2 = interactsystem.Choice("Choose the middle bin", False,
                                            answerText="You approached the middle bin. However two other people with bags of trash appeared and chose the two bins left by you.\nYou opened the bin and found it empty. You checked around you to see what the other two got, but could only see their reactions:\n The left person looked satisfied and the right person looked rather happy.")
interaction3Choice3 = interactsystem.Choice("Choose the right bin", True, trash6,
                                            "You approached the right bin. However two other people with bags of trash appeared and chose the two bins left by you.\nYou opened the bin and found a small hammer. You checked around you to see what the other two got, but could only see their reactions:\n The left person looked satisfied and the middle person looked disappointed.")
interaction3 = interactsystem.Interaction([interaction3Choice1, interaction3Choice2, interaction3Choice3],
                                          "You spot three trash bins in the area. What bin will you investigate first?")
area4 = Area("Apartment Building", "", interaction3, "Check the trash area")

# Player variables
playerName = ""
playerAge = 0
inventory = []

# Starts a new player and goes through an age check before allowing play
# If a player is loading an existing player, goes through its data and prepares the player to continue
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
    try:
        with open("peliprojekti/intro.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("Cannot print a quide, because intro.txt cannot be accessed, has been modified or doesn't exists!")
    
else:
    data = savesystem.loadPlayer()
    playerName = data["name"]
    playerAge = data["age"]
    inventory = data["inventory"]
    location = data["location"]
    area1.trashPickedUp = data["area1Explore"]
    area2.trashPickedUp = data["area2Explore"]
    area3.trashPickedUp = data["area3Explore"]
    area2.interactionDone = data["area2Interact"]
    area3.interactionDone = data["area3Interact"]
    area4.interactionDone = data["area4Interact"]

# Initializes player and the fifth area, trash and interaction
player = Player(playerName, int(playerAge), inventory, area1)

trash8 = Trash("bag of torn clothes")
trash9 = Trash("batteries")
interaction4Choice = interactsystem.Choice("Open the box", True, trash8,
                                           "You used the hammer to open the wooden box. Inside was a medium sized trashbag, you opened it and it was full of torn apart clothes.\nYou picked up the bag and left the box open.")
interaction4 = interactsystem.AlleyInteraction(player, [interaction4Choice],
                                               "You walked closer to the wooden box, its closed with a bunch on nails. Thankfully you have a small hammer to open it with.")
area5 = Area("Alley", trash9, interaction4, "Check out a wooden box", "Look at the nearby bins")

areas = (area1, area2, area3, area4, area5)

# Prepares rest of the variables for a continuing player
if (newPlayer==False):
    for area in areas:
        if area.name == location:
            player.location = area
    area5.interactionDone = data["area5Interact"]
    area5.trashPickedUp = data["area5Explore"]

# Prints player statistics
def printStatistics():
    print("------------------")
    print(f"Welcome, {player.name}")
    print(f"Age: {player.age}")
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
    confirmation = input("Do you want to save your current progress? (Yes or No): ")
    if confirmation == "Yes": 
        savesystem.savePlayer(player.name, player.age, player.inventory, player.location.name,
                             area1.trashPickedUp, area2.trashPickedUp, area3.trashPickedUp, area5.trashPickedUp,
                             area2.interactionDone, area3.interactionDone, area4.interactionDone, area5.interactionDone)
    else: pass
    sys.exit()

# Checks if the current area can be either Explored or has something to Interact with
# If either one is possible, asks the player if they want to continue with the option(s)
def checkSurrounding():
    currentLocation = player.location
    choices = []

    print("------------------")
    if currentLocation.interactionDone == False or currentLocation.trashPickedUp == False:

        print(f"You're currently in {currentLocation.name}. You looked around and have the following things to do:") 

        if currentLocation.interactionDone == False:
            choices.append("Interact")
            print(f"- {currentLocation.interactionText} [i]")         
        if currentLocation.trashPickedUp == False:
            choices.append("Explore")
            print(f"- {currentLocation.exploreText} [e]")
        print("- Do nothing [any]")

        choice = input("What will you choose (number of option): ")

        if choice == "i" and currentLocation.interactionDone == False:
            trash = currentLocation.beginInteraction()
            if trash != "":
                player.inventory.append(trash.name)
                print(f"You got {trash.name}")
        elif choice == "e" and currentLocation.trashPickedUp == False:
            print("------------------")
            print(f"You decide to look around the area for a bit and found a {currentLocation.trash.name}! You put it in your backpack.")
            trash = currentLocation.giveItem()
            player.inventory.append(trash.name)
        else:
            pass
    else:
        print(f"You're currently in {currentLocation.name}. You looked around, but everything is already done here.")

# Moves the player to the next location or ends the game if currently on the fifth area
def move():
    currentLocation = player.location
    locationIndexInAreas = areas.index(currentLocation)
    print("------------------")
    if locationIndexInAreas + 1 < len(areas):
        player.location = areas[locationIndexInAreas + 1]
        print(f"You moved forward to {player.location.name}.")
    else:
        endGame()

# Asks the player for different commands during the game
def askCommands():
    print("------------------")
    command = input("What would you like to do? (inventory, surrounding, statistics, move or exit): ")
    while command != "exit" :
        if command == "inventory":
            printInventory()
        elif command == "surrounding":
            checkSurrounding()
        elif command == "statistics":
            printStatistics()
        elif command == "move":
            move()
        else:
            print("Unknown command, try again!")
    
        print("------------------")
        command = input("What would you like to do? (inventory, surrounding, statistics, move or exit): ")

    exitProgram()

# Once last area is moved on from, end game with one of the possible endings
def endGame():
    trashPickedUp = len(player.inventory)
    specialTrash = False
    for trash in player.inventory:
        if trash == "bag of torn clothes":
            specialTrash = True

    ending = ""
    if trashPickedUp == 0:
        ending = "ending1"
    else:
        if trashPickedUp < 5:
            if specialTrash == False:
                ending = "ending2"
            else:
                ending = "ending3"
        else:
            if specialTrash == False:
                ending = "ending4"
            else:
                ending = "ending5"

    try:
        with open(f"peliprojekti/endings/{ending}.txt", "r") as file:
            data = file.read()
            print(data)
    except FileNotFoundError:
        print("Cannot print an ending, because ending(numOfEnding).txt cannot be accessed, has been modified or doesn't exists!")

    sys.exit()

# Start program
printStatistics()
askCommands()