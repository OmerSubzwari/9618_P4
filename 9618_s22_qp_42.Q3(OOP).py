global NumbersChosen


class Card:
    def __init__(self, n, c):
        self.__number = n  # Private number : Integer
        self.__colour = c  # Private colour : String

    def getnumber(self):
        return self.__number

    def getcolour(self):
        return self.__colour


def ChooseCard():
    global NumbersChosen
    flagContinue = True
    while flagContinue == True:
        CardSelected = int(input("Select a Card from 1 to 30: "))
        if CardSelected < 1 or CardSelected > 30:
            print("Number must be between 1 and 30.")
        elif NumbersChosen[CardSelected - 1] == True:
            print("Already taken.")
        else:
            print("Valid.")
            flagContinue = False
    NumbersChosen[CardSelected - 1] = True
    return CardSelected - 1


arrayCard = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # Integer
try:
    f = open("CardValues.txt", 'r')
    for i in range(0, 30):
        num = int(f.readline())
        col = f.readline()
        arrayCard[i] = Card(num, col)
    f.close()
except IOError:
    print("File not found.")

NumbersChosen = [False for i in range(30)]

Player1 = []  # of type Card
for x in range(0, 4):
    ReturnNumber = ChooseCard()
    Player1.append(arrayCard[ReturnNumber])
for x in range(0, 4):
    print(Player1[x].getnumber())
    print(Player1[x].getcolour())
