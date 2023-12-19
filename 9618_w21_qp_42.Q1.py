def unknown(x, y):
    if x < y:
        print(str(x + y))
        return unknown(x + 1, y) * 2
    elif x == y:
        return 1
    else:
        print(str(x + y))
        return int(unknown(x - 1, y) / 2)


def iterativeunknown(x, y):
    total = 1
    while x != y:
        print(str(x + y))
        if x < y:
            x += 1
            total = total * 2
        else:
            x -= 1
            total = int(total / 2)
    return total


print("10, 15")
print(str(unknown(10, 15)))
print("10, 10")
print(str(unknown(10, 10)))
print("15, 10")
print(str(unknown(15, 10)))

print("Iterative: ")

print("10, 15")
print(str(iterativeunknown(10, 15)))
print("10, 10")
print(str(iterativeunknown(10, 10)))
print("15, 10")
print(str(iterativeunknown(15, 10)))
