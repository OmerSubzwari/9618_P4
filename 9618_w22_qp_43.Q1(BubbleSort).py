dataArray = []  # 100 elements array


def readfile():
    global dataArray
    try:
        with open("IntegerData.txt", 'r') as f:
            for i in range(0, 100):
                line = f.readline().rstrip('\n')
                if not line:
                    break  # Exit the loop if no more lines are left in the file
                dataArray.append(int(line))

    except IOError:
        print("File not found.")


def findvalues():
    global dataArray
    count = 0
    user = int(input("Enter a value between 1 and 100: "))
    while user < 1 or user > 100:
        user = int(input("Number must be between 1 and 100: "))
    for value in dataArray:
        if value == user:
            count += 1
    return count


def bubblesort():
    global dataArray
    n = len(dataArray) - 1
    for i in range(n):
        for j in range(0, n - i):
            if dataArray[j] > dataArray[j + 1]:
                dataArray[j], dataArray[j + 1] = dataArray[j + 1], dataArray[j]


readfile()
found = findvalues()
if found != 0:
    print(f"Your value was found {found} times.")
else:
    print("Your value was not found.")
bubblesort()
print(dataArray)
