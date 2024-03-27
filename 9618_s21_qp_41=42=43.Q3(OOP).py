class TreasureChest:
    def __init__(self, p, a, q):
        self.__question = p  # Private question : String
        self.__answer = a  # Private answer : Integer
        self.__points = q  # Private points : Integer

    def getquestion(self):
        return self.__question

    def checkanswer(self, user):
        if int(self.__answer) == user:
            return True
        else:
            return False

    def getpoints(self, attempts):
        if attempts == 1:
            return int(self.__points)
        elif attempts == 2:
            return int(self.__points) // 2
        elif attempts == 3 or attempts == 4:
            return int(self.__points) // 4
        else:
            return 0


# arrayTreasure(5) as treasurechest
arrayTreasure = []


def readdata():
    try:
        f = open("TreasureChestData.txt", "r")
        data = (f.readline()).strip()
        while data != "":
            question = data
            answer = (f.readline()).strip()
            points = (f.readline()).strip()
            arrayTreasure.append(TreasureChest(question, answer, points))
            data = (f.readline()).strip()
    except IOerror:
        print("File was not found.")


readdata()
choice = int(input("Pick which treasure chest you want to open: "))
if 0 < choice < 6:
    result = False
    attempts = 0
    while not result:
        answer = int(input(f"{arrayTreasure[choice - 1].getquestion()}: "))
        result = arrayTreasure[choice - 1].checkanswer(answer)
        attempts += 1
    print(int(arrayTreasure[choice - 1].getpoints(attempts)))
