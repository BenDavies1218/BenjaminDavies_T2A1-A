def linearSearch(list, target):
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None
# big0 (n) constant time
# writin as bigO(1)

def verify(index):
    if index is not None:
        print("Target found at in index", index)
    else:
        print("Target not found in list")

numbers = range(1, 999999999)
result = linearSearch(numbers, 9998334)
verify(result)

# -----------------------------------------------------------------------------------------

def binary_search(list, target):
    first = 0
    last = len(list) -1

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
verify(result)

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
                return recursive_binary(list[midpoint+1:], target)
            else:
                return recursive_binary(list[:midpoint], target)

def verify(result):
    print("Target Found: ", result)

result = recursive_binary(numbers, 9998334)
verify(result)
