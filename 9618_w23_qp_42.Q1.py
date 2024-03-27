def push_data(alpha):
    global vowel_top, consonant_top

    if alpha == "a" or alpha == "e" or alpha == "i" or alpha == "o" or alpha == "u":

        if stack_vowel == 100:
            print("Stack is full")
        else:
            stack_vowel.append(alpha)
            vowel_top += 1
    else:

        if stack_consonant == 100:
            print("Stack is full")
        else:
            stack_consonant.append(alpha)
            consonant_top += 1


def read_data():
    try:
        with open("StackData.txt", 'r') as data:
            for line in data:
                push_data(line.strip())

    except FileNotFoundError:
        print("File not found")


def pop_vowel():
    global vowel_top

    if vowel_top == 0:
        return "No Data"
    else:
        stack_vowel.pop()
        vowel_top -= 1
        return stack_vowel[-1]


def pop_consonant():
    global consonant_top

    if consonant_top == 0:
        return "No Data"
    else:
        stack_consonant.pop()
        consonant_top -= 1
        return stack_consonant[-1]


stack_vowel = []  # string of 100 letters
stack_consonant = []  # string of 100 letters

global vowel_top  # declared as integer
global consonant_top  # declared as integer
vowel_top = 0
consonant_top = 0

read_data()
storage = ""
for i in range(5):
    user = input("Enter your choice, 'Vowel', 'Consonant': ")
    if user == "Vowel":
        storage += pop_vowel()
    else:
        storage += pop_consonant()

print(storage)
