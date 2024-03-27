def iterative_calculator(num):

    find = num
    total = 0

    while num != 0:
        if find % num == 0:
            total += num

        num -= 1
    return total

def recursive_value(num, find):

    if num == 0:
        return 0
    else:
        if find % num == 0:
            return num + recursive_value(num - 1, find)
        else:
            return recursive_value(num - 1, find)


print(iterative_calculator(10))
print(recursive_value(50, 50))
