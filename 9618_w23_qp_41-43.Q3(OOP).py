class Character:

    def __init__(self, name, xpos, ypos):
        self.__name = name  # Private class name As String
        self.__xpos = xpos  # Private class xpos As Integer
        self.__ypos = ypos  # Private class ypos as Integer

    def getxposition(self):
        return self.__xpos

    def getyposition(self):
        return self.__ypos

    def setxposition(self, addval):
        self.__xpos = self.__xpos + addval
        if self.__xpos > 10000:
            self.__xpos = 10000
        elif self.__xpos < 0:
            self.__xpos = 0

    def setyposition(self, addval):
        self.__ypos = self.__ypos + addval
        if self.__ypos > 10000:
            self.__ypos = 10000
        elif self.__ypos < 0:
            self.__ypos = 0

    def move(self, change):
        if change == "up":
            self.setyposition(+10)
        elif change == "down":
            self.setyposition(-10)
        if change == "left":
            self.setxposition(-10)
        elif change == "right":
            self.setxposition(+10)


class bikecharacter(Character):
    def __init__(self, name, xpos, ypos):
        super().__init__(name, xpos, ypos)

    def move(self, change):
        if change == "up":
            super().setyposition(+20)
        elif change == "down":
            super().setyposition(-20)
        if change == "left":
            super().setxposition(-20)
        elif change == "right":
            super().setxposition(+20)


myChar = Character("Jack", 50, 50)
myBike = bikecharacter("Karla", 100, 50)

cmove = input("Do you want to move Jack or Karla: ").lower()
while cmove != "jack" and cmove != "karla":
    cmove = input("Invalid, enter a correct name: ").lower()

disp = input("Choose a direction from up, down, left or right: ").lower()
while disp != "up" and disp != "down" and disp != "left" and disp != "right":
    disp = input("Invalid direction, enter again: ").lower()

if cmove == "jack":
    myChar.move(disp)
    print(f"Jack's new position is X = {myChar.getxposition()}, Y = {myChar.getyposition()}")
else:
    myBike.move(disp)
    print(f"Karla's new position is X = {myBike.getxposition()}, Y = {myBike.getyposition()}")
