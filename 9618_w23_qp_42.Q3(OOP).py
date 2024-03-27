from datetime import datetime  # Import this function for the dates used in the input


class Character:
    def __init__(self, name, dob, intl, speed):
        self.__cname = name  # Private class of type String
        self.__cdob = dob  # Private class of type Integer
        self.__cintl = intl  # Private class of type Integer
        self.__cspeed = speed  # Private class of type Integer
        self.__ctype = ""  # Private class of type String

    def getintelligence(self):
        return self.__cintl

    def getname(self):
        return self.__cname

    def setintelligence(self, val):
        self.__cintl = val

    def learn(self):
        self.__cintl = self.__cintl * 1.10

    def returnage(self):
        age = 2023 - self.__cdob.year
        return int(age)


class MagicCharacter(Character):
    def __init__(self, element, cname, dob, intl, speed):  # Private class of type String
        super().__init__(cname, dob, intl, speed)
        self.__celement = element

    def learn(self):
        if self.__celement == "fire" or self.__celement == "water":
            super().setintelligence(super().getintelligence() * 1.2)
        elif self.__celement == "earth":
            super().setintelligence(super().getintelligence() * 1.3)
        else:
            super().setintelligence(super().getintelligence() * 1.1)


firstCharacter = Character("Royal", datetime(2019, 1, 1), 70, 30)  # datetime(YYYY, MM, DD) used by importing datetime from datetime function

firstCharacter.learn()
print(
    f"{firstCharacter.getname()} is {firstCharacter.returnage()} years old, and has an intelligence of {firstCharacter.getintelligence()}.")

firstMagic = MagicCharacter("fire", "Light", datetime(2018, 3, 3), 75, 22)  # datetime(YYYY, MM, DD) used by importing datetime from datetime function

firstMagic.learn()
print(
    f"{firstMagic.getname()} is {firstMagic.returnage()} years old, and has an intelligence of {firstMagic.getintelligence()}.")