class balloon:

    def __init__(self, d, c):
        self.__defenceitem = d  # String
        self.__colour = c  # String
        self.__health = 100  # Integer

    def getdefenceitem(self):
        return self.__defenceitem

    def changehealth(self, change):
        self.__health = self.__health + change

    def checkhealth(self):
        if self.__health <= 0:
            return True
        else:
            return False


def defend(userballoon):
    strength = int(input("Enter your opponent's strength: "))
    userballoon.changehealth(-strength)
    print(f"You defended with {str(userballoon.getdefenceitem())}")
    if userballoon.checkhealth() == True:
        print("Defence failed, balloon died.")
    else:
        print("Defence successful, balloon alive.")
    return userballoon

ditem = input("Please enter your defence item: ")
bcolour = input("Please enter your balloon colour: ")
Balloon1 = balloon(ditem, bcolour)
defend(Balloon1)

