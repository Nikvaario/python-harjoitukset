# Used to create a single interaction choice
class Choice():
    def __init__(self, optionText=str, correct=bool, trash="", answerText=str):
        self.interaction = {"OptionText": optionText,
                            "Correct": correct,
                            "AnswerText": answerText,
                            "Trash": trash}
        self.correct = correct

# Used to create an interaction, that uses given Choice objects to form a question with choices for the player
class Interaction():
    def __init__(self, interactions=[], text=str):
        self.text = text
        self.interactions = interactions

    # Goes through the whole interaction
    def startInteraction(self):
        print("------------------")
        print(self.text)
        optionNum = 1
        for interaction in self.interactions:
            print(f"- {interaction.interaction["OptionText"]} [{optionNum}]")
            optionNum += 1

        value = int(input("What will you choose (number of option): "))
        option = self.interactions[value - 1].interaction
        print("------------------")
        print(option["AnswerText"])
        if option["Correct"] == True:
            return option["Trash"]
        else: 
            return ""

class AlleyInteraction(Interaction):
    def __init__(self, player, interactions=[], text=str):
        super().__init__(interactions, text)
        self.player = player

    # Goes through the whole interaction, if player has a small hammer
    def startInteraction(self):
        hammerFound = False
        for item in self.player.inventory:
            if item == "small hammer": hammerFound = True

        if hammerFound == True:
            super().startInteraction()
            return self.interactions[0].interaction["Trash"]
        else:
            print("------------------")
            print("You walked closer to the wooden box, its closed with a bunch on nails. You have no possible way to open it sadly, if only you had found something to open it with.")
            return ""
        

# --- EXAMPLE CODE ---

# CREATES CHOICES
#testChoice_1 = Choice("This one is true", True, "You answered the correct option!")
#testChoice_2 = Choice("This one is false", False, "You answered the wrong option!")

# CREATES AN INTERACTION
#testInteraction = Interaction("Mold", "Test_obj", "This is a test interactable object", [testChoice_1, testChoice_2])

# STARTS INTERACTION AND RETURNS TRASH IF POSSIBLE
#trash = testInteractable.startInteraction()

# PRINTS WHAT USER GOT FROM THE INTERACTION
#if trash != "": print(f"You got {trash}")
#else: print("You got nothing")


