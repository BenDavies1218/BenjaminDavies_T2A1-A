numbers = range(1, 999999999)


def binary_search(list, target):
    first = 0
    last = len(list) - 1

    while first <= last:
        midpoint = (first + last) // 2

        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1

    return None


result = binary_search(numbers, 9998334)

# logiritmic time
# Constant Space
# bigO(log(n))


# --------------------------------------------------------------------------------------------------


def recursive_binary(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint = (len(list)) // 2
        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return recursive_binary(list[midpoint + 1 :], target)
            else:
                return recursive_binary(list[:midpoint], target)


def verify(result):
    print("Target Found: ", result)


result = recursive_binary(numbers, 9998334)
verify(result)
