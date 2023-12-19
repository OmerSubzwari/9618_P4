data = [[""] * 2 for i in range(11)]  # String


def readhighscores():
    f = open("HighScore.txt", 'r')
    for i in range(0, 10):
        data[i][0] = f.readline()[:3]
        data[i][1] = f.readline()
    f.close()


def outputhighscores():
    for j in range(0, 11):
        if data[j][0] != "":
            result = str(data[j][0]) + " " + str(data[j][1])
            print(result)


def topten(name, score):
    for i in range(0, 10):
        if score > int(data[i][1]):
            temp1 = data[i][0]
            temp2 = data[i][1]
            data[i][0] = name
            data[i][1] = score
            k = i + 1
            while k < 10:
                temp3 = data[k][0]
                temp4 = data[k][1]
                data[k][0] = temp1
                data[k][1] = temp2

                temp1 = temp3
                temp2 = temp4
                k += 1

            break

def writetopten():
    filename = "NewHighScore.txt"
    filename = open(filename, 'w')
    for i in range(0, 10):
        filename.write(str(data[i][0]) + '\n')
        filename.write(str(data[i][1]) + '\n')
    filename.close()

readhighscores()
outputhighscores()

print("\n")

name = "xxxx"
while len(name) != 3:
    name = input("Enter your name: ")

score = 0
while True:
    score = int(input("Enter your high score: "))
    if 0 <= score <= 100000:
        break
    else:
        print("Invalid score. Please enter a score between 0 and 99999.")

topten(name, score)
outputhighscores()

writetopten()
