global animals
animals = []  # Array animals to store 10 elements

animals.append("horse")
animals.append("lion")
animals.append("rabbit")
animals.append("mouse")
animals.append("bird")
animals.append("deer")
animals.append("whale")
animals.append("elephant")
animals.append("kangaroo")
animals.append("tiger")


def sortdescending():
    arraylength = len(animals)
    for i in range(arraylength - 1):
        for y in range(arraylength - i - 1):
            if animals[y][0] < animals[y + 1][0]:
                temp = animals[y]
                animals[y] = animals[y + 1]
                animals[y + 1] = temp



sortdescending()
for i in range(0, 10):
    print(animals[i])