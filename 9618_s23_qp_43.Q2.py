class Vehicle:
    def __init__(self, i, s, a):
        self.__id = i  # self.__id : String
        self.__maxspeed = s  # self.__maxspeed = Integer
        self.__increaseamount = a  # self.__increaseamount = Integer
        self.__currentspeed = 0  # self.__currentspeed = Integer
        self.__horizontalposition = 0  # self.__horizontalposition = Integer

    def getcurrentspeed(self):
        return self.__currentspeed

    def getincreaseamount(self):
        return self.__increaseamount

    def getmaxspeed(self):
        return self.__maxspeed

    def gethorizontalposition(self):
        return self.__horizontalposition

    def setcurrentspeed(self, speed):
        self.__currentspeed = speed

    def sethorizontalposition(self, position):
        self.__horizontalposition = position

    def increasespeed(self):
        self.__currentspeed = self.__currentspeed + self.__increaseamount
        if self.__currentspeed > self.__maxspeed:
            self.__currentspeed = self.__maxspeed
        self.__horizontalposition = self.__horizontalposition + self.__currentspeed

    def outputpos(self):
        print(f"The current position is: {self.__horizontalposition}.")
        print(f"The current speed is: {self.__currentspeed}.")


class Helicopter(Vehicle):

    def __init__(self, i, s, a, v, h):
        super().__init__(i, s, a)
        self.__verticalposition = 0  # self.__verticalposition = Integer
        self.__verticalheight = v  # self.__verticalheight = Integer
        self.__maxheight = h  # self.__maxheight = Integer

    def increasespeed(self):
        self.__verticalposition = self.__verticalposition + self.__verticalheight
        if self.__verticalposition > self.__maxheight:
            self.__verticalposition = self.__maxheight
        Vehicle.setcurrentspeed(self, Vehicle.getcurrentspeed(self) + Vehicle.getincreaseamount(self))
        if Vehicle.getcurrentspeed(self) > Vehicle.getmaxspeed(self):
            Vehicle.setcurrentspeed(self, Vehicle.getmaxspeed(self))
        Vehicle.sethorizontalposition(self, Vehicle.gethorizontalposition(self) + Vehicle.getcurrentspeed(self))

    def outputpos(self):
        print(f"The current position is: {Vehicle.gethorizontalposition(self)}.")
        print(f"The current speed is: {Vehicle.getcurrentspeed(self)}.")
        print(f"The current vertical position is: {self.__verticalposition}.")


car = Vehicle("Tiger", 100, 20)
helicopter = Helicopter("Lion", 350, 40, 3, 100)

for j in range(2):
    car.increasespeed()

car.outputpos()

print("------")

for k in range(2):
    helicopter.increasespeed()

helicopter.outputpos()
