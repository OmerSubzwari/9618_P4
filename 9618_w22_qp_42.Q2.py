class Character:
    def __init__(self, n, xcoord, ycoord):
        self.__name = n  # String
        self.__xcoordinate = xcoord  # Integer
        self.__ycoordinate = ycoord  # Integer

    def getname(self):
        return self.__name

    def getx(self):
        return self.__xcoordinate

    def gety(self):
        return self.__ycoordinate

    def changeposition(self, xchange, ychange):
        self.__xcoordinate += xchange
        self.__ycoordinate += ychange


characters = []
try:
    with open("Characters.txt", 'r') as f:
        for i in range(0, 10):
            name = f.readline().strip()
            xcoord = int(f.readline().strip())
            ycoord = int(f.readline().strip())
            tempVal = Character(name, xcoord, ycoord)
            characters.append(tempVal)
except FileNotFoundError:
    print("File was not found.")

while True:
    user = input("Enter the character that you want to move (or type 'quit' to exit): ").strip().lower()

    if user == 'quit':
        break  # Exit the loop if the user wants to quit

    # Find the character position (case-insensitive)
    pos = -1
    for i in range(0, 10):
        temp = str(characters[i].getname().strip()).lower()
        if temp == user:
            pos = i
            break  # Exit the loop after finding the position

    if pos == -1:
        print(f"Character '{user}' not found. Please try again.")
        continue  # Ask for the character again if not found

    IsValid = False
    while not IsValid:
        Move = input("Enter A for left, W for up, S for down, or D for right: ").upper()
        if Move == "A":
            characters[pos].changeposition(-1, 0)
            IsValid = True
        elif Move == "W":
            characters[pos].changeposition(0, 1)
            IsValid = True
        elif Move == "S":
            characters[pos].changeposition(0, -1)
            IsValid = True
        elif Move == "D":
            characters[pos].changeposition(1, 0)
            IsValid = True

    print(user, " has changed coordinate to X =", str(characters[pos].getx()), " Y =", str(characters[pos].gety()))
