class Card:
    def __init__(self, num, col):
        self.__number = num  # Private number : Integer
        self.__colour = col  # Private colour : String

    def getnumber(self):
        return self.__number

    def getcolour(self):
        return self.__colour


class Hand:
    def __init__(self, c1, c2, c3, c4, c5):
        self.__cards = []  # Private Cards[10] : Card
        self.__cards.append(c1)
        self.__cards.append(c2)
        self.__cards.append(c3)
        self.__cards.append(c4)
        self.__cards.append(c5)
        self.__firstcard = 0  # Private firstcard : Integer
        self.__numbercards = 5  # Private numbercards : Integer

    def getcards(self, i):
        return self.__cards[i]


def calculatevalue(player):
    score = 0
    for i in range(0, 4):
        card = player.getcards(i)
        score += card.getnumber()
        colour = card.getcolour()
        if colour == "red":
            score += 5
        elif colour == "blue":
            score += 10
        else:
            score += 15
    return score


red1 = Card(1, "red")
red2 = Card(2, "red")
red3 = Card(3, "red")
red4 = Card(4, "red")
red5 = Card(5, "red")

blue1 = Card(1, "blue")
blue2 = Card(2, "blue")
blue3 = Card(3, "blue")
blue4 = Card(4, "blue")
blue5 = Card(5, "blue")

yellow1 = Card(1, "yellow")
yellow2 = Card(2, "yellow")
yellow3 = Card(3, "yellow")
yellow4 = Card(4, "yellow")
yellow5 = Card(5, "yellow")

player1 = Hand(red1, red2, red3, red4, yellow1)
player2 = Hand(yellow2, yellow3, yellow4, yellow5, blue1)

p1 = calculatevalue(player1)
p2 = calculatevalue(player2)

if p1 > p2:
    print("Player 1 wins!")
elif p1 < p2:
    print("Player 2 wins!")
else:
    print("Draw.")