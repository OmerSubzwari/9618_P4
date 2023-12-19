Animals = []  # 10 elements Array

Animals.append("horse")
Animals.append("lion")
Animals.append("rabbit")
Animals.append("mouse")
Animals.append("bird")
Animals.append("deer")
Animals.append("whale")
Animals.append("elephant")
Animals.append("kangaroo")
Animals.append("tiger")


def SortDescending():
    # arraylength : INTEGER
    # temp : STRING
    arraylength = len(Animals)
    for x in range(0, arraylength - 1):
        for y in range(0, arraylength - x - 1):
            if Animals[y][0] < Animals[y + 1][0]:
                temp = Animals[y]
                Animals[y] = Animals[y + 1]
                Animals[y + 1] = temp

SortDescending()
for i in range(0, 9):
    print(Animals[i])