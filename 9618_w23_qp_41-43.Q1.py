def IterativeVowels(value):
    total = 0
    lengthstring = len(value)
    for x in range(0, lengthstring):
        firstcharacter = value[0]
        if firstcharacter == 'a' or firstcharacter == 'e' or firstcharacter == 'i' or firstcharacter == 'o' or firstcharacter == 'u':
            total += 1

        value = value[1:lengthstring]

    return total


def RecursiveVowels(value):
    if len(value) != 0:
        firstcharacter = value[0]
        if firstcharacter == 'a' or firstcharacter == 'e' or firstcharacter == 'i' or firstcharacter == 'o' or firstcharacter == 'u':
            return 1 + RecursiveVowels(value[1:len(value)])
        else:
            return RecursiveVowels(value[1:len(value)])
    else:
        return 0


val = IterativeVowels("house")
print(val)

print(" ")

val2 = RecursiveVowels("imagine")
print(val2)
