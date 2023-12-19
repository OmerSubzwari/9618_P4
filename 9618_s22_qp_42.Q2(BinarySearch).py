import random


def printarray(arr):
    for i in range(0, 10):
        for j in range(0, 10):
            print(arr[i][j], " ", end='')
        print("")


def binarysearch(searcharray, lower, upper, searchvalue):
    if upper >= lower:
        mid = (lower + upper) // 2
        if searcharray[0][mid] == searchvalue:
            return mid
        elif searcharray[0][mid] > searchvalue:
            return binarysearch(searcharray, lower, mid - 1, searchvalue)
        else:
            return binarysearch(searcharray, mid + 1, upper, searchvalue)
    return -1


arraydata = [[0] * 10 for i in range(10)]  # Integer
for j in range(0, 10):
    for k in range(0, 10):
        arraydata[j][k] = random.randint(1, 100)

print("Before sorting: ")
printarray(arraydata)

arraylength = 10
for x in range(0, arraylength):
    for y in range(0, arraylength - 1):
        for z in range(0, arraylength - y - 1):
            if arraydata[x][z] > arraydata[x][z + 1]:
                tempvalue = arraydata[x][z]
                arraydata[x][z] = arraydata[x][z + 1]
                arraydata[x][z + 1] = tempvalue

print("After sorting: ")
printarray(arraydata)


def test_and_print(search_value):
    result = binarysearch(arraydata, 0, 9, search_value)
    status = f"Found {search_value} at index {result}." if result != -1 else f"{search_value} not found."
    print(status)


# Test for a number that is in the first line of the array
test_and_print(arraydata[0][random.randint(0, 9)])

# Test for a number that is not in the first line of the array
test_and_print(random.randint(0, 100))

val = int(input())
print(binarysearch(arraydata, 0, 10, val))

val = int(input())
print(binarysearch(arraydata, 0, 10, val))
